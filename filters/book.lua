-- book.lua: the book's semantic blocks, rendered for print (LaTeX) and web (HTML/EPUB).
--
-- Authoring syntax (in .qmd):
--   ::: {.tryit lab="ch01"}      ... :::   Try it box (+ QR code in the margin)
--   ::: {.breaks}                ... :::   Where this breaks
--   ::: {.threshold}             ... :::   Set the threshold
--   ::: {.deeper}                ... :::   Going deeper (optional maths)
--   ::: {.keyidea}               ... :::   One-line reveal
--   ::: {.goals}                 ... :::   By the end of this chapter
--   ::: {.exercises}             ... :::   Exercises
--   ::: {.nexthook}              ... :::   Closing hook to the next chapter
--   ::: {.bookquote by="Name, Source"} ... ::: Pull quote
--   ::: {.sidebar title="..."}   ... :::   Neutral sidebar
--   ::: {.wide}                  ... :::   Figure that runs into the outer margin
--   ::: {.summary}               ... :::   Full-page visual summary
--   ::: {.margin}                ... :::   Margin note
--   [[AUTHOR STORY: topic]]  (own paragraph)  -> visible draft marker
--   [[VERIFY]]               (inline)         -> visible draft marker

local is_latex = quarto.doc.is_format("latex") or quarto.doc.is_format("pdf")
local is_html = quarto.doc.is_format("html") or quarto.doc.is_format("epub")

local ENVS = {
  tryit = "tryit", breaks = "breaks", threshold = "threshold", deeper = "deeper",
  keyidea = "keyidea", goals = "goals", exercises = "exercises", nexthook = "nexthook",
  wide = "widefig", summary = "summarypage", partintro = "partintro",
}

local LABELS = {
  tryit = "Try it", breaks = "Where this breaks", threshold = "Set the threshold",
  deeper = "Going deeper", goals = "By the end of this chapter", exercises = "Exercises",
}

local function latex(s) return pandoc.RawBlock("latex", s) end
local function latexi(s) return pandoc.RawInline("latex", s) end

local function escape_tex(s)
  s = s:gsub("\\", "\\textbackslash{}")
  s = s:gsub("([#$%%&_{}])", "\\%1")
  s = s:gsub("~", "\\textasciitilde{}")
  s = s:gsub("%^", "\\textasciicircum{}")
  return s
end

-- ---------------------------------------------------------------- images
function Image(img)
  if not is_latex and img.src:match("%.pdf$") and img.src:match("figures/") then
    img.src = img.src:gsub("%.pdf$", ".svg")
  end
  if is_latex and img.src:sub(1, 1) == "/" then
    img.src = img.src:sub(2)
  end
  return img
end

-- ---------------------------------------------------------------- draft markers
local function marker_text(inlines)
  return pandoc.utils.stringify(inlines)
end

function Para(p)
  local s = marker_text(p.content)
  local topic = s:match("^%[%[AUTHOR STORY:%s*(.-)%]%]$")
  if topic then
    if is_latex then
      return latex("\\authorstory{" .. escape_tex(topic) .. "}")
    else
      return pandoc.Div({pandoc.Para({pandoc.Strong({pandoc.Str("Author story:")}), pandoc.Space(), pandoc.Str(topic)})},
        pandoc.Attr("", {"author-story"}))
    end
  end
  return nil
end

function Inlines(inls)
  -- replace the three-token sequence "[[VERIFY]]" (possibly split) with a marker
  local out = pandoc.Inlines({})
  local i = 1
  while i <= #inls do
    local el = inls[i]
    if el.t == "Str" and el.text:find("%[%[VERIFY%]%]") then
      local before, after = el.text:match("^(.-)%[%[VERIFY%]%](.*)$")
      if before ~= "" then out:insert(pandoc.Str(before)) end
      if is_latex then
        out:insert(latexi("\\verifymark{}"))
      else
        out:insert(pandoc.Span({pandoc.Str("VERIFY")}, pandoc.Attr("", {"verify"})))
      end
      if after ~= "" then out:insert(pandoc.Str(after)) end
    else
      out:insert(el)
    end
    i = i + 1
  end
  return out
end

-- ---------------------------------------------------------------- blocks
function Div(div)
  local cls = nil
  for _, c in ipairs(div.classes) do
    if ENVS[c] or c == "bookquote" or c == "sidebar" or c == "margin" then cls = c break end
  end
  if not cls then return nil end

  if is_latex then
    local blocks = pandoc.List({})
    if cls == "margin" then
      blocks:insert(latex("\\sidenote{"))
      blocks:extend(div.content)
      blocks:insert(latex("}"))
      return blocks
    end
    if cls == "tryit" and div.attributes["lab"] then
      local ch = div.attributes["lab"]
      blocks:insert(latex("\\marginqr{figures/" .. ch .. "/qr.pdf}{Scan to open this chapter's notebook in Colab.}"))
    end
    if cls == "bookquote" then
      blocks:insert(latex("\\begin{bookquote}{" .. escape_tex(div.attributes["by"] or "") .. "}"))
      blocks:extend(div.content)
      blocks:insert(latex("\\end{bookquote}"))
      return blocks
    end
    if cls == "sidebar" then
      blocks:insert(latex("\\begin{sidebar}{" .. escape_tex(string.upper(div.attributes["title"] or "")) .. "}"))
      blocks:extend(div.content)
      blocks:insert(latex("\\end{sidebar}"))
      return blocks
    end
    blocks:insert(latex("\\begin{" .. ENVS[cls] .. "}"))
    blocks:extend(div.content)
    blocks:insert(latex("\\end{" .. ENVS[cls] .. "}"))
    return blocks
  end

  -- HTML / EPUB: keep the div, add a visible label where the print book has one
  local label = LABELS[cls]
  if cls == "sidebar" and div.attributes["title"] then label = div.attributes["title"] end
  if label then
    div.content:insert(1, pandoc.Div({pandoc.Plain({pandoc.Str(label)})}, pandoc.Attr("", {"box-label"})))
  end
  if cls == "bookquote" and div.attributes["by"] then
    div.content:insert(pandoc.Div({pandoc.Plain({pandoc.Str("\u{2014} " .. div.attributes["by"])})}, pandoc.Attr("", {"quote-by"})))
  end
  if cls == "tryit" and div.attributes["lab"] then
    local ch = div.attributes["lab"]
    local url = "https://colab.research.google.com/github/Mukkandi-Sridhar/JEVBook/blob/main/labs/" .. ch .. ".ipynb"
    div.content:insert(pandoc.Para({pandoc.Link({pandoc.Str("Open this chapter's notebook in Colab \u{2192}")}, url)}))
  end
  div.classes:insert("bookbox")
  return div
end

-- ---------------------------------------------------------------- chapter opener map
function Header(h)
  if h.level == 1 then
    local ch = h.identifier:match("^sec%-(ch%d%d)$")
    if ch then
      local map = "figures/" .. ch .. "/map"
      if is_latex then
        return {h, latex("\\vspace{-4pt}\\noindent\\includegraphics[width=\\textwidth]{" .. map .. ".pdf}\\par\\vspace{14pt}\\noindentnext")}
      else
        return {h, pandoc.Para({pandoc.Image({}, "/" .. map .. ".svg", "", pandoc.Attr("", {"you-are-here"}))})}
      end
    end
  end
  return nil
end
