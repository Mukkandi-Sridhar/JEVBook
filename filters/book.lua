-- book.lua: the book's semantic blocks, rendered for print (LaTeX) and web (HTML/EPUB).
--
-- Authoring syntax (in .qmd):
--   ::: {.tryit lab="ch01"}      ... :::   Try it box (web: link to the chapter's notebook)
--   ::: {.breaks}                ... :::   Where this breaks
--   ::: {.threshold}             ... :::   Set the threshold
--   ::: {.deeper}                ... :::   Going deeper (optional maths)
--   ::: {.keyidea}               ... :::   Key idea: one sentence to remember (listed again in "Keep these" and the appendix)
--   ::: {.keyideaslist}          ... :::   The Key ideas appendix (back/key-ideas.qmd, made by tools/make_key_ideas.py)
--   [ ]{.kref ref="key-ch05-2"}             Page number (print) or link (ebook) for a key idea, used in that appendix
--   ::: {.goals}                 ... :::   By the end of this chapter
--   ::: {.exercises}             ... :::   Exercises
--   ::: {.nexthook}              ... :::   Closing hook to the next chapter
--   ::: {.bookquote by="Name, Source"} ... ::: Pull quote
--   ::: {.epigraph by="Name, Source"}  ... ::: Short quotation under a chapter title
--   ::: {.sidebar title="..."}   ... :::   Neutral sidebar
--   ::: {.wide}                  ... :::   Figure that runs into the outer margin
--   ::: {.summary}               ... :::   (dropped from all outputs)
--   ::: {.margin}                ... :::   Margin note
--   [[AUTHOR STORY: topic]]  (own paragraph)  -> marker in draft builds, hidden in print
--   [[VERIFY]]               (inline)         -> marker in draft builds, hidden in print

local is_latex = quarto.doc.is_format("latex") or quarto.doc.is_format("pdf")
local is_epub = quarto.doc.is_format("epub")
-- Draft markers ([[AUTHOR STORY]], [[VERIFY]]) show only in a draft build: BOOK_DRAFT=1 quarto render
local draft = os.getenv("BOOK_DRAFT") == "1"
local is_html = quarto.doc.is_format("html") or quarto.doc.is_format("epub")

local ENVS = {
  tryit = "tryit", breaks = "breaks", threshold = "threshold", deeper = "deeper",
  keyidea = "keyidea", goals = "goals", exercises = "exercises", nexthook = "nexthook",
  wide = "widefig", summary = "summarypage", partintro = "partintro", indexlist = "indexlist",
  keepthese = "keepthese", keyideaslist = "keyideaslist",
}

local LABELS = {
  tryit = "Try it", breaks = "Where this breaks", threshold = "Set the threshold",
  deeper = "Going deeper", goals = "By the end of this chapter", exercises = "Exercises",
  keyidea = "Key idea", keepthese = "Keep these",
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
    -- the ebook gets 300 dpi PNGs (made by tools/epub_figures.py); e-readers handle them better than SVG
    img.src = img.src:gsub("%.pdf$", is_epub and ".png" or ".svg")
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
    if not draft then return {} end
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
      if not draft then
        -- print build: drop the marker and the space before it
        if #out > 0 and (out[#out].t == "Space" or out[#out].t == "SoftBreak") then out:remove(#out) end
      elseif is_latex then
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
    if ENVS[c] or c == "bookquote" or c == "epigraph" or c == "sidebar" or c == "margin" then cls = c break end
  end
  if not cls then return nil end
  if cls == "summary" then return {} end          -- one-page summaries repeat "Where we are"; not printed

  if is_latex then
    local blocks = pandoc.List({})
    if cls == "margin" then
      blocks:insert(latex("\\begin{asidenote}"))
      blocks:extend(div.content)
      blocks:insert(latex("\\end{asidenote}"))
      return blocks
    end
    if cls == "bookquote" then
      blocks:insert(latex("\\begin{bookquote}{" .. escape_tex(div.attributes["by"] or "") .. "}"))
      blocks:extend(div.content)
      blocks:insert(latex("\\end{bookquote}"))
      return blocks
    end
    if cls == "epigraph" then
      blocks:insert(latex("\\begin{chapterepigraph}{" .. escape_tex(div.attributes["by"] or "") .. "}"))
      blocks:extend(div.content)
      blocks:insert(latex("\\end{chapterepigraph}"))
      return blocks
    end
    if cls == "sidebar" then
      blocks:insert(latex("\\needspace{7\\baselineskip}\\begin{sidebar}{" .. escape_tex(string.upper(div.attributes["title"] or "")) .. "}"))
      blocks:extend(div.content)
      blocks:insert(latex("\\end{sidebar}"))
      return blocks
    end
    local keep = cls == "deeper" and "\\needspace{7\\baselineskip}" or ""
    local label = (div.identifier ~= "" and cls == "keyidea") and ("\\phantomsection\\label{" .. div.identifier .. "}") or ""
    blocks:insert(latex(keep .. "\\begin{" .. ENVS[cls] .. "}" .. label))
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
  if (cls == "bookquote" or cls == "epigraph") and div.attributes["by"] then
    div.content:insert(pandoc.Div({pandoc.Plain({pandoc.Str("\u{2014} " .. div.attributes["by"])})}, pandoc.Attr("", {"quote-by"})))
  end
  div.classes:insert("bookbox")
  return div
end

-- Key idea references in the appendix: a page number in print, a link in the ebook, nothing on the web (where
-- each chapter is its own page).
function Span(el)
  local kref = false
  for _, c in ipairs(el.classes) do if c == "kref" then kref = true end end
  if not kref then return nil end
  local ref = el.attributes["ref"] or ""
  if is_latex then return latexi("\\keypage{" .. ref .. "}") end
  if is_epub then return pandoc.Link({pandoc.Str("\u{2192}")}, "#" .. ref, "", pandoc.Attr("", {"kref"})) end
  return {}
end

-- Chapters open with their title only: no progress map (removed for a cleaner print page).

-- Short code names with hyphens (jev-mock-synthetic, x-jevkit-synthetic) must not break across lines in print.
function Code(el)
  if not is_latex then return nil end
  if el.text:find("-", 1, true) and not el.text:find("%s") and #el.text <= 34 then
    return {latexi("\\mbox{"), el, latexi("}")}
  end
end

-- ---------------------------------------------------------------- print index
-- tools/make_index.py lists the terms in back/index-terms.json. In print, a term gets a LaTeX \index entry where
-- a paragraph defines it in bold and, unless it's an ordinary word ("strict"), at its first mention in each chapter.
local function load_index_terms()
  local dir = (quarto and quarto.project and quarto.project.directory) or "."
  local fh = io.open(dir .. "/back/index-terms.json", "r")
  if not fh then return {} end
  local data = pandoc.json.decode(fh:read("*a"))
  fh:close()
  return data.terms or {}
end

local function lua_escape(s) return (s:gsub("[%^%$%(%)%%%.%[%]%*%+%-%?]", "%%%0")) end

local function index_matches(text, lower, patterns)
  for _, p in ipairs(patterns) do
    local src = (p ~= p:lower()) and text or lower              -- capitals mean case-sensitive
    local prefix = p:sub(-1) == "*"
    local body = prefix and p:sub(1, -2) or p
    local pat = lua_escape(body)
    if body:sub(1, 1):match("%w") then pat = "%f[%w]" .. pat end
    if not prefix and body:sub(-1):match("%w") then pat = pat .. "%f[^%w]" end
    if src:find(pat) then return true end
  end
  return false
end

local function index_entry(t, suffix)
  local shown = t.display:gsub("([&%%#_])", "\\%1")
  if t.code then shown = "\\texttt{" .. shown .. "}" end
  local key = t.sort:gsub("[!@|\"]", "")
  return pandoc.RawInline("latex", "\\index{" .. key .. "@" .. shown .. (suffix or "") .. "}")
end

local function taught_in(t, chapter)
  for _, c in ipairs(t.taught or {}) do if c == chapter then return true end end
  return false
end

-- Two passes over the same blocks, in the same order. Pass 1 numbers the paragraphs of each chapter and finds the
-- first and last paragraph that mention each taught term; pass 2 writes the entries: a page range (|( ... |)) for a
-- taught term in a chapter that teaches it, nothing for it elsewhere, and for other terms an entry at a bold
-- definition or (unless strict) at the first mention in each chapter.
local function index_blocks(blocks, st)
  for i = 1, #blocks do
    local b = blocks[i]
    -- the "Keep these" list repeats the chapter's key ideas; it mustn't stretch a term's page range
    if b.t == "RawBlock" and b.text:find("\\begin{keepthese}", 1, true) then st.skip = true
    elseif b.t == "RawBlock" and b.text:find("\\end{keepthese}", 1, true) then st.skip = false
    elseif st.skip then -- inside "Keep these"
    elseif b.t == "Header" and b.level == 1 then
      local id = b.identifier or ""
      local n = id:match("^sec%-ch(%d+)")
      if n then st.chapter, st.seen, st.para = tonumber(n), {}, 0 else st.chapter = nil end
    elseif st.chapter and (b.t == "Para" or b.t == "Plain") then
      st.para = st.para + 1
      local text = pandoc.utils.stringify(b)
      local lower = text:lower()
      local strong = {}
      pandoc.walk_block(b, {Strong = function(s) strong[#strong + 1] = pandoc.utils.stringify(s) end})
      local stext = table.concat(strong, " | ")
      local slower = stext:lower()
      local adds = {}
      for _, t in ipairs(st.terms) do
        if #(t.taught or {}) > 0 then
          if taught_in(t, st.chapter) and index_matches(text, lower, t.patterns) then
            local key = t.display .. "@" .. st.chapter
            if st.pass == 1 then
              st.span[key] = st.span[key] or {first = st.para}
              st.span[key].last = st.para
            else
              local sp = st.span[key]
              if sp.first == sp.last then adds[#adds + 1] = index_entry(t)
              elseif st.para == sp.first then adds[#adds + 1] = index_entry(t, "|(")
              elseif st.para == sp.last then adds[#adds + 1] = index_entry(t, "|)") end
            end
          end
        elseif st.pass == 2 then
          local defined = #strong > 0 and index_matches(stext, slower, t.patterns)
          local first = (not t.strict) and (not st.seen[t.display]) and index_matches(text, lower, t.patterns)
          if defined or first then
            st.seen[t.display] = true
            adds[#adds + 1] = index_entry(t)
          end
        end
      end
      if #adds > 0 then
        for k = #adds, 1, -1 do b.content:insert(1, adds[k]) end
        blocks[i] = b
      end
    elseif b.t == "Div" or b.t == "BlockQuote" then
      b.content = index_blocks(b.content, st)
      blocks[i] = b
    elseif b.t == "BulletList" or b.t == "OrderedList" then
      local items = b.content
      for k = 1, #items do items[k] = index_blocks(items[k], st) end
      b.content = items
      blocks[i] = b
    end
  end
  return blocks
end

function Pandoc(doc)
  if not is_latex then return nil end
  local terms = load_index_terms()
  if #terms == 0 then return nil end
  local span = {}
  index_blocks(doc.blocks:clone(), {terms = terms, chapter = nil, seen = {}, span = span, pass = 1, para = 0})
  doc.blocks = index_blocks(doc.blocks, {terms = terms, chapter = nil, seen = {}, span = span, pass = 2, para = 0})
  return doc
end

-- ---------------------------------------------------------------- key ideas
-- Runs before everything else. Each ::: {.keyidea} in a chapter gets the id key-chNN-K (K counts within the chapter,
-- in order; tools/make_key_ideas.py numbers them the same way). Just before the chapter's exercises, a "Keep these"
-- box repeats the chapter's key ideas as a list.
local function has_class(el, c)
  for _, x in ipairs(el.classes) do if x == c then return true end end
  return false
end

local function key_blocks(blocks, st)
  local out = pandoc.List({})
  for _, b in ipairs(blocks) do
    if b.t == "Header" and b.level == 1 then
      local n = (b.identifier or ""):match("^sec%-ch(%d+)")
      st.chapter, st.keys = n and tonumber(n) or nil, {}
      out:insert(b)
    elseif b.t == "Div" and has_class(b, "keyidea") and st.chapter then
      st.keys[#st.keys + 1] = b.content
      b.identifier = string.format("key-ch%02d-%d", st.chapter, #st.keys)
      out:insert(b)
    elseif b.t == "Div" and has_class(b, "exercises") and st.chapter and #st.keys > 0 then
      local items = {}
      for _, k in ipairs(st.keys) do
        local inl = pandoc.List({})
        for _, kb in ipairs(k) do if kb.content then inl:extend(kb.content) end end
        items[#items + 1] = {pandoc.Plain(inl)}
      end
      out:insert(pandoc.Div({pandoc.BulletList(items)}, pandoc.Attr("", {"keepthese"})))
      st.keys = {}
      out:insert(b)
    elseif b.t == "Div" then
      b.content = key_blocks(b.content, st)
      out:insert(b)
    else
      out:insert(b)
    end
  end
  return out
end

local function key_ideas(doc)
  doc.blocks = key_blocks(doc.blocks, {chapter = nil, keys = {}})
  return doc
end

return {
  {Pandoc = key_ideas},
  {Image = Image, Para = Para, Inlines = Inlines, Div = Div, Span = Span, Code = Code, Pandoc = Pandoc},
}
