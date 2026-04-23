# Content Invariants

These are non-negotiable. Every agent checks against them. Violations are deductions, not suggestions. Critics cite invariant numbers (e.g., "violates INV-3") in their reports.

---

## Paper

**INV-1.** Every table has notes explaining key variables, sample, and data source — via `threeparttable` + `tablenotes` (traditional) or `talltblr` with `note{}` keys (tabularray).

**INV-2.** Every figure has a `\caption{}` with a note explaining what is shown, how to read it, and the data source.

**INV-3.** No `\hline` — use `\toprule`, `\midrule`, `\bottomrule` (booktabs). No vertical rules.

**INV-4.** Statistical reporting follows the journal profile. Engineering journals: report mean ± uncertainty (expanded, k=2) or confidence intervals. Significance stars are not standard in engineering — use p-values or confidence intervals explicitly. Check the journal profile for deviations.

**INV-5.** Abstract length follows the journal profile. Default for engineering: 200–300 words. Elsevier journals typically allow up to 300 words. Do not exceed the journal's stated limit.

**INV-6.** Keywords (5–8) present after the abstract. No JEL codes for engineering papers. Highlights (3–5 bullet points, ≤85 characters each) required for Elsevier journal submissions — check the journal profile.

**INV-7.** Notation is consistent across all sections — the same symbol means the same thing everywhere. Different concepts get different symbols. A Nomenclature section is required when more than 10 symbols are used (standard in heat transfer and fluid mechanics papers).

**INV-8.** Every experimental or mechanistic claim must be supported by evidence: measured data with uncertainty, validated simulation, or theoretical derivation. Qualitative claims ("the heat transfer improves") must be quantified ("by 23 ± 4% at Re = 5000").

**INV-9.** `biblatex` + `biber`, not `natbib` + `bibtex`.

**INV-10.** `hyperref` loaded second-to-last in preamble; `cleveref` loaded immediately after it.

**INV-11.** Numbers in text match the tables and figures exactly. No rounding discrepancies, no stale values.

**INV-12.** No titles inside ggplot/matplotlib figures. Titles go in LaTeX `\caption{}`. Panel labels ("Panel A: ...") inside multi-panel figures are fine.

**INV-13.** R/Python/Julia scripts export bare `tabular` environments — no `\begin{table}`, `\caption{}`, or notes. The paper's `main.tex` wraps them.

## Code

**INV-14.** `set.seed()` (or language equivalent) called exactly once, at the top of the main script, if any stochastic element exists.

**INV-15.** All packages/libraries loaded at the top of the script, before any data loading or computation.

**INV-16.** No absolute paths. All paths relative to project root via `here()` (R), `pathlib.Path` (Python), or `joinpath(@__DIR__, ...)` (Julia).

**INV-17.** No growing vectors/lists in loops. Pre-allocate result containers or use vectorized operations.

**INV-18.** Output files go to the path specified by the Output Organization setting in `CLAUDE.md`.

**INV-19.** No prohibited functions: `setwd()` / `os.chdir()` / `cd()`, `rm(list = ls())`, `install.packages()` in scripts, `attach()` / `detach()`.

## Talk

**INV-20.** Notation in talk matches paper exactly — same symbols, same subscripts, same definitions.

**INV-21.** Every claim on a slide is traceable to the paper. No orphan results or numbers that don't appear in the manuscript.

---

## How Agents Use This File

| Agent | Checks | Action on Violation |
|-------|--------|-------------------|
| **writer-critic** | INV-1 through INV-13 | Deduct per scoring rubric |
| **coder-critic** | INV-13 through INV-19 | Deduct per scoring rubric |
| **storyteller-critic** | INV-20, INV-21 | Deduct per scoring rubric |
| **verifier** | INV-9, INV-10, INV-14, INV-15, INV-16, INV-19 | FAIL if present |
| **lint hook** | INV-14, INV-15, INV-16, INV-19 | Advisory warning |
