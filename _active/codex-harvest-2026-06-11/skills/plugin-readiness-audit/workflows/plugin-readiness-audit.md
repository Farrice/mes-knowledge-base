# Plugin Readiness Audit Workflow

## Inputs

- Candidate workflow names, or the default hot operating layer.
- Current workspace root.
- Any named failure pattern or packaging goal.

## Steps

1. Load the Workflow Packaging Ladder primitive.
2. Run `python3 execution/plugin_readiness_audit.py`.
3. Review the generated scorecard under `deliverables/plugin-readiness/`.
4. Recommend one of:
   - package now
   - improve first, then package
   - keep as workflow or skill
   - keep as prompt/reference/archive candidate
5. If packaging is recommended, identify the smallest plugin bundle and the fresh-thread tests.

## Quality Bar

The audit is complete only when it explains why each candidate should or should not become a plugin. Do not recommend plugin packaging just because the workflow is important.

