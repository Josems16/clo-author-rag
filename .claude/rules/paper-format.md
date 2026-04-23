# Paper Format Standard — Engineering & Materials Science

This rule applies to the writer, writer-critic, and verifier agents. It replaces the economics working paper format for engineering and materials science fields.

---

## Two Modes

### Mode 1 — Draft / Preprint

Use when writing for internal review, conferences, or preprint servers (arXiv, ESSOAr, SSRN Engineering). Clean, journal-agnostic LaTeX.

### Mode 2 — Journal Submission

Use when preparing the final submission. Apply the target journal's official LaTeX class. The writer reads `domain-profile.md` to identify the target journal and applies the appropriate template.

**Priority rule:** If the domain profile lists a target journal, Mode 2 applies. Otherwise Mode 1.

---

## Mode 1 — Draft Preamble

```latex
\documentclass[12pt]{article}

% ====== Page Layout ======
\usepackage[left=2.5cm,right=2.5cm,top=2.5cm,bottom=2.5cm]{geometry}
% Single spacing — engineering papers are single-spaced
\usepackage{setspace}
\singlespacing

% ====== Line numbers (for peer review) ======
\usepackage{lineno}
\linenumbers

% ====== Typography ======
\usepackage{lmodern}
\usepackage{microtype}
\usepackage[T1]{fontenc}

% ====== Math ======
\usepackage{amssymb, amsmath, amsfonts, mathtools}
\usepackage{siunitx}           % SI units: \SI{9.81}{\metre\per\second\squared}
\sisetup{
  separate-uncertainty = true,
  multi-part-units     = repeat,
}

% ====== Tables ======
\usepackage{array, booktabs, makecell}
\usepackage[flushleft]{threeparttable}
\usepackage{tabularx, rotating}
\usepackage{tabularray}
\UseTblrLibrary{booktabs, siunitx}

% ====== Figures ======
\usepackage{graphicx, subcaption}
\usepackage{caption}
\captionsetup{font=small, labelfont=bf, justification=justified}
\usepackage{float}

% ====== Lists ======
\usepackage{enumitem}

% ====== Bibliography — author-year for drafts ======
\usepackage{xurl}
\usepackage{xcolor}
\definecolor{linkcolor}{RGB}{0, 100, 200}

\usepackage[backend=biber,
            style=authoryear,
            maxcitenames=2,
            mincitenames=1,
            maxbibnames=99,
            giveninits=true,
            uniquename=false,
            dashed=false,
            url=true,
            natbib=true]{biblatex}
\addbibresource{../Bibliography_base.bib}

% ====== Hyperref (second-to-last) ======
\usepackage[colorlinks=true,
            linkcolor=linkcolor,
            citecolor=linkcolor,
            urlcolor=linkcolor,
            breaklinks]{hyperref}

% ====== Cleveref (last) ======
\usepackage[nameinlink]{cleveref}
```

---

## Mode 2 — Journal Submission Templates

### Elsevier journals (IJHMT, ATE, Additive Manufacturing, Materials & Design, etc.)

Most engineering journals in scope use the `elsarticle` class:

```latex
\documentclass[review,12pt]{elsarticle}
% 'review': double-column preview → single-column review with line numbers
% Use 'preprint' for arXiv / preprint server

\usepackage{amssymb, amsmath, mathtools, siunitx}
\usepackage{booktabs, tabularx, tabularray}
\UseTblrLibrary{booktabs, siunitx}
\usepackage{graphicx, subcaption, caption}
\usepackage{lineno}
\modulolinenumbers[5]

\usepackage[colorlinks=true, linkcolor=blue, citecolor=blue, urlcolor=blue]{hyperref}
\usepackage[nameinlink]{cleveref}

\journal{International Journal of Heat and Mass Transfer}
\bibliographystyle{elsarticle-harv}   % author-year; use elsarticle-num for numbered
```

**Elsevier requirements:**
- Highlights: 3–5 bullet points, ≤ 85 characters each (including spaces), in a separate `highlights.tex` or at the start of the manuscript file
- Abstract: structured or unstructured, 200–300 words
- Keywords: 4–8, separated by semicolons
- Line numbers in review mode (included via `lineno`)

### ASME journals (JHT, JMSE)

```latex
\documentclass{asme2ej}    % download from ASME
% Or use the modern ASME template: asmeconf (available on CTAN)
\usepackage[T1]{fontenc}
\usepackage{siunitx, booktabs, graphicx, amsmath}
```

---

## Title Page Format

### Draft mode
```latex
\title{Paper Title}

\author{
  First Author\textsuperscript{a},
  Second Author\textsuperscript{a,b},
  Corresponding Author\textsuperscript{b,*}
}

\date{
  \textsuperscript{a} Department, University, City, Country \\
  \textsuperscript{b} Department, Institution, City, Country \\[0.5em]
  \textsuperscript{*} Corresponding author. Email: email@institution.edu
}
```

### Elsevier (elsarticle)
```latex
\begin{frontmatter}
\title{Paper Title}

\author[inst1]{First Author}
\author[inst1,inst2]{Second Author}
\author[inst2]{Corresponding Author\corref{cor1}}
\cortext[cor1]{Corresponding author.}
\ead{email@institution.edu}

\affiliation[inst1]{organization={Department},
             addressline={Street},
             city={City},
             country={Country}}
\affiliation[inst2]{organization={Institution}, country={Country}}

\begin{abstract}
Abstract text (200--300 words).
\end{abstract}

\begin{highlights}
\item Highlight 1 (≤85 characters)
\item Highlight 2
\item Highlight 3
\end{highlights}

\begin{keyword}
Keyword 1 \sep Keyword 2 \sep Keyword 3 \sep Keyword 4 \sep Keyword 5
\end{keyword}
\end{frontmatter}
```

---

## Section Structure

Standard engineering paper order:

1. **Introduction** — motivation, literature gap, objectives, paper structure
2. **Materials and Methods** (or Experimental Setup / Numerical Methods)
   - Materials / specimens
   - Equipment and instrumentation
   - Procedure
   - Uncertainty analysis
   - Numerical model (if applicable) + validation
3. **Results** (or Results and Discussion)
4. **Discussion** (if separate from Results)
5. **Conclusions**
6. **Nomenclature** (if > 10 symbols)
7. **Acknowledgements**
8. **References**
9. **Appendix** (if needed)

Each section uses `\section{}` with `\label{sec:name}`. Use `\cref{sec:name}` to reference sections.

---

## Nomenclature Section

Required when more than 10 symbols appear in the paper.

```latex
\section*{Nomenclature}

\begin{tabbing}
  \hspace{2cm} \= \kill
  $T_{db}$    \> Dry-bulb temperature [\si{\degreeCelsius}] \\
  $T_{wb}$    \> Wet-bulb temperature [\si{\degreeCelsius}] \\
  $\dot{m}$   \> Mass flow rate [\si{\kg\per\s}] \\
  $Nu$        \> Nusselt number [--] \\[0.5em]
  \textit{Greek symbols} \\[0.3em]
  $\varepsilon$ \> Effectiveness [--] \\
  $\rho$      \> Density [\si{\kg\per\m\cubed}] \\[0.5em]
  \textit{Subscripts} \\[0.3em]
  $db$        \> Dry-bulb \\
  $wb$        \> Wet-bulb \\
\end{tabbing}
```

---

## Tables

Engineering tables show experimental data, material properties, process parameters, or uncertainty budgets — not regression coefficients.

**Experimental data table:**
```latex
\begin{table}[htbp]
\centering
\begin{threeparttable}
\caption{Measured heat transfer coefficients at varying Reynolds number.}
\label{tab:htc}
\begin{tabular}{S[table-format=5.0]
                S[table-format=3.1]
                S[table-format=1.3]
                S[table-format=2.1]}
\toprule
{$Re$ [--]} & {$Nu$ [--]} & {$h$ [\si{\W\per\m\squared\per\K}]} & {$U_h$ [\%]} \\
\midrule
 5000 &  42.3 & 1.823 &  3.2 \\
10000 &  78.1 & 3.367 &  2.8 \\
20000 & 138.4 & 5.966 &  2.5 \\
\bottomrule
\end{tabular}
\begin{tablenotes}\small
  \item $U_h$: expanded uncertainty (k = 2, 95\% confidence level).
\end{tablenotes}
\end{threeparttable}
\end{table}
```

**Rules:**
- Use `siunitx` `S` columns for numerical data — automatic decimal alignment
- Units in column headers, never in data cells
- Uncertainty column (`U_x`) alongside each measured quantity
- `booktabs` rules only — no `\hline`, no vertical lines

---

## Figures

- **Resolution:** ≥ 300 dpi for raster (photographs, micrographs); vector (PDF/EPS) for plots
- **Format:** PDF for plots (vector); TIFF or PNG (≥ 300 dpi) for micrographs and photographs
- **Size:** Single-column figures: ≈ 88 mm wide; double-column: ≈ 180 mm wide (Elsevier standard)
- **Font:** Match body text — minimum 8 pt in the final printed size
- **Axes:** Always labelled with quantity and unit: `Dry-bulb temperature, $T_{db}$ (°C)`
- **No titles inside figures** — title goes in `\caption{}`
- **Colorblind-safe palettes** — use Color Brewer or Okabe-Ito; never red/green only
- **Grayscale readable** — distinguish series by both color and marker/linetype

---

## Uncertainty Reporting

All experimental results must report expanded uncertainty:

- Method: Kline & McClintock (1953) or GUM (ISO/IEC Guide 98-3)
- Coverage factor: k = 2 (95% confidence), stated explicitly
- Format in text: `$h = 1.82 \pm 0.06~\si{\W\per\m\squared\per\K}$` (k = 2)
- Format in tables: separate `U_x` column or `±` in the same cell with `siunitx`

---

## Bibliography

**Author-year (draft mode and most engineering journals):**
```latex
\printbibliography
```

**Numbered (some ASME, IEEE-affiliated journals):**
Change `style=authoryear` to `style=numeric-comp` in the biblatex options.

**Compile:**
```bash
cd paper && latexmk main.tex   # handles biber automatically
```

---

## What the Writer-Critic Checks

**Required — blocking:**
- No line numbers in review submission (-5)
- Missing uncertainty analysis for experimental results (-10)
- Missing nomenclature when > 10 symbols (-5)
- Units missing from table headers (-5) or axis labels (-5)
- `\hline` instead of booktabs rules (-3)
- Missing figure notes in caption (-5)
- Missing table notes (-5)
- `hyperref` not second-to-last (-2)
- Missing `cleveref` (-2)
- Missing highlights for Elsevier submission (-5)
- Abstract exceeds journal word limit (-3)
- Keywords missing or outside 4–8 range (-3)
- Absolute paths in scripts (-5)
- `bibtex` instead of `biber` (-3)

**Advisory — reported, not deducted:**
- Figures not vector format for plots
- Font size < 8 pt in figures
- Non-colorblind-safe palette
- Missing Gage R&R or measurement system analysis for manufacturing studies
