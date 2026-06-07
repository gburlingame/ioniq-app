# IONIQ 5 Companion — Marketing Landing Page

**Date:** 2026-06-06
**Status:** Built — Jekyll port complete (index.html + _layouts/landing.html + assets/css/landing.css); pending a real Jekyll/GitHub Pages build to verify rendering
**Repo:** `ioniq-app` (the support/marketing site, Jekyll → GitHub Pages at theburl.com/ioniq-app)

## Goal

A customer generated a polished marketing landing page (Google Stitch → Netlify) and supplied
a matching design system ("Voltage Obsidian"). We are adopting the **design** of that page —
NOT its copy — as a new marketing front door for the existing support site. The current
`just-the-docs` documentation continues to live underneath, linked from the landing page footer.

## Hard constraint: copy must be accurate

The sample site's copy was largely LLM-fabricated. A claim-by-claim audit found ~4 publish-blockers
and ~8 false claims. **All copy on the landing page is sourced from the real `index.md` or the
App Store screenshots.** Specifically, the following sample claims are BANNED:

- ❌ "Thermal runaway pre-detection" — fabricated safety claim, legal exposure
- ❌ "10Hz sampling rate" / "millisecond precision" — impossible on ELM327/BLE (~100ms+ per signal)
- ❌ "Predictive SoC estimation" — not a feature (app reports BMS SoC, doesn't predict)
- ❌ "all 192 battery cells" — fabricated cell count; we don't publish unsourced hardware specs
- ❌ "SOH calculation based on discharge cycles" — SOH is BMS-reported, not app-computed
- ❌ "raw CAN-bus data" / "advanced algorithms" — it's OBD-II/UDS DID decoding
- ❌ "The only companion app that…" — unverifiable competitive superlative
- ❌ "IONIQ Labs" attribution — wrong owner; trademark risk

Telemetry numbers shown on the page are **clearly illustrative** (representative values, like the
App Store screenshots already use) — not implied to be live from a specific car.

## Design decisions

- **Architecture:** Landing page becomes the site's front door (root URL) as a custom full-bleed
  Jekyll layout with NO docs sidebar. The current `index.md` feature list moves to a `/features`
  docs page. `just-the-docs` keeps serving support, privacy, versions, features. One repo, one deploy.
- **Palette ("Voltage Obsidian"):**
  - Primary green `#4ADE80` (green-400) — brightened from the spec's `#22C55E` (green-500) per
    Greg's feedback that 500 read too dark on the dark background. `#22C55E` retained for hovers.
  - Secondary blue `#3B82F6`, Tertiary amber `#F59E0B`, Neutral/background slate `#0F172A`.
  - These map onto the app's own status colors (green SoC / blue info / amber warning).
- **Typography:** Hanken Grotesk (headline + body), JetBrains Mono (labels / telemetry numbers —
  consistent with the app's monospaced-digit CarPlay chips).
- **Hero (LOCKED):** Faithful replica of the sample — full-bleed generated IONIQ 5 background image
  (neon-lit studio, telemetry light trails), dark gradient + soft vignette for legibility, centered
  headline "See What Your EV Is **Really Doing**" (green glow on "Really Doing"), eyebrow, subtitle,
  primary "Download on the App Store" + ghost "See How It Works" buttons, and a JetBrains-Mono
  telemetry chip strip (Pack SoC / Power / Cell Δ / 12V / Batt Temp) using the three accent colors.
- **Imagery:** Real App Store screenshots from `ioniq5/app-store-assets/raw/` (dashboard, cell
  voltages/temps, CarPlay, charging session, signal history). The hero background is the customer's
  generated image, self-hosted (native res 1248×832).

## Page structure

1. **Hero** — locked (above).
2. **The Diagnostic Suite** — glass feature-card grid (Material icons + accurate one-liners):
   Live Dashboard · Charging Telemetry · Cell Voltages & Temps · History + iCloud · Advanced Tools.
3. **CarPlay showcase** — wide CarPlay screenshot, "telemetry on your dashboard," the real tab set.
   ⚠️ VERIFY live tab set with Greg before shipping — the App Store screenshot shows
   Status/Driving/Charging/Parking/EVSE; memory recorded Driving/Status/dynamic-Charging/dynamic-EVSE.
4. **Charging Intelligence** — "requested vs delivered" (the genuine EVSE-max-vs-pack feature).
5. **Data gallery** — real app screenshots in CSS/device frames.
6. **Reviews** — real, attributable tester quotes (Greg to supply: name/handle + permission).
   No quote is written or attributed by Claude. Section omitted at build time if quotes not ready.
7. **Privacy** — "No accounts. No ads. No tracking. Stays on device & iCloud."
8. **Supported vehicles** — real roster: IONIQ 5 / 5 N / 6 / 9 / EV6 (full); GV60 and Kia EV9 (nearing full).
9. **Download** — "$12.99 one-time · buy once, own it · no subscriptions, no IAP, no ads"
   (note: price varies by region). App Store button.
10. **Footer** — links back into the docs: Support, Privacy Policy, Version History,
    "Why Some Features Are Hard," "Should I Unplug My Adapter?"

## Implementation notes (Jekyll)

- New layout `_layouts/landing.html` — full-bleed, no `just-the-docs` chrome, own `<style>` block
  (or `assets/css/landing.scss`) with the Voltage Obsidian tokens. Loads Hanken Grotesk +
  JetBrains Mono + Material Symbols from Google Fonts.
- `index.md` → `layout: landing`, content authored as section includes/HTML.
- Move current `index.md` feature list to `features.md` (`layout: default`, nav_order 1).
- Hero image + screenshots into `assets/images/landing/`.
- Keep `color_scheme: ioniq` (cyan) for the docs pages — landing page overrides via its own layout.
  Open question for later: retheme docs green to fully unify, or keep green-marketing/cyan-docs.

## Out of scope

- Re-theming the existing docs pages (separate, later decision).
- Any new app features or screenshots beyond what already exists in `app-store-assets/`.
- i18n of the landing page (docs privacy pages are already localized; landing launches English-first).

## TODO from Greg

- Real tester quotes for the Reviews section (name/handle + permission).
- Confirm the live CarPlay tab set (section 3).
