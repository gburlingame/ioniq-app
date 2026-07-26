// Build the published "How Range and Efficiency Are Calculated" page.
//
//   efficiency-and-range.src.md   (Markdown + LaTeX — the source of truth)
//        |  node render.mjs
//        v
//   ../../efficiency-and-range.md (Markdown + inline MathML + front matter)
//        |  jekyll, via _layouts/paper.html
//        v
//   the published page
//
// Only the MATH is converted here. Prose, tables, and code fences stay
// Markdown; kramdown renders them and `_layouts/paper.html` styles them.
//
// Why pre-render the math: the site is built by GitHub Pages, whose plugin
// allowlist excludes kramdown-math-*, and a client-side engine would mean
// shipping a JS bundle plus webfonts and a visible reflow on load. MathML is
// markup the browser typesets natively.
//
// Re-run after ANY edit to the source. Do not hand-edit the generated page.

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import katex from 'katex';

const here = path.dirname(fileURLToPath(import.meta.url));
const SRC = path.join(here, 'efficiency-and-range.src.md');
const OUT = path.join(here, '..', '..', 'efficiency-and-range.md');

let md = fs.readFileSync(SRC, 'utf8');

const store = [];
const tok = (i) => `@@T${i}@@`;
const stash = (s) => { store.push(s); return tok(store.length - 1); };

let mathCount = 0;
const tex = (src, display) => {
  mathCount++;
  return katex.renderToString(src, { output: 'mathml', displayMode: display, throwOnError: true });
};

// ---- Code fences. Protected first: a `$` inside one is not math. The
// diagnostic-log samples are retagged `console` so the layout can quote them
// as a terminal; everything else is worked arithmetic.
let logBlocks = 0;
md = md.replace(/^```([^\n]*)\n([\s\S]*?)^```/gm, (_, info, code) => {
  const isLog = /^\[(ENERGY|GPSDIST)\]|eff=\d/m.test(code);
  if (isLog) logBlocks++;
  return stash('```' + (isLog ? 'console' : info) + '\n' + code + '```');
});
md = md.replace(/`[^`\n]+`/g, (m) => stash(m));

// ---- Math. Display math becomes a block-level div (blank lines around it
// make kramdown pass it through); inline math becomes an inline span.
md = md.replace(/^\$\$\n([\s\S]*?)\n\$\$/gm, (_, src) =>
  stash(`<div class="eq">\n${tex(src.trim(), true)}\n</div>`));
md = md.replace(/\$([^$\n]+)\$/g, (_, src) => stash(tex(src.trim(), false)));

// ---- Section anchors. Explicit kramdown IDs (`{#s3}`) rather than relying on
// auto-generated slugs, so the contents rail can never link to a heading that
// silently re-slugged after an edit.
const sections = [];
md = md.replace(/^## (.+)$/gm, (_, heading) => {
  const id = `s${sections.length + 1}`;
  const plain = heading.replace(/@@T(\d+)@@/g, (__, i) => store[+i].replace(/<[^>]+>/g, '')).trim();
  const m = plain.match(/^(\d+)\.\s*(.+)$/);
  sections.push({ id, n: m ? m[1] : '', label: m ? m[2] : plain });
  return `## ${heading} {#${id}}`;
});

// ---- Tables scroll inside their own container. just-the-docs adds this
// wrapper itself; the paper layout does not use that theme, so we add it here.
// `markdown="1"` keeps kramdown parsing the table inside the div.
md = md.replace(/(^\|.*\n)+/gm, (t) => `<div class="tablewrap" markdown="1">\n\n${t}\n</div>\n`);

md = md.replace(/@@T(\d+)@@/g, (_, i) => store[+i]);

const yaml = (s) => JSON.stringify(s); // valid YAML double-quoted scalar
const frontMatter = [
  '---',
  'layout: paper',
  'title: How Range and Efficiency Are Calculated',
  'nav_order: 6',
  'description: How the app measures driving efficiency and turns it into a range estimate — every formula worked out.',
  'sections:',
  ...sections.flatMap((s) => [
    `  - id: ${s.id}`,
    `    n: ${yaml(s.n)}`,
    `    label: ${yaml(s.label)}`,
  ]),
  '---',
  '',
  '<!-- =========================================================',
  '     GENERATED FILE — DO NOT EDIT.',
  '     Edits here are lost on the next build.',
  '     Source:  docs/efficiency-and-range/efficiency-and-range.src.md',
  '     Rebuild: cd docs/efficiency-and-range && node render.mjs',
  '     ========================================================= -->',
  '',
].join('\n');

fs.writeFileSync(OUT, frontMatter + md);
console.log(`math rendered:  ${mathCount}`);
console.log(`log blocks:     ${logBlocks}`);
console.log(`sections:       ${sections.length}`);
console.log(`wrote:          ${OUT} (${fs.statSync(OUT).size} bytes)`);
