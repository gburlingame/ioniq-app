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

```sh
cd docs/efficiency-and-range
npm install          # first time only
node render.mjs      # regenerates ../../efficiency-and-range.md
```

`render.mjs` converts only the math. Prose, tables, and code fences stay
Markdown for kramdown to render; `_layouts/paper.html` styles the result.

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
identically offline. (It also knows how to inline webfonts, which this page does
not use: `paper.html` is set in system faces. That path only fires for a page
built on the just-the-docs theme.) Both `preview.html` and `node_modules/` are
gitignored.

## Publishing

Pushing to `main` publishes. GitHub Pages rebuilds the site within a minute or
two, and the page is live at
<https://www.theburl.com/ioniq-app/efficiency-and-range.html>.

**Commit the source and the generated page together:**

```sh
node render.mjs               # from docs/efficiency-and-range — do not skip
cd ../..
git add docs/efficiency-and-range/efficiency-and-range.src.md efficiency-and-range.md
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
`ADR-0023`. When those change, the paper's constants tables and §9 need
re-checking against the code.
