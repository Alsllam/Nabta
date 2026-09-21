# Decision records

**The only door a technology can enter this repo through.** One file per decision:
`ADR-<nnn>-<slug>.md`, from `TEMPLATE.md`, with Context · Options considered (the candidates
and the numbers from the experiment that compared them) · Decision · Consequences · Experiment.

- The plan's **P-1 … P-7** (`docs/PLAN.md` §8.2) are the baseline product and process
  decisions; they are not ADRs.
- Every open component in `docs/PLAN.md` §8.1 gets an ADR in the study step that decides it.
  **ADR-001** is reserved for the lab runtime (step 1.1). Phase 5 step E5 ends with one ADR per
  remaining component; only then are the build phases expanded.
- An ADR without a linked experiment and a results table is a draft, not a decision.
- Superseding: write a new ADR that names the old one; never edit a decision in place.
- Referenced by `/make-doc architecture` and `/make-doc study-notes`.

| ADR | Title | Status | Decided in |
| --- | --- | --- | --- |
| 001 | Lab runtime | reserved | 1.1 |
