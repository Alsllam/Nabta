# child-app/ — Child experience (placeholder)

**Provisional name. Nothing here is built until Phase 5's decision records exist.**

This folder will hold the child's app: the garden, the daily session, the template activities
with their skins, cached audio, stroke capture for tracing, the offline activity pack, and
result submission that is idempotent on client-generated ids. It also holds the parent lock
with quick settings (session minutes, microphone) — everything else a parent does lives on the
parent web (SRS, proposed decision D-2026-09-21-8).

- Built in **Phase 7**, in the platform class chosen at E5 (native · cross-platform toolkit ·
  web/PWA), scored against `srs.md` NFR-PERF (≤ 100 ms touch response), NFR-OFF (full session
  with no network, pack ≤ 60 MB planning), NFR-DEV (device floor; ≥ 12 cm canvas for tracing)
  and NFR-ACC (no reading required, ≥ 64 px targets, reduced motion).
- Interaction design: the private design prototype of 2026-09-21 (13 screens) referenced in
  `vision.md`'s appendix; the child never reads an instruction, nothing is ever red.

The name may change when the platform is chosen; the goals G1–G6 and G12 will not.
