-- {{< num ch21 auto_rate pct >}} -> a number from results/ch21.json, formatted.
-- Formats: pct (12%), pct1 (12.3%), int (12,345), f1, f2, f3, money ($12,345), raw
local cache = {}

local function load(ch)
  if cache[ch] then return cache[ch] end
  local path = quarto.project.directory .. "/results/" .. ch .. ".json"
  local fh = io.open(path, "r")
  if not fh then error("num: missing results file " .. path) end
  local data = quarto.json.decode(fh:read("*a"))
  fh:close()
  cache[ch] = data
  return data
end

local function commas(n)
  local s = string.format("%d", math.floor(n + 0.5))
  local out = s:reverse():gsub("(%d%d%d)", "%1,"):reverse()
  return (out:gsub("^,", ""):gsub("^%-,", "-"))
end

local function fmt(v, f)
  if type(v) ~= "number" then return tostring(v) end
  if f == "pct" then return string.format("%.0f%%", v * 100)
  elseif f == "pct1" then return string.format("%.1f%%", v * 100)
  elseif f == "int" then return commas(v)
  elseif f == "money" then return "$" .. commas(v)
  elseif f == "f1" then return string.format("%.1f", v)
  elseif f == "f2" then return string.format("%.2f", v)
  elseif f == "f3" then return string.format("%.3f", v)
  elseif f == "f4" then return string.format("%.4f", v)
  else return tostring(v) end
end

return {
  ["num"] = function(args)
    local ch = pandoc.utils.stringify(args[1])
    local key = pandoc.utils.stringify(args[2])
    local f = args[3] and pandoc.utils.stringify(args[3]) or "raw"
    local data = load(ch)
    local v = data
    for part in key:gmatch("[^%.]+") do
      if type(v) ~= "table" then v = nil break end
      v = v[part]
    end
    if v == nil then error("num: no key '" .. key .. "' in results/" .. ch .. ".json") end
    local s = fmt(v, f)
    if quarto.doc.is_format("latex") then s = s:gsub("%%", "\\%%"):gsub("%$", "\\$") return pandoc.RawInline("latex", s) end
    return pandoc.Str(s)
  end
}
