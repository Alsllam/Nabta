---
title: "Nabta — Docs Pipeline Smoke Test"
subtitle: "نبتة — اختبار خطّ إنتاج المستندات"
author: "Abdulsalam"
version: "0.1"
date: "2026-09-21"
status: "Draft"
---

# Purpose

This document exists only to prove that Markdown renders to a Word file with the project
template: headings, tables, code, right-to-left Arabic prose, and — the case that matters most
for Nabta — child-facing text with full harakat.

## Revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 0.1 | 2026-09-21 | Abdulsalam | First render |

## Arabic prose

English body text uses the Latin font; the Arabic block below is a fenced div with the `RTL`
custom style, which maps to a Word paragraph style with `bidi` set.

::: {custom-style="RTL"}
نبتة معلّم ذكي متكيّف للأطفال من ٤ إلى ٨ سنوات يعلّمهم القراءة والكتابة والحساب بالعربية.
يهيّئ الوالد ملف الطفل، ثم يلتقي الطفل بنبتة يوميًا في جلسة قصيرة تنتهي دائمًا على نجاح.
:::

## Child-facing text

Everything a child sees is fully diacritised and set in the `ChildText` style: larger, with
extra line spacing so the marks above and below the letters do not collide.

::: {custom-style="ChildText"}
مَاسَة تُنَادِي تُوت.

تُوت لَا يَرُدّ.

تُوت نَامَ!
:::

## Tables

| Code | Name (ar) | Stage | Prerequisites |
| --- | --- | --- | --- |
| `R-L-SOUND-م` | صوت الميم | letters | `R-L-SHAPE-م` |
| `R-H-م-FATHA` | مَ | harakat | `R-L-SOUND-م`, `R-H-FATHA-CONCEPT` |

## Code and lists

```json
{ "kind": "word", "text": "مَاسَة", "letters": ["م", "ا", "س", "ة"], "level": 2 }
```

1. Markdown source lives in `docs/deliverables/<key>.md`.
2. `build.ps1 <key>` renders it to `out/<Key>.docx`.
3. Both are committed, so Word files travel with the repo.
