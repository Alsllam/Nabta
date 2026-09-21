# <step-id> — <Experiment title>

> **Step:** <id> · **Module:** A | B | C | D | E · **Date:** <yyyy-mm-dd> · **Status:** planned | run | not run (why)

## Question for Nabta

The one product question this experiment answers (from `docs/PLAN.md` §4, "Nabta question").

## Hypothesis

What I expect to see, stated so it can be wrong. Include the number that would change my mind.

## Method

- **Candidates:** what is compared (models, engines, algorithms). A candidate that is free to
  me is still compared with at least one alternative, and priced at list price.
- **Sample:** what goes in, how many, where it came from. Synthetic text, my own voice, or
  consented adult recordings only — **no child data**.
- **Metrics:** each one defined so someone else could compute it. Arabic quality is rated
  blind by a native speaker (me) with the rubric below.
- **Rubric** (if any rating is subjective): the scale and what each level means.
- **Cost & latency:** recorded for every candidate that has them, in the cost model's units —
  per session, per child-day.

## How to run

```
# keys and endpoints come from environment variables only (see .env.example at the repo root)
<command>
```

Inputs live in `data/`, outputs in `out/` (ignored by git if large or personal).

## Results

| Candidate | Metric 1 | Metric 2 | Cost / session | Latency | n |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

Raw outputs: `out/`. Rating sheet: `ratings.csv` (if any).

## Limits

What this sample and method cannot tell us. Small is fine; hidden is not.

## What this means for Nabta

Two to five sentences: the design choice this changes, confirms or rules out, and the goal or
component it touches.

## Decision

ADR-<nnn> (link) — or "none yet: <what would still need to be true>".
