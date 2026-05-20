---
layout: default
title: Version History
nav_order: 5
---

# Version History


---
## Build 75 — Kia EV6 AC charging and precondition detection fixes, Italian language support

NOTE TO TESTERS: This build has a changed that is only intended to fix preconditioning and AC charge detection in the Kia EV6 -- but the change was a bit risky (could be a big blast radius) and might have unintended consequences for IONIQ testers -- please let me know right away if you see anything out of sorts with preconditioning or AC/DC charge detection.  

### Kia EV6 AC charging detection and preconditioning detection fix

This build changes how AC charging is detected in the Kia EV6 -- in some cars this signal was also present when preconditioning, which resulted in preconditioning not being properly indicated.  This build hopefully fixes both issues -- pending tester verification.   Thanks to EV6 testers Mike, David, and Brett for their help last evening and today!  

### Italian language support

Italiano joins Deutsch, English, Español, Français, Nederlands, and Svenska in Settings → Language. All 753 user-facing strings translated. The language picker is now sorted alphabetically by native name (system default still pinned first).

### Inspect tab label now translates

The Inspect tab at the bottom of the main app stayed in English when the app language was set to anything else. It was looking up the literal string "Inspect" as a translation key — a key that had no entry in the catalog — so SwiftUI fell back to English for every language. Reusing the existing translation key already used by the scanner page now means the tab and its page header share one translation: Inspizieren / Inspeccionar / Inspecter / Inspecteren / Inspektera / Ispeziona. English unchanged.

### Polling Headroom popup polish

The Polling Headroom info popup has been rewritten — the intro paragraph reframes the metric in terms of capacity for additional signals (replacing the previous "Higher is better"), and the trailing Caveats section was removed. All copy now ships in DE/ES/FR/NL/SV/IT

---
## Build 74 — NEW Polling Headroom indicator, IONIQ 6 Indonesia CarPlay layout fix

NOTE TO TESTERS: Everyone has a bit of homework with this release -- when you have time, please check out the new polling headroom metric on the CarPlay Status tab or in the phone app in Daashboard / Overview.   Please let me know what percentage you see after a few minutes of operation -- this metric needs time to stabilize.   I am considering bumping up the priority and rate of the brake light signal, but want to get a better sense of wider fleet performance (different cars, different adapters, etc..)   As a point of reference, my polling headroom is 61% -- which is excellent, lots of room to add/improve signals.  Thank you!

### Polling Headroom indicator

Dashboard Overview gains a new chip showing the percentage of time the OBD adapter is NOT busy on the wire. Higher is better — it's the slack you have for more polling work. Tapping the chip's info button opens a sheet that explains the metric, how to read it, and an important caveat: the number takes about two minutes to converge on its final reading after polling starts, so don't react to early values.

The same number is mirrored as a row on the CarPlay Status tab so you can monitor it on the head unit. Counters reset every time a fresh full-rotation polling window begins (ignition on/off, BLE disconnect, diagnostic pause), so each polling session is measured independently.

### CarPlay: IONIQ 6 Indonesia head-unit layout

Some IONIQ 6 head units report a logical screen width around 645 points — narrower than the IONIQ 5's full-screen 775 points, but wider than its split-screen 518. Until this build, anything below 650pt fell into the cramped 3-row compact layout intended for IONIQ 5 split mode, which left chips visibly tiny on a screen that has room for the standard 7-up layout. Threshold is now 600pt, so IONIQ 6 head units in this band get the full Driving and Charging chip layouts. The chips scale slightly smaller than they do on the IONIQ 5 — CarPlay handles that automatically — but stay legible. IONIQ 5 split-screen mode (518pt) is unaffected and continues to use the compact layout.

---
## Build 73 — Automatic Driving Tab selection, New adapter auto-connect feature, Signal chart polish, localization update

NOTE TO TESTERS: A couple of big quality of life improvements in this build - CarPlay will now automatically navigate to the Driving tab for you -- faster time to Dashboard!  You can disconnect the adapter from CarPlay, and then reconnect.   This will be a big help to folks using more than one OBD-II app -- please let me know if you run into any issues with this.  To all the new Kia EV6 testers -- welcome aboard, and good luck with your upcoming preconditioning and charging sessions!  I couldn't figure this out without you!

### CarPlay: auto-open Driving tab on connect

New "CarPlay" section in Settings with a single toggle, "Open Driving Tab on Connect" (default ON). When enabled, the CarPlay tab bar auto-switches from Status to Driving the moment the adapter is connected and the vehicle registry loads.

### Adapter connection control

New Auto-Connect toggle in Settings → OBD-II Adapter (default ON). The connected-state button is now "Disconnect" (drops BLE without forgetting); "Forget Saved Device" remains for full unpair. CarPlay Status tab gains a Connect/Disconnect row so you can hand the adapter off to another OBD app without leaving CarPlay. User intent persists across BLE drops and launches — turning Auto-Connect off actually stays off. Status reads "Disconnected (you)" when you've deliberately disconnected.

### History → Signals: odometer 0/mileage oscillation fixed

The odometer chart alternated between 0 and real mileage because the History writer recorded both the km and mi side of each AUX odometer poll — only one side ever has real data. Fixed; a one-shot purge scrubs existing 0 readings on first launch.

### Signal-history chart: major polish pass

- **Dots-only rendering.** Each sample now appears as a small colored dot at its actual (time, value) location — no connecting lines. Eliminates lines bridging gap bands, segments extending into gap-band edges, and single-sample invisibility. Bicolor pack-current still color-codes per dot (red draw, green regen).
- **Gap bands align to the no-data interval.** A snapshot at 1:18 represents the bucket [1:18, 1:19) and holds data — the no-data span between 1:18 and 1:21 is two minutes, not three. Sample dots no longer land inside their own band.
- **Heartbeat writes.** Every minute-bucket flush now forces one sample per signal recorded this session, so steady signals like SoC always show ≥1 dot per minute (no more empty regions during cruise).
- **Live data appears in real time.** New minutes show up immediately during an active session — no more back-out and re-enter. Smart-follow keeps you on the live edge when you're viewing the latest data; if you've scrolled back, the visible window is left alone.
- **Chart fills the viewport.** Adapts to device size and orientation. Tap the chart for focus mode (shrinks chips so the chart grows). Landscape/small screens get a scroll fallback.
- **5-pill navigation row** above the chart: «Prior data set», «Next data set», Jump to Latest, Zoom to All, Toggle Focus.
- **Y-range chip removed**; **X-range chip moved** below the x-axis tick labels, centered (was a top-left overlay that obstructed data). **"Tap to interact" hint** added at the top in non-focus mode.
- **Live-session indicator pill** ("● Live: Updating once a minute") appears inside the chart's bottom-left during active recording, disappears ~30 s after the recorder goes quiet.
- **Value/unit consistency** on the signal-detail page: Lifetime Min/Max cards, focus-mode chips, and the selection callout now render units small + grey, matching the Dashboard.
- **Isolation Resistance Y-axis pinned to 0–3000 kΩ**.

### CarPlay 12V chip: tighter SoC text

Removed the space between the remaining-energy number and "kWh" (e.g. "52.3 kWh" → "52.3kWh").

### Localization catalog: 100% complete

Filled in 977 previously-missing translation cells across DE/ES/FR/NL/SV.


---
## Build 72 — Signal-history gaps + chart focus mode, cold-pack preconditioning gate, CarPlay 12V SoC polish

NOTE TO TESTERS:  The History / Signals section is a work in progress - there will be more polish added over the next build or two.

### Signal-history charts now show real gaps

When you open a signal in History → Signals (e.g. Pack Voltage), the time-series chart now shows a subtle shaded vertical band over each span of time when the app wasn't actually recording data — for example, the gaps between two drives or charges. The data line cleanly breaks at each band edge instead of misleadingly drawing a straight line across parked time. Long-press to scrub inside a band and the value readout shows "No data" rather than an interpolated value.

### Tap a signal chart to focus

Tap anywhere inside the time-series chart and the stats chips above shrink to a compact horizontal strip, the headline value scales down, and the chart grows vertically so you can read finer detail. Tap the date/value back above the chart to collapse out of focus mode. The chart's existing pan / pinch / scrub gestures still work inside the focused chart unchanged.

### Preconditioning detection: cold-pack gate

The activation edge for preconditioning sessions now also requires the BMS minimum pack temperature to be below 25 °C before indicating that preconditioning is turned on.

This addresses false positives reported by a hot-climate EV6 tester (>90 °F ambient) where the heater-command byte pattern occasionally landed in the activation shape while the pack was already well above heater target. Deactivation logic is intentionally unchanged — once a session is active, the heater warming the pack past 25 °C cannot strand a stuck-on session.

### CarPlay 12V chip: readable SoC % overlay

The 12V battery chip on the CarPlay Driving tab now shows its SoC % overlay in black when the bar fills the white (40–80%) neutral band, so the value stays readable against the bright fill.


---
## Build 71 — Regeneration gauge, live driving stats, localization fixes

NOTE TO TESTERS: Thank you to everyone for the warms wishes regarding my son who graduated from college this weekend!  I'm hoping to get App Store version 2.0 out in 10-14 days - so I'm going to be making a big push to get things buttoned up.

### New Regeneration visualization

A new "Regeneration" surface appears in two places: a Dashboard section and a CarPlay Driving-tab chip (which replaces the Odometer chip for now).  Both render the same three-arc circular gauge:

- The full dial scales from 0 to your pack's peak power capability — about 277 kW on an IONIQ 5, about 503 kW on the 5 N.
- The white arc fills to how much regen power the BMS is currently willing to accept.
- A green arc overlays the white showing live regen flow at this instant.

The Dashboard section is hidden while AC or DC charging is active. Two new History signals — **Available Regen Power** and **Pack Peak Power** — are recorded under Battery so you can chart them over time.

### Active driving sessions update live

The History tab's active session card now refreshes distance, energy used, end-of-window SoC, and battery temp range every few seconds while you drive. Previously these only appeared after the drive ended; only max speed updated live. Now the whole summary fills in as the drive happens.

### SoC gauge color — blue band is now white

The 40-79% State-of-Charge band used to render in blue, which is hard to read against the dark CarPlay chip background. It now uses the system foreground color — white on the dark CarPlay chip, white on dark Dashboard, black on light Dashboard. The red/orange/green warning bands for low/warning/full SoC are unchanged.

### Settings: About moved to the bottom

The About section now sits at the bottom of Settings, below Reset. All your action-bearing sections — Adapter, Units, History, Recording, Advanced Tools, Reset — cluster together, with the static info as a tail.

### Localization fixes

A pass through History views fixed several places where labels were leaking English regardless of your language setting:

- Signal Detail view: **Lifetime Min**, **Lifetime Max**, **Recorded Since**, **Source ECU**, and **Unit** now translate.
- Time-series chart: month/date labels follow the in-app language (previously used the system locale).
- Session and signal chips: **Max Speed**, **Energy Used**, **Duration**, **Avg Power**, **Charge Type**, **Energy Added**, **EVSE Max**, **Peak Power**, **Today**, **Yesterday**, **Latest**, **Updated**, **No samples yet** — all now translate across German, Spanish, French, Dutch, and Swedish.

Plus a small spacing polish on the Regeneration gauge so the live kW value and unit read as one token (`60kW` instead of `60 kW`).

---
## Build 70 — History chart clipping fix, Kia EV6 Dashboard label

### History signal charts: plotted lines stay inside the chart area

Zooming in on a signal whose history contains an extreme outlier elsewhere — Isolation Resistance with a 3000 kΩ lifetime-max spike is the easiest one to reproduce — used to let the chart line escape the plot rectangle, shooting up above the top gridline or sliding off the left edge. The chart now keeps the line inside the visible plot area no matter how tight the zoom or how far away the off-screen samples sit. Nothing is lost or hidden; the data is still there, it just no longer paints outside the chart bounds.

### Dashboard now correctly shows "Kia EV6"

EV6 owners running the app were seeing "IONIQ 5" on the Dashboard regardless of their actual vehicle. VIN decoding and registry selection were already correct in earlier builds — the right per-vehicle polling map was loading and every signal was being decoded against the EV6's ECU layout — but the model-name label the Dashboard reads from was missing the EV6 case and silently falling back to "IONIQ 5". The label now reads "Kia EV6" on EV6 vehicles. Any datalogs and history you already collected on the app were captured correctly; only the on-screen name was wrong.

---
## Build 69 — Tire-pressure history fix, CarPlay EVSE info screen, CarPlay tap-spinner cleanup

### Tire-pressure history showed wildly wrong values

The History chart for tire pressure was showing roughly a quarter of the real value — a tire at ~38 psi would render as ~5.5 psi, regardless of whether you had the app set to psi, kPa, or bar. Live Dashboard readings were always correct; only the recorded history was affected. The fix converts pressures to the right internal unit at the moment they're recorded, so new samples will chart correctly across every unit preference. Samples already saved before this build remain mis-scaled — they aren't migrated.

### CarPlay EVSE tab: long AC-charging explanation no longer cut off

During AC charging, the EVSE tab includes a several-sentence explanation of the values it shows. CarPlay was truncating that paragraph mid-sentence inside the row. The explanation has been moved behind an "About these values" row that opens a dedicated info screen, with each sentence as its own item so nothing gets clipped. DC fast charging's single short sentence still appears inline on the main page. Translations were updated for German, Spanish, French, Dutch, and Swedish.

### CarPlay: tapping data-only rows no longer triggers an infinite spinner

Build 68 fixed this for the Status tab's adapter row. Build 69 finishes the job across the rest of CarPlay — 18 more data-display rows (battery cells, individual tire pressures, EVSE values, charging stats, and others). These rows are just status readouts and aren't meant to navigate anywhere, but tapping one used to leave a spinning wheel that never went away. They now respond instantly to taps as no-ops, and the rows that are supposed to navigate still do.

---
## Build 68 — CarPlay split-screen support and chip polish, improved tire viewability in CarPlay

**NOTE TO TESTERS:**  I addded support for CarPlay split screen in this build -- but I am not happy with the results because the chips are just too small.  I'm going to explore some other options.

### CarPlay split-screen support

Added detection for screen resolution, includes an experimental view with 2 rows of 5 chips, and 1 row of 4 chips to eliminate the need for vertical scrolling when the IONIQ 5 screen is set to split screen mode.

### CarPlay chips: new light-mode background color and automatic day/night adaptation

When the head unit is in light/day mode, chips now render with an opaque slate-blue background — replacing the washed-out grey that previously appeared in light mode. The slate has a subtle blue cast that complements the green text used for charging and regen states. When the head unit switches to dark/night mode, chips return to their original near-black appearance, automatically, in about half a second. Dark-mode appearance is unchanged from prior builds.

### CarPlay chip corner halo fix

Chips on the Driving and Charging tabs had a faint colored halo at each rounded corner. The chip's rounded-rect background was slightly more rounded than CarPlay's own clip mask, leaving a sliver of the container's background visible at each corner. The chip corner radius is now slightly less rounded so the chip background fills out cleanly to where CarPlay's clip begins.

### CarPlay tire chip: drop shadow for readability

Added a subtle drop shadow to the text so it reads cleanly across all tile colors without changing the semantic color palette.

### CarPlay Status tab: adapter row no longer triggers an infinite spinner

The adapter row at the top of the Status tab (showing the adapter name and signal strength) is read-only. Tapping it previously showed a loading spinner that never dismissed because no action was wired up. Tapping the row now briefly shows the spinner and dismisses it immediately, matching the pattern used for the other read-only rows in Status.

---
## Build 67 — Kia EV6 support, CarPlay NEW: AC Draw, charging-session robustness

**NOTE TO TESTERS:** This build adds a silent recovery path for testers whose app couldn't open the storage container after Build 66 which led to an immediate crash.

### Kia EV6 support

The app now recognizes 5XYC (US, West Point) and KNDC (Korea, Hwasung) VINs as Kia EV6 and routes them to dedicated registries instead of falling back to IONIQ 5 defaults. If your EV6 trim doesn't decode correctly, please let me know.

### CarPlay AC Draw chip

The Charging tab's "Demand" chip was accurate during DC fast charging but misleading during AC charging.  The chip now flips dynamically: during AC charging it shows "AC Draw" with a three-row V/A/kW layout sourced from the OBC's real measurements; during DCFC and idle it shows the original "Demand" layout unchanged.

### Charging sessions stuck "in progress" after relaunch

If a charging session was open when the app got killed by iOS, the session row could be left orphaned with no way to close cleanly. The recorder now re-seeds active charging state on relaunch and closes the session the next time it observes the car has stopped charging. Pre-existing stuck sessions get cleaned up automatically.

### At most one active charging session per VIN

Whenever a charging session is created or restored, any older still-open rows for the same VIN are closed with status "Superseded." Cleans up dual-orphan rows from prior crashes.

### Driving session chart no longer blank on short drives

Short drives could show "No charted signals" even though the session had start/end SoC populated — Build 66's 60-second storage buckets weren't flushing reliably at session-end. The recorder now explicitly flushes pending readings before closing the session. Forward-looking — doesn't recover data already lost.

### iCloud sync toggle verifies before enabling

Toggling "Sync to iCloud" on in Settings now checks whether iCloud is actually available before letting the change stick. If it isn't — signed out, restricted, or storage in recovery mode — the toggle reverts and a popup explains. Previously the toggle flipped on regardless and the user discovered sync wasn't working later.

### History tab degraded-mode message

When the local history store can't be opened normally, the History tab now shows "Historical data cannot be shown — please check the device's permissions" instead of an empty list. Avoids the silent-empty-tab confusion when storage is degraded.

---
## Build 66 — Reduction in device and cloud storage size (7-12x reduction)

**NOTE TO TESTERS:** This build is a major rework of how your history is stored. You'll see a one-time migration overlay on first launch (a few seconds) that converts existing data to the new compact format. Your sessions, events, and signal readings are preserved end-to-end — just packed much more efficiently. Please let me know if anything looks wrong after migration. Please reach out if you run into any difficulty.

### History storage is now 7-12× smaller

Reworked the time-series store to coalesce many signal readings into a single record covering a 60-second window. A typical history database that used to weigh ~50 MB on disk now lands around 5 MB after migration, with the same data fidelity — same readings, same per-signal arrival times, same charts. iCloud upload time and bandwidth shrink proportionally, and multi-device sync settles faster.

The migration runs once per device on first launch. A brief overlay shows progress; runs are resume-safe if interrupted.

A note about charts: live drive/charge sessions now update on the chart roughly every minute instead of every few seconds. Live values you see on the Dashboard during a drive are still instant — only the **historical** chart view reflects new readings at a 60-second cadence. A small caption under each chart calls this out.

---
## Build 65 — History polish, tap-and-hold scrub, live charging sessions, smarter off-state polling, vLinker / vgate compatibility

**NOTE TO TESTERS:** Making headway on Version 2.0 - still lots to do!  Please check out the new HISTORY tab -- go for drives, charge your car -- note that new DRIVE and/or CHARGING sessions appear automatically!  Let me know what you think about the direction I'm headed.  :-)  Also, please let me know if you experience any crashes or anything unusual. 

### History → Signals — list and detail redesign

The signals list has a colored icon tile per row matching its category — green Battery, yellow 12V & LDC, blue Charging, purple Drive, orange Tires, teal Climate. About 25 signals get a more specific symbol (motors, tire pressures, brake lights, cell voltages, isolation resistance, etc.); the rest inherit their category's icon. Section headers carry the same color and are no longer all-caps.

The signal detail page now matches the polished Driving Session view: a 44pt latest-value reading with unit and "Updated N ago" subtitle, then a 3-column stat grid with Lifetime Min, Lifetime Max, Samples (1.2k / 1.4M format), Recorded Since, Source ECU, and Unit — all in your preferred units. Boolean signals show "Active" / "Inactive" instead of 1.0 / 0.0.

The multi-touch chart now supports **tap-and-hold scrub**: hold for about half a second, feel a light haptic, then drag a vertical crosshair. A badge shows the time and value at the crosshair. The crosshair persists after you let go; pan or double-tap clears it.

### History → Charging Session — redesigned and live

The charging-session detail page now leads with a 44pt Peak kW hero, a start → end SoC battery widget, and a 3-column stat grid (Duration, Energy Added, Avg Power excluding preconditioning, Charge Type, EVSE Max, Battery Temp). In-progress sessions update live: SoC number advances each sample, the green delta segment grows, Energy Added appears at 0.1 kWh, Avg Power surfaces around 60s, and the SoC bar animates between integer steps.

### State-of-Charge bars — bright = what changed

On both Charging and Driving Session detail pages, the bright-green segment now always highlights what changed in this session (energy added when charging, used when driving); the translucent-green segment fills the rest.

### Inspect (J1979) — card redesign

The Inspect page now matches the History views' card aesthetic — status hero, Discovery card, and Interrogation table on thin-material panels. Cancel moved to a destructive toolbar button.

### Isolation Resistance info sheet — readable again

The info sheet behind the "i" on the Isolation Resistance chip previously displayed lookup identifiers ("iso_info.intro_1", etc.) - fixed and updated copy
### Smart polling when the car is off

When you turn the car off with the app still open, polling now backs off to once every 5 seconds until the car comes back on. When you restart, live data reappears immediately — no re-reading the VIN, re-identifying ECUs, or re-training each DID.

### ELM327 v2.3 clone compatibility

Initial connection to v2.3 Bluetooth adapter clones (vLinker MC-IOS, vgate iCar Pro 2S, etc.) is now reliable. Their boot banner was being consumed as the response to the app's first command, cascading into a one-command offset — most visibly Settings → Adapter reading "Unknown (ATDPN 6)" instead of "CAN 500k (ISO 15765-4)". Fixed.

### Settings polish

- The model name now appears in **all caps** everywhere — Settings → Registry, the vehicle-off prompt, and elsewhere.
- **Sync to iCloud** toggle no longer pops a "Restart Now" alert that quit the app. Toggling saves immediately; an inline "Change pending — takes effect the next time you open the app" note appears under the toggle.
- **Time Charts** renamed to **Dashboard Charts** with a clarified footer.
- **History** footer generalized from "your IONIQ 5" to "your vehicle".
- **Reminders → unplug-reminder** simplified.

---
## Build 64 — Genesis GV60 support, polish to History views, multi-touch Signals charts, Cell Voltage Δ mini heatmap, localization bug fix

### Vehicle support — Genesis GV60

Genesis GV60 is now recognized as its own vehicle (model years 2021–2024). The app ships registries for **RWD** (225 hp), **AWD** (314 hp), and **AWD Performance** (429 hp). Genesis VINs (those starting with KMT) now route to a GV60 configuration with the correct drivetrain, motor gauges, and battery layout instead of defaulting to an IONIQ 5 Standard Range.

AWD Performance auto-binds from VIN today against a verified tester capture. RWD and AWD registries are in place and will auto-bind once a tester from each trim shares their VIN.

### History → Signals — full multi-touch charts

Every signal in History → Signals now has a true multi-touch chart. Pinch to zoom, drag to pan, double-tap to reset. Toolbar buttons "Zoom to all data" and "Initial view" are always visible with active/inactive coloring. Charts open at the most recent driving/charging session by default. Pack current renders bicolor (green regen / red draw) with a zero line. Boolean signals (lights, brakes) use step interpolation so the line holds its state across long time gaps. The Y axis auto-scales smoothly when spikes enter or leave view; two corner badges show the visible time span and Y range. Charts honor Settings unit preferences 

### History → Signals — smaller, faster database

The noisiest signals — pack current, pack voltage, and the LDC trio (output voltage / output current / input voltage) — now record only changes large enough to matter. Quantization noise is filtered while every real event (regen pulses, load transitions, regulation deviations) is still captured. Less storage per hour of driving, less iCloud sync bandwidth, no resolution loss for the high-fidelity signals (temperatures, SoC, energy totals, cell voltages).

### History → Sessions — redesigned detail view

The Driving Session detail page (tap a session row) is redesigned around a large efficiency metric (km/kWh or mi/kWh in your units), a horizontal battery widget visualizing start→end SoC, a three-column stat grid (Duration, Distance, Max Speed, Energy Used, Battery Temp range), and a polished SoC chart with a green gradient fill. Header shows a relative date ("Today", "Yesterday", weekday, or short date) above the time range. Session list rows now also use your Settings units.

Driving session start values stay correct when the BMS is slow to wake after ignition. Previously, if HVAC reported before the BMS, the session captured 0 for odometer / SoC / energy — producing absurd distances and a hidden SoC row. The session now backfills those snapshots as the BMS catches up.

**Swipe-to-delete** session rows. Right-to-left swipe reveals Delete; deletion propagates across devices and removes attached photos. Signal samples remain.

### CarPlay — Cell Voltage Δ mini heatmap

The Cell Voltage Δ chip in CarPlay (Battery and Charging tabs) now displays a mini heatmap of every cell's voltage above the delta value. Each cell is a tiny colored square — green ≤30 mV, yellow ≤100 mV, red >100 mV deviation from pack mean — mirroring the iOS Dashboard cell grid. Pack imbalance and outliers are visible at a glance from the head unit.

### Odometer history fix

On cars whose ECU reports the odometer in miles, the odometer value displayed correctly in the app and CarPlay but wasn't being persisted to History → Signals → Odometer; the chart stayed empty. Now miles convert to kilometers (the canonical storage unit) and the history records as expected.

### Localization

The J1979 Inspect screen is now localized into German, Spanish, French, Dutch, and Swedish — six previously-English-only strings now render in your selected app language.

---
## Build 63 — iCloud History sync, Isolation Resistance, new History tab

**NOTE TO TESTERS:** This is the first early build of what will ultimately become VERSION 2.0 -- the new features are lacking a lot of polish, that will improve over time. I'm bumping the major number due to the addition of Apple CloudKit for data retention and cloud syncing. I have a lot to figure out in regards to data retention, making sure I don't fill up people's iPhones and iCloud accounts! Think of this build as beginning to lay the foundation of what will be coming.

**NOTE TO IONIQ 6 AND IONIQ 9 TESTERS:** Please check out the new isolation resistance chip in Dashboard / Overview -- are you seeing a value in that location? Please let me know.

### History — drives, charges, and signals across your devices

A new **History** tab on the iPhone records what your IONIQ 5 has been doing over time and syncs it privately across every device signed into your Apple ID. Open the app on your iPad, and all your data will automatically synchronize in the background.

**Sessions** captures driving and charging episodes as discrete entries. Tap a row to see a step-end SoC chart over the session window with a point at every recorded sample, plus aggregates like distance, peak charge power, and energy used. The chart updates live while you sit in the car.

**Signals** is a time-series view of every catalog signal — battery voltage / current / temperatures, motor RPMs, isolation resistance, charging power, tire pressures, climate, and more (50+ signals). The Battery category also includes per-cell-voltage and per-module-temperature snapshot views, captured every 15 minutes during ignition.

History syncs only to your private iCloud, visible only to you. Sync is on by default; turn it off in Settings → History. Records stay in lockstep across devices — delete one, delete everywhere.

### Isolation Resistance — new Dashboard chip

A full-width chip in Dashboard → Overview shows your battery's isolation resistance: the electrical isolation between the HV pack and the car's chassis. Higher kΩ is better — the pack is well isolated from the car's metal frame.

Tap the blue info badge for a full explainer — what the number means, why typical idle / AC-charging / DC-charging readings differ (the onboard charger is in the measurement loop only during AC charging), the FMVSS 305a regulatory floor for an 800-volt pack, and how to read the trend over time as a possible early signal of insulation breakdown in the ICCU.

---
## Build 62 — Polling Paused state, diagnostic back-button guards, Curated Scan polish, Scan status panel change, updated brake light chip - second App Store release (v1.1)

**NOTE TO TESTERS:** This is RC4 for Version 1.1 -- the issues identified yesterday have been fixed and verified (by me) -- please let me know if you run into any issues.

### Polling Paused — new state across CarPlay and Dashboard

While a diagnostic feature has paused live data, the BLE adapter status now correctly reads **Polling paused** with a pause icon — in CarPlay's top status row, in the Scan Status row, and on the iPhone Dashboard's adapter panel. Previously every screen incorrectly said **Reading**, implying live polling was happening. Covers all seven features that pause polling: Curated Scan, Complete ECU Scan, Adapter Quiet Check, J1979 Scanner, DID Range Scan, ECU Finder, ECU Identifier.

### Curated Scan — three polish fixes

**Start button green from frame one.** The green Start button on the Curate DIDs screen used to render disabled-grey for about a second after each navigation push, then flip to green. It's now correctly green from the first frame.

**Abort confirmation no longer shows a stray pointer.** The "Abort capture session?" confirmation triggered by the back arrow during a capture used to render with a directional pointer arrow on iPad/Catalyst that didn't fit the context. It now uses a clean centered alert on every device.

**Done lands cleanly back at Settings.** Tapping Done on the Results screen used to occasionally land on a brief blank screen with a back chevron before reaching Settings. The pop is now clean, and Done feels instant because the cleanup runs in the background.

### Adapter Quiet Check — polish pass

The mid-test Cancel Test button is gone. To abort a running test, tap the back chevron — a confirmation alert appears asking whether to abort. Once a test is done, the screen no longer shows a Run Again button; instead, navigating away and back always returns you to the same idle starting screen.

### Diagnostic back-chevron confirmation guards

DID Range Scan, ECU Finder, and Create Curated DID List now prompt for confirmation if you tap the back chevron mid-scan, instead of silently cancelling. Create Curated DID List uses **Stop** rather than **Abort** language to reflect that partial scans are saved and resumable.

### J1979 Inspect — Start crawl correctly disabled during diagnostic pause

The Start crawl button on the Inspect tab was incorrectly enabled during a paused window from another diagnostic. It's now correctly disabled with a "Polling paused" indicator until the other diagnostic finishes.

### Battery-cooling Fan section — hidden where the underlying signal is wrong

The Battery-cooling Fan section on the Dashboard previously showed two stuck-at-zero chips on every IONIQ 5 / 6 / 9. The section is now hidden on every supported vehicle until correct mappings are identified.

### Scan Status panel — orange info badge removed

The orange info-circle badge that appeared on the ICCU row of the Scan Status panel was reading as a warning for what is in fact normal behavior. The badge is removed; the panel now shows only the polling-readiness icons it exists for.

### CarPlay brake-light "On" chip — point-source glow

The brake-light "On" chip in CarPlay is restyled with a radial point-source glow (a smaller, more saturated lamp with a circular halo) instead of the prior flat top-down gradient — closer to how a real LED tail-lamp looks on a chip-sized surface.

---
## Build 61 — ICCU softening, Advanced Tools opened up to all, true cold-launch Reset Onboarding, Curated Scan Start fix

**NOTES TO TESTERS:** Unfortunately, I am not calling this RC4 -- I know there are some things in this build I need to fix in the Advanced Tools Section.   I needed to get this build out to unlock some additional testing.

### Curated Scan — green Start button regression fixed

Build 60 introduced a regression: tapping the green **Start** button on the Curate DIDs screen did nothing. The cause was the new nav-stack rework which still needs work.

### Advanced Tools menu — unhidden for everyone

The settings section formerly known as **Advanced Diagnostics** is renamed to **Advanced Tools** and is now visible to everyone — no 5-tap-on-Build unlock required. It contains DID Range Scan, ECU Finder, Create Curated DID List, ABC test with Curated DID List.  

The 5-tap mechanic is still there but now gates only the **Experimental Features** section (currently the per-vehicle Parking sensors toggle on 2022-2024 IONIQ 5). Existing testers keep their Experimental unlock state.

### Reset Onboarding — true in-process cold launch

Previously, tapping Reset Onboarding cleared the onboarding flag and forgot the adapter, but the in-memory Bluetooth manager still remembered the previously-adopted peripheral via iOS's known-peripherals list — so the Welcome screen would immediately re-detect it. Now Reset Onboarding releases the old central manager and instantiates a fresh one (iOS binds known-peripheral history to the manager instance, so a new manager has no history), clears all transient discovery/observer state, and rebuilds the SwiftUI subtree so view-local state (sheets, nav stacks, timers) also resets. No app relaunch needed.

### ICCU "fields not reported" notice — softened from warning to info

Tester feedback flagged the prior orange warning banner ("X of Y fields unavailable") as alarming for what is in fact normal behavior — many ICCUs, factory and replaced, only respond to a subset of identification DIDs. The banner is now a soft blue informational hint with a lightbulb icon, copy reads "X of Y fields not reported", and tapping it expands the list of unresponsive DIDs **inline** with an animated chevron rotation rather than presenting a full-screen sheet which had no obvious way to exit.

### IONIQ 6 RWD Standard Range — MY2023 coverage

The IONIQ 6 Standard Range registry now correctly covers model year 2023. Previously a 2023 SR VIN fell through to the default registry. The Long Range variants already supported MY2023 since Build 56; this brings SR in line.

### Internal — diagnostic instrumentation for Curated Scan polling-resume bug - KNOWN ISSUE

A separate, intermittent bug — about 1 in 5 Curated Scans, polling silently fails to resume after pressing Done — has new `[POLL]` and `[CURATED]` log lines around `startPolling`/`stopPolling` and around `CuratedScanRunner.finish()`. No behavior change for users; if you reproduce the bug please share the log so we can pinpoint which of three candidate paths is silently bailing out.

---
## Build 60 — CarPlay polish, Curated Scan flow fixes, adoption-modal first-tap bug fixed

**NOTES TO TESTERS:**

Headlights are verified working on 2026 IONIQ 5 -- thanks Jeff! This is RC3 for version 1.1, fixed a couple of bugs I found and some polish.

### Adapter Reminder modal — first-tap dismiss bug fixed (for real this time)

The first attempt at fixing the "Reminder modal flashes and dismisses on first tap" bug only addressed half the problem. The deeper cause was sheet-host stability inside a Form's conditional Section. Sheet attachment has been lifted up to a stable parent above the Form. First presentation is now reliable.

### Curated Scan — flow & navigation fixes

Three navigation issues fixed:

- **Done button on Results now works** — previously a dead no-op because its `dismiss()` was captured 2 nav levels deep. Results is now a stage swap rather than a nav-push, so Done has a single level to pop.
- **No more system back arrow on Results** — Results used to push on top of the still-running active screen, so back returned to a live session. Now Active and Results swap in place; nothing to back out to.
- **Curate DIDs back arrow returns to Pick a curated list** instead of dismissing the entire flow back to Settings.

### Curated Scan — Abort replaces View Results / Share / Done on active screen

Mid-session those buttons don't make sense — the run isn't finished. Replaced with a single full-width red Abort button that opens a confirmation dialog ("Abort capture session? This will end the current A-B-C session.") before exiting. Auto-advance to Results on Capture C commit is unchanged.

### Curated Scan — preflight buttons restyled

Start button on Curate DIDs now renders green-on-white to signal "ready to commit forward" — previously read as low-contrast accent text in dark mode. Select all / Deselect all buttons in the header are now bordered capsules. Confirm on the Label Capture popup gets the same treatment with a disabled state until the label has content. Cancel button on Pick a curated list removed — back chevron is sufficient.

### Curated Scan — Latest Values column alignment

Rows whose byte responses fit on one line appeared further indented than rows whose responses wrapped to two lines. Fixed-width DID column + value flowing leading from a consistent x. First byte of every row now sits in the same column for easy scanning.

### CarPlay — tire pressure tile shape

Tile shapes changed from very-slightly-rectangular (0.40w × 0.42h) to perfect squares — the 2% aspect mismatch read as accidental. Each tile's outer corner (the one facing the chip frame) now rounds at a radius concentric with the chip's own outer corner so the curves run visually parallel.

### CarPlay — battery row chips visually unified

Several chips got proportional tuning so they read as a coherent set:

- **12V chip recomposed** — circular SoC arc replaced with a horizontal pill bar (same low-alpha track + filled deficit visual, stretched into a line). V on top, SoC bar in middle, I on bottom, with hairline dividers between rows. Voltage and current font sizes bumped to match the Pack chip.
- **Battery Heater Temp / Battery Temp** — fixed value text intruding into the bottom of the sparkline plot. Battery Temp font bumped to match Heater Temp.
- **Pack Power chip** — added subtle grey hairlines between V/A/kW rows matching the Climate chip's divider style; chip now fills its tile more densely.


---
## Build 59 — Curated Scan stability fix + checklist redesign, swipe-to-confirm for already-connected adapters, polish

**NOTES TO TESTERS:**

1. This is RC2 for the Version 1.1 App Store release. Please report anything abnormal.
2. 2026 IONIQ 5 owners — please test your low-beam and high-beam indicators. The 2026 mapping is a calculated bet based on our success with 2025. Please test both low beams and high beams, do the app and CarPlay follow the state of the headlights? Please, please let me know!
3. Anyone with a VLink-branded adapter — confirm it now appears in the scan list without removing the name filter

### ABC test with Curated DID List — stability fix and checklist redesign

The biggest fix in this build. The Curated Scan no longer runs a continuous live-preview polling task in the background. Each Capture A/B/C now runs a single bounded polling cycle (~1-3s on a healthy bus). This eliminates the orphan-task class of bug that killed Tom's Build 57 twice with `0x8BADF00D` watchdog hangs after he turned off the OBD adapter and car.

The active view has been redesigned as a checklist. Each row (Capture A / Capture B / Capture C) shows a Begin button when it's next, a spinner with a small cancel xmark while it's in flight, or a green check seal when committed. The bottom "Begin Capture" button is gone — you advance by tapping each row's Begin in sequence. When Capture C commits, the view auto-pushes you to the renamed Curated Scan Results view.

A new instructions banner up top counters a recurring misconception: each capture represents one steady state of the car (e.g. "lights off"), not a transition between states. Below the captures, a "Latest Values" section shows the most recent snapshot's values dimmed between captures and lit up to full opacity as a capture fills in.

### Curated Scan Results — Share + Done as bottom action row

The Results view (was "Diff") now has a clean bottom action row with Share and Done as equal-width prominent capsule buttons. Above them, a footnote with a folder icon points you at the on-device archive: "Results are saved to the IONIQ 5 Companion folder in the Files app." Done dismisses the entire flow back to Settings.

### Complete ECU Scan completion screen — matching footer

The Complete ECU Scan completion screen now uses the same bottom action row as the Curated Scan Results view: Share and Done as equal-width prominent capsule buttons, with the same Files-app footnote. The Share button now ships **both** the curated `.iqlist` artifact and the raw scan log — previously, a zero-positives scan had no way to share the raw log for triage.

### Already-connected adapter — swipe-to-confirm reminder

If your iPhone has an OBD-II adapter connected via another app, the Welcome screen's one-tap shortcut now opens a confirmation sheet before adopting. The sheet reminds you that OBD-II adapters can only talk to one app at a time, and asks you to slide a control from left to right to continue. A "Go Back" button below the slider returns you to the shortcut panel.

Behind the scenes, adoption is also more resilient: if the iPhone has already torn down the prior app's connection by the time you swipe, the app now silently rescans for the adapter and reconnects, all under a single continuous "Connecting…" indicator. No more long blank "Connecting…" stalls.

### VLink adapter detection

Added "vlink" to the OBD adapter-name filter so VLink-family ELM327 adapters (without the trailing "er") show up in the scan list. Replaces the narrower "vlinker" entry; the hyphenated "v-link" entry is retained for adapters that brand with the dash.


---
## Build 58 — Welcome-screen shortcut for already-connected adapters, 2025 headlight detection (thanks Tom!), dashboard polish (thanks Bjorn!), fixed some Advanced Diagnostic tools/polish

**NOTES TO TESTERS:**

1. Please report anything abnormal — I'm calling this RC1 (release candidate 1) for Version 1.1 App Store release.
2. All 2025 IONIQ 5 owners — please, please test out your headlights and let me know if they are working: manually on, auto on, high beams and low beams (no DRL yet — we'll go for that at some point).
3. Let me know if you see anything strange if you have Dynamic Type cranked up.

### Welcome-screen shortcut for already-connected adapters

If your iPhone already has an OBD-II adapter connected via another app (or a system-level Bluetooth pairing), the Welcome screen now offers a one-tap shortcut instead of the generic 1-2-3 tutorial. Each detected adapter shows up as a full-width prominent button — tap the adapter name to use it. Below the panel, a smaller grey "Set up a different adapter" button takes you back to the regular flow.

A soft tip on the shortcut panel notes that running multiple OBD-II apps at the same time can degrade the experience for both apps. If you tap "Set up a different adapter" by mistake, a "Show already connected adapters" button appears at the top of the regular tutorial so you can restore the discovery list — dismissing is now a navigation action, not a permanent setup commitment.

Discovery only runs when no adapter is saved; if you already use IONIQ 5 Companion regularly, nothing about your launch experience changes.

### 2025 IONIQ 5 — headlight detection (all variants)

Low-beam and high-beam indicators now light up on the 2025 IONIQ 5 (RWD LR, AWD LR, RWD SR, IONIQ 5 N). The 2025 firmware moved the headlight signals to a different DID than the 2024 mapping uses, leaving them silent until now. Mapping verified against five physical states from Tom's tests (auto-off, auto-on, manual low ×2, manual high). 2024 IONIQ 5 cars are unchanged in this build.

### Dashboard — Auxiliary Battery SoC chip refinement

The 12V auxiliary-battery SoC mini-gauge in the Low Voltage section was rendering badly at larger Dynamic Type sizes (the percentage was overflowing the small circular plot). The percentage now stays size-stable inside the plot regardless of your text-size preference. The "State of Charge" descriptor moved out of the small inner plot — where it was crowding the percentage — to a chip-style caption below the circle.

### Dashboard — Motor RPM gauges

The "rpm" unit moved out of the inside of each circular plot to the bottom label, which now reads "Front Motor (rpm)", "Rear Motor (rpm)", or "Motor (rpm)" depending on drivetrain. The arc stroke was thickened so the gauges read with more visual weight and the value sits as the single focal point inside each circle.

### Advanced Diagnostics

Renamed all Advanced Diagnostics tools, added brief descriptions of what each one is used for including Reset Onboarding. Adding a confirmation dialog if Reset Onboarding is pressed to guard against an accidental press.

### ABC test with Curated DID List — Share button fix

Share buttons now appear in two places once all three snapshots (A/B/C) are captured: a new footer button on the active view, and the existing toolbar button on the Diff view. Both hand the JSON archive to the iOS share sheet so testers can email the artifact back consistently. Fixes a prior bug where the Diff-view Share button never appeared because it was bound to a file URL that was nil until Done dismissed the whole sheet.


---
## Build 57 — Curated Scan workflow, CarPlay Scan Status fixes, Experimental Parking Sensors (2022-2024 IONIQ 5)

**NOTE TO TESTERS:** Please report anything abnormal — I'm hoping to release version 1.1 to the App Store tomorrow or Tuesday. Please make sure the expanded 12V/Aux features are working well for you.

### Curated Scan workflow

Complete ECU Scan and Curated Scan now share a lighter user-facing artifact: the **curated list** (`.iqlist`). When a Complete ECU Scan finishes, the app auto-generates an `.iqlist` next to the heavier scan log, and the completion screen's Share button now shares that curated list rather than the full log.

The Curated Scan picker is updated to match. The picker lists `.iqlist` files exclusively, and copy is updated throughout: navigation title becomes "Pick a curated list", and the empty state explains how to create one (run a Complete ECU Scan, or copy an `.iqlist` into the IONIQ 5 Companion folder via the Files app).

The underlying scan log is still written to Documents and accessible via Files for forensic / triage use; only the user-facing flow changes.

### CarPlay Scan Status fixes

**Fixed:** tapping an ECU row in Scan Status no longer shows an infinite spinner. The rows are informational and now indicate that with no disclosure chevron and an immediate tap response.

**Fixed:** the Scan Status summary now reads "x/y DIDs" instead of "x/y ECUs". The number was always a count of polled DIDs (typically ~20 across 8 ECUs).

### J1979 common-DTC notice opens larger

The post-scan notice that appears when a known-benign permanent code is detected now opens at full sheet height instead of a half-sheet. Several testers reported the body text was off the screen and could be missed.

### Experimental Parking Sensors (only available on 2022-2024 IONIQ 5)

A new toggle in **Settings → Experimental Features → Parking sensors** re-enables the Dashboard parking panel and CarPlay parking tab on 2022-2024 IONIQ 5 registries. The Experimental Features section is itself gated under the 5-tap "Advanced Diagnostics" unlock, and the toggle only appears when the active vehicle's registry has parking-sensor coverage. Footer warns that readings may be inaccurate; with the toggle off, the Dashboard panel is hidden and the CarPlay tab is omitted.

### Complete ECU Scan reliability on clone adapters

Relaxed an internal first-frame timeout from 32 ms to 128 ms for the fast-scan path. A tester's 2026 IONIQ 5 BCM scan on a clone "ELM327 v2.2" was aborting partway through because the adapter's RX path needed slightly more settle time after large multi-frame batches. The relaxed ceiling adds margin without affecting normal scan speed — successful responses return as fast as ever. Cost on clone adapters is roughly 14 minutes of additional time across a full 65,536-DID scan, paid only on legitimately empty regions.

---
## Build 56 — 12V telemetry, CarPlay Driving tab redesign, IONIQ 6 MY2023 coverage, IONIQ 5 N coverage

### Auxiliary battery telemetry

A new collapsible **12V** panel on the Dashboard surfaces the auxiliary battery's full state, sourced from a slow-poll ICCU detail set: state of charge, voltage, current (with a charging / discharging label), and temperature — plus the DC-DC converter's temperature, output voltage, output current, and HV pack input voltage.

The same data feeds a redesigned CarPlay 12V chip on the Driving tab. A small SoC arc sits at the top with the percentage in the center; voltage and current are stacked underneath. The current value follows the same negative-for-charging sign convention as the HV pack chip across the row, so the row reads consistently.

The legacy single-voltage 12V chip on the Dashboard Overview section is removed in favor of this richer panel.

### CarPlay Driving tab reorganization

The Driving tab is reorganized for at-a-glance scanning. Row 1 groups battery-health telemetry — **Pack SoC**, **Pack Power**, **Odometer**, **12V**, **Cell Δ**, motor RPM, headlights. Row 2 groups motor and environmental chips — **Tires**, **Climate**, **Pre-Condition**, **Battery Heater**, **Battery Temp**, motor RPM, brake light.

A new **Tires** chip replaces the standalone Energy chip (now redundant since the SoC chip shows kWh remaining underneath the percentage). Four corner tiles show pressure and temperature for FL/FR/RL/RR, color-graded by status against your registry's pressure thresholds.

RWD cars get a new **One Motor** chip — an earthy ocean-to-land gradient backdrop with a centered peace-sign glyph — where the front-motor RPM lives on AWD. Celebrates the simpler single-motor drivetrain.

The Pack chip turns green when energy is flowing into the pack (charging or regenerative braking); white otherwise.

The Pre-Condition chip on Driving now shows a stacked composition when active: **Active** label, **Time to 21°C / 70°F** caption (locale-aware), and the calculated ETA — same formatting as the Charging tab.

Two row 1 chips were renamed: **SoC** → **Pack SoC** (disambiguates from the new aux SoC reading in the 12V chip), and **Pack** → **Pack Power**.

### Ioniq 6 MY2023 coverage

The Ioniq 6 RWD LR and AWD LR registries now correctly cover model year 2023. Previously, MY2023 VINs (year code `P`) fell through to a default registry and could be decoded as the wrong drivetrain — first surfaced by a tester whose 2023 RWD car was being read as AWD.

### Ioniq 5N coverage

Added new decoding logic and registry entries for the IONIQ 5 N

### Localization

CarPlay Driving tab chip titles **Front RPM**, **Rear RPM**, and **One Motor** are now localized in German, Spanish, French, Dutch, and Swedish. Previously rendered in English regardless of the user's app-language setting because the strings were passed as raw literals.

### Other refinements

- CarPlay climate chip now draws a thin divider between the outdoor (AAT) and indoor (IAT) rows for clearer separation.
- Dashboard motor-RPM gauge no longer renders the value with a thousands separator (e.g. "3200" instead of "3,200").
- CarPlay SoC chip auto-shrinks the kWh-remaining text if it would impinge on the colored ring — protects layout against future larger battery packs.

---
## Build 55 — Adapter Quiet Check, common-DTC reassurance

### Adapter Quiet Check

A new tool under **Settings → Diagnostics → Adapter Quiet Check** answers a question that's surprisingly common: "is another app talking to my OBD adapter at the same time as IONIQ 5 Companion?"

iOS lets multiple apps share one BLE connection to the same peripheral, and OBD adapters weren't designed for that. When two apps both send AT commands to the same adapter, they corrupt each other's session — symptoms include missed multi-frame responses, garbled DIDs, and scans that take far longer than they should. Until now there was no way to confirm whether your symptoms came from foreign-app interference or something else.

Tap **Run Quiet Check** and accept the consent prompt (the adapter is briefly put in a special listening mode and re-initialized when the test ends). The app pauses its own polling and listens silently for 60 seconds for any byte the adapter shouldn't be sending.

- **PASS** — no foreign traffic detected; the adapter is connected only to this app.
- **FAIL** — another app is sharing the adapter. The first frames captured are shown as decoded hex with timestamps, useful for support cases. Force-quit other diagnostic apps (Carista, OBDeleven, OBD Fusion, Torque, Bimmercode, etc.), unplug-replug the adapter, and re-run.

The last 5 runs are kept in the history list on screen. Designed primarily as a forensic artifact — when you suspect interference, this gives a one-tap yes/no answer.

### "Common Hyundai code" reassurance

A J1979 scan on virtually every Hyundai EV reports a permanent diagnostic code, **P0C17** (Drive Motor Position Sensor Circuit), on the drive motor controller. This code does not represent a real fault — it's a self-test artifact that the controller never fully clears, and permanent codes are sticky by design.

When your scan completes and finds P0C17 in the permanent slot, IONIQ 5 Companion now shows a brief explanation of why it's normal, when it would actually warrant attention (driving symptoms like stuttering, limp mode, or dashboard alerts), and a "Don't show this again" preference. The DTCs help bubble in the interrogation table also picks up a short note so users who haven't run a scan yet can read the explanation.

The reassurance is restricted to the **permanent** code class only — a confirmed or pending P0C17 would represent an active fault and is not suppressed.

---
## Build 53 — Brake Light Indicator setting, Curated DID Scan sharing, app polish

### Brake Light Indicator setting

Settings now has a **Dashboard** section with a **Brake Light Indicator** option. Three modes:

- **Off** — the brake chip is hidden entirely.
- **Red Background** — full red flash on brake press (Build 52 behavior).
- **Red Text** — only the value "On" shows in red, no background flash.

The new default is **Red Text**. If you preferred the Build 52 flash behavior, switch to **Red Background** under Settings → Dashboard. The Dashboard section only appears on cars whose registry decodes a brake-light signal — older registries hide it automatically.

### Curated DID Scan sharing made easier

Previously, sending a full ECU scan to another tester meant routing through Files → On My iPhone → Ioniq 5 Diagnostics. That dance is gone.

**Sender side.** In the Curated Scan source picker, long-press (or left-swipe) a row and pick **Share findings…**. The share sheet opens with a small `.iqlist` file pre-attached — pick AirDrop, Messages, Mail, etc. The shared file contains just the POSITIVE DIDs from that scan plus minimal metadata (capture date, app build, source ECU). The full scan log stays on your device.

**Receiver side.** When a tester taps an `.iqlist` attachment in iMessage, Mail, or Files, iOS shows a Quick Look preview with the ECU name, DID count, capture date, sender's app build, and a horizontal preview of the first 12 DIDs. Tap the share icon in Quick Look's bottom toolbar and pick IONIQ 5 Companion to import — the file lands in Documents and the Curated Scan source picker opens with it at the top, ready to use.

If you receive a scan with zero positives, you'll get a polite "no positives to share" alert instead of an empty file.

### Settings copy updates

The advanced diagnostics-unlock dialog (the one that pops after the 5-tap on Build) now reads **"Enable Advanced Diagnostics"** instead of the older DID-Scanner-specific phrasing. The matching re-hide dialog reads **"Hide Advanced Diagnostics"**. Both translated across all six locales.

### First-launch folder visibility

iOS hides empty app Documents folders from Files → On My iPhone, which led to "the app doesn't have a folder, did the install break?" confusion on fresh installs. Build 53 writes a one-line `README.txt` on first launch describing what the folder is for, so the IONIQ 5 Companion folder shows up in Files immediately. The file is only written if absent — your edits or deletions stick across launches.

---
## Build 52 — App rename and first-launch defaults polish — first App Store release (v1.0)

*First public App Store release — version 1.0.*

Build 52 renames the app to **IONIQ 5 Companion** and sets smarter first-launch defaults. No diagnostic feature changes — this is a polish pass before wider release.

### App renamed to IONIQ 5 Companion

The Home Screen icon, app switcher, Settings entry, and Bluetooth permission prompt all now read **IONIQ 5 Companion**. Existing installs will pick up the new name on update — your saved data, app placement, and adapter pairings carry over unchanged.

The bundle identifier and your in-app history are untouched, so this is a name-only change with no migration to think about.

### Locale-aware unit defaults on first launch

Previously the app defaulted everyone to °C / mi / psi. Build 52 reads your phone's locale once on first launch and picks defaults that match your location:

- **US** — °F, miles, psi
- **UK** — °C, miles, psi
- **Continental Europe, Australia, Japan, etc.** — °C, kilometers, bar

If you've already set Settings → Units to your preference, that choice is preserved — only fresh installs get the new defaults.

### Dark mode is the new default appearance

The app now defaults to Dark on first launch instead of Auto (follow system). If you've already picked Auto or Light in Settings → Appearance, your choice is unchanged.

---
## Build 51 — 2026 Ioniq 5 charging fix - part 2

Build 51 fixes the underlying issue in how the app loads addresses from the registry. With this build, 2026 owners should see charging-state detection, EVSE info, and Control Pilot duty cycle all working when plugged in.

### What this fixes

On 2026 cars, the Scan Status panel on the Dashboard was showing 14/14 DIDs found instead of the expected 17 — VCMS was silently being dropped at registry-load time. Build 51 makes the per-vehicle registry the single source of truth for ECU addresses, with regression tests that prevent this class of bug from recurring.

No changes to 2022–2025 Ioniq 5 behavior — those registries already use the canonical addresses and are unaffected.

---
## Build 50 — 2026 Ioniq 5 charging support

Hyundai moved the VCMS (Vehicle Charging Management System) ECU to a new CAN bus address starting with the 2026 model year, and the app was still polling the 2024-era address. Build 50 ships a per-model-year registry for 2026+ that points the charging signals at the correct location.

### What should work in 2026 Ioniq 5

- **Charging state detection** — the dashboard now correctly recognizes when AC or DC charging is active.
- **EVSE info** — the dynamic CarPlay charging tab populates with EVSE max voltage, max current, present voltage/current, and max power.
- **Control Pilot duty cycle** — the J1772/CCS PWM signal that advertises the EVSE's max-current capability.

No changes to 2022–2025 Ioniq 5 behavior. 2024 RWD and AWD LR continue to use their existing registries; 2025 single-year registry preserved verbatim. Same DIDs, same signal byte offsets, same polling intervals — only the bus address changed for 2026+.

### Tester credit

Thanks to tester Jeff for providing the 2026 ECU bus scan + targeted DID probe against the new address that confirmed the data layout migrated unchanged with the move. Without his diagnostic data, this fix wouldn't have been possible.

---
## Build 49 — Curated DID Scan, ECU Scanner overhaul, J1979 share card

NOTE TO TESTERS 1: I think we're getting close to the first release candidate -- a new issue with 2026 Ioniq 5's might delay things a bit - looks like Hyundai move the VCMS to another address.
NOTE TO TESTERS 2: The Parking section and CarPlay parking tab are temporarily hidden in this build while we polish the app for its first public release. The underlying mapping work is preserved and will return in a follow-up build.

### New tool: Curated List DID Scan

Settings → Diagnostics → **Curated List DID Scan**.

Pick a saved Complete-ECU-Scan log, curate which DIDs you want to investigate, then capture up to three labeled snapshots (A/B/C) under different physical states — for example: door closed, door open, door closed again. The diff view buckets results into:

- **Gold** — bytes that round-trip A==C ≠ B (strong evidence of a state signal). Expandable to bit-level decomposition.
- **Other change** — bytes that changed but didn't round-trip cleanly.
- **Static** — bytes that never changed.
- **Missing** — DIDs that errored in some snapshot.

Saves a `curated_scan_*.json` archive plus a sibling `.md` summary to Documents (visible via the Files app and ShareLink).

### ECU Scanner — rewritten end-to-end

The 0x700–0x7FF discovery scan is now reliable, fast, and substantially more informative per ECU. On a 2024 Ioniq 5 it consistently finds all 38 ECUs on the bus.

### Complete ECU Scan — in-progress UI redesigned for in-car readability

Big circular progress gauge with the percent in the middle and the current DID below it. Elapsed and ETA are now side-by-side labeled tiles. The Found DIDs list moved into a collapsible disclosure group. Progress is derived from the actual DID being scanned, so the bar can no longer exceed 100%, and on resume the gauge immediately reflects real progress.

### J1979 crawler — styled PNG share card

The share button now exports a styled PNG report card (matching the ICCU share card style) instead of a raw `.log` file. The card includes:

- Vehicle context (model / year / variant / odometer when available)
- Crawl Summary (Started, Duration, Outcome, ECUs found, Discovery, DTCs rollup)
- A per-ECU panel for every interrogated ECU showing the four bucket-status chips (Identity / Capabilities / DTCs / Monitors), CAL-IDs, Mode 01 PID counts, Mode 06 MID counts, and any confirmed/pending/permanent DTCs

VIN is intentionally omitted from every panel so the card can be shared publicly.

### J1979 crawler — diagnostic logging integration

Diagnostic logging now flows into your normal diagnostic log (when diagnostic logging is on) instead of producing a dedicated per-crawl `.log` file. When diagnostic logging is off, a J1979 crawl leaves no on-disk trace at all. Removes the "mystery file" friction.

### Parking sensors hidden for now

The experimental Dashboard "Parking" section and CarPlay parking tab are turned off in this build while we get the rest of the app ready for its first public release. Underlying mapping work is preserved and will re-enable in a follow-up.

---
## Build 48 — Climate section, regen indicator on RPM gauges

NOTE TO TESTERS: The new "Climate" section appears on the Dashboard between Overview and Charging. If you've previously customized your section order, the new section will appear at the bottom by default — you can re-order it from Settings. If you find the AAT (outside) reading drifts from what your car's dashboard shows, that's expected: the app reads the raw sensor while the cluster applies its own filtering.

### New "Climate" section on the Dashboard

A new section between Overview and Charging shows three live cabin readings, all from the HVAC ECU:

- **AAT Sensor** — outside-air temperature (formerly the "Outside" chip in the Overview section, now relabeled and moved here).
- **IAT Sensor** — interior cabin-air temperature.
- **Relative Humidity** — cabin relative humidity, as a percentage.

Each chip shows `--` until the first valid reading arrives. Tap "What's AAT, IAT, and RH?" below the chips for a short explanation of each value, including a note that AAT may not match the outdoor temperature shown on the car's dashboard — AAT is a raw sensor reading, while the cluster applies its own adjustment.

### CarPlay: "Outside Temp" replaced by a "Climate" chip

On the Driving and Charging tabs, the "Outside Temp" chip has been renamed to "Climate" and now displays three rows:

- AAT: outside air
- IAT: cabin air
- RH: relative humidity

Same chip footprint, three values instead of one. The labels (AAT, IAT, RH) are small and grey, the values are bold, and the units use the same proportions as the 12V chip.

### CarPlay: Regen indicator on the RPM gauges

The RPM gauges on the Driving tab now show **green text in the center when the battery is regenerating** (current flowing from the motors back into the pack), and white text when motoring. The colored ring around the gauge still reflects RPM magnitude (green/yellow/orange).

Suggested by a tester — thanks for the idea!

### Smaller polish

- Info buttons (Climate, Battery Health, Battery Odometer) are now system blue instead of grey so they're clearly tappable. The orange ⓘ in the ECU status panel is unchanged because it signals a problem rather than a tap target.

---
## Build 47 — Smoother battery preconditioning countdown

NOTE TO TESTERS: If you precondition your battery before a DC fast-charge session, please watch the new "Estimated time to 70°F" countdown — both during preconditioning and as the pack approaches 70°F (21°C). Let me know how the descent feels and whether the end-of-session timing matches what you observe.  I would very much like to collect full diagnostic logs for entire pre-conditioning cycles to help tune the algorithm -- thanks to TheIoniqGuy for supplying log data!

### Estimated time to 70°F — full rewrite

The "Estimated time to 70°F" chip that appears during battery preconditioning has been rewritten end-to-end. The previous version had two visible problems:

- **It got stuck.** The displayed value would sit at the same number for 6-7 minutes at the start of a session, then jump down by 3-5 minutes at once, then stick again. That happens because the cold pack doesn't actually warm in the first ~6 minutes — heat is moving through the coolant loop before reaching the modules — and the old algorithm assumed it was warming from the moment the heater engaged.
- **It ended too high.** Even after the pack was within 1°C of target, the chip would still read "≈ 2 min" or "≈ 3 min" right up to the moment the pack reached 70°F.

What's new:

- **Continuous mm:ss display.** The chip now shows time as `≈ 12:34` instead of `≈ 13 min`, and updates several times per minute. You see a real ticking countdown rather than discrete jumps.
- **Smooth descent.** A first-order low-pass filter spreads any change in the underlying estimate over ~60 seconds. Where the old chip jumped 3-5 minutes at a step, the new one descends one minute at a time.
- **Honest dead-time.** The first ~6 minutes of a cold-pack session are explicitly modeled as "the pack hasn't moved yet" — the countdown ticks down minute by minute on wall-clock time, just like a real countdown should.
- **Correct end behavior.** As the pack closes in on 70°F the displayed value glides down toward 0:30 (a small floor that prevents the chip from claiming "0:00" while the pack is still cold), and disappears the moment the pack actually crosses 70°F.

### What it looks like in practice

For a cold-morning preconditioning session starting at 9°C, you'd typically see the chip start near `≈ 30:00`, descend smoothly through `25:00`, `20:00`, `15:00`, etc., transition into `1:30`, `1:00`, `0:30` as the pack reaches 20°C, and then disappear (`--`) when the pack hits 70°F.

If preconditioning is interrupted (you start DC fast charging, or shut off the car), the chip disappears immediately — DC fast charging takes over thermal management and the preconditioning estimate is no longer meaningful.

### Caveats

This is a calibration tuned to the two preconditioning sessions we have detailed data on (a 9°C cold start that ran into DC fast charging, and a 14°C session that ran to completion). On unusually slow-heating sessions — colder ambient, weak heater, low state-of-charge — the chip may reach 0:30 before the pack actually reaches 70°F, and sit there until done. If that happens to you, please share the diagnostic log so I can tune the floor.

---
## Build 46 — New Inspect tab: J1979 diagnostic crawl

NOTE TO TESTERS:   This new feature revealed that I have a permanent trouble code on my 2024 Ioniq 5 that I didn't know about - I'll have to look into that!   After you run the scan, pleae let me know if you also have any error codes or other issues.  Thanks!

### New Inspect tab

A new **Inspect** tab sits between Dashboard and Settings (magnifying-glass icon). It runs a one-shot **J1979 diagnostic crawl** across every ECU on your vehicle that responds to the universal OBD-II protocol — the same protocol every car sold in the last ~25 years is required to support.

For each responding ECU the crawl collects:

- **Identity** — Vehicle Identification Number, calibration IDs, and ECU name (Mode 09)
- **Capabilities** — which live-data PIDs the ECU exposes (Mode 01)
- **DTCs** — confirmed, pending, and permanent trouble codes (Modes 03 / 07 / 0A), each decoded into the standard J2012 description; freeze-frame snapshot is read when there's at least one confirmed DTC (Mode 02)
- **Monitors** — supported on-board diagnostic monitor IDs (Mode 06)

Results appear in two sections on the Inspect tab:

- **Discovery** — a compact summary of how many ECUs answered the broadcast vs. the per-address physical probe
- **Interrogation** — one row per discovered ECU showing identity, capability, DTC, and monitor status with at-a-glance status icons. Tap any row to expand the full per-ECU details

A **Share** button at the end exports the full transcript as a `j1979_crawl_*.log` file. **Your VIN is encrypted in the saved log file** — only the developer holds the decryption key — so sharing the log doesn't disclose your vehicle identifier. The in-app view still shows the full VIN to you.

### What the icons mean

Status icons are consistent across both Discovery and Interrogation:

- empty circle — pending
- spinner — in progress
- green check — completed cleanly
- orange exclamation — completed but with DTCs found
- gray minus — skipped (e.g. ECU rejected the request)
- red triangle — failed

A small `info.circle` button on the Interrogation header opens a help sheet explaining each column.

### Live polling pauses during the scan

Live data polling on the Dashboard pauses while a J1979 crawl is running, then resumes automatically when the crawl completes (or you cancel it). The Dashboard will go briefly blank during the crawl — that's expected.


---
## Build 45 — Faster startup on partial-response ICCUs, ICCU panel cleanup, headlight indicator hidden on 2025 Ioniq 5

NOTE 1 TO TESTERS:  Some of the changes in this build are a litle risky, and impossible for me to fully test on my 2024 vehicle.  Please let me know if you have any problems.

NOTE 2 TO TESTERS: If you have an ICCU that does not report all DIDs, it would be great if you could send me diagnostic log using this build -- please be sure and start the diagnostic recording before you plug in the adapter in order to capture the initialization sequence -- I want to verify the init sequence is going smoothly on your vehicle - thank you!

NOTE 3 TO TESTERS:  If you have a 2025 Ioniq 5, please verify you are no longer seeing the headlight chip -- that will be gone until we find a reliable headlight signal.

### Faster startup on cars where the ICCU does not reply to all polled DIDs

Improved handling of multi-DID messages when some of the DIDs do not respond

### Removed the FACTORY / SERVICED badge on the ICCU panel

Earlier builds displayed a green FACTORY badge in the ICCU section, driven by a single diagnostic identifier on the ICCU module. In practice that identifier only ever reported "FACTORY" or failed to respond at all — and we've now seen replacement ICCUs that also report "FACTORY". The badge was at best uninformative and at worst misleading, so Build 45 removes it.

All other ICCU identity fields — part number, hardware number, serial number, build date, boot software, firmware hashes, etc. — are unchanged.

### Reassurance text below the "N fields unavailable" banner

When an ICCU responds to only some of its identification fields, the app shows an orange warning banner ("N of M fields unavailable"). With the FACTORY/SERVICED badge gone, that banner is the most prominent signal on the panel, and it can read as alarming.

Build 45 adds a short caption directly below the banner:

**Many ICCUs respond to only some of these fields. A partial response here is normal and does not indicate a problem with your car.**

The caption is only shown when the banner itself is shown — panels where every field came through successfully display nothing new. Text is localized against all five of the app's supported languages (English, German, Spanish, French, Dutch, Swedish).

### Headlight indicator hidden on 2025 Ioniq 5 (until we find a reliable signal)

On 2025 Ioniq 5 cars, neither of the BCM data identifiers we've tried for headlight state has held up: the high-beam byte we relied on for 2022-2024 is missing entirely from the 2025 BCM payload, and the low-beam mapping that carried over from older model years has never been confirmed on a 2025 capture. Rather than display a perpetually-incorrect "Off" indicator, Build 45 hides the headlight chip on the 2025 Dashboard and the CarPlay driving grid.

The chip will reappear once a future tester capture identifies a reliable signal — no app update required beyond a registry tweak. 2022-2024 Ioniq 5 is unaffected.

---
## Build 44 — Complete ECU Scan fixes, preconditioning detection rewrite, added byte to the Ioniq 5 (2025+) polling loop

### Complete ECU Scan: data-integrity fix, resume fixes, and UI polish

#### NRC responses no longer counted as positive hits

A full DID sweep could record thousands of false "positive" rows with payload `7F 22 31` — the ECU's own negative-response pattern, which the scanner was treating as valid data. Build 44 fixes the classifier so rejected DIDs are correctly dropped. Scans from Build 44 onward produce clean data; previously-recorded scans are not retroactively scrubbed.

#### Resume no longer bricks scan logs

Trying to resume a scan with the adapter disconnected could permanently mark the log as "finished" behind the scenes, making it disappear from the resume list forever. Build 44 now:

- Checks adapter connectivity before touching the log, and shows a clear "Adapter not connected — reconnect and try again" error if it isn't.
- Marks the scan paused (resumable), not finished, if the connection drops mid-scan.

Logs already broken by earlier builds remain unrecoverable; this is a fix going forward only.

#### Resume clock and ETA fix

On a resumed scan, the elapsed-time readout and "estimated time remaining" now reflect just the current session, not the paused gap between sessions. Resuming an hours-paused scan no longer produces a wildly inflated ETA that ticks back and forth.

#### Preflight and scan-progress UI polish

- Session picker matches the ECU picker's style (single row with selected value, tap-through to list). Labels simplified to "Default (0x01)", "Extended (0x03)", "Both (0x01 and 0x03)".
- New section footer explains the session-type distinction and scan-duration expectations.
- Start-Scan is now a full-width prominent green button; Stop is tinted red.
- Scan-phase labels use explicit service IDs.
- Monospaced digits on counters and summary so numbers don't jitter as they tick.
- Vehicle-state presets lead with "driving" and "mixed state".

### Preconditioning detection rewrite

The preconditioning chip previously used a single bit from the BMS as its trigger, with an asymmetric debounce — slow to come on, instant to go off. Tester TheIoniqGuy saw the chip briefly flicker off mid-preconditioning (most visibly in Corbin's captures) because of a single-sample transition in the underlying command byte that happened to clear the watched bit.

Build 44 replaces the detector with a rule that reads both of the BMS's battery-loop pump-duty command bytes directly, not through a single bit. It requires both bytes to be in a heating-calibration regime, and adds symmetric debounce on both turn-on and turn-off. The charging-state gate from the previous build is retained — preconditioning does not trigger during an active charging session.

Validated across six captures from multiple testers covering preconditioning, preconditioning→drive→DCFC, preconditioning→drive→AC charging, post-DCFC drive-home, plain driving, and the single-sample-glitch session. No false positives, no false negatives.

### Extra BCM signal polled on 2025+ Ioniq 5

Build 44 re-enables a BCM data identifier (`0xBC09`) that was previously disabled on 2025 Ioniq 5 registries. This is a diagnostic follow-up for the open 2025 AUTO-headlamp question — the previously-watched signal stayed at a "not commanded" value while headlamps were physically on in a parking garage. No user-visible behavior change.

---
## Build 43 — OBDLink CX Polling Responsiveness (for real this time)

Special thanks to testers James and Daria for the rapid turn around on diagnostic logs!

### OBDLink CX: Build 42 Tuning Now Actually Takes Effect

Build 42 advertised improved polling responsiveness on OBDLink CX, but a holdover from an earlier build was quietly undoing the tuning shortly after connect — so testers on OBDLink CX likely didn't feel any difference between Build 41 and Build 42.

Build 43 removes the leftover overrides.

---
## Build 42 — OBDLink CX Polling Responsiveness

### OBDLink CX: Tighter First-Frame Timeout

Build 42 tightens one timing parameter on STN-family adapters (OBDLink CX and kin) based on measured first-frame response latencies from Build 41 tester logs. Projected polling utilization on OBDLink CX drops back to ~73 %, actually below the Carista baseline. Multi-frame reliability is unchanged — that fix (Build 41's adapter-aware configuration) is preserved intact.

Carista and other classic ELM327 clones are unaffected by this change.

---
## Build 41 — OBDLink CX Multi-Frame Reliability

### OBDLink CX: Adapter-Aware Timing

Build 41 targets the intermittent "partial data" errors some testers have seen on VCMS and ICCU multi-frame reads when using an OBDLink CX adapter.

The app now branches its ELM327 configuration during init based on a capability probe: OBDLink CX (and other STN-chipset adapters) receive a timing profile tuned for reliable multi-frame reception, while Carista and other classic ELM327 clones continue to use the same timing as Build 40 — which has been reliable on that hardware.

---
## Build 40 — Resumable ECU Scans, Graceful Pause, Reliability Fixes

### OBDLink CX and other adapters: Multi-Frame Timeout

Stage-1 fix for the VCMS 0xE001 intermittent multi-frame failures observed on genuine OBDLink CX adapters. The ELM327 init sequence now explicitly configure the consecutive-frame reception window to 100 ms — tight enough to not penalize successful multi-frame tails, generous enough to catch the observed 30–60 ms CF arrival latency when VCMS does respond. Transparent no-op on non-STN adapters (Carista clones respond `?` which is caught and ignored; init continues with adapter defaults).

### Complete ECU Scan: Resumable Scans

A paused Complete ECU Scan can now be **resumed from where it left off**, with full provenance recorded across all sessions.

When you reopen the tool, any incomplete scan_log files in your Documents directory show up as a **"Resume prior scan"** button in the preflight. Tap it to see a list of candidates with per-scan progress, session choice (default / extended / both), and the state label from the prior session. Pick one → a confirmation screen shows what UDS session and starting DID will be swept next, with a state-label field pre-filled from the prior session. You can edit the label to reflect how conditions have changed since you paused.

The resumed scan appends to the **same** `scan_log_*.txt` and `scan_found_*.md` files, so your finished-scan artifact shows the full session history — every pause, every resume, every state label, every outcome. For "Both" session choice, resume automatically runs default first, then extended, skipping any UDS session that was already complete.

### Complete ECU Scan: Graceful Pause When the Car Turns Off

EV-specific pain point: if you start a 1–2 hour scan and leave the car idle, it'll eventually turn off on its own. Previously that would leave the scan in a broken state — now it **pauses gracefully** and attributes the cause correctly.

When the target ECU falls silent for 10 consecutive requests, the app automatically probes HVAC (the same mechanism the Dashboard uses for ignition detection). If HVAC also doesn't respond → "the car turned off." If HVAC still responds → "the target ECU stopped responding while the car is still on" (suggests an adapter or ECU issue). Both paths preserve partial results and surface a **Resume** button so you can pick up when conditions are ready.

### Complete ECU Scan: Smaller Polish

- **Elapsed + ETA display.** Progress section now shows running elapsed time and an ETA that improves as the scan runs. ETA is suppressed until at least 20 DIDs have been scanned so early-scan noise doesn't produce jumpy estimates.
- **Stop button + reassurance footer.** The red "Abort Scan" button is now a plain "Stop" button, with a localized footer directly below it: "A stopped scan can be resumed later, you will not lose your progress." Translated to de / es / fr / nl / sv.
- **Extended-session ignition warning.** Preflight now shows an orange warning when Extended or Both session is selected and the app doesn't detect the ignition as on. Warn-only (Start stays enabled) since the ignition reading can be briefly stale.
- **Localization pass.** The completion messaging (Scan complete / Scan stopped / Scan paused — the car turned off / Scan paused — ECU stopped responding) and all phase-progress labels now respect your in-app language override. Previously they stayed English if your iOS system language didn't match the app's language setting.

### Reliability Fixes

- **Dashboard crash fix.** Opening the Battery Temperatures section while BMS data was updating could crash the app
- **"Car off" false reading.** The app could briefly report "car off" while the car was actually running, particularly if a second Bluetooth-connected diagnostic app was sending commands to the same OBD adapter. The app now only flips to "off" when HVAC genuinely stops responding (adapter reports NO DATA / UNABLE TO CONNECT). Transient glitches — multi-frame reception errors, CAN bus hiccups, cross-app interference — keep the previous ignition state rather than falsely flipping.

### ICCU Details: "Failed DIDs" → "Unavailable DIDs"

The list that surfaces DIDs the ICCU declined to report is now labeled **"Unavailable DIDs"** instead of "Failed DIDs". "Failed" implied a tester-side fault; "Unavailable" correctly reflects that the ECU itself chose not to respond (typically NRC 0x31 on a serviced/replaced ICCU). The heading respects the in-app language override via the localization helper. Translated to de / es / fr / nl / sv.

---
## Build 39 — Complete ECU Scan, Files App Access, Potential Fix for OBDLink CX adapters

### OBDLink CX potential fix

Changed adaptive timeout to the default setting which will hopefully remedy the problem with incomplete multi-frame messages

### New: Complete ECU Scan

A new advanced-diagnostic tool that sweeps the full **0x0000–0xFFFF** DID address space of a single ECU — the full 65,536 possible IDs, not just the ones we already know about. Meant for discovery: when a tester sees a signal we don't yet read, this is how we find where it lives.

Find it under **Settings → Advanced Diagnostics → Complete ECU Scan** (same place as DID Scanner and ECU Scanner).

### Diagnostic Logs in Files App

All diagnostic logs and DID snapshots the app writes are now accessible from the **iOS Files app**. Open Files → **On My iPhone** → **Ioniq 5 Diagnostics**. You'll see:

- `diagnostics_YYYY-MM-DD_HHmmss.log` — files from the "Start Recording" button in Settings
- `DID_ABC_*.log` — files from the A/B/C snapshot feature
- `scan_log_*.txt` and `scan_found_*.md` — new, from Complete ECU Scan

You can share, delete, or drag these out to your Mac (via AirDrop, iCloud Drive, or a cable) without needing to go through the in-app Share sheet.

---
## Build 38 — Battery Heating ETA, CarPlay Polish

**NOTE TO TESTERS:** Hi team - I don't normally release an untested feature, but the new "Time to 70°F"/"Time to 21°C" feature seemed fairly safe and I don't know when I'll have a chance to charge next. Please let me know how this works out for you -- this was a feautre suggested by TheIoniqGuy, thanks Corbin for the great idea! Also worth noting, last build I added a feature (multi-DID) intended to speed up initial scanning. It helps most folks, but I think may be lengthening the scan for others. I'm looking into this. Thanks -- Greg

### New: Battery Heating ETA

During user-invoked preconditioning, the Dashboard and CarPlay now display an estimate of how much longer until the coldest battery module reaches **21 °C (≈ 70 °F)** — the threshold the pack needs for DC fast-charge readiness.

On the Dashboard, a new full-width chip inside **Battery · Temperatures > Pre-conditioning** shows the estimate (e.g. "Estimated time to 70°F — ≈ 12 min"). On the CarPlay **Charging** tab, the 12 V voltage chip is repurposed as "Time to 70°F" — showing `--` when preconditioning is not active and `≈ N min` while it is.

The estimate uses a hybrid model: during the first ~10 minutes of a heating session it falls back to a constant warming rate derived from recorded captures (thanks TheIoniqGuy); once the session has gathered enough data, it switches to your car's actual observed slope. Displayed minutes only ever decrease within a session — no "time went up" surprises from sensor noise.

Label switches automatically between °F and °C based on your temperature units preference, and the Dashboard chip is translated into German, Spanish, French, Dutch, and Swedish.

### CarPlay Polish

- **Monospaced digits.** Numeric values in every CarPlay chip (SoC, power, 12 V, current, voltage, heating ETA, etc.) no longer jitter left/right as their digits change width. Same system font face, just tabular digit spacing.
- **Unit-switch rebuild.** Switching between °F and °C now correctly updates chip labels that embed the unit (like "Time to 70°F" → "Time to 21°C"). Previously only an app-language change triggered a rebuild.

### ICCU Name Correction

Corrected the expanded form of "ICCU" from "Integrated **Charger** Control Unit" to "Integrated **Charging** Control Unit" to match Hyundai's official E-GMP terminology. The abbreviation "ICCU" and all other labels stay unchanged.

---
## Build 37 — ICCU Details with Share Sheet, Multi-Frame Reliability, Dashboard Polish

### ICCU Details Section

The Dashboard has a new collapsible **ICCU** section showing decoded identification data for your car's Integrated Charger Control Unit: module ID, part numbers, dataset and software versions, calibration and build dates, serial number, and programming state (FACTORY vs. SERVICED). The data is read automatically at connect, before regular polling begins, and stays constant for the session.

CarPlay gets a new **ICCU** row in the Status tab with the same information in a driver-appropriate 10-row detail view.

From the iOS ICCU section, a new Share button exports a **1080×1350 branded PNG card** suitable for posting to social media or sharing with other testers. The card leads with your vehicle identity (model, year, variant, odometer), lists the ICCU fields, and carries a "Report prepared by IONIQ 5 Companion" badge with a UTC timestamp. Dark aesthetic over a blurred app-icon background. Files save as "ICCU details - YYYY-MM-DD HH-mm-ss.png".

### Multi-Frame Reliability

Removed the `ATCRA` flow-control command from polling and scanning paths. On genuine OBDLink firmware, `ATCRA` disabled the adapter's automatic flow-control filter updates, causing every multi-frame DID after the first ECU switch to stall mid-stream. The same fix empirically resolves long-standing intermittent multi-frame errors on Carista clones: a 2,750-line driving-capture now shows zero ISO-TP errors, with every VCMS multi-frame DID and the 62-byte BMS response completing cleanly across multiple polling cycles.

### Full Session Reset on Disconnect

Pulling the adapter now resets all session-derived state — VIN, model year, variant, ECU registry, and live vehicle data. Only your saved-device preference and general app settings persist. Fixes a class of bug where a prior session's VIN or registry could leak into the next connection and produce wrong-variant readings (e.g., a 2025 RWD displayed as AWD after a reconnect). The CarPlay Status tab follows the same discipline — Scan Status and ICCU rows show "Not Available" after disconnect.

### Dashboard Polish

Overview reorganized: VIN now sits on its own full-width row directly below the state-of-charge gauge, so the full 17 characters display without font shrinking. The duplicate Pre-Conditioning chip was removed from Overview — it already appears in Battery · Temperatures.

Battery · Temperatures restructured into labeled sub-sections: Module Temperatures (with Min/Avg/Max/Delta stats), a new **Pre-conditioning** sub-section grouping Pre-Conditioning status and Battery Heater Temp, and a new **Fan** sub-section. The three history charts now use the same visual style as the Charging section.

### Diagnostics Recorder Now Visible to All Users

The Diagnostics recorder — Start / Stop / Share — is now visible in Settings to every user, no longer hidden behind the five-tap-Build reveal. It's the single most useful tool for reporting unexpected behavior.

A new footer explains when and how to use it and reassures that **your VIN is encrypted in the log file** — only the developer holds the decryption key — so sharing a log doesn't disclose your vehicle identifier. Translated into German, Spanish, French, Dutch, Swedish.

---
## Build 36 — Headlight indicator accuracy + multi-frame reliability

### Headlight Indicator Responsiveness (2022-2024 Ioniq 5)

The low-beam indicator in the app and CarPlay now updates promptly when you turn the headlights off. Previously, the underlying signal from the Body Control Module could take several minutes to retract after the stalk was moved to Off — producing a "stuck on" indicator that only cleared on the next long drive or power cycle. The app now reads the headlight state from a different register that updates within about 6 seconds of the stalk movement.

Small caveat worth knowing about: when Auto mode decides it's bright enough to extinguish the lamps during a daytime drive, the new register is still slower to retract — in the tens-of-seconds range. Most drivers won't notice, because that's a background transition you're not watching for, but it can produce a brief "indicator still on" window when driving from shade into sunlight.

### No More Transient High-Beam Icon (2022-2024 Ioniq 5)

Fixed a glitch where the high-beam icon would briefly illuminate in the app and CarPlay when the headlights came on automatically — particularly visible on a rainy day with the stalk in Auto mode. The old decoder flagged the high-beam indicator on any activity in the high-beam status byte, including unrelated state transitions the BCM produces during Auto-mode lamp changes. The decoder now looks for a specific bit pattern that only appears when the high beams are genuinely engaged.

### More Reliable Multi-Frame Vehicle Data

Hardened the ISO-TP parser — the component that reassembles multi-frame responses from the car. It now validates consecutive-frame sequence counters according to the ISO 15765-2 specification, catching dropped or out-of-order frames that previously produced silently corrupt data for any ECU response longer than 7 bytes. Parser failures are now self-diagnosing, logging specific ECU addresses and byte counts rather than quietly passing bad data up the stack.

Also reordered initial adapter setup to match the ELM327 datasheet more carefully (auto-formatting before auto-flow-control) — should improve connection reliability with clone adapters that have order-sensitive state machines.

---
## Build 35 — Crash fixes + preconditioning accuracy

### CarPlay Crash on Vehicle Disconnect

Fixed a crash that could occur in CarPlay when the Scan Status detail view had been opened and the vehicle then disconnected (or the CarPlay scene reactivated). The app would trip an "Index out of range" error inside the scan-status refresh path and terminate.

Affected four testers across builds 32, 33, and 34 on iOS 26.3 and 26.4. The fix restructures the underlying data so the two lists that had to stay in sync are now a single list — the mismatch that caused the crash is now impossible by construction.

### Dashboard Crash During Battery Updates

Fixed a crash on the Dashboard when viewing the cell voltage grid. If the BMS pushed a payload with a different cell count while the grid was on screen, a stale index could reach into the new shorter array and crash the app.

Affected two testers on build 33 (iPhone 17 Pro Max, iOS 26.4.1). The grid now takes a single snapshot of the cell voltages at render time and iterates over that snapshot, so the index and the data can never get out of step.

### Preconditioning After DC Fast Charging

Fixed false "Preconditioning Active" readings that appeared for the entire drive home after a DC fast charging session. After a high-power charge, the pack's thermal-management system runs its coolant loop for 15–20 minutes or more to bring the battery back to target temperature — and the app was misreading that cooling activity as active preconditioning.

Worked through 56 historical logs and 1,425 samples from four testers (2024 and 2025 AWD variants) to isolate the exact bit in the BMS thermal-status byte that separates heating from cooling. The app now distinguishes the two cleanly: heating turns on the indicator, cooling does not.

---
## Build 34 — Brake light indicator fix

### Brake Light Indicator

Fixed a long-standing issue where the brake-light indicator could appear "stuck on" while driving, even when the brake light was not on. Originally reported by tester Tom on his 2025 Ioniq 5 RWD, with a similar report later from tester Michael on his 2025 AWD Ioniq 5.

The brake-light value lives in a BCM byte that appears to pack several unrelated status bits — only one of those bits actually represents the brake-light state. The previous decoder treated any non-zero value as "brake on," so when any of the other bits in the same byte happened to be set while the brake bit was clear, the indicator would falsely show "On" until the rest of the byte cleared.

Build 34 changes the decoder to look at only the specific brake bit, ignoring the unrelated status bits. The fix applies across all supported vehicles — 2022–2024 Ioniq 5 / Ioniq 6 read the brake state from BCM DID 0xBC06 byte 4, while 2025+ Ioniq 5 and 2026 Ioniq 9 read it from BCM DID 0xBC17 byte 4. Same byte position, same bit, just a different containing DID by model year.

The fix was validated against brake-on captures from three different vehicles (eight distinct byte values, all with the brake bit set) and confirmed live on a 2024 Ioniq 5 test drive that re-captured the exact failure pattern and decoded it correctly under the new rule.

---
## Build 33 — Battery config display + diagnostics unlock fix

### Battery Configuration Display

The Battery Configuration chip on the Dashboard now reflects the actual detected series cell count when it differs from the registry. This catches vehicles whose pack layout differs from the factory spec.

For example, Pieter's 2022 AWD (Hyundai's limited-edition "Project 45") uses a 180-series pack instead of the standard 192 series. The chip now shows "180 series x 2 parallel" based on live BMS data rather than the registry default. The existing registry value is still used as a fallback until the BMS has reported cell voltages.

### Fix: 5-Tap Diagnostics Unlock

The hidden 5-tap gesture that unlocks the developer/diagnostics settings in the About section was incorrectly attached to the Registry row. It's now back on the Build number row, which is where it was designed to live.

---
## Build 32 — CarPlay overhaul, VIN match fix

### CarPlay State-Driven Lifecycle

CarPlay has been completely reworked. Previously, all tabs (Driving, Charging, Parking) were built immediately when CarPlay connected — before the app knew what vehicle you had. This caused RWD vehicles to incorrectly show the AWD layout (Front RPM + Rear RPM instead of just Motor RPM).

Now CarPlay shows only the Status tab until the adapter connects, VIN is read, and ECU training completes. Once the app knows your vehicle, the correct tabs appear. When the car turns off or the adapter disconnects, tabs are removed and the app returns to a clean Status-only state.

The Status tab connection sequence now progresses smoothly: Looking for adapter → Reading → Scanning ECUs → Connected

### Fix: VIN Matching for AWD Vehicles

Fixed VIN matching for 2022-2024 AWD vehicles with VIN position 8 = C (e.g. Pieter's Project 45). These were previously falling through to the default registry instead of explicitly matching the AWD Long Range registry.

### CarPlay Polish

- Fixed the "Vehicle Off" status icon being stretched (the car icon is now properly proportioned)
- Fixed a brief "Vehicle Off" flash during startup when the car was actually on (stale state from the previous session)
- Fixed a brief "Connected" flash during VIN read before ECU scanning starts

### Known Issues

1. **Unplug reminder does not fire while charging** — The HVAC ECU stays awake when the car is off but charging, so the app thinks the car is still on.
2. **Pre-conditioning detection is experimental** — May produce false positives during autonomous BMS thermal management.
3. **Battery odometer shows incorrect values on some vehicles** (Issue #6).
4. **Parking sensors 7 and 12 (rear-side corners) not yet mapped.**
5. **Parking sensor values may flicker** — ECU-side behavior, not an app bug.
6. **Headlight signal sometimes delayed when manually activated in daylight** (Issue #10).
7. **Brake light indicator updates every ~3 seconds** due to OBD polling constraints.
8. **VCMS flow control intermittent failure** — Mitigated but root cause unknown.
9. **Parking sensors only available on 2022-2024 Ioniq 5** — Not yet verified on 2025 or other models.

---
## Build 31 — VIN detection rewrite, 2025 fixes, privacy

### VIN Encryption in Diagnostic Logs

Diagnostic logs now encrypt your VIN using public-key cryptography. This allows you to safely share logs on GitHub without exposing your VIN. Your VIN can only be unencrypted with the private key that I have -- and that private key is not part of code repository -- it is safe and secure.

I don't want anyone feeling nervous about sharing a diagnostic log on Github, and I want to encourage Github for issue reporting because it is a huge help to me. It is really hard to keep everything straight with so many testers sending me information.

Thanks for your support!

### VIN Detection Rewrite

Rewrote the vehicle identification sequence for improved reliability across all model years. The app now waits for ignition before reading the VIN from the MCU, which works universally across 2022–2025 Ioniq 5, Ioniq 6, and Ioniq 9. The previous method (CGW) failed on 2022 models.

The VIN chip in the Overview section is now always visible — it shows "Unknown" in red text until the VIN has been read. Settings > About > Registry also shows "Not read yet" before VIN detection.

### New Vehicle Registry: Ioniq 5 RWD Long Range 2025+

Added a dedicated registry for the 2025 Ioniq 5 RWD Long Range, confirmed by Tester Tom.

### Fix: RWD Long Range Variant Detection (2022-2024)

Fixed variant detection for 2022-2024 RWD Long Range models (Issue #11). These vehicles were previously falling back to the default AWD registry.

### Fix (hopefully): 2025 Ioniq 5 Headlights and Brake Light

Fixed headlight and brake light signal mappings for the 2025 Ioniq 5, which uses different BCM byte positions than the 2022-2024 models.

### Fix: CarPlay Power Display

Fixed CarPlay Power showing "--" when not charging. Now shows instantaneous power value, and uses it as a fallback during charging until enough history accumulates for the sparkline (Issue #13).

### Battery Configuration Display

The Battery Configuration chip now shows the correct cell configuration from the vehicle registry (e.g. "168 series x 3 parallel" for Ioniq 9) instead of a hardcoded value.

### RWD Motor Display

The front motor RPM gauge is now hidden on RWD vehicles in both the Dashboard and CarPlay. The Motors section title changes to "Motor" on RWD vehicles.

### Known Issues

1. **Unplug reminder does not fire while charging** — The HVAC ECU stays awake when the car is off but charging, so the app thinks the car is still on.
2. **Pre-conditioning detection is experimental** — May produce false positives during autonomous BMS thermal management.
3. **Battery odometer shows incorrect values on some vehicles** (Issue #6).
4. **Parking sensors 7 and 12 (rear-side corners) not yet mapped.**
5. **Parking sensor values may flicker** — ECU-side behavior, not an app bug.
6. **Headlight signal sometimes delayed when manually activated in daylight** (Issue #10).
7. **Brake light indicator updates every ~3 seconds** due to OBD polling constraints.
8. **VCMS flow control intermittent failure** — Mitigated but root cause unknown.
9. **Parking sensors only available on 2022-2024 Ioniq 5** — Not yet verified on 2025 or other models.

---
## Build 30 — Ioniq 9 fixes, battery temperature cleanup

### Fix: Ioniq 9 Battery Configuration

Corrected the Ioniq 9 cell configuration to 168S3P (504 total cells).

### Fix: Ioniq 9 Tire Pressure Thresholds

The Ioniq 9 recommends 40 psi. Tire pressure color coding now uses the correct thresholds for the Ioniq 9 (green range 38–43 psi). Previously it was using Ioniq 5 values (33–38 psi), which would show orange for correctly inflated tires. Also fixed a logic issue with the registry files.

### Removed BMS Max/Min Temp Chips

Removed the BMS Max Temp and BMS Min Temp data chips from the Battery Temperatures section. These values from the BMS were unclear in meaning and not useful alongside the module temperature grid.

### Known Issues

1. **Unplug reminder does not fire while charging** — The HVAC ECU stays awake when the car is off but charging, so the app thinks the car is still on.
2. **Pre-conditioning detection is experimental** — May produce false positives during autonomous BMS thermal management.
3. **Battery odometer shows incorrect values on some vehicles** (Issue #6).
4. **Parking sensors 7 and 12 (rear-side corners) not yet mapped.**
5. **Parking sensor values may flicker** — ECU-side behavior, not an app bug.
6. **Headlight signal sometimes delayed when manually activated in daylight** (Issue #10).
7. **Brake light indicator updates every ~3 seconds** due to OBD polling constraints.
8. **VCMS flow control intermittent failure** — Mitigated but root cause unknown.

---
## Build 29 — VIN detection fixes, Ioniq 9 RWD support, variant display

### Fix: VIN Detection for Ioniq 6 and Ioniq 9

Vehicle type detection now uses the full 4-character VIN prefix instead of a single position. Ioniq 6 and Ioniq 9 could not be distinguished previously (both share "M" at VIN position 4). The app now correctly identifies:

* **KM8K / 7YAK** — Ioniq 5
* **KMHM** — Ioniq 6
* **7YAM** — Ioniq 9

Also fixed the Ioniq 6 AWD registry — VIN position 8 was incorrectly set to "F" (copied from Ioniq 5). Corrected to "C" based on confirmed real-world Ioniq 6 VINs.

### New: Ioniq 9 RWD Registry

Added a separate registry for the RWD Ioniq 9 (VIN position 8 = 1). Both RWD and AWD Ioniq 9 variants share the same 110 kWh battery. The app now supports 10 vehicle configurations total.

### Variant Display from Registry

The Dashboard "Variant" chip (e.g., "AWD Long Range", "RWD") now reads directly from the vehicle registry file instead of parsing VIN codes. This ensures correct variant names for all vehicle types, including Ioniq 6 and Ioniq 9.

### Known Issues

1. **Unplug reminder does not fire while charging** — The HVAC ECU stays awake when the car is off but charging, so the app thinks the car is still on.
2. **Pre-conditioning detection is experimental** — May produce false positives during autonomous BMS thermal management.
3. **Battery odometer shows incorrect values on some vehicles** (Issue #6).
4. **Parking sensors 7 and 12 (rear-side corners) not yet mapped.**
5. **Parking sensor values may flicker** — ECU-side behavior, not an app bug.
6. **Headlight signal sometimes delayed when manually activated in daylight** (Issue #10).
7. **Brake light indicator updates every ~3 seconds** due to OBD polling constraints.
8. **VCMS flow control intermittent failure** — Mitigated but root cause unknown.

---
## Build 28 — Per-vehicle registry, battery temp improvements, chart & CarPlay fixes

**NOTE TO TESTERS:** Build 28 was a major code refactoring to make supporting different vehicle types easier long term. Features that used to work may have become broken, so please pay very close attention and report anything that seems incorrect. Thanks!

### Per-Vehicle ECU Registry

The app now reads your VIN immediately on adapter connect and loads a vehicle-specific signal configuration. This enables correct decoding for different models and model years.

* **9 vehicle configurations** — Ioniq 5 (5 variants by drivetrain and year), Ioniq 6 (3 variants), and Ioniq 9
* **Automatic detection** — VIN is read from the CGW before the car even needs to be on
* **Dashboard shows detected model** — New "Model" chip in Overview, registry name in Settings > About
* **2025 Ioniq 5 AC voltage fixed** — OBC byte offset corrected for 2025 models (Issue #8)
* **Ioniq 9 light signals mapped** — BCM headlight and brake light DIDs configured for Ioniq 9 (Issue #9)
* **Parking sensors per-vehicle** — Automatically hidden on vehicles where they don't respond (Issue #7)

### Battery Temperature Improvements

* **More accurate temperature sparklines** — CarPlay battery temp chart now plots the actual min/max across all 16 module temperature sensors instead of the BMS-reported max/min (which included a non-cell sensor reading ~6°C higher than actual cell temps)
* **Cleaned up heater chart** — Removed misleading BMS Max, BMS Min, and inlet temperature lines from the dashboard temperature history chart. Renamed to "Heater Temp History."

### Fixes

* **Charging charts appear immediately** — Previously required collapsing and re-expanding the Charging section when a charge session started
* **Charts visible on first navigation** — Temperature and charging charts now appear immediately when sections are already expanded (no more toggle to reveal)
* **Chart expand animation** — Removed 0.25s delay, charts appear instantly
* **CarPlay parking tab** — Now appears dynamically after ECU training completes. Previously could be missing if CarPlay connected before training finished.
* **CarPlay stale tabs** — Data now refreshes correctly when returning from another app
* **Headlight icon visibility** — Low beam icon now visible in dark mode

### Share Sheet

DID Scanner and ECU Scanner now have a Share button. Exports results to a timestamped text file via the iOS share sheet (AirDrop, Messages, Mail, Files, etc.).

### Known Issues

1. **Unplug reminder does not fire while charging** — The HVAC ECU stays awake when the car is off but charging, so the app thinks the car is still on.
2. **Pre-conditioning detection is experimental** — May produce false positives during autonomous BMS thermal management.
3. **Battery odometer shows incorrect values on some vehicles** (Issue #6).
4. **Parking sensors 7 and 12 (rear-side corners) not yet mapped.**
5. **Parking sensor values may flicker** — ECU-side behavior, not an app bug.
6. **Headlight signal sometimes delayed when manually activated in daylight** (Issue #10).
7. **Brake light indicator updates every ~3 seconds** due to OBD polling constraints.
8. **VCMS flow control intermittent failure** — Mitigated but root cause unknown.

---
## Build 27 — Training reliability, Scan Status dark mode fix, CarPlay Scan Status grouping

### Fix: ECU Training Reliability

The startup ECU scan occasionally failed to detect the VCMS (charging system) and other ECUs. Multiple improvements:

* **Stale frame recovery** — When an ECU's multi-frame response is incomplete, the app now recovers data from subsequent attempts instead of discarding it. Previously, a single failed response could cascade and cause 3-6 ECUs to appear as "not found."
* **Partial response acceptance** — If an ECU responds with a valid first frame but can't complete the full multi-frame exchange during the fast-paced training scan, it is now accepted as found. Normal polling (with 5-second intervals) reliably reads the full response.
* **Retry with recovery** — Failed probes are retried once with a brief pause to clear stale data.

### Fix: Scan Status Visibility

* **HVAC ECU** now shows a green checkmark in Scan Status after training completes. Previously showed an empty circle despite being responsive.
* **Dark mode** — Scan Status icons (checkmark, dash, hourglass) and ECU names now use primary color for better visibility. Previously nearly invisible in dark mode on both Dashboard and CarPlay.

### CarPlay: Scan Status Grouped by ECU

The Scan Status detail list now groups DIDs by ECU name (e.g., "BMS — 9/9 Found") instead of listing each DID individually. Shows "Found" or "Not Found" for each ECU group. This also resolves an issue where some ECUs were missing from the CarPlay Scan Status list.

### Known Issues

1. **Unplug reminder does not fire while charging** — The HVAC ECU stays awake when the car is off but charging, so the app thinks the car is still on.
2. **Pre-conditioning detection is experimental** — May still produce false positives. We are investigating reading the pre-conditioning state directly from the instrument cluster.
3. **Battery odometer shows incorrect values on some vehicles** — The cumulative energy charged/discharged values may be incorrect on some model years due to variable BMS payload lengths. Under investigation (Issue #6).
4. **Parking sensors may not report on some vehicles** — The 2025 Ioniq 5 and Ioniq 9 may show all-zero parking sensor values. Under investigation (Issue #7).
5. **AC voltage may display incorrectly on some vehicles** — Some 2025 models report incorrect AC charging voltage (e.g., 26 V instead of 240 V). Under investigation (Issue #8).
6. **Parking sensors 7 and 12 not yet mapped** — The rear-side corner sensors (driver and passenger) have not responded in any test condition.
7. **Parking sensor values may flicker** — The 1-byte ultrasonic sensors (front center and rear) intermittently report 0 (no detection) even when an object is present. This is ECU-side behavior, not an app bug.
8. **Headlights vs DRL** — The app cannot yet distinguish between headlights on and daytime running lights. Both show the headlight icon.
9. **Brake light response time** — The brake light indicator updates every ~3 seconds due to OBD polling constraints. It is not suitable as a real-time brake light indicator.
10. **Headlights and brake light not working on Ioniq 9** — The Ioniq 9's BCM uses different DIDs for light status. Under investigation (Issue #9).

---
## Build 26 — CarPlay Status tab, consistent connection states, Scan Status detail view

### CarPlay Improvements

* **Connection tab renamed to "Status"** — Now mirrors the Dashboard connection phases: "Looking for adapter", "Reading", "Vehicle Off", "Scanning ECUs", "Connected".
* **Consistent pre-connection states** — CarPlay and Dashboard now both show "Looking for adapter" for all pre-connection states. CarPlay previously showed "Connecting..." and "Scanning..." which were inconsistent.
* **Scan Status detail view** — The Status tab now includes a Scan Status summary row. Tap to view the full DID list with icons showing which ECUs were found (checkmark), not found (dash), or still being scanned (hourglass). The list updates live as training progresses.

### Known Issues

1. **Unplug reminder does not fire while charging** — The HVAC ECU stays awake when the car is off but charging, so the app thinks the car is still on.
2. **Pre-conditioning detection is experimental** — May still produce false positives. We are investigating reading the pre-conditioning state directly from the instrument cluster.
3. **Battery odometer shows incorrect values on some vehicles** — The cumulative energy charged/discharged values may be incorrect on some model years due to variable BMS payload lengths. Under investigation (Issue #6).
4. **Parking sensors may not report on some vehicles** — The 2025 Ioniq 5 and Ioniq 9 may show all-zero parking sensor values. Under investigation (Issue #7).
5. **AC voltage may display incorrectly on some vehicles** — Some 2025 models report incorrect AC charging voltage (e.g., 26 V instead of 240 V). Under investigation (Issue #8).
6. **Parking sensors 7 and 12 not yet mapped** — The rear-side corner sensors (driver and passenger) have not responded in any test condition.
7. **Parking sensor values may flicker** — The 1-byte ultrasonic sensors (front center and rear) intermittently report 0 (no detection) even when an object is present. This is ECU-side behavior, not an app bug.
8. **Headlights vs DRL** — The app cannot yet distinguish between headlights on and daytime running lights. Both show the headlight icon.
9. **Brake light response time** — The brake light indicator updates every ~3 seconds due to OBD polling constraints. It is not suitable as a real-time brake light indicator.

---
## Build 25 — ECU training, headlights & brake light, polling optimizations, CarPlay tab navigation fix

### New: ECU Training Phase

On each Bluetooth connection, the app now automatically discovers which ECUs are present in your car before starting to poll. A progress bar is shown on the Reading screen during this scan. Only ECUs that respond are included in the polling loop, which improves data update rates and eliminates wasted bandwidth on ECUs that don't exist on your vehicle (e.g., parking sensors on models without them).

* **Scan Status panel** in the Dashboard Overview section shows which ECUs responded (green check) or failed (red X) during training. A note explains that some sensors may not be found due to model feature differences.
* **Parking section** is now automatically hidden in both Dashboard and CarPlay if the parking sensor ECU was not detected during training.

### New: Headlights & Brake Light Indicators

* **Headlights chip** — Added to Dashboard Overview and CarPlay Driving tab. Shows a low beam icon on a white background when headlights are on. When high beams are active, the icon switches to the high beam symbol in bright blue. Shows "Off" when headlights are off.
* **Brake Light chip** — Added to Dashboard Overview and CarPlay Driving tab. Background turns red with "On" when the brake pedal is pressed.
* Note: The headlight indicator currently cannot distinguish between headlights on and daytime running lights — both show the low beam icon. We are investigating whether the BCM provides a separate DRL signal.
* Note: The brake light indicator polls every 3 seconds. This is not fast enough to be a real-time brake light indicator — it is an informational display showing brake state, not a safety-critical signal.

### Fix: Charging Charts

* Charging Power, Pack Voltage, and Requested Current charts now sample from the BMS core data poll (3-second, high priority) instead of the VCMS poll (5-second, medium priority). This resolves the sparse, gapped time series that some users reported during charging sessions.

### Fix: CarPlay Tab Reset

* Expanding or collapsing Dashboard sections no longer causes CarPlay to navigate back to the Connection tab. Language changes still correctly rebuild CarPlay templates, and the previously selected tab is now preserved.

### Parking Sensors

* Added "Experimental" warning label and notes explaining that front sensors only report when the car is in Drive, and rear sensors only report when in Reverse.
* Parking section re-layout: sensors grouped into Front and Rear cards with individual notes.

### Known Issues

1. **Unplug reminder does not fire while charging** — The HVAC ECU stays awake when the car is off but charging, so the app thinks the car is still on.
2. **Pre-conditioning detection is experimental** — May still produce false positives. We are investigating reading the pre-conditioning state directly from the instrument cluster.
3. **Battery odometer shows incorrect values on some vehicles** — The cumulative energy charged/discharged values may be incorrect on some model years due to variable BMS payload lengths. Under investigation (Issue #6).
4. **Parking sensors 7 and 12 not yet mapped** — The rear-side corner sensors (driver and passenger) have not responded in any test condition.
5. **Parking sensor values may flicker** — The 1-byte ultrasonic sensors (front center and rear) intermittently report 0 (no detection) even when an object is present. This is ECU-side behavior, not an app bug.
6. **Headlights vs DRL** — The app cannot yet distinguish between headlights on and daytime running lights. Both show the headlight icon.
7. **Brake light response time** — The brake light indicator updates every ~3 seconds due to OBD polling constraints. It is not suitable as a real-time brake light indicator.

---
## Build 24 — Parking sensors - EXPERIMENTAL, motor RPM, CarPlay improvements

### New: Parking Sensor Heatmap - EXPERIMENTAL

* **Dashboard** — New "Parking" section displays all 12 ultrasonic parking sensors in a two-row layout matching the physical bumper arrangement. Sensors use a green-to-red heatmap based on proximity (green >150cm, yellow 75–150cm, orange 30–75cm, red <30cm). 10 of 12 sensors are confirmed and mapped; sensors 7 and 12 are still under investigation.
* **CarPlay** — New "Parking" tab replaces the Experimental tab. Two rows of 6 rendered chips with heatmap background coloring showing distance values for all sensors.
* Distances shown in cm (metric) or inches (imperial), honoring the app's distance unit preference.
* Added ADAS_PRK ECU (0x7B1) to polling at 3-second intervals.

### New: Motor RPM Gauges

* **Dashboard** — New "Motors" section with front and rear motor RPM arc gauges, styled like the SoC gauge. Color transitions from green to yellow to orange based on RPM.
* **CarPlay** — Front and rear motor RPM gauge chips added to the Driving tab.

### CarPlay Improvements

* Driving and Charging tabs now use RowElement layout for better label wrapping in all languages.
* Chip titles use text labels instead of emoji icons, with full translations.
* CarPlay refresh rate increased from 2 seconds to 1 second.

### Translations

* Expanded abbreviated labels across all languages (de, es, fr, nl, sv) for Pre-Condition, Outside Temp, Battery Temp, Battery Heater Temp.
* Swedish: "Laddar" corrected to "Laddning" for Charging tab.
* New strings translated: Parking, Motors, Front Motor, Rear Motor, Front, Rear, sensor activation notes.

### Known Issues

1. **Unplug reminder does not fire while charging** — The HVAC ECU stays awake when the car is off but charging, so the app thinks the car is still on.
2. **Pre-conditioning detection is experimental** — May still produce false positives. We are investigating reading the pre-conditioning state directly from the instrument cluster.
3. **Battery odometer shows incorrect values on some vehicles** — The cumulative energy charged/discharged values may be incorrect on some model years due to variable BMS payload lengths. Under investigation (Issue #6).
4. **Parking sensors 7 and 12 not yet mapped** — The rear-side corner sensors (driver and passenger) have not responded in any test condition. Physical sensor housings are present but may not be wired or may require specific activation conditions.

---


## Build 23 — Translation fix

### Bug Fix

* **EVSE note text not translating** — The explanatory notes on the EVSE tab (both AC and DC) appeared in English regardless of language setting. Caused by duplicate empty entries in the localization file that overrode the translated versions. Fixed.

### Known Issues

1. **Unplug reminder does not fire while charging** — The HVAC ECU stays awake when the car is off but charging, so the app thinks the car is still on.
2. ~~**Charging status lags ~1 minute after stopping**~~ — Should be fixed in build 20. The new VCMS signal transitions immediately. Needs verification.
3. **Pre-conditioning detection is experimental** — May still produce false positives. We are investigating reading the pre-conditioning state directly from the instrument cluster.
4. **Battery odometer shows incorrect values on some vehicles** — The cumulative energy charged/discharged values may be incorrect on some model years due to variable BMS payload lengths. Under investigation (Issue #6).

---

## Build 22 — Scanner improvements, EVSE fix, translations

### ECU Scanner Reliability

* Two-pass scanning: TesterPresent (3E 00) first, then ReadVIN (22 F1 90) for ECUs that don't support TesterPresent (e.g., HVAC). Scan takes 3–5 minutes but finds more ECUs.
* Fixed adapter stability issues that caused incomplete scans or crashes.

### DID Scanner Improvements

* **Custom ECU address** — New "Custom" option in the ECU picker. Enter any TX address (e.g., 7C4) and the RX address is auto-calculated as TX+8. Useful for scanning the unknown ECUs discovered by the ECU scanner.
* **NRC filtering** — Negative responses are no longer counted or displayed. Only DIDs that return actual data appear in results.
* **Polling resume fix** — Navigating away from the DID scanner while a scan is running no longer leaves polling stopped.

### EVSE Power Calculation Fix

* AC power displayed on the EVSE tab was incorrect on some vehicles. Now calculated from AC voltage and max current derived from the control pilot duty cycle, which is reliable across all markets.

### Translations

* Added translations (de/es/fr/nl/sv) for AC Voltage, CP Duty, CP Duty Cycle, Max Current, Max Power, Max Voltage, and EVSE explanatory notes.

### Known Issues

1. **Unplug reminder does not fire while charging** — The HVAC ECU stays awake when the car is off but charging, so the app thinks the car is still on.
2. ~~**Charging status lags ~1 minute after stopping**~~ — Should be fixed in build 20. The new VCMS signal transitions immediately. Needs verification.
3. **Pre-conditioning detection is experimental** — May still produce false positives. We are investigating reading the pre-conditioning state directly from the instrument cluster.

---

## Build 20 — Charging detection rewrite

### Charging Detection Rewrite

The charging detection system has been completely rewritten using a new signal from the Vehicle Charging Management System (VCMS).

* **Works across all markets.** The previous detection relied on a BMS signal that did not work on European vehicles. The new signal has been verified on both US and EU cars.
* **Immediate AC vs DC detection.** The app now knows whether you are AC or DC charging as soon as the charger connects — no more "Detecting" transitional state or 6-second delay.
* **Works with car on or off.** The previous detection could miss charging sessions that started with the car off. The new VCMS signal is active regardless of ignition state.

**Please test and report!** If you charge (AC or DC) with this build, let us know if the charging status displays correctly.

### Known Issues

1. **Unplug reminder does not fire while charging** — The HVAC ECU stays awake when the car is off but charging, so the app thinks the car is still on.
2. ~~**Charging status lags ~1 minute after stopping**~~ — Should be fixed in this build. The old BMS signal was slow to clear; the new VCMS signal transitions immediately. Needs verification.
3. **Pre-conditioning detection is experimental** — May still produce false positives. We are investigating reading the pre-conditioning state directly from the instrument cluster.

---

## Build 19 — Charging signal investigation, ECU scanner, diagnostic improvements

### Charging Signal Investigation

* Added polling of VCMS (0x744) DIDs E002 and E003 for raw diagnostic capture. These contain EVSE (charger station) data, control pilot voltage, battery target voltage/current, and charging counters. No decoded values yet — the raw data is captured in diagnostic logs to help us analyze and improve charging detection across different vehicle markets.
* **If you are charging (AC or DC), please record a diagnostic log and share it.** We are actively investigating charging detection signals that work across all Ioniq 5 variants. Logs that capture the transition from not-charging to charging are especially valuable.

### ECU Scanner

* New tool under Settings > Advanced Diagnostics. Scans all CAN bus addresses (0x700–0x7FF) to discover which ECUs are present on your vehicle. Results can be copied to clipboard. This helps us identify ECUs that may differ between model years and markets.

### Diagnostic Logging Improvements

* BLE scanning events are now captured in diagnostic logs — scan start, device discovery, and device selection. Previously only post-connection events were logged, making it difficult to diagnose connection issues.

### Known Issues

1. **Charging status shows "Inactive" on some European vehicles** — The BMS charging flag (used to determine if charging is active) does not set on some EU-market vehicles during AC charging. We are investigating alternative signals from the VCMS (Vehicle Charging Management System) that appear to work across all markets.
2. **Unplug reminder does not fire while charging** — The HVAC ECU stays awake when the car is off but charging, so the app thinks the car is still on.
3. **Charging status lags ~1 minute after stopping** — The BMS isCharging flag is slow to clear.
4. **Pre-conditioning detection is experimental** — May still produce false positives. We are investigating reading the pre-conditioning state directly from the instrument cluster.

---

## Build 18 — Pre-conditioning experiment, CarPlay improvements

### Pre-Conditioning Detection (Experimental)

* The "Battery Heater" indicator has been renamed to "Pre-Conditioning" throughout the app and CarPlay.
* Detection now uses a different BMS signal (byte 9, believed to be heater power) instead of byte 12 (which turned out to be a temperature reading, not a power indicator).
* Added a 25-second debounce filter — the signal must be sustained for 25 seconds before pre-conditioning is shown as active. This filters out brief thermal management events that are not user-initiated preconditioning.
* Pre-conditioning is automatically suppressed while AC or DC charging is active.
* **This is experimental.** We are still working to reliably distinguish user-initiated pre-conditioning from autonomous BMS thermal management. Please report if you see false positives or missed detections.

### CarPlay Improvements

* **Driving tab expanded to two rows.** Row 1: SoC, Pack, Odometer. Row 2: Energy, Outside temp, Pre-Condition status, Heater Temp, Battery Temp, 12V, Cell Δ. Previously only had one row with 5 chips.
* **Charging tab also uses explicit two-row layout** for consistent spacing with the Driving tab.
* Updated chip labels: "Batt Temp" is now "Battery 🌡️", "Outside" is now "Outside 🌡️", added new "🔋 Heater 🌡️" chip showing heater temperature, "Pre-Conditioning" shortened to "Pre-Condition" to avoid truncation.

### Bug Fixes

* **Settings connecting spinner disappearing on scroll** — The spinning indicator next to the adapter name in Settings would vanish when scrolled off screen and back. Replaced with an animated SF Symbol that survives cell recycling.
* **Missing translations** — Added translations (de/es/fr/nl/sv) for "Reading" and "Turn on your vehicle to view diagnostics." which were missing after the Build 17 dashboard refactor.

### Known Issues

1. **Unplug reminder does not fire while charging** — The HVAC ECU stays awake when the car is off but charging, so the app thinks the car is still on. The "don't forget your dongle" reminder never triggers. Need a better on/off signal than HVAC responsiveness.
2. **Charging status lags ~1 minute after stopping** — When charging is ended, the app continues to show active charging for about a minute. The BMS isCharging flag is slow to clear. May need a faster stop-detection signal or combination of signals.
3. **Pre-conditioning detection is experimental** — May still produce false positives or miss real preconditioning events. See above.

---

## Build 17 — Swedish language, smoother dashboard, unplug reminder fix

### Swedish Language Support

* Svenska is now available as a language option in Settings. All ~200 strings are translated, including UI labels, status messages, and the longer educational text (battery health explanations, efficiency descriptions).

### Dashboard Improvements

* The connection screens (searching for adapter, reading data, vehicle off) are now a single unified panel. Previously these were separate screens that swapped in and out, causing a jarring jump during the connection process. Now the panel stays in place and only the text, icons, and indicators change smoothly within it.
* When connected to the adapter, the OBD port image is replaced by a car icon. When the vehicle is off, the car appears dimmed with a pulsing "Turn on your vehicle to view diagnostics" prompt.
* Removed the "Ioniq 5" reference from the vehicle-off message — the app now says "Turn on your vehicle to view diagnostics."

### Bug Fixes

* **Unplug reminder was not firing even when the toggle showed ON.** If you installed the app and never manually toggled the Unplug Reminder switch, the setting was never actually written — the toggle displayed as ON (its visual default) but the code read it as OFF. This affected all users who hadn't explicitly toggled the switch. Fixed by registering proper defaults at app launch. Thanks to Tom for the diagnostic log that identified this.

### Known Issues

1. **Unplug reminder does not fire while charging** — The HVAC ECU stays awake when the car is off but charging, so the app thinks the car is still on. The "don't forget your dongle" reminder never triggers. Need a better on/off signal than HVAC responsiveness.
2. **Charging status lags ~1 minute after stopping** — When charging is ended, the app continues to show active charging for about a minute. The BMS isCharging flag is slow to clear. May need a faster stop-detection signal or combination of signals (e.g., OBC voltage drop for AC, or VCMS byte 6 transition).
3. **Battery heater is not a reliable pre-conditioning indicator** — The heater signal (BMS 0106 byte 12) shows the battery heater cycling on/off briefly during normal charging, not just during user-initiated pre-conditioning. Previous byte (9) gave false positives when heater was off; current byte gives false positives when heater is on for reasons other than pre-conditioning. Need a better signal or combination to distinguish true pre-conditioning from normal thermal management.

---

## Build 16 — Odometer fix for 2025 models

### Bug Fix

* Odometer was showing 0 on some 2025 Ioniq 5 vehicles. The instrument cluster ECU on these cars sends a "please wait" response before the actual odometer data, which the app wasn't handling. The app now correctly processes this delayed response pattern. Thanks to TheIoniqGuy for the diagnostic log that identified this.

### Known Issues

1. **Unplug reminder does not fire while charging** — The HVAC ECU stays awake when the car is off but charging, so the app thinks the car is still on. The "don't forget your dongle" reminder never triggers. Need a better on/off signal than HVAC responsiveness.
2. **Charging status lags ~1 minute after stopping** — When charging is ended, the app continues to show active charging for about a minute. The BMS isCharging flag is slow to clear. May need a faster stop-detection signal or combination of signals (e.g., OBC voltage drop for AC, or VCMS byte 6 transition).
3. **Battery heater is not a reliable pre-conditioning indicator** — The heater signal (BMS 0106 byte 12) shows the battery heater cycling on/off briefly during normal charging, not just during user-initiated pre-conditioning. Previous byte (9) gave false positives when heater was off; current byte gives false positives when heater is on for reasons other than pre-conditioning. Need a better signal or combination to distinguish true pre-conditioning from normal thermal management.

---

## Build 15 — AC/DC charge detection, signal fixes, smarter polling

### Charging

* Charge type (AC vs DC) now correctly identified. Uses the On-Board Charger's AC input voltage to distinguish: ~245V means AC charging, near-zero means DC fast charging. Verified at Level 2 AC and 123kW DC CCS. Replaces the previous approach which caused the Type chip to flicker between AC, DC, and Not Charging.
* When charging begins, the Type chip briefly shows "Detecting" while the app confirms AC vs DC. Previously it would flash "DC Fast" for a few seconds during AC charging startup.
* Removed "Locked In" chip — the signal we were using turned out to be the battery main relay status, not the charging socket. It stayed latched after DC charging even with no cable connected.
* Removed "Inlet Temp" from CarPlay charging view — the reading was tracking outdoor ambient temperature, not battery coolant. Showed no change during DC fast charging while module temps rose 15°C.

### Odometer Fix - finally!

* The odometer was showing incorrect values (zero or swapped units) for many testers. Root cause: the car's instrument cluster only provides the odometer in whichever unit the display is set to (km or miles) — the other value is zero. The app now reads both, uses whichever is non-zero, and converts to get the other. This has been verified to resolve the odometer issues reported by multiple testers.
* Odometer now polls every 30 seconds (was 60) for more responsive updates while driving.

### Bug Fixes

* Battery heater status was showing "On" when the heater was off. The signal was reading the wrong byte in an undocumented BMS response. Corrected based on comparison of heater-on and heater-off diagnostic logs. See Known Issue #3.
* DID Scanner no longer causes the CarPlay display to jump back to the Connection tab.

### DID Scanner

* Scanner remembers your last ECU, start DID, and end DID between visits.
* New "Copy All" button copies all scan results to clipboard.

### Performance

* When the car is off, the app now only polls HVAC as an ignition probe instead of polling all ECUs. Reduces adapter traffic. All ECUs refresh immediately when the car turns back on.

### Known Issues

1. **Unplug reminder does not fire while charging** — The HVAC ECU stays awake when the car is off but charging, so the app thinks the car is still on. The "don't forget your dongle" reminder never triggers. Need a better on/off signal than HVAC responsiveness.
2. **Charging status lags ~1 minute after stopping** — When charging is ended, the app continues to show active charging for about a minute. The BMS isCharging flag is slow to clear. May need a faster stop-detection signal or combination of signals.
3. **Battery heater is not a reliable pre-conditioning indicator** — The heater signal shows the battery heater cycling on/off briefly during normal charging, not just during user-initiated pre-conditioning. Previous byte gave false positives when heater was off; current byte gives false positives when heater is on for reasons other than pre-conditioning. Need a better signal or combination to distinguish true pre-conditioning from normal thermal management.


---

## Build 14 — Odometer fix, dynamic cell detection, CarPlay polish

### Bug Fixes

* Odometer now updates in real time while driving. Previously read from a BMS snapshot that only updated at key-on. Now reads from the instrument cluster ECU (per OBDb database).
* Cell voltage display no longer gets stuck on "Loading cells 180/192". The app now dynamically detects the actual number of cells in your battery and shows whatever is available. Fixes the issue for Project 45 and other variants with non-standard cell counts.

### CarPlay

* All value+unit labels refined — units now appear in a smaller, non-bold font baseline-aligned with the value. Cleaner look across all chips.
* Full temperature unit labels on Batt Temp sparklines — now shows "°C" or "°F" instead of just the degree symbol.
* Odometer chip no longer clips on high-mileage vehicles.
* "Bat Temp" renamed to "Batt Temp" on Driving tab for consistency.
* Green checkmark now displays correctly when connected.

### Diagnostics

* Diagnostic log now starts with a header showing app version/build, device name, adapter firmware, protocol, and VIN. Makes it much easier to identify which tester and configuration produced a log.

---

## Build 13 — Battery Health info, CarPlay Driving tab, notification logging

### Battery Health

* Info icon on the Health chip — tap it for an explanation of what the BMS-reported State of Health value means, and why it should be treated as a general indicator rather than a precise measurement.

### CarPlay

* "Battery" tab renamed to "Driving" with a new Odometer chip showing distance in your preferred unit (km/mi).

### Odometer

* Polling frequency increased from every 2 minutes to every 60 seconds. Should update more reliably during drives.

### Bug Fixes

* Navigation titles (Settings, Dashboard, Connect) could get stuck in a non-English language when switching back to System Default. Fixed by using the bundle-based localization approach for all main navigation titles.
* Tire pressure chips no longer wrap to two lines on narrow screens — values scale down to fit instead.
* DataChip height is now consistent across a row — long values like "Not Charging" that scale down no longer cause shorter chips.

### Unplug Reminder

* Diagnostic log now captures the full notification decision — if you're not seeing the unplug reminder, record a diagnostic log and turn the car off. The log will show whether the notification fired and why or why not.

---

## Build 12 — Battery Odometer with efficiency tracking

### Battery Odometer

* New section replacing the old Energy display. Shows your battery's lifetime energy charged and discharged as a visual equation: Discharged / Charged × 100 = Efficiency %.
* Efficiency percentage tells you how much energy your battery retains vs. loses as heat over its lifetime. Tap the info button for a full explanation.
* "Battery · Energy" section renamed to just "Battery".

### Bug Fix

* Language section header and picker label in Settings were not translating. Added missing translations.

---

## Build 11 — Connection fix for adapter timeout

### Bug Fix

* Fixed a connection failure affecting multiple testers where the app would repeatedly time out trying to connect. The root cause: some adapters send a stray byte during initialization that broke the app's ability to read the response. The adapter was responding correctly — the app just couldn't see it. Should be fixed for all affected testers.

---

## Build 10 — CarPlay SoC fix, connection diagnostics

### Bug Fix

* CarPlay SoC gauge now matches the dashboard — both use floor rounding to match the car's instrument cluster. Previously 79.6% showed as 79% on dashboard but 80% on CarPlay.

### Connection Improvements

* Increased adapter settle time from 500ms to 1 second after Bluetooth service discovery before sending the first command. May help adapters that need more warm-up time after connecting.
* Diagnostic logs now capture significantly more detail for troubleshooting connection issues — if you're having trouble connecting, please capture a diagnostic log and send it our way.

---

## Build 9 — Adapter compatibility, device info

### Adapter Compatibility

* Removed firmware version validation — the app no longer rejects adapters based on their ATZ response string. ELM327 clones report a wide variety of version strings ("ELM327 v1.5", "OBDII v2.2", etc.) and they're all compatible. If the adapter responds at all, it's accepted.

### Settings

* The OBD-II Adapter section now shows three details when connected: Device (Bluetooth name), Adapter (firmware version), and Protocol.

---

## Build 8 — Diagnostic recording, expanded snapshots

### Diagnostic Recording

* "Record Data" renamed to "Start Recording Diagnostics" — now captures everything: BLE connection events, adapter initialization commands and responses, disconnect reasons, plus all vehicle data. If you're having connection issues, start recording before connecting and share the log for troubleshooting.

### A-B-C Snapshots

* Snapshot data and diffs now write to a shareable log file instead of requiring a console connection. A "Share ABC Log" button appears after taking snapshots.
* Snapshots now capture all 12 ECUs (45 DIDs total) instead of just BMS and HVAC — much more comprehensive for identifying what changes between conditions.

### Settings

* Diagnostics section reorganized — recording and sharing are in their own "Diagnostics" section, while DID Scanner, Snapshots, Simulate, and Reset Onboarding are grouped under "Advanced Diagnostics".

---

## Build 7 — Odometer fix, battery thermal monitoring

### Bug Fix

* Odometer was wrong for vehicles over 65,535 km — was reading 2 bytes instead of 3, causing high-mileage vehicles to show incorrect values (e.g. 91,874 km displayed as ~26,227 km)

### Battery Thermal Monitoring

* New Battery Inlet Temp sensor — tracks the coolant temperature entering the battery pack. Shown as a green line on the BMS Temp History chart alongside BMS Max (red), BMS Min (blue), and Heater (orange)
* Renamed "Heater" to "Battery Heater" throughout the app to clarify this is the battery pre-conditioning heater, not the cabin climate heater

### CarPlay

* Battery Heater chip is now smarter — shows a heater temperature sparkline when the heater is active, and "Off" when inactive
* New Inlet Temp sparkline chip replaces the old dedicated heater temp chart, giving a more complete thermal picture while charging

---

## Build 6 — Multi-language support, temperature fix

### Localization

* Full app localization in Dutch, German, Spanish, and French (~190 strings per language)
* In-app language picker in Settings — choose System Default, English, Nederlands, Deutsch, Español, or Français
* All screens translate live when you switch languages, including CarPlay
* CarPlay tab titles, card labels, and connection status all translate

### Bug Fix

* Outside temperature was incorrectly showing cabin temperature instead of ambient. Now correctly reads the Ambient Air Temperature sensor per the OBDb community database.

### Overview Section

* Added outside temperature chip showing the ambient temperature in your preferred unit

### Tire Pressure

* Extended green (normal) tire pressure range from 33–38 psi to 33–40 psi based on beta tester feedback.

---

## Build 5 — Battery fan monitoring, CarPlay demand power

### Battery Temperatures

* New Fan Status and Fan Speed gauges — compact arc gauges showing the commanded fan level (0–9) and actual fan tachometer feedback (0–120 Hz). Useful for monitoring battery cooling and detecting potential fan issues.

### CarPlay

* Demand chip now shows calculated demand power (kW) and requested current (A) instead of a sparkline chart — easier to read at a glance while driving
* 12V battery color made consistent (white) across Battery and Charging tabs

---

## Build 4 — CarPlay overhaul, new sensors, time series improvements

### CarPlay

* Completely redesigned — all tabs now use card-style elements with titles and rendered images
* Charging tab expanded to 14 items across 2 rows
* Battery tab shows SoC gauge, pack info, BMS min/max temp sparkline, and 12V battery
* Connection icon now changes color by state (green=connected, yellow=connecting, red=error)
* All temperatures respect your chosen unit (°C/°F)
* No more tab bar flickering when switching between tabs

### Dashboard

* Battery section split into "Battery – Energy" and "Battery – Temperatures"
* Battery Temperatures section reorganized with module temperature grid, color legend, BMS Temp History chart, and Heater Status chart
* Heater chip pulses with an orange glow when the battery heater is active
* Dashboard sections can be reordered — tap the list icon to drag sections into your preferred order

### New Sensors

* BMS Max Temp and BMS Min Temp
* Battery Heater Temperature
* Tire temperatures displayed below each tire pressure reading
* Outside temperature now matches the car's dashboard display

### Time Series Charts

* New "Time Charts" setting to limit chart time range (1–83 hours, default 3 hours)
* Charts break lines across time gaps instead of drawing misleading straight lines
* Temperature chart Y-axis moved to left side with clock time on X-axis

---

## Build 3 — VIN fix for 2025 models, reliability improvements

### VIN Reading

* Fixed: VIN now reads correctly on 2025 models (US-market VINs starting with "7" were incorrectly rejected)
* VIN detection is faster and more reliable on cold start

### Notifications

* Fixed: Unplug reminder notification now works on first install — the permission prompt was never shown unless you toggled the setting manually

### Display

* Screen stays awake while the app is in the foreground
