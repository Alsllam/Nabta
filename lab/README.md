# lab/ — Experiments

One folder per experiment, named `<step-id>-<slug>/`, started from [`TEMPLATE/`](TEMPLATE/README.md):
hypothesis stated so it can be wrong · method (candidates, sample, metrics, rubric) · how to run
· results table · limits · what this means for Nabta · decision (ADR link or "none yet").

| Folder | Step | What it measures | Status |
| --- | --- | --- | --- |
| [`0.4-skill-graph/`](0.4-skill-graph/README.md) | 0.4a | The skill graph is a well-formed DAG; the frontier behaves (concept unlocks at 3 sounds) | run — 328 nodes, acyclic |

Study experiments (A1 … E4) are added as Phases 1–5 are expanded.

## Rules (from `CLAUDE.md`)

- **Measure, don't assume.** Every comparison has a table: candidates × metrics, with the sample
  size. Arabic quality is rated blind by a native speaker with a written rubric.
- **Small is fine, hidden is not.** State the sample and its limits.
- **Record cost and latency** for every candidate that has them, per session and per child-day,
  at **list price** — a provider that is free to the developer is still costed.
- **A free candidate is measured beside at least one alternative.**
- **Keys and endpoints come from environment variables only**, read inside `lab/` and nowhere
  else. Copy `.env.example` (repo root) to `.env`; `.env` is ignored by git.
- **No child data.** Synthetic text, the developer's own voice, or consented adult recordings
  only. Audio files and `out/` folders under `lab/` are ignored by git.
- **The lab runtime** (language, environment) is chosen in step 1.1 by ADR-001 on one criterion:
  how fast we learn with it. `0.4-skill-graph/check_graph.py` predates that decision and moves
  with it if needed.
