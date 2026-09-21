-- Pandoc Lua filter: drop Mermaid source blocks from the rendered document.
-- The Markdown keeps the diagram source (diffable, reviewable); Word shows the PNG that
-- render-diagrams.py produced from it. Without this filter the .docx would show both.
function CodeBlock(el)
  if el.classes:includes("mermaid") then
    return {}
  end
end
