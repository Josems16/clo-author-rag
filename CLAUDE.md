# CLAUDE.md — Research Project with Claude Code + RAG

**Project:** [YOUR PROJECT TITLE]
**Institution:** [YOUR INSTITUTION]
**Field:** [YOUR FIELD — e.g., Additive Manufacturing / Thermal Engineering]
**Branch:** main

---

## Core Principles

- **Plan first** — enter plan mode before non-trivial tasks; save plans to `quality_reports/plans/`
- **Verify after** — compile and confirm output at the end of every task
- **Single source of truth** — Paper `main.tex` is authoritative; talks and supplements derive from it
- **Quality gates** — weighted aggregate score; nothing ships below 80/100; see `quality.md`
- **Worker-critic pairs** — every creator has a paired critic; critics never edit files
- **Auto-memory** — corrections and preferences are saved automatically via Claude Code's built-in memory system

---

## Getting Started

1. Fill in the `[BRACKETED PLACEHOLDERS]` in this file
2. Fill in `.claude/references/domain-profile.md` with your field, journals, and conventions
3. Run `/discover interview [topic]` to build your research specification
4. Or run `/new-project [topic]` for the full orchestrated pipeline

---

## Folder Structure

```
your-project/
├── CLAUDE.md                    # This file
├── .claude/                     # Rules, skills, agents, hooks
├── Bibliography_base.bib        # Centralized bibliography
├── paper/                       # Main LaTeX manuscript (source of truth)
│   ├── main.tex
│   ├── sections/
│   ├── figures/
│   ├── tables/
│   ├── talks/
│   ├── quarto/
│   ├── preambles/
│   ├── supplementary/
│   └── replication/
├── data/
│   ├── raw/                     # Original data (gitignored)
│   └── cleaned/
├── scripts/                     # Analysis code (R, Python, Julia)
├── quality_reports/             # Plans, session logs, reviews, scores
├── explorations/                # Research sandbox
├── papers/                      # Reference PDFs (gitignored, sync via cloud)
├── master_supporting_docs/      # Supporting papers and data docs
└── rag-engine/                  # RAG engine (git submodule)
```

---

## RAG Setup

```bash
# Index existing PDFs in papers/ and keep watching for new ones
python watcher.py

# One-shot: rebuild index and exit
python watcher.py --once
```

Copy your reference PDFs to `papers/` (from cloud storage). The watcher indexes them into `rag-data/` automatically.

---

## Commands

```bash
# Paper compilation
cd paper && latexmk main.tex

# Talk compilation
cd paper/talks && latexmk talk.tex

# Clean auxiliary files
cd paper && latexmk -c
```

---

## Quality Thresholds

| Score | Gate | Applies To |
|-------|------|------------|
| 80 | Commit | Weighted aggregate (blocking) |
| 90 | PR | Weighted aggregate (blocking) |
| 95 | Submission | Aggregate + all components >= 80 |
| -- | Advisory | Talks (reported, non-blocking) |

---

## Skills Quick Reference

| Command | What It Does |
|---------|-------------|
| `/new-project [topic]` | Full pipeline: idea → paper (orchestrated) |
| `/discover [mode] [topic]` | Discovery: interview, literature, data, ideation |
| `/strategize [mode] [question]` | Identification strategy or pre-analysis plan |
| `/analyze [dataset]` | End-to-end data analysis |
| `/write [section]` | Draft paper sections |
| `/review [file/--flag]` | Quality reviews (paper, code, peer) |
| `/revise [report]` | R&R cycle: classify + route referee comments |
| `/talk [mode] [format]` | Create or compile Beamer presentations |
| `/submit [mode]` | Journal targeting → package → final gate |
| `/tools [subcommand]` | Utilities: commit, compile, validate-bib, journal |
| `/checkpoint [--flag]` | Session handoff: memory + session report |

---

## Output Organization

Output organization: by-script

---

## Current Project State

| Component | File | Status | Description |
|-----------|------|--------|-------------|
| Paper | `paper/main.tex` | not started | Main manuscript |
| Data | `data/raw/` | not started | Raw datasets |
| Scripts | `scripts/` | not started | Analysis code |
| Replication | `paper/replication/` | not started | Replication package |
