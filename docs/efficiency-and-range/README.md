# Efficiency and range paper — build tooling

Source and build scripts for the published page
[`/efficiency-and-range.md`](../../efficiency-and-range.md)
("How Range and Efficiency Are Calculated").

This folder lives under `docs/`, which `_config.yml` excludes from the built
site, so nothing here is published.

## Files

| File | Role |
|---|---|
| `efficiency-and-range.src.md` | **The source of truth.** Markdown + LaTeX math |
| `render.mjs` | Renders the math to MathML and writes the published page |
| `preview.sh` | **The editing loop.** Runs all four build stages; `--watch` to rebuild on save |
| `annotate.py` | Draws the annotated screenshots from raw captures + `callouts.json` |
| `callouts.json` | Crop boxes, callout points and label copy, in raw-capture pixels |
| `screenshots/raw/` | The unannotated captures. Committed — they are the input |
| `preview.py` | Builds a self-contained `preview.html` from the local Jekyll build |
| `package.json` | Pins KaTeX (the only dependency) |
| `../../_layouts/paper.html` | The page's own layout — typography, contents rail, all CSS |

## The paper does not use the site theme

It renders through `_layouts/paper.html`, not just-the-docs: a serif reading
column with its own light/dark palette and a sticky contents rail, because a
document read start-to-finish wants different treatment from a docs page.
The rail's first item links back to the support site, and the site's normal
navigation still lists the paper from every other page — so it is reachable
in both directions without belonging to the docs chrome.

The rail is built from the `sections:` list in the generated page's front
matter, which `render.mjs` derives from the H2 headings. It also stamps
explicit kramdown IDs (`{#s1}`, `{#s2}`, …) on those headings so a rail link
can never drift from its target when a heading is reworded.

## Editing the paper

Edit `efficiency-and-range.src.md`, never the generated page.

**The copy lives in two files, not one.** Prose is in `efficiency-and-range.src.md`.
The text *inside* the figures — every callout label, its detail line, and each
figure's caption — is in `callouts.json`, because it is drawn into the PNG.
Editing the Markdown will not change a word that appears in a picture.

```sh
cd docs/efficiency-and-range
npm install            # first time only
./preview.sh --watch   # rebuild on every save, ~6s a cycle
```

`preview.sh` runs all four stages in order and is the recommended way to edit.
The individual steps, if you need them:

```sh
python3 annotate.py  # regenerates ../../assets/images/efficiency-and-range/*.png
node render.mjs      # regenerates ../../efficiency-and-range.md
```

`annotate.py` only needs re-running when a raw capture or `callouts.json`
changes; `render.mjs` does not depend on it. Run both when in doubt — each is
idempotent and takes under a second.

`render.mjs` converts only the math. Prose, tables, and code fences stay
Markdown for kramdown to render; `_layouts/paper.html` styles the result.

## The figures

Part 1's screenshots are generated, not hand-drawn. `screenshots/raw/` holds the
unannotated captures; `callouts.json` says where to crop and what to point at;
`annotate.py` draws the result into `assets/images/efficiency-and-range/`.

The point of the split is that a UI change costs one screenshot rather than a
redrawing session: replace the raw PNG, adjust any coordinate that moved, re-run.
Every coordinate in `callouts.json` is in **raw capture pixels**, so it can be
checked by opening the capture and reading the point off directly.

Three constraints are baked into the script, and all three are easy to undo by
accident:

* **The caption is drawn into the PNG, not written in Markdown.** One artifact
  then reads correctly here, on the forum, and in a saved copy. The Markdown
  carries the same words as alt text, because the drawn caption is pixels.
* **Each image is a self-contained dark card.** The paper has a light and a dark
  palette and the forum is dark-by-default, so nothing may depend on the page
  background — and a white canvas would glare in dark mode.
* **Type is sized against the final canvas width, not in absolute pixels.** The
  figures are drawn wider than the 41rem reading column and scaled down into it,
  so absolute sizes would land at whatever each source's aspect ratio dictated.
  `REFERENCE_WIDTH` is what keeps every figure's labels the same size on the page.

Complex figures are still tap-to-zoom on a phone, as any technical diagram is.

## Why the math is pre-rendered

The math is converted to [MathML](https://developer.mozilla.org/en-US/docs/Web/MathML)
at build time rather than by a script in the reader's browser. Three reasons:

1. **The GitHub Pages plugin allowlist.** This site is built by GitHub Pages
   from the `github-pages` gem, and `kramdown-math-katex` is not on the
   allowlist — so `math_engine: katex` in `_config.yml` is not available.
2. **No runtime cost.** A client-side engine means a JavaScript bundle plus
   webfonts, and a visible reflow as the equations settle after load. MathML is
   markup every current browser typesets natively (Chrome and Edge since early
   2023; Firefox and Safari for years).
3. **No third-party dependency** for the page's core content.

The trade-off is the build step above: the published `.md` is generated, so
hand-edits to it are lost on the next render.

## Previewing before you publish

Either build once and open a self-contained copy:

```sh
bundle exec jekyll build      # from the repo root
cd docs/efficiency-and-range
python3 preview.py            # writes preview.html
open preview.html
```

…or run a live server and refresh after each `node render.mjs`:

```sh
bundle exec jekyll serve      # http://localhost:4000/ioniq-app/efficiency-and-range.html
```

`preview.py` produces a single file with everything inlined and no network
requests, which is what makes it shareable — hand it to someone and it renders
identically offline. **The figures are embedded as data URIs**, which is what
makes that true: the built page's `src` attributes are site-absolute
(`/ioniq-app/...`) and resolve to nothing from a `file://` copy, so without
inlining every figure would be a broken-image icon. The preview is consequently
about 1.8 MB rather than 100 KB. (It also knows how to inline webfonts, which
this page does not use: `paper.html` is set in system faces. That path only fires
for a page built on the just-the-docs theme.) Both `preview.html` and
`node_modules/` are gitignored.

## Publishing

Pushing to `main` publishes. GitHub Pages rebuilds the site within a minute or
two, and the page is live at
<https://www.theburl.com/ioniq-app/efficiency-and-range.html>.

**Commit the source and the generated page together:**

```sh
cd docs/efficiency-and-range
python3 annotate.py           # only if a capture or callouts.json changed
node render.mjs               # do not skip
cd ../..
git add docs/efficiency-and-range/ efficiency-and-range.md assets/images/efficiency-and-range/
git commit -m "docs(efficiency): ..."
git push origin main
```

The failure mode to watch for is skipping the render: edit the source, commit
both paths, and `efficiency-and-range.md` still holds the *previous* render. The
push succeeds, nothing errors, and the live page silently lags the source.

**The tell is in `git status`.** A source edit should produce a matching change
in the generated page, so both paths appear dirty. If only `.src.md` is dirty,
the render was skipped. A commit that touches only `efficiency-and-range.md` is
equally suspect — it means the generated page was hand-edited, and the next
render will discard it.

## Where the paper's content comes from

The measurement details described in the paper are drawn from the app source
in the `ioniq5` repo — chiefly `EnergyPaceEstimator.swift`,
`DriveLocationPipeline.swift`, `VehicleDataService.swift`, and
`ADR-0023`. When those change, the paper's constants tables and §8 need
re-checking against the code.

The **figures** have the same dependency in visual form: if a tile is restyled or
a value moves on screen, the raw captures in `screenshots/raw/` are stale and no
build step will say so.
