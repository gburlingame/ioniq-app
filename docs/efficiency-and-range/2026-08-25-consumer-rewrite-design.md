# Consumer-first rewrite of the efficiency and range paper

**Date:** 2026-08-25 · **Status:** implemented

The paper was written for readers who wanted the arithmetic, and it did that job.
What it could not do was answer "what am I looking at?" for someone who had just
found the Range tile on their dashboard. This change puts that reader first
without taking anything away from the one who wants the derivation.

## What changed

1. **A new Part 1** — four illustrated sections above the existing §1, covering
   the Range & Efficiency tile (and its trend line), arrival state of charge, and
   the efficiency of a completed drive. No formulas.
2. **The existing material becomes Part 2**, its numbering intact apart from the
   removal below.
3. **§7, lifetime round-trip efficiency, is gone.** It described a pack-health
   ratio, not a driving statistic, and readers were taking it for one.
4. **The H1 now says "EV Dashboard"**, ending a divergence with the forum copy.
5. **Four generated figures**, produced by `annotate.py` from committed raw
   captures.

## Decisions, and what was rejected

### Prepend rather than restructure

Three shapes were considered: prepend a plain-language Part 1; interleave the
prose and the math section by section; or promote the plain-language material to
be the document and demote the math to an appendix.

Prepending won because the paper is **linked from the Build 138 release notes and
from App Store and TestFlight copy as a math reference**. Interleaving would have
renumbered every section and broken every `§N` reference in the text; the
appendix shape would have buried the material testers actually open it for. The
cost of prepending is a longer document, which a contents rail already mitigates.

### The "which number answers which question" table moved up

It was §2's opening table. It contains no math, it is the single most useful
thing in the document for a confused reader, and it belongs where that reader is.
It was **moved, not copied** — two versions of a summary table drift.
§2 keeps its technical paragraphs and now refers up to it.

### §7 was cut rather than rewritten

The section was accurate. The problem is that it sat in a document about driving
efficiency while describing something else entirely — the ratio of lifetime
energy out to lifetime energy in, which is a property of the cells and says
nothing about how you drive. Every reader who tried to reconcile it with the
other three numbers was doing work that could not succeed.

The feature stays in the app; only the paper drops it. Removal also took the
`0x0101` lifetime-counters row out of the constants reference and turned §2's
"four efficiency values" into three.

**Anchors shifted.** `render.mjs` assigns section IDs positionally (`s1`, `s2`,
…), so what was `#s8` is now `#s7`. No in-repo link depends on those, so this was
accepted rather than papered over with redirects. An external bookmark to a deep
anchor now lands one section early.

### The app name was settled, not deferred

The support-site rename to "EV Dashboard" had been deliberately held until v3.0
ships. The paper could not wait, for a mechanical reason: the H1 becomes the
Discourse topic title, `post-support-article.rb` matches topics by exact title,
and the live topic had already been renamed. The two were out of step, so
`UPDATE=1` would have aborted.

Renaming the H1 fixes the mismatch and makes `import-support-article.py`'s
`--rename "IONIQ 5 Companion=EV Dashboard"` unnecessary. The rest of the support
site still says the old name; that inconsistency is known and accepted here.

### Figures are generated, not drawn

`annotate.py` + `callouts.json` + committed raw captures, rather than finished
PNGs from a graphics tool. A UI change then costs one screenshot swap instead of
a redrawing session, and what each callout claims is reviewable as text in a
diff. Three constraints inside the script are load-bearing and documented in the
README: the caption is drawn into the PNG, each image is a self-contained dark
card, and type is sized against the final canvas width.

### The rounding trap is pre-empted

The captured drive shows 4.0 mi, 1.0 kWh, and 3.9 mi/kWh. Both components are
rounded for display, so dividing them gives 4.0 and looks like an error. In a
document that promises every formula worked out, that discrepancy would have
produced a forum reply within a day. The figure's caption and the surrounding
prose both say so before the reader gets there.

## What was not done

- **The two CarPlay captures and the phone capture are different drives** (5:57pm
  and 2:40pm). They are captioned as such. Asking for a matched set would have
  cost another drive to remove an ambiguity the caption already removes.
- **No redirect for the shifted anchors**, per above.
- **The `Version:` header moved to 2026-08-25; `Applies to:` was left at build
  146**, which is still where the described behaviour landed.

## Where the process lives now

The publishing chain spans two repos and a live forum, and it was previously
documented in four places with nothing owning the join — which is how a hand edit
to the forum copy came to look reasonable. It now has one owner:
`imanevp/runbooks/publishing-the-efficiency-paper.md`.
