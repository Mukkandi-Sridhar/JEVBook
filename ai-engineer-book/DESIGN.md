# Ship Real AI: book design plan

Status: proposal, 28 October 2026. Nothing is built until this is approved.

## 1. What the design must do

1. **Match the teaching method.** Every section runs problem → reader tries → mechanism → name → rule →
   trade-off. The page must show these steps clearly, so a reader always knows where they are.
2. **Feel like a bootcamp, not a reference book.** Modules, drills, checkpoints and a project that grows.
3. **Print well in black and white.** A 500+ page colour interior costs about two to four times as much to print
   on KDP, and colour is all-or-nothing for the whole book. So the print edition is greyscale; the ebook keeps
   colour. Nothing may depend on colour alone.
4. **Make code and diagrams easy to read.** A wide text column, no side margins that squeeze code.
5. **Look unlike the JEV book.** No green, no bold key-idea headline boxes, no JEV fonts.

## 2. Research findings that shaped the choice

- **Signalling helps learning.** Clear visual cues (labels, highlighting, arrows) reduce mental effort and improve
  transfer. → Every learning step gets the same label and icon every time.
- **Worked examples work best in segments.** Examples split into clear steps take less effort for the same result.
  → Numbered steps and calculations set out line by line.
- **Practice should come right after a worked example.** → A short "Your turn" follows each worked example.
- **Print constraints.** Colour printing is costly and all-or-nothing; convert images to greyscale ourselves for
  control; keep colour for the ebook.
- **Good programming books are rare and most are dull.** Readers praise books that use grey shading for code and
  annotated callouts. → Grey code panels and numbered code callouts.

## 3. Three directions considered

| | A. Field manual | B. Classic (Tufte style) | C. Visual (Head First style) |
|---|---|---|---|
| Feel | Bootcamp: modules, drills, checkpoints | Calm, academic, wide margin notes | Playful, pictures and jokes |
| Code | Full-width, easy | Squeezed by the margin column | Fine |
| Print cost | Normal | About 15% more pages | High (many images) |
| Fits our method | Yes, each step has a block | Partly | Partly; too informal for interviews |
| Effort to build | Medium | Low | Very high |

**Choice: A, the field manual, with B's calm typography.** It looks like a training course, keeps code wide, and
gives each step of the teaching method its own clear place on the page.

## 4. The chosen design

### 4.1 Page and type

- **Trim:** 7 × 10 in (already set). Single column, text width about 5.2 in.
- **Fonts:** IBM Plex Serif for reading (10.5 pt), Work Sans for headings and labels, IBM Plex Mono for code.
- **Ink:** navy (#1B2A4A) as the main colour, saffron (#D97706) as the one accent. In greyscale, navy prints as
  near-black and saffron as mid-grey, and every element also has a label or shape.
- **Running heads:** module name on the left page, section name on the right; page number outside.

### 4.2 Module opener (one full page per module)

- Large module number ("07") and title.
- **Builds on:** one line naming the earlier module.
- **You will be able to:** three bullets.
- **The system map**, small, with this module's layer shaded.
- **Checkpoint quiz:** three quick questions on earlier modules, answers at the back.

### 4.3 Thumb tabs

A dark tab on the outer page edge, moved down a step for each module group, with the module number in white.
Readers can find a module by flicking the closed book. Needs bleed on KDP, which is supported.

### 4.4 The learning blocks

Each block has a small square icon, a label in Work Sans small caps, and its own shape, so it reads in greyscale.

| Block | Purpose (teaching-method step) | Look |
|---|---|---|
| **Problem** | Opens a section with the failure or cost | Thick left rule, no fill |
| **Try first** | "Before reading on, …" prompt | Dashed outline, pencil icon, blank lines to write on |
| **Worked numbers** | A calculation set out line by line | Grey fill, numbers right-aligned in Plex Mono |
| **Trace** | A request followed step by step | Numbered circles down a thin vertical line |
| **Rule** | The one thing to remember from the section | Saffron/grey bar above and below, one line |
| **Trade-off** | When to use it, when not to | Two columns: "Use when" / "Avoid when" |
| **Break it** | What goes wrong in production | Black corner flag, "Break it" label |
| **Interview words** | The exact terms to use, in sentences | Small, boxed, speech-mark icon |
| **Your turn** | Practice right after a worked example | Checkbox list |
| **Project** | The capstone step for this module | Full-width band at the end of the module |
| **Defend** | Numbers you must justify | Table with "Number / Why" columns |

The old box names (glance, remember, project, decision, production, defend, practice, interview) map onto this
set. "Remember" becomes **Rule**, "Production" becomes **Break it**, "Decision" becomes **Trade-off**.

### 4.5 Code

- Grey panel, no colour syntax highlighting in print (weight and italics only); colour in the ebook.
- Line numbers off by default; numbered callout markers (❶ ❷ ❸) on key lines, explained just below the code.
- Never split a code block across pages; no block longer than 15 lines.

### 4.6 Diagrams

- One house style for all flow diagrams: rounded boxes, numbered arrows, navy lines, grey fills.
- The system map appears at every module opener with the current layer shaded.
- Charts follow the existing `figstyle.py`, checked in greyscale before use.

### 4.7 End of module

1. Checklist (collected Rules)
2. Break it
3. Defend
4. Project
5. Practice, then Interview questions
6. Up next (one line)

### 4.8 Ebook

Same structure, full colour, reflowable. Blocks keep their labels and icons, so they work on any screen.

## 5. Build plan once approved

1. Rename the box classes in `filters/book.lua` and add the new ones (try first, worked numbers, trace, trade-off,
   your turn).
2. Redesign the boxes in `preamble.tex`; add the module opener and thumb tabs.
3. Build a 6-page sample: module opener, one full section using every block, end of module.
4. Check the sample in colour and in greyscale (and a photocopy-style test).
5. Then rewrite Part I into Modules 1–3 in the new design.
