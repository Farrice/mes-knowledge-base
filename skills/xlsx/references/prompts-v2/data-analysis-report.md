---
name: "XLSX Engineer — Spreadsheet Data Analysis"
source_prompt: born-v2
skill: xlsx
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are operating under Claude's built-in xlsx skill's data-analysis guidance: **"For data analysis, visualization, and basic operations, use pandas which provides powerful data manipulation capabilities."** This deliverable is the read/analyze path of the skill, distinct from the build/edit path — pandas is the primary tool here, with openpyxl invoked only if the analysis output itself needs to be written back as a formatted or formula-bearing workbook.

## Input Required

- **[SOURCE FILE]** — the .xlsx/.xlsm/.csv/.tsv file to analyze
- **[SHEET(S) IN SCOPE]** — specific sheet name(s), or all sheets if the question spans the workbook
- **[ANALYSIS QUESTION]** — what the user wants to know (trends, summary statistics, comparisons, anomalies, a specific metric)
- **[OUTPUT FORM]** — whether the answer should be delivered as prose/findings, a new summary sheet, a chart, or a combination
- **[DATA TYPE HINTS, IF KNOWN]** — columns that need explicit dtype handling (IDs as strings, dates, etc.) to avoid pandas inference errors

## Execution Protocol

1. **Load appropriately for the scope**: `df = pd.read_excel('file.xlsx')` for the first sheet, or `all_sheets = pd.read_excel('file.xlsx', sheet_name=None)` to get every sheet as a dict when the analysis spans the workbook.

2. **Guard against dtype inference issues** per the skill's Working with pandas guidance: specify dtypes explicitly where they matter — `pd.read_excel('file.xlsx', dtype={'id': str})` — so identifiers, codes, or zero-padded values don't silently get coerced to numbers. Parse dates explicitly rather than trusting inference: `pd.read_excel('file.xlsx', parse_dates=['date_column'])`.

3. **For large files, scope the read**: pull specific columns with `usecols=['A', 'C', 'E']` rather than loading the entire sheet if the analysis only needs a subset.

4. **Orient before analyzing**: `df.head()` to preview, `df.info()` for column/dtype/null overview, `df.describe()` for summary statistics. This orientation pass is what catches the skill's flagged pitfalls before they corrupt the analysis — specifically:
   - **NaN handling**: check for null values with `pd.notna()` before any calculation that would silently propagate or mis-handle them
   - **Multiple matches**: when searching for a value or pattern, search all occurrences, not just the first hit
   - **Far-right columns**: if the source is a wide financial/reporting export, FY or period data is often in columns 50+ — confirm you've located every relevant column, not just the visible/near ones

5. **Run the actual analysis** against the stated question — filtering, grouping, aggregation, or comparison as the question requires — using pandas operations. If the deliverable calls for a chart or visualization, produce it as part of this step.

6. **If the output is written back to Excel**: use `df.to_excel('output.xlsx', index=False)` for a simple data export. If the output needs formulas, formatting, multiple sheets, or a specific layout, hand off to openpyxl for that write step and follow the same CRITICAL rule that governs every xlsx build in this skill — any calculated value the recipient might want to audit or re-derive should be an Excel formula, not a pandas-computed hardcoded number, so the output stays live if source data changes.

7. **If formulas were written in step 6**, the standard recalc obligation still applies: `python recalc.py output.xlsx`, read the JSON, fix any errors by type, and recalculate until `total_errors` is 0.

## Output Contract

- A direct answer to the analysis question, grounded in the actual data (no invented figures)
- Key supporting numbers cited with enough context to be checked (which column/sheet/filter produced them)
- Any caveats surfaced during orientation (nulls found and how handled, dtype corrections made, ambiguous multi-match situations resolved)
- If a file was produced: the file itself, plus the same zero-error guarantee as any other xlsx deliverable if it contains formulas
- Length calibrated to the question — a single-metric lookup gets a short direct answer; a multi-part analysis gets one section per sub-question

## Output Skeleton

```
Analysis of [SOURCE FILE], sheet(s) [SCOPE]

Data notes:
- Rows/columns: [N x M] | Nulls found: [WHERE, IF ANY, AND HOW HANDLED]
- Dtype corrections applied: [LIST, IF ANY]

Findings:
- [QUESTION/SUB-QUESTION 1]: [DIRECT ANSWER] — derived from [COLUMN/FILTER/CALCULATION]
- [QUESTION/SUB-QUESTION 2, if applicable]: [DIRECT ANSWER] — derived from [...]

[IF FILE OUTPUT PRODUCED]
Output file: [FILENAME].xlsx
- Contents: [WHAT WAS WRITTEN — data export / formatted summary / formulas]
- recalc.py result (if formulas present): status=[success], total_errors=[0]
```

## Quality Gate

- [ ] Were dtypes and dates handled explicitly rather than left to pandas inference, for any column where that mattered?
- [ ] Was a null-value check (`pd.notna()`) run before any calculation that nulls could have silently corrupted?
- [ ] If searching for values/patterns, were ALL occurrences checked rather than stopping at the first match?
- [ ] Does every reported figure trace back to an actual column/filter/calculation in the source data (no invented numbers)?
- [ ] If a file was produced with formulas, does the final `recalc.py` run show zero errors?

## Deploy When

User asks to read, analyze, summarize, or extract insight from an existing spreadsheet — including questions like "what's the trend in this data," "summarize this workbook," or "pull the totals from this sheet" — whether or not a new file needs to be produced as output.
