# Checkpoints

One row per attempt. A phase closes only on a pass answered from memory before the answer is
shown (CLAUDE.md rule 7).

| Date | Phase | Question | Verdict | Note |
| --- | --- | --- | --- | --- |
| 2026-09-21 | 0 | Name the capabilities in PLAN §6 and explain why a child is not a user account | **not passed** — answer requested before attempting | Answer was shown on request; retry next session from memory (spaced retrieval beats immediate retry) |
| 2026-09-21 | 0 | same question, answered after reading the answer | **partial — not passed** | Named the learner model, the speech service and the parent report, and the consent reason for "not an account". Missed the scheduler, the content pipeline (generate → validate → safety → cache) and the AI gateway/platform; listed word lists, harakat and illustrations (out of v1) as capabilities. Retry next session: scheduler + content pipeline + two reasons closes the phase |
