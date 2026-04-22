# clo-author-rag

Research scaffold for empirical papers, combining [clo-author](https://github.com/hugosantanna/clo-author) multi-agent pipeline with a local RAG engine for PDF knowledge bases.

Built on top of [clo-author](https://github.com/hugosantanna/clo-author) (Hugo Sant'Anna) and [Proyecto-RAG](https://github.com/hugosantanna/clo-author).

---

## What It Does

- **Multi-agent research pipeline** — librarian, strategist, coder, writer, and critic pairs guide you from idea to submission
- **Local RAG** — drop reference PDFs into `papers/`, they get indexed automatically; Claude queries them instead of re-reading every session
- **10 slash commands** — `/discover`, `/strategize`, `/analyze`, `/write`, `/review`, `/revise`, `/talk`, `/submit`, `/tools`, `/checkpoint`
- **Simulated peer review** — `/review --peer [journal]` runs a full desk review + two independent referees

---

## Prerequisites

| Tool | Install |
|------|---------|
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | `npm install -g @anthropic-ai/claude-code` |
| Python 3.10+ | [python.org](https://www.python.org/) |
| XeLaTeX | [TeX Live](https://tug.org/texlive/) or [MacTeX](https://tug.org/mactex/) |

---

## Clone and Set Up

```bash
# 1. Clone with RAG engine submodule
git clone --recurse-submodules https://github.com/YOUR_USER/clo-author-rag.git
cd clo-author-rag

# 2. Install RAG dependencies
pip install -r requirements.txt

# 3. Copy your reference PDFs to papers/ (from cloud storage or USB)

# 4. Index PDFs and start watching for new ones
python watcher.py
#   → indexes existing PDFs and keeps listening
#   → any new PDF you copy is processed automatically
#   → stop with Ctrl+C
#
# Alternative (rebuild index once and exit):
# python watcher.py --once

# 5. Open Claude Code
claude
```

If you already have the repo cloned but the submodule is missing:
```bash
git submodule update --init --recursive
```

---

## First Steps After Cloning

1. **Fill in `CLAUDE.md`** — replace `[BRACKETED PLACEHOLDERS]` with your project details
2. **Fill in `.claude/references/domain-profile.md`** — your journals, data sources, notation, and seminal references. Use `/discover interview` to populate it interactively.
3. **Add your PDFs** to `papers/` and run `python watcher.py --once`
4. **Open Claude Code** and run:

```
I am starting a new research project in [YOUR FIELD] on [YOUR TOPIC].
Read CLAUDE.md and help me set up the project structure.
```

---

## Project Structure

```
your-project/
├── CLAUDE.md                    # Project configuration (fill in placeholders)
├── .claude/                     # Agents, skills, rules, hooks
├── watcher.py                   # RAG indexing script
├── requirements.txt             # RAG dependencies
├── Bibliography_base.bib        # Centralized bibliography
├── papers/                      # Reference PDFs (gitignored — sync via cloud)
├── rag-engine/                  # RAG engine (git submodule)
├── paper/                       # LaTeX manuscript
│   ├── main.tex
│   ├── sections/
│   ├── figures/
│   └── tables/
├── data/                        # Raw and cleaned datasets
├── scripts/                     # Analysis code (R, Python, Julia)
├── quality_reports/             # Plans, session logs, reviews, scores
└── master_supporting_docs/      # Supporting papers and data docs
```

---

## RAG: What Gets Indexed

PDFs placed in `papers/` are processed into `rag-data/` (gitignored — local only). The index is rebuilt with `python watcher.py --once` on any new machine after cloning.

`rag-data/` is never committed. Transfer PDFs via cloud storage; the index regenerates in minutes.

---

## License

MIT. Fork it, customize it, make it yours.

Based on [clo-author](https://github.com/hugosantanna/clo-author) by Hugo Sant'Anna (MIT).
