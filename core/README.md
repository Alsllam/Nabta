# core/ — Tutor core (placeholder)

**Provisional name. Nothing here is built until Phase 5's decision records exist.**

This folder will hold the one deployable backend described in `docs/deliverables/architecture.md`
§ Capabilities: curriculum store, learner model, scheduler, content service, speech service,
reports and the parent assistant, and the platform (parent identity, storage, background jobs
with the nightly pack build, the AI gateway with its ports, caps and usage ledger, observability).

- Built in **Phases 6 and 8** (`ROADMAP.md`), in the stack chosen by the ADRs of step E5.
- Module rules it must satisfy: `architecture.md` § Module rules (no shared storage; AI only
  through ports; nothing unvalidated reaches a child; children are not accounts; offline).
- Requirements it implements: `docs/deliverables/srs.md` — `FR-CUR`, `FR-LRN`, `FR-TUT`,
  `FR-CNT`, `FR-SPC`, `FR-RPT`, `FR-AI` and the non-functional tables.

The name may change when the stack is chosen; the responsibilities will not.
