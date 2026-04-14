"""
Ensemble Probability Engine — Multi-model Bayesian integration (GP-5).

Implements PolySwarm's 70/30 pattern:
  P_final = 0.70 * P_ensemble + 0.30 * P_market

Three independent models (GP-2: independence requirement):
  1. Analytical (GPT-4o-mini, 40% weight) — statistical pattern recognition
  2. Credibility (Haiku 4.5, 35% weight) — source credibility evaluation
  3. Contrarian (Gemini Flash, 25% weight) — alternative interpretation

Key constraints:
  - Models forecast INDEPENDENTLY before aggregation (GP-2)
  - If models see each other's outputs, you get herding (zero additional signal)
  - High model disagreement (std_dev > 30%) → NO TRADE
  - Ensemble is for markets WITHOUT a superior reference price (NOT sports/weather)
  - Target categories: politics, economics, AI/tech events

Paper trading phase uses cheap models ($4-10/mo). Upgrade to full models at Phase 5.
API cost at scale: ~$0.007 per ensemble call with cheap models.
"""

import json
import logging
import math
import os
from datetime import datetime, timezone
from typing import Optional

from projects.prediction_market_arb.models import EnsembleEstimate, Opportunity, StrategyType, EdgeType

logger = logging.getLogger("polymarket.ensemble")


# =============================================================================
# MODEL PROMPTS — Each model gets a DIFFERENT analytical frame (GP-2)
# =============================================================================

SYSTEM_PROMPTS = {
    "analytical": """You are a statistical analyst evaluating prediction market probabilities.
Your approach is DATA-DRIVEN: base rates, historical precedent, quantitative indicators.
You focus on statistical patterns, not narratives.

Given a prediction market question and context, estimate the probability of the YES outcome.
Be precise. Avoid anchoring to the current market price — form your own estimate independently.

Respond in JSON format ONLY:
{"probability": 0.XX, "confidence": X, "reasoning": "brief explanation"}
where probability is 0.01-0.99 and confidence is 1-10.""",

    "credibility": """You are a source credibility analyst evaluating prediction market probabilities.
Your approach is CREDIBILITY-FOCUSED: which sources to trust, information quality assessment,
distinguishing primary sources from echo chambers.

When one journalist reports something and three others repeat without independent verification,
you identify the 3:1 ratio as 1:0 actual sources.

Given a prediction market question and context, estimate the probability of the YES outcome.
Be precise. Avoid anchoring to the current market price — form your own estimate independently.

Respond in JSON format ONLY:
{"probability": 0.XX, "confidence": X, "reasoning": "brief explanation"}
where probability is 0.01-0.99 and confidence is 1-10.""",

    "contrarian": """You are a contrarian analyst evaluating prediction market probabilities.
Your approach is CONTRARIAN: look for consensus blind spots, identify what the crowd
is missing, consider alternative scenarios that mainstream analysis ignores.

You are correct less often than the other analysts, but when you are correct, it is on
the most valuable calls — the ones everyone else missed.

Given a prediction market question and context, estimate the probability of the YES outcome.
Be precise. Avoid anchoring to the current market price — form your own estimate independently.

Respond in JSON format ONLY:
{"probability": 0.XX, "confidence": X, "reasoning": "brief explanation"}
where probability is 0.01-0.99 and confidence is 1-10.""",
}


# =============================================================================
# LLM CLIENTS (multi-provider)
# =============================================================================

def _call_openai(model: str, system: str, user: str) -> dict:
    """Call OpenAI API. Returns parsed JSON response."""
    import requests as req

    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set")

    resp = req.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": 0.3,
            "max_tokens": 500,
            "response_format": {"type": "json_object"},
        },
        timeout=30,
    )
    resp.raise_for_status()
    content = resp.json()["choices"][0]["message"]["content"]
    return json.loads(content)


def _call_anthropic(model: str, system: str, user: str) -> dict:
    """Call Anthropic API. Returns parsed JSON response."""
    import requests as req

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not set")

    resp = req.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "system": system,
            "messages": [{"role": "user", "content": user}],
            "temperature": 0.3,
            "max_tokens": 500,
        },
        timeout=30,
    )
    resp.raise_for_status()
    content = resp.json()["content"][0]["text"]
    # Extract JSON from response (Anthropic may wrap in markdown)
    if "```" in content:
        content = content.split("```")[1]
        if content.startswith("json"):
            content = content[4:]
    return json.loads(content.strip())


def _call_google(model: str, system: str, user: str) -> dict:
    """Call Google Gemini API. Returns parsed JSON response."""
    import requests as req

    api_key = os.environ.get("GOOGLE_API_KEY", "")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not set")

    resp = req.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
        params={"key": api_key},
        headers={"Content-Type": "application/json"},
        json={
            "systemInstruction": {"parts": [{"text": system}]},
            "contents": [{"parts": [{"text": user}]}],
            "generationConfig": {
                "temperature": 0.3,
                "maxOutputTokens": 500,
                "responseMimeType": "application/json",
            },
        },
        timeout=30,
    )
    resp.raise_for_status()
    content = resp.json()["candidates"][0]["content"]["parts"][0]["text"]
    return json.loads(content)


PROVIDER_CALLERS = {
    "openai": _call_openai,
    "anthropic": _call_anthropic,
    "google": _call_google,
}


# =============================================================================
# ENSEMBLE ENGINE
# =============================================================================

class EnsembleEngine:
    """
    Multi-model probability estimation with Bayesian market integration.

    Calls 3 models independently (GP-2), aggregates with fixed weights,
    then applies 70/30 Bayesian integration with market price (GP-5).
    """

    def __init__(self, config):
        self.config = config
        self.models = config.ensemble.models
        self.market_weight = config.ensemble.market_weight
        self.min_edge = config.ensemble.min_edge_pct
        self.max_std_dev = config.ensemble.max_std_dev

    def estimate(self, question: str, market_price: float,
                 context: str = "") -> Optional[EnsembleEstimate]:
        """
        Run the full ensemble pipeline on a single market.

        1. Call each model independently with its analytical frame
        2. Aggregate with fixed weights
        3. Apply 70/30 Bayesian integration with market price
        4. Check trade trigger (edge > 5% AND std_dev < 30%)

        Returns EnsembleEstimate or None on failure.
        """
        user_prompt = self._build_user_prompt(question, context)
        model_configs = self.models if isinstance(self.models, dict) else self.models._data

        results = {}
        for role, cfg in model_configs.items():
            if isinstance(cfg, dict):
                provider = cfg["provider"]
                model = cfg["model"]
                weight = cfg["weight"]
            else:
                provider = cfg.provider
                model = cfg.model
                weight = cfg.weight

            system = SYSTEM_PROMPTS.get(role, SYSTEM_PROMPTS["analytical"])
            caller = PROVIDER_CALLERS.get(provider)
            if not caller:
                logger.error(f"Unknown provider: {provider}")
                continue

            try:
                resp = caller(model, system, user_prompt)
                prob = float(resp.get("probability", 0.5))
                conf = float(resp.get("confidence", 5))
                reasoning = resp.get("reasoning", "")

                # Clamp probability
                prob = max(0.01, min(0.99, prob))
                conf = max(1, min(10, conf))

                results[role] = {
                    "probability": prob,
                    "confidence": conf,
                    "reasoning": reasoning,
                    "weight": weight,
                }
                logger.info(f"  {role} ({model}): p={prob:.2f}, conf={conf}/10")
            except Exception as e:
                logger.error(f"  {role} ({model}) failed: {e}")
                results[role] = {
                    "probability": 0.5,
                    "confidence": 1,
                    "reasoning": f"Error: {e}",
                    "weight": weight,
                }

        if not results:
            return None

        # Weighted aggregation
        roles = list(results.keys())
        probs = [results[r]["probability"] for r in roles]
        weights = [results[r]["weight"] for r in roles]
        total_weight = sum(weights)

        ensemble_prob = sum(p * w for p, w in zip(probs, weights)) / total_weight if total_weight > 0 else 0.5

        # Standard deviation of model estimates (disagreement signal)
        if len(probs) > 1:
            mean = sum(probs) / len(probs)
            variance = sum((p - mean) ** 2 for p in probs) / len(probs)
            std_dev = math.sqrt(variance)
        else:
            std_dev = 0.0

        # 70/30 Bayesian integration with market (GP-5)
        ensemble_weight = 1.0 - self.market_weight
        final_prob = ensemble_weight * ensemble_prob + self.market_weight * market_price

        # Edge and trade signal
        edge = final_prob - market_price
        trade_signal = (abs(edge) > self.min_edge and std_dev < self.max_std_dev)

        # Build result
        r = lambda role: results.get(role, {})
        estimate = EnsembleEstimate(
            market_id="",  # Set by caller
            question=question,
            model_1_prob=r("analytical").get("probability", 0.5),
            model_1_confidence=r("analytical").get("confidence", 1),
            model_1_reasoning=r("analytical").get("reasoning", ""),
            model_2_prob=r("credibility").get("probability", 0.5),
            model_2_confidence=r("credibility").get("confidence", 1),
            model_2_reasoning=r("credibility").get("reasoning", ""),
            model_3_prob=r("contrarian").get("probability", 0.5),
            model_3_confidence=r("contrarian").get("confidence", 1),
            model_3_reasoning=r("contrarian").get("reasoning", ""),
            ensemble_prob=round(ensemble_prob, 4),
            std_dev=round(std_dev, 4),
            market_price=round(market_price, 4),
            final_prob=round(final_prob, 4),
            edge=round(edge, 4),
            trade_signal=trade_signal,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

        logger.info(f"Ensemble: p_ensemble={ensemble_prob:.3f}, "
                     f"p_final={final_prob:.3f}, "
                     f"edge={edge:+.3f}, std={std_dev:.3f}, "
                     f"signal={'YES' if trade_signal else 'NO'}")
        return estimate

    def _build_user_prompt(self, question: str, context: str) -> str:
        """Build the user prompt for model evaluation."""
        prompt = f"""Prediction market question: {question}

Evaluate the probability of YES being the correct outcome.

"""
        if context:
            prompt += f"""Additional context:
{context}

"""
        prompt += """Important:
- Form your own probability estimate INDEPENDENTLY
- Do not assume the current market price is correct
- Consider base rates and historical precedent
- Be specific about your uncertainty

Respond in JSON: {"probability": 0.XX, "confidence": X, "reasoning": "..."}"""
        return prompt

    def scan_markets(self, markets: list, client) -> list[Opportunity]:
        """
        Run ensemble analysis on pre-filtered markets.

        Returns list of Opportunity objects for markets with trade signals.
        """
        opportunities = []
        max_calls = self.config.ensemble.max_calls_per_scan

        for i, market in enumerate(markets[:max_calls]):
            question = market.question if hasattr(market, 'question') else market.get("question", "")
            market_id = market.id if hasattr(market, 'id') else market.get("id", "")

            # Get current price
            prices = client.get_market_price(market_id)
            if not prices:
                continue

            market_price = prices["yes"]

            logger.info(f"Ensemble [{i+1}/{min(len(markets), max_calls)}]: "
                        f"{question[:60]}...")

            estimate = self.estimate(question, market_price)
            if not estimate or not estimate.trade_signal:
                continue

            estimate.market_id = market_id

            # Determine edge type
            if estimate.std_dev < 0.10:
                edge_type = EdgeType.INFORMATION_ASYMMETRY.value
            elif estimate.std_dev < 0.20:
                edge_type = EdgeType.NARRATIVE_MISPRICING.value
            else:
                edge_type = EdgeType.UNKNOWN.value

            # EV calculation
            if market_price > 0 and market_price < 1.0:
                ev = estimate.final_prob / market_price - 1.0
                b = (1.0 / market_price) - 1.0
                kelly_f = max(0.0, (estimate.final_prob * b - (1.0 - estimate.final_prob)) / b) if b > 0 else 0.0
            else:
                ev = 0.0
                kelly_f = 0.0

            opp = Opportunity(
                strategy=StrategyType.ENSEMBLE.value,
                market_id=market_id,
                token_id="",  # Resolved by orchestrator
                question=question,
                category="",  # Set by pre-filter
                our_probability=round(estimate.final_prob, 4),
                market_price=round(market_price, 4),
                edge=round(estimate.edge, 4),
                edge_after_fees=round(abs(estimate.edge) - 0.01, 4),  # ~1% fee drag for politics
                ev=round(ev, 4),
                kelly_f=round(kelly_f, 4),
                edge_type=edge_type,
                reference_source="ensemble_3model",
                confidence=round(1.0 - estimate.std_dev, 3),
                context={
                    "ensemble_prob": estimate.ensemble_prob,
                    "model_probs": [estimate.model_1_prob, estimate.model_2_prob, estimate.model_3_prob],
                    "model_confidences": [estimate.model_1_confidence, estimate.model_2_confidence, estimate.model_3_confidence],
                    "std_dev": estimate.std_dev,
                    "market_weight": self.market_weight,
                },
                timestamp=datetime.now(timezone.utc).isoformat(),
            )
            opportunities.append(opp)

        opportunities.sort(key=lambda x: abs(x.edge_after_fees), reverse=True)
        logger.info(f"Ensemble scan: {len(opportunities)} trade signals "
                     f"from {min(len(markets), max_calls)} markets analyzed")
        return opportunities
