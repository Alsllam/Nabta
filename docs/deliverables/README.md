# Deliverable documents

Markdown sources rendered to `.docx` with `/make-doc <key>` (Pandoc + the reference template in
`_template/`). Keys and the phase each grows in are in `docs/PLAN.md` §10: `vision`, `pedagogy`,
`srs`, `study-notes`, `architecture`, `database`, `api`, `ai-safety`, `privacy`, `user-guide`,
`test-plan`, `pilot-report`. Rendered files go to `docs/deliverables/out/` and are committed, so
the Word versions travel with the repo.

The pipeline is a **documents tool, not a stack choice**: Pandoc renders, a small Python script
generates the style template. Neither is a product decision.

Each document has a front-matter block (title, subtitle in Arabic, version, date, status) and a
revision-history table.

## Building

```powershell
.\docs\deliverables\_template\build.ps1 pedagogy   # one document
.\docs\deliverables\_template\build.ps1 all        # every *.md here except README
```

- `_template/reference.docx` is the style sheet Pandoc copies (fonts, headings, the `RTL` and
  `ChildText` styles, table borders). It is generated — edit `_template/make-reference.py` and
  re-run it (`python make-reference.py` inside `_template/`), never the `.docx` by hand.
- Arabic prose: wrap in `::: {custom-style="RTL"}` … `:::`.
- Text a child would see (always fully diacritised): `::: {custom-style="ChildText"}` … `:::`.
  Large, right-to-left, extra line spacing so harakat do not collide.
- Front matter `title`/`subtitle`/`author`/`date` render on the title page; `version`/`status`
  are metadata only — the revision-history table is the visible version record.
- `smoke.md` is the pipeline's smoke test; re-render it after touching the template.
- Diagrams: write Mermaid in a fence directly under its `![caption](assets/name.png)` line and
  run `python docs/deliverables/_template/render-diagrams.py <key>` before `build.ps1`
  (uses `npx @mermaid-js/mermaid-cli`; the source stays in the `.md`, the PNG is what Word shows —
  `_template/drop-mermaid.lua` removes the source block from the `.docx`).
