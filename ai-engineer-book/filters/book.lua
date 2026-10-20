-- book.lua: the boxes of The Applied AI Engineer, for print (LaTeX) and screen (HTML/EPUB).
--
--   ::: {.glance}      ... :::   This chapter (three points)
--   ::: {.remember}    ... :::   One sentence to remember; collected into the chapter checklist
--   ::: {.project}     ... :::   Build it: Kaveri Kart
--   ::: {.decision}    ... :::   Design decision
--   ::: {.production}  ... :::   In production, this goes wrong
--   ::: {.defend}      ... :::   Defend your numbers
--   ::: {.practice}    ... :::   Practice (the chapter checklist is inserted just before it)
--   ::: {.interview}   ... :::   Interview corner
--   ::: {.nexthook}    ... :::   Up next
--   ::: {.partintro}   ... :::   Part opener text
--   ::: {.sidebar title="..."} ::: Sidebar
--   [[VERIFY]] (inline) -> marker in draft builds (BOOK_DRAFT=1), dropped in print

local is_latex = quarto.doc.is_format("latex") or quarto.doc.is_format("pdf")
local draft = os.getenv("BOOK_DRAFT") == "1"

local ENVS = {glance = true, remember = true, project = true, decision = true, production = true, defend = true,
  practice = true, interview = true, nexthook = true, partintro = true, checklist = true, sidebar = true}
local LABELS = {glance = "This chapter", remember = "Remember", project = "Build it: Kaveri Kart",
  decision = "Design decision", production = "In production, this goes wrong", defend = "Defend your numbers",
  practice = "Practice", interview = "Interview corner", nexthook = "Up next", checklist = "Chapter checklist"}

local function latex(s) return pandoc.RawBlock("latex", s) end
local function has_class(el, c)
  for _, x in ipairs(el.classes) do if x == c then return true end end
  return false
end

function Image(img)
  if is_latex and img.src:sub(1, 1) == "/" then img.src = img.src:sub(2) end
  if not is_latex and img.src:match("%.pdf$") then img.src = img.src:gsub("%.pdf$", ".png") end
  return img
end

function Inlines(inls)
  local out = pandoc.Inlines({})
  for _, el in ipairs(inls) do
    if el.t == "Str" and el.text:find("%[%[VERIFY%]%]") then
      local before, after = el.text:match("^(.-)%[%[VERIFY%]%](.*)$")
      if before ~= "" then out:insert(pandoc.Str(before)) end
      if draft then
        out:insert(is_latex and pandoc.RawInline("latex", "\\verifymark{}") or pandoc.Span({pandoc.Str("VERIFY")}, pandoc.Attr("", {"verify"})))
      elseif #out > 0 and (out[#out].t == "Space" or out[#out].t == "SoftBreak") then
        out:remove(#out)
      end
      if after ~= "" then out:insert(pandoc.Str(after)) end
    else
      out:insert(el)
    end
  end
  return out
end

function Div(div)
  local cls
  for _, c in ipairs(div.classes) do if ENVS[c] then cls = c break end end
  if not cls then return nil end
  if is_latex then
    local blocks = pandoc.List({})
    local arg = cls == "sidebar" and ("{" .. string.upper(div.attributes["title"] or "") .. "}") or ""
    blocks:insert(latex("\\begin{" .. cls .. "}" .. arg))
    blocks:extend(div.content)
    blocks:insert(latex("\\end{" .. cls .. "}"))
    return blocks
  end
  local label = LABELS[cls] or div.attributes["title"]
  if label then div.content:insert(1, pandoc.Div({pandoc.Plain({pandoc.Str(label)})}, pandoc.Attr("", {"box-label"}))) end
  div.classes:insert("bookbox")
  return div
end

-- Runs first: collect each chapter's Remember notes and repeat them as a checklist just before Practice.
local function collect(blocks, st)
  local out = pandoc.List({})
  for _, b in ipairs(blocks) do
    if b.t == "Header" and b.level == 1 then
      st.notes = {}
      out:insert(b)
    elseif b.t == "Div" and has_class(b, "remember") then
      st.notes[#st.notes + 1] = b.content
      out:insert(b)
    elseif b.t == "Div" and has_class(b, "practice") and #st.notes > 0 then
      local items = {}
      for _, n in ipairs(st.notes) do
        local inl = pandoc.List({})
        for _, nb in ipairs(n) do if nb.content then inl:extend(nb.content) end end
        items[#items + 1] = {pandoc.Plain(inl)}
      end
      out:insert(pandoc.Div({pandoc.BulletList(items)}, pandoc.Attr("", {"checklist"})))
      st.notes = {}
      out:insert(b)
    else
      out:insert(b)
    end
  end
  return out
end

return {
  {Pandoc = function(doc) doc.blocks = collect(doc.blocks, {notes = {}}) return doc end},
  {Image = Image, Inlines = Inlines, Div = Div},
}
