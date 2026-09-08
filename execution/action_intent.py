"""Shared bounded action/negation parsing for existing preflight owners.

This is an advisory routing helper, never permission to perform an action.
Sentence/contrast boundaries end prohibitions; later requested actions remain
visible. Word boundaries prevent buyer/publisher from becoming buy/publish.
"""
import re

def has_requested_action(intent: str, action_pattern: str) -> bool:
    """Return True when an action is requested rather than explicitly denied."""
    intent = intent.lower()
    denial_scope_words = {
        "it", "this", "that", "them", "anything", "yet", "spend", "money",
        "paid", "tools", "tool", "api", "apis", "send", "sending", "outreach",
        "use", "using", "credits", "buy", "buying", "purchase", "purchasing",
        "a",
        "all",
        "an",
        "and",
        "any",
        "approved",
        "automatic",
        "automatically",
        "broad",
        "broadly",
        "delete",
        "deleted",
        "deleting",
        "deletion",
        "deletions",
        "destructive",
        "external",
        "file",
        "files",
        "further",
        "local",
        "locally",
        "material",
        "materials",
        "original",
        "originals",
        "or",
        "publish",
        "published",
        "publishing",
        "public",
        "the",
        "unauthorized",
        "unapproved",
        "user",
    }
    for match in re.finditer(action_pattern, intent):
        prefix = intent[: match.start()]
        local_prefix = re.split(
            r"[.;!?]|\b(?:but|however|then)\b",
            prefix,
        )[-1]
        deny_matches = list(
            re.finditer(r"\b(?:do not|don't|never|without|no)\b", local_prefix)
        )
        if not deny_matches:
            return True
        between = local_prefix[deny_matches[-1].end() :]
        between_words = re.findall(r"[a-z]+", between)
        if any(word not in denial_scope_words for word in between_words):
            return True
    return False



def has_requested_terms(intent: str, terms) -> bool:
    q = intent.lower()
    for term in terms:
        term = term.strip().lower()
        if not term:
            continue
        pattern = r"(?<![\w])" + re.escape(term) + r"(?![\w])"
        if term == "publish":
            pattern = r"\bpublish(?:es|ed|ing)?\b"
        elif term == "delete":
            pattern = r"\bdelet(?:e|es|ed|ing|ion|ions)\b"
        if term in {"post", "email", "dm", "message"}:
            # Content nouns after an explicit drafting verb are local artifacts.
            # A separate send/publish verb is still tested independently.
            matches = list(re.finditer(pattern, q))
            if matches and all(re.search(r"\b(?:draft|write|rewrite|edit|review|prepare)\s+(?:(?:a|an|the|this|that|short|brief|full|complete|new|one|approved|buyer-first|revised|conversational)\s+){0,5}$", q[:m.start()]) for m in matches):
                continue
        if has_requested_action(q, pattern):
            return True
    return False
