# Hidden Knowledge - Lance Martin & Yichao "Peak" Ji

## Tacit Knowledge 1: Pre-Rot Threshold Is Model AND Task Specific
Peak says "128K-200K" but emphasizes this requires evaluation for YOUR model and YOUR task. The number isn't universal—it's discovered through measurement. Most teams use the stated context limit and wonder why agents degrade; experts find the actual working limit.

## Tacit Knowledge 2: Compaction Preserves Behavioral Examples
The reason to compact OLD context while keeping NEW context full isn't just about relevance—it's about maintaining behavioral examples. The model needs to see correct tool usage format in recent context or it will output compacted formats inappropriately.

## Tacit Knowledge 3: Dynamic Tool Loading Breaks More Than It Fixes
RAG-based tool loading seems elegant but causes two critical problems: KV cache invalidation and orphaned tool references in history. The "dumb" solution (fixed atomic tools + sandbox extensibility) works better in practice.

## Tacit Knowledge 4: Open Source Models Are Often More Expensive
Counterintuitive truth: at scale, frontier models with distributed KV cache infrastructure can be cheaper than self-hosted open models without that infrastructure. The "cost savings" of open source don't account for the infrastructure gap.

## Tacit Knowledge 5: MCP Changes Everything About Fine-Tuning
Model Context Protocol creates an infinitely extensible action space. Fine-tuning on a fixed action space becomes obsolete when your action space is dynamic. This is why Manus doesn't fine-tune.

## Tacit Knowledge 6: Benchmark-Product Misalignment Is Real
Manus found that models scoring high on GAIA benchmark weren't preferred by users. The evaluation that matters is user ratings, not academic benchmarks. Public benchmarks measure the wrong things for production agents.

## Tacit Knowledge 7: The ToDo.md Pattern Was Wasteful
Manus initially used todo.md files for planning—and found one-third of agent actions were just updating the todo list. Structured planning via a separate planner agent eliminated this waste.
