"""Build reference.docx — the *style sheet* Pandoc copies into every deliverable.

Pandoc only takes styles (fonts, colours, spacing) from the reference file; its content is
ignored. Think of it as a theme file for Word. This script is the source of truth — never edit
reference.docx by hand. Re-run after editing:  python make-reference.py

This is a documents tool, not a stack choice (ROADMAP 0.2): it produces Word files and touches
nothing in the product.
"""
import subprocess
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

LATIN = "Calibri"     # body text for English
# Complex-script font for Arabic. Arial ships with every Windows and renders harakat (fatha,
# kasra, damma, sukoon, shadda) correctly on top of every letter form — which matters here,
# because the pedagogy and safety documents quote fully diacritised child-facing text.
ARABIC = "Arial"
ACCENT = RGBColor(0x2F, 0x7A, 0x55)   # Nabta leaf green (the prototype's primary colour)

# 1. Start from Pandoc's own default so every style Pandoc emits exists.
subprocess.run(["pandoc", "-o", "reference.docx", "--print-default-data-file", "reference.docx"], check=True)
doc = Document("reference.docx")


def set_fonts(style, size=None, bold=None, color=None):
    style.font.name = LATIN
    if size: style.font.size = Pt(size)
    if bold is not None: style.font.bold = bold
    if color: style.font.color.rgb = color
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts"); rpr.append(rfonts)
    # Word picks the font per script: ascii/hAnsi for Latin runs, cs for Arabic runs.
    # Both must be set or Arabic falls back to whatever Word guesses.
    for attr in ("w:ascii", "w:hAnsi", "w:eastAsia"):
        rfonts.set(qn(attr), LATIN)
    rfonts.set(qn("w:cs"), ARABIC)


for name in ("Normal", "Body Text", "First Paragraph", "Compact"):
    set_fonts(doc.styles[name], size=11)
set_fonts(doc.styles["Title"], size=26, bold=True, color=ACCENT)
set_fonts(doc.styles["Subtitle"], size=16, color=ACCENT)
for level, size in ((1, 18), (2, 14), (3, 12), (4, 11)):
    set_fonts(doc.styles[f"Heading {level}"], size=size, bold=True, color=ACCENT)


def add_rtl_style(name, base, size):
    """A right-to-left paragraph style, used from Markdown as  ::: {custom-style="<name>"}."""
    style = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
    style.base_style = doc.styles[base]
    style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    set_fonts(style, size=size)
    ppr = style.element.get_or_add_pPr()
    ppr.append(OxmlElement("w:bidi"))      # paragraph direction = right-to-left
    rpr = style.element.get_or_add_rPr()
    rpr.append(OxmlElement("w:rtl"))       # run direction, so punctuation sits on the correct side
    return style


# 2. RTL — ordinary Arabic prose (summaries, glossary entries, the parent-facing sections).
add_rtl_style("RTL", "Body Text", 12)
# 3. ChildText — text a child would see: fully diacritised, large, one idea per line. Kept as
#    its own style so a reviewer can spot every child-facing sample in a document at a glance.
child = add_rtl_style("ChildText", "RTL", 18)
child.paragraph_format.space_before = Pt(6)
child.paragraph_format.space_after = Pt(6)
child.paragraph_format.line_spacing = 1.6  # harakat need vertical room or they collide with the line above

# 4. Tables: Pandoc uses the "Table" style; give it borders.
tbl = doc.styles["Table"]
tpr = tbl.element.find(qn("w:tblPr"))
if tpr is None:
    tpr = OxmlElement("w:tblPr"); tbl.element.append(tpr)
borders = OxmlElement("w:tblBorders")
for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
    b = OxmlElement(f"w:{edge}")
    b.set(qn("w:val"), "single"); b.set(qn("w:sz"), "4"); b.set(qn("w:color"), "BFBFBF")
    borders.append(b)
tpr.append(borders)

doc.save("reference.docx")
print("reference.docx written; custom styles:", ", ".join(s.name for s in doc.styles if s.name in ("RTL", "ChildText", "Table")))
