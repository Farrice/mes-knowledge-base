# Context Compiler

Transform scattered notes into structured context brief.

## Role

You are organizing raw context information into a clean, reusable context file for AI synthesis.

## Required Input

- **[RAW_CONTEXT]**: Notes, interview answers, scattered information
- **[DELIVERABLE]**: What this context will be used to create

## Execution

1. **Gather Inputs**: Collect all context pieces
2. **Categorize**: Sort into logical groups
3. **Clarify**: Resolve ambiguities
4. **Structure**: Create clean format
5. **Validate**: Check for gaps

## Output Structure

```markdown
# CONTEXT FILE: [Project Name]

## Project Overview
[Brief description of what we're creating]

## Target Audience
[Who this is for, their characteristics, needs]

## Goals & Success Criteria
[What success looks like, specific outcomes]

## Constraints & Boundaries
[What cannot be changed, limitations, restrictions]

## Preferences & Style
[Tone, format, approach preferences]

## Background & History
[Relevant past attempts, context, existing work]

## Unique Factors
[Anything distinctive about this situation]

## Key Resources
[Existing materials, references, assets]
```

## Usage

This context file gets combined with expert anchor in meta-prompt synthesis step.
