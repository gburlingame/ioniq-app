---
layout: default
title: Version History
nav_order: 5
---

# Version History



---
## Build 139 — Improved navigation guidance, fixed DC session end bug, improved Genesis GV60 support

NOTE TO TESTERS: If you use the nearest charger feature in order to navigate to a charger, please listen to the spoken guidance and let me know if you hear anything unusual.  If you share your drive diagnostic file with me (Settings / Diagnostics),  I'll be able to replay your drive in the simulator, allowing me to experience what you experienced -- just like I was in the car with you!

### Spoken guidance now works with another app on screen
Turn-by-turn was silently dropped whenever Apple Music — or anything else — owned the CarPlay display: the app never declared that it plays audio, so the prompt was composed and then thrown away. It does now.

### Road numbers are spoken correctly
"RT-3A" was read aloud as "R T negative 3 A" — a hyphen just before a digit is parsed as a minus sign. Route designators now expand to words ("Route 3A", "Interstate 95", "State Route 16") in your chosen language, and any remaining hyphen before a digit becomes a short pause. That second rule needs no vocabulary, so it also fixes the Spanish and Turkish national routes numbered with hyphens (A-2, N-340, D-100).

### Better maneuver banners over other CarPlay apps
Instruction text no longer truncates to "…". CarPlay picks the longest instruction that fits from a list of progressively shorter ones, and the app supplied only the full sentence from Maps, so a narrow banner had nothing to fall back on. Each maneuver now carries a short form as well ("Turn right"), translated across all nine languages — which also fixes the turn arrow outside English, since the icon was chosen by matching English words and a German, French, Korean or Turkish instruction always drew a plain straight-ahead arrow. The banner no longer sits on screen indefinitely either: it was being re-presented with fresh distance on every GPS fix, about once a second, so it could never time out.

### No more false "rerouting" at highway interchanges
Off-route detection compared your heading against the nearest piece of the whole route. At an interchange the route can loop back within a few metres of itself on a different heading, so on the ramp the app measured against the leg you would drive half a minute later — reporting a 79° divergence while the car sat 3 m from its own route, and rerouting three times in a row. Heading is now compared against the road you are currently on, which cannot double back on itself.

### A DC fast charging session now ends when charging ends
Since Build 131 the app kept a session open long after the charger stopped — that bug is fixed in this build.

### Genesis GV60 is identified correctly
Fixed a gap in the GV60 VIN decoding logic.  Thanks Ron!

---
## Build 138 — Improvements to efficiency and range measurements, easy access whole-trip map view, and a DC Charging band fix

NOTE TO TESTERS:   If you wonder how IONIQ 5 Companion calculates range and efficiency (and estimates SoC%), you may be interested in a paper that explains the calculations under the hood, now available on the support site:  https://www.theburl.com/ioniq-app/efficiency-and-range.html

### Efficiency and range now come from the battery's own accounting
The CarPlay rolling efficiency used to integrate pack volts × amps while the History trip figure used the battery's available-energy reading.  Both figures now use the BMS available energy and determine distance from the same distance calculation engine.   Please see the paper for a more in depth explanation.

### Steadier rolling efficiency
Rolling efficiency updates at most once a minute rather than roughly once a second. Stopping no longer resets the measurement either — idling with the climate running spends real energy over no distance, and now shows up as worse efficiency instead of being ignored.

### Smoother arrival-charge estimate
The CarPlay arrival-SoC estimate was disproportionately sensitive to efficiency.  It now shows a running average of the last five one-per-minute projections, turning a 5-point jump into five 1-point steps; a new destination or reroute starts a fresh average. 

### See the whole trip on the CarPlay map
The navigation map's `+` button is now a zoom-to-fit button that frames the road still ahead — from where you are to the destination, north-up — plus your own position, so a missed turn still shows the car. Tap Recenter to return to the driving view. Zooming out no longer hits a wall either: `-` used to stop dead at a 15 km view and now widens to a continental view. The fit is one continuous glide — the map tilts flat, turns north-up and pulls back to trip scale in a single motion. The charger map's `+` and `-` are unchanged.

### Fixes
- Fixed an issue that led to the DC Charging signal recording as 0 during a DC Fast Charge session. Thanks Akio!
- History ▸ Signals now shows battery energy at its real precision. Available energy resolves to 0.002 kWh and the lifetime charged/discharged counters to 0.1 kWh, but the value formatter rounded both below what the signal can report, hiding 98% of available energy's resolution. They now read to three decimals and one decimal respectively, in the stats row and the chart's scrub readout.
- The CarPlay Range chip's efficiency unit no longer runs off the edge of the tile. `kWh/100km` — the default in every metric locale — was too wide for the chip and appeared as `kWh/10(`. Both rows are now measured against the tile's margin, with the unit shrinking first and the value only giving ground once the unit reaches its legibility floor.

---
## Build 137 — CarPlay appearance control, smarter rerouting, and a nationwide charger map

### Choose your CarPlay appearance
A new Settings / CarPlay / Appearance setting offers Auto, Light, and Dark. Auto works exactly as before, following how Appearance is selected in CarPlay's Settings menu. Light and Dark pin the app's appearance no matter what the car says, and bring their own background — the aurora from your Settings / Themes selection — so text and tiles stay readable. This fixes the long-standing dark-on-dark case where a car set to "Always Dark" without "Always Show Dark Maps" left some labels hard to read, and allows for a new level of personalization.

### Smarter wrong-turn rerouting
CarPlay navigation now recognizes a wrong turn in about a second — from your direction of travel, not just how far you've drifted from the route. Rerouting never opens with an immediate U-turn while you're moving: the app assumes you'll keep heading the way you're pointed and offers a route that continues with your travel ("continue, then turn right").  If a turn-back genuinely is the only option, it's shown as a normal maneuver ahead — never "make a U-turn now."

### The charger map now covers the whole country
Zoom out and you'll see real charger density everywhere instead of an empty map. A compact "survey atlas" of every DC fast-charge site (≥50 kW) in your country downloads once — about 15 MB for the US, refreshed weekly with tiny updates and re-downloaded monthly — and shows grouped "×N" pins. Speed and network filters apply instantly with no downloading, and the crosshair can point to the nearest matching charger anywhere in the country. Point the crosshair at a survey site to fetch that one site's full details (name, address, connectors) in place; zoom into an area and complete local AC+DC detail fills in as before. Zoom-out now caps at about a 2,500 km-wide view.

### More pins, finer clusters
The map now shows roughly 3× as many pins at every zoom level — wide-area "×N" groupings spread into finer clusters instead of collapsing into a few big buckets. In dense areas clusters may visually touch, the accepted cost of the denser field.

### Charger map fixes
- Fixed the map freezing (up to several seconds per frame) when zoomed far out: the viewport query now scales with how many chargers are known rather than the visible area, network-brand classification is cached, and repeated zoom presses at the zoom limit no longer re-run the full recompute.
- Fixed the crosshair selecting a far-away charger while sitting directly on a group of pins: it now scans the full set of chargers in view and merges the survey-atlas layer by distance, so pointing at a cluster picks what's actually under it.

---
## Build 135 — CarPlay speaks your directions; Charger filter updated for use around the world, tweak to Headlight tile

NOTE TO TESTERS: CarPlay navigation now talks you through every turn, in a voice you pick. The charger network filter also stopped being a USA-only list. Please tell me how the voice cadence feels at speed, and whether your local networks show up correctly when you filter.  

KNOWN ISSUES:
- Experimental parking feature is not implemented yet

### CarPlay navigation now speaks your directions
Turns are announced as you approach them.  Music and podcasts duck for each prompt and come back afterward. Spoken guidance is on by default and can be silenced either from the navigation map while driving or in Settings / CarPlay.

### Choose which voice speaks
Settings / CarPlay / Select Navigation Voice lists the voices installed for your language, best first, with a play button to hear each one before choosing. If only the basic voice is installed, the app points you to Settings / Accessibility, where a more natural Premium or Enhanced voice can be downloaded.  I like the Ava (Premium) voice, but that may only be available in iOS27 (not sure).

### The charger network filter now works anywhere in the world
The filter adapts to your region instead of offering a fixed USA list: it shows the networks actually present in the surrounding area, organized alphabetically with range drill-downs ("A–E") when the list is long. Selected networks pin to the top; sites with unknown operators live under "Other". The list follows the map — pan to a distant city and the filter offers that area's networks, updating in place if it is already open. Rows show a local site count ("Electrify America (6 nearby)"). Previously saved network selections are reset once.

With a network selected, the app downloads that network's full site list continent-wide, and the charger-map crosshair always points toward the nearest matching station — at any distance — instead of pointing at nothing when none is nearby.

### A faster, quieter charger map
Apple Maps is now queried once per map position, with no background search sweeps or pacing queues behind it — which fixes the constantly-spinning search indicator and the sluggish panning reported in testing. The Open Charge Map area download is unchanged and remains the complete local data source. The "search paused" state and its hint line are gone.

### Charger info box
The headline shows the full Open Charge Map station title when available, the network line always shows the operator ("3.9 mi · IONNA"), and a new street-address line wraps below it.

### Navigation map: zoom, pan, and a new turn banner
During guidance the +/− buttons now set an absolute zoom (roughly 150 m to 15 km) rather than a cap tied to your speed, and beyond about 1.5 km the map flattens toward a top-down survey view. Dragging the map breaks out of follow mode into a free north-up pan so you can look ahead along the route; Recenter resumes following. The "next turn" banner on the Driving page moves from an opaque box at the top to a dark glass capsule floated at the bottom center, tinted to match the tiles in both day and night.

### Headlight tile
- The CarPlay Headlights tile (Icons mode) now respects the CarPlay day/night setting. At night it uses the standard dark tile background with a white low-beam glyph instead of a fixed white tile with a black glyph; daytime appearance is unchanged and high beam stays blue in both.   Thanks Tom!

---
## Build 134 — CarPlay turn-by-turn improvement

NOTE TO TESTERS: Fixed a navigation bug

KNOWN ISSUES:
- Experimental parking feature is not implemented yet

### CarPlay navigation fix
Fixed CarPlay guidance skipping the next navigation maneuver 

### CarPlay performance
Initial cold launch view of the map is faster

---
## Build 133 — Customizable CarPlay Driving tiles, Help for every tile, on-device recorders, and fixes

NOTE TO TESTERS: The headline is CarPlay tile customization -- you now have the ability to customize both full size and split screen CarPlay layouts!  Single motor owners can replace the peace symbol, owners without a Battery Warmer are no longer reminded of what they dont' have.   Split screen fans can finally see the tiles!  Some old favorite tiles have made their return.   I'm excited to start working on the big backlog of tiles I need to implement (after Version 3.0 gets released).

KNOWN ISSUES:
- Experimental parking feature is not implemented yet
- Navigation skips ahead in maneuver guidance, rerouting needs improvement

### Customize your CarPlay Driving tiles
Settings → CarPlay → Customize Tiles lets you choose which tiles show and where, with separate Full Screen (2×8) and Split Screen (2×4) arrangements. More tiles are in the pool: Compass and Odometer can now show together, the tire faces split into three tiles (Tire Pressure / Tire Temp / both together), and the climate "Cabin" tile (Exterior / Cabin / Humidity) returns. Split-screen head units switch to the 2×4 layout automatically. The old "Replace Odometer with Compass" toggle is retired — existing dashboards migrate 1:1.

### Help for every CarPlay tile
All 20 tiles now have their own authored Help page. The Help ring shows pages for exactly the tiles on your current layout, in slot order, and re-derives the list when you switch between full and split screen. Each tile page shows the live tile as its hero image, the tile customizer shows the same help text under the selection wheel (read what a tile does before you place it), and Help remembers which page you were on when you leave and come back.

### Hiding the Brake Light and Headlight tiles
The Brake Light and Headlight indicator settings lose their "Off" options — hide those tiles by leaving them out of your CarPlay layout instead; the pickers keep their appearance choices. 

### Diagnostics: two on-device recorders, now default-on
Settings → Diagnostics now hosts two flight recorders, both recording by default and each with its own Share button:
- App Activity Log (app-activity.log): app lifecycle, Bluetooth connection, adapter interference, and History storage events. It always records at full detail now, and self-trims to stay under ~5 MB (one file, no more rotation).   If you have an interference event that you believe is a false positive, please send me this file.
- Drive Diagnostics Recorder: a per-drive record of GPS fixes, vehicle-speed samples, and distance decisions, for troubleshooting distance and navigation accuracy. 

### The map-engine choice is gone
The rebuilt CarPlay map engine that shipped on by default in Build 131 is now the only engine — the Experimental "New map engine" toggle is retired.

### Fixes
- CarPlay crash at navigation start/resume: connecting a CarPlay session could ask a banner callback a question off the main thread, tripping a Swift 6 safety check.

---
## Build 131 — Measured drive distance, new CarPlay map engine, CarPlay Light Mode polish, fix for Japan DCFC detection, fix for another false positive interference detection

NOTE TO TESTERS: Trip distance and efficiency are now MEASURED (fusion of GPS and vehicle speed) eliminating the 1km/1mi resolution issue of the odometer signal.  After your next drive, look at the drive in History and you'll notice a smooth distance curve instead of stair-step shape.   There was a change to the charge detection logic to fix a problem in Japan -- please let me know if you encounter anything unusual like a false positive or missed charging session.  Please let me know if you encounter any false positive interference detection messages.

KNOWN ISSUES:

- The original climate chip information (Outdoor, Indoor, RH), tire temps, and odometer will be added to CarPlay shortly, along with a feature to customize the Driving page.
- Experimental parking feature is not implemented yet

### Drive distance is now measured, not read from the odometer
Driving-session distance — and the efficiency figure — is now measured by integrating GPS and wheel speed over the drive, so short trips no longer jump in whole 1 mi / 1 km steps.  The Distance chart plots the measured trip as a smooth curve, and there's a new Trip Distance signal under History → Signals. To keep measuring through app switches the app now requests background location during drives. 

### A second DC fast-charging detector
One tester's Japan-market IONIQ 5 ran a real ~45 kW DC session that went undetected because his car reports DC in a form the original detector didn't match. 

### Energy Added no longer collapses after a mid-charge relaunch
On a long AC charge interrupted by an app relaunch, the session's Energy Added no longer collapses to a fraction of the true value. 

### New Experimental toggle: New map engine
New map engine switches the CarPlay map to a rebuilt renderer. Turn-by-turn guidance gets an Apple-Maps-style camera: 3D perspective, course-up rotation, the road ahead framed in front of the vehicle, and speed-adaptive zoom. Zoom reframes the guidance view and Recenter restores it; the charger map and dashboard are identical on either engine. 

### CarPlay navigation
Trip time/distance and guidance now also keep updating while stopped — the ETA no longer freezes at red lights.

### CarPlay Light Mode and polish
- The top breadcrumb (Status · Driving · Charging · Help) paints the active page in dark ink over the light wallpaper, the others a legible grey; the Help ‹ › tip chevrons get the same day/night treatment (Dark Mode unchanged).
- The top ‹ › page arrows use a larger, bolder chevron that fills the button.
- Help hero visuals now use the same translucent slate as the Help panel, letting the CarPlay backdrop read through instead of black boxes.
- Status page: "Scan Status" and "Polling Headroom" are now title case, not ALL CAPS; with no headroom value yet the field reads Not Available in a neutral color, not a bare dash.
- The Nearest Charger Help tip now also covers the "Arrive" gauge the tile morphs into during navigation.

### Efficiency info sheet restructured
Rewritten for the measured-distance era: "How distance is measured" covers the GPS + wheel-speed measurement, and a new "How energy is measured" explains energy comes from the pack's own available-energy accounting (regen credited, climate and pack loads included).

### History: "Signal lost" session badge
The connection-drop badge now reads "Signal lost" instead of "BLE lost", ahead of classic-Bluetooth adapter support.

### Fixed: false "interference" disconnect on rebooting adapters
On adapters that announce themselves after powering on (field report on a Veepeak), a reboot-and-reconnect could be misread as foreign interference and disconnect the session. Reset banners now only count as interference once the app's own adapter setup has completed.

---
## Build 130 — Redesigned CarPlay DC charging page, true Requested Current reading, mid-trip rerouting, 12V/lights fix for Japan market IONIQ 5s

NOTE TO TESTERS:  This build fixes an issue with the interference detector.  Please be sure and let me know if you have any difficulty.  Also fixed in this build is somewhat misleading reporting at 400V DC Fast chargers, specifically the requested power curve.  There's a small adjustment to background BLE auto-connecting - the app will no longer attempt to auto-connect unless it is in the foreground (either the iPhone app or CarPlay need to be in the foreground) - please be sure and let me know if you observe any differences with the way your adapter connects.   

KNOWN ISSUES:
- The original climate chip information (Outdoor, Indoor, RH), tire temps, and odometer will be added to CarPlay shortly, along with a feature to customize the Driving page.
- Experimental parking feature is not implemented yet
- Range estimation and efficiency algorithms will continue to be improved during beta
- SoC at arrival is not populated initially

### Interference detection
Resolved an issue that was leading to false positive detection immediately after an adapter was connected.  Thanks Tom and Howard for your reports!

### Background automatic connection
The app will no longer re-establish a BLE connection unless it is in the foreground.   I made this change because I believe the app connecting in the background may have been leading to many of the background crash reports.

### "Requested Current" now shows your vehicle's real request
During DC fast charging the app now reads the current your vehicle commands the charger to deliver over the CCS link, not the battery's internal demand — the old figure could read misleadingly different on 400V chargers. It feeds the Dashboard's live "Requested" readout, the session history, and the CarPlay charts.  Thanks Sean for the 400V session logs!

### CarPlay: Updates to the DC fast-charging page
The DC charging page is updated with: Session Power (supplied vs. to-pack), Pack Voltage, Session Current (Requested / Supplied / Pack), and the charger's published voltage/current/power.  Cell delta, battery temps, SoC, and the session timer had small tweaks.

### History: Session Current chart gains a Pack line
In a session's detail, the former "EVSE Current" chart is now "Session Current," adding a Pack current series alongside Requested and Delivered, matching CarPlay.

### CarPlay: reroute mid-trip
Navigation now reroutes if you drift off course: more than 50 m off route for three consecutive good GPS fixes recomputes from your position and swaps the guidance in place.

### 12V and lights now read on some 2024 IONIQ 5s
Japan market 2024 IONIQ 5s appear to include 2025-generation electronics that don't match their model year, leaving the 12V Auxiliary readout blank and the headlight/brake indicators non-functioning. At connection the app now detects which ECU generation your ICCU and BCM actually speak and polls the matching signals.  Vehicles that already worked are unaffected.  Thanks Akio for your help!

### CarPlay Help: Cell Δ and 12V tips
Two more Help tips, each beside a live example: Cell Δ explains the cell-balance heatmap and delta, and 12V explains the auxiliary battery's voltage/charge/current readout, including its current color-coding (green = charging, amber = powering electronics, white = at rest). "Chip" is now "tile" throughout CarPlay Help.

### CarPlay dashboard: refined page buttons
The two top-corner page-switch buttons now use circled chevrons in place of plain arrows — a more tactile, pressable look. They still cycle Status / Driving / Charging / Help.

### Charger map: weekly re-scan
The charger map now re-scans already-covered areas weekly instead of daily, cutting background network and rendering churn. Chargers already found stay on the map regardless — only the refresh cadence changed.

---
## Build 129 — CarPlay Help readability tip, clearer page indicator, IONIQ 5 N odometer fix

NOTE TO TESTERS:  IONIQ 5 N testers -- the missing odometer signal issue should now be fixed -- please try out the build and let me know.  Special thanks to tester Dusko for mapping the entire instrument cluster and finding the missing odometer signal in a couple of new DIDs.

KNOWN ISSUES:
- The original climate chip information (Outdoor, Indoor, RH), tire temps, and odometer will be added to CarPlay shortly, along with a feature to customize the Driving page.
- Experimental parking feature is not implemented yet
- Rerouting during navigation is not implemented yet
- Range estimation and efficiency algorithms will continue to be improved during beta
- SoC at arrival is not populated initially

### CarPlay Help: new "Hard to Read?" tip
A new first tip on the CarPlay Help page addresses a common misconfiguration: with CarPlay's appearance set to Always Dark but "Always Show Dark Maps" turned off, some of this app's labels can render dark-on-dark and become hard to read. The tip shows a small illustration of the Appearance screen — Always Dark selected, the dark-maps toggle highlighted ON — and points to exactly where to fix it, using Apple's own setting names in each language. 

### CarPlay dashboard: clearer page indicator
The page-name strip (Status · Driving · Charging · Help) no longer looks like a tappable tab bar. Some drivers were trying to touch or swipe it, but the CarPlay window is touchless — pages switch with the arrow buttons in the top corners. The pill background and blue selection underline are gone, leaving a dot-separated wayfinding label; the current page is now brighter, heavier, and slightly enlarged so "you are here" stays obvious without looking interactive.

### IONIQ 5 N: odometer and trip distance now populate
On IONIQ 5 N vehicles whose instrument cluster reported a zeroed odometer on the usual reading, the odometer and per-drive distance now populate correctly — History no longer shows "Too short / Less than 1 mi tracked" after a real drive. 

### Diagnostic Trace Recorder: fully localized
The Diagnostic Trace Recorder controls in Experimental Features (the toggle, its "Verbose detail" sub-toggle, and the footer) had shipped English-only; they're now translated in all 8 languages.

---
## Build 128 — Fix to CarPlay RHD screen issue, Background crash fix, CarPlay Help page, Filter chargers by power capability

NOTE TO TESTERS: Thanks to everyone who reported a problem with the CarPlay layout in right hand drive vehicles, that's fixed in this build.  

KNOWN ISSUES:
- The original climate chip information (Outdoor, Indoor, RH), tire temps, and odometer will be added to CarPlay shortly, along with a feature to customize the Driving page.
- Experimental parking feature is not implemented yet
- Rerouting during navigation is not implemented yet
- Range estimation and efficiency algorithms will continue to be improved during beta
- SoC at arrival is not populated initially

### Background stability
Background data collection is now suspension-safe: History writes land in an append-only journal file first and drain into the database only while the app or CarPlay is open.  This avoids iOS terminating the app for holding a database lock when it is in the background.  Thanks to everyone who has been reporting this ongoing issue!

### CarPlay: new Help page
A Help page is pinned to the far right of the ring once your vehicle is connected, explaining a few dashboard chips one tip per screen — each with a live example — for the Compass (with the flat-phone orientation note), the Range chip, and the Nearest Charger chip. Page through with prev/next, or jump to the charger map from the same corner cluster.   More coming soon!

### CarPlay: charger map minimum-speed filter
The charger Filter screen gains a Minimum Speed section — Any / 50 kW+ / 150 kW+ / 250 kW+ (combines with the network filter). A station qualifies when any connector meets the chosen speed; stations with no speed data (including Apple-Maps-only results) are hidden while a speed filter is active.

### CarPlay: range chip now starts from your own driving
Each drive's efficiency estimate now starts where your last drive ended instead of a fixed value — the rolling average is saved while driving (per vehicle) and restored at the next drive's start, and the "~" approximate marker is gone. The first drive after updating still starts from the 3 mi/kWh baseline.

### CarPlay: day/night polish
The light "day" map now gets its own styling: the floating dashboard⇄map and Connect/Disconnect buttons, the navigation map's arrival-SoC capsule and hint label, the turn-by-turn maneuver card (now repainting the instant day/night flips), and the charger details panel and target pin all adapt to day tiles instead of staying dark and washed-out. Night is unchanged.

### CarPlay: right-hand-drive layout
CarPlay now lays out correctly on right-hand-drive vehicles, whose head units place the app dock on the right and had left dashboard widgets partly hidden (issue #87). The dashboard clears the dock on whichever side it appears, the charger map's Go button moves to the driver's side, and the Status page's Connect/Disconnect label sits beside its corner button in both layouts.

### CarPlay Status screen polish
The disconnected / Bluetooth-off hero now shows a slashed-antenna status icon (a tester had mistaken the old X-in-a-circle for a button); "Looking for adapter" shows an animated antenna instead of a static dotted circle; added a Connect / Disconnect hint to the corner button.

### Adapter interference: fewer false alarms
Removed the fast-reconnect timing heuristic from interference detection — its scenario (connecting while another app holds the adapter) is already caught by the held-link check, and the timing tell could misfire after a force-quit and quick relaunch. 

### New: Diagnostic Trace Recorder (Experimental Features)
A new Experimental Features toggle records a compact, tagged timeline of app-lifecycle, Bluetooth, background-task, and History-storage events to a shareable file, for troubleshooting hard-to-reproduce background issues (e.g. the app not auto-reconnecting after a long park). Off by default; a "Verbose detail" sub-toggle adds per-frame detail.

---
## Build 127 — Adapter interference detection fixes

NOTE TO TESTERS:  Sending out this quick fix for some false positive detections of adapter interference on 2025 and 2026 vehicles.  If you encounter an issue with adapter interference and you are 100% positive you have no other apps running -- this new feature can be disabled under Settings / Experimental Features.   If you do not have Experimental Features turned on, navigate to Settings / About and tap on the build number 127 five times -- that will unlock Experimental Features.   

### 2025 and 2026 vehicles: false interference disconnect
Some 2025- and 2026-model-year vehicles were force-disconnected on every connect with a false "adapter interference" warning. Their VCMS answers the identity probe with a combined identity listing that leads with a different record instead of echoing the exact request — which the new detector misread as another app's response. The app now accepts that reply as valid, so these vehicles connect normally and their VCMS details resolve correctly again.

### Fewer false alarms during ECU scans
Hardened the same check against the app's own delayed replies: if a response matches a request the app itself made in the last 30 seconds — most likely a late answer arriving during a fast ECU scan — it's set aside for data integrity but no longer treated as interference. Only responses for something nobody on the app's side asked for still trigger a disconnect.

---
## Build 126 — CarPlay rebuilt: EV charger maps, in-app navigation, live range, Kia EV9 AC charging voltage fix, automatic adapter interference detection

NOTE TO TESTERS: This is the first build of Version 3.0 -- and it's a big one!  CarPlay has been rewritten from the ground up, and I'm glad to report the music notes bug is fixed!  Most features are in, but a few are not yet.   If you use any other OBD-II apps such as ABRP or CarScanner, please run those intentionally at the same time as IONIQ 5 Companion to verify the new auto-interference detection works as designed.  Please play around with the EV charger locating map - I'm curious what people think about that -- try filtering, panning, zooming, etc... 
   
KNOWN ISSUES:
- The original climate chip information (Outdoor, Indoor, RH), tire temps, odometer, and instructions for the Compass will be added shortly along with a feature allowing you to customize the Driving page for the first time.
- Experimental parking feature is not implemented yet
- Rerouting during navigation is not implemented yet
- Range estimation and efficiency algorithms will be improved during beta
- SoC at arrival is not populated inititally
- App in the background crashes can still happen - REAL fix for that coming soon!

### CarPlay: expanded to 2x8 in full screen mode
Two new tiles bring the CarPlay grid from 2x7 to 2x8: Range (a live range estimate) and Nearest Charger (a live micro-map of the closest charger and its distance).

### CarPlay: visual aesthetic
The tiles are now slightly translucent, so the wider range of CarPlay wallpapers in iOS 27 shows through. There's an all-new Status page — cleaner and simplified — with the connect/disconnect button in the bottom-right corner.

### CarPlay: charging page
The charging tab is no longer always visible: a graphics-rich charging page now appears when a session begins.  

### CarPlay: EV charger map and navigation
A full-screen charger map with a center crosshair and a banner naming the closest charger that meets your filter criteria.  Chargers you pass accumulate into a local directory, so places you've been load instantly.  Move the map around to explore charger locations.

### CarPlay: in-app turn-by-turn navigation 
During guidance you can peek the driving dashboard while the trip keeps running, and an Apple-Maps-style turn popup slides in as each maneuver approaches. 

### CarPlay: live range and energy efficiency
The Driving page shows projected range at your actual pace, from real energy use.  

### Charging: no more phantom "DC Fast" sessions
Fixed a brief phantom DC charging session that could appear before the real one began. The car reports "DC charging" the instant the plug handshake starts — before any power flows — so a stalled handshake could flash the screen and open an empty 0 kWh session. The app now waits for real pack current before opening a DC session, as it already did for AC.

### New: Adapter Interference detection
The app now takes a zero-tolerance stance: the moment it sees traffic that isn't its own, it disconnects and tells you to close the other app and reconnect (which re-initializes the adapter and clears the warning). Disable it under Settings → Experimental Features; the Connection Report gains a matching section and CSV fields.

### CarPlay: snappier dashboard
State changes — brake lights, turn signals, gear — now appear on the CarPlay dashboard the instant their data arrives

### Kia EV9: AC charging voltage and frequency
While charging, AC voltage and frequency now read correctly on the Kia EV9.

---
## Build 123 — Version 2.2 rebuild for App Store submission

NOTE TO TESTERS: This build is functionally identical to Build 121 — no new features or fixes. 

### Why the build number jumped from 121 to 123
Version 2.2 had to be rebuilt to meet Apple's App Store build requirements — a toolchain and code-signing matter (Apple does not accept App Store releases built with beta versions of their own tools).  Builds 122 and 123 carry the same code as Build 121; 123 is the binary headed to the App Store for the 2.2 release.

---
## Build 121 — BLE adapter wording

NOTE TO TESTERS: I'm sending this build over to Apple today as version 2.2.  Thank you to everyone for the continued support - constructive feedback, issue reports, and diagnostic logs.  There will be a few days with no new builds due to the Apple approval cycle timing.  The next build will be the first one for Version 3.0.

### Curated DID List scan: updated failure message
When a curated scan (Create Curated DID List) fails right at the opening session request, it no longer always says "Paused — BLE disconnected." It now reports what actually happened:

- A module that never answers — like the GV60 instrument cluster — shows "Scan ended — no response from this module," with a note that it may not be reachable on your vehicle.
- If your vehicle is off, it says that instead.
- A module that refuses the Extended session shows that the module refused the session request, with a hint to retry using Default.

All new messages are translated into every supported language.

### Settings: "BLE ELM327-compatible adapter"
The adapter-scan explainer in Settings now specifies "A BLE ELM327-compatible adapter is required" (was "An ELM327-compatible adapter"), clarifying that a Bluetooth Low Energy adapter is needed. Updated in every supported language.

---
## Build 120 — Standard Range battery module fix, Mode 01 broadcast scanning, Overview polish

NOTE TO TESTERS: This is RC6 for Version 2.2 -- this may be the build I send over to Apple.  Standard Range vehicle testers — please check the battery module temperature grid on this build: the two permanent 0° modules should be gone, and the Min/Avg/Delta temperature stats should be correct.

### Standard Range packs: two phantom 0° modules removed
Standard Range vehicles no longer show two phantom 0° battery modules in slots 15 and 16

### Broadcast DID Scan: Mode 01 PID reads
The Broadcast DID Scan tool (Experimental Features) gains a Service selector: alongside UDS DID reads (service 22) it now speaks standard OBD Mode 01 PID reads (service 01) — one PID per request, single-frame responses. Verified on the IONIQ 5 with a full 00–FF PID sweep (31 responses): Mode 01 support turns out to be distributed across six drivetrain ECUs, the supported-PID chain ends at PID 9A, and the legislated odometer PID (A6) is unsupported — ruling out Mode 01 as a platform-independent odometer source.

### Dashboard Overview: one less sub-panel
The Overview section drops its inner frosted sub-panel: the state-of-charge gauge, chips, and Scan Status card now sit directly on the section's glass card, gaining a little width and a cleaner look

---
## Build 119 — Vehicle on/off detection reworked, new Broadcast DID Scan tool, background-crash hardening

NOTE TO TESTERS: This is RC5 for Version 2.2.  I think we're back on track -- this build ships with improved vehicle ON/OFF detection. EV9 testers especially: please report whether driving sessions now end promptly after shutoff.  Everyone else -- please report any abnormal new behaviors -- I think this change is low risk, but you never know! 

### Vehicle on/off detection reworked
The app now requires BOTH the climate ECU (HVAC) and the charge controller (ICCU) to be responding before declaring the vehicle awake, and either one going truly silent ends the awake state. This fixes the Kia EV9 "app stays on after shutoff" report.

### Adapter glitches can no longer flip the app to "vehicle off"
Only the adapter's literal NO DATA response now counts as an ECU non-response. Interpreter aborts, protocol failures, CAN-bus errors, torn multi-frame responses, and BLE drops are all state-neutral, and a negative diagnostic response counts as "ECU alive." Should decrease/eliminate the "app shut down while driving" class of tester reports.

### New: Broadcast DID Scan (Experimental Features)
Sends a single read to the CAN broadcast address so every ECU serving that DID answers in one request, grouped by ECU. Multi-frame responders — which by design only send their first frame over broadcast — are automatically re-read at their physical address, with a delayed retry for ECUs that stay quiet. Built to hunt an odometer mirror on the GV60; verified on the IONIQ 5 with zero unrecovered multi-frame reads. Settings → Experimental Features, behind the 5-tap unlock.

### "Vehicle Awake" / "Vehicle Asleep"
The green Dashboard banner now reads "Vehicle Awake" — it correctly shows while charging with the car off — and the off-state panel is now titled "Vehicle Asleep" (Dashboard and CarPlay). Its footer changed from the pulsing "Turn on your vehicle to view diagnostics." call-to-action to quiet status text: "Waiting for your vehicle to turn on or start charging." All languages updated.

### Background database-lock crash hardening
A full audit of every history-store writer closed the remaining paths that could crash the app when iOS suspends it mid-write (the dominant remaining crash cluster through Build 117). The signal-index rebuild now takes the background-task protection; the storage-cap evictor and launch-time snapshot scrubber hold it per-chunk instead of across a whole sweep (a long sweep could silently strip protection from every concurrent writer); and deleting a session or attaching/removing a session photo now saves immediately under the guard. 

### Tire Target Pressure: round values in bar and kPa
The picker now offers 0.05-bar steps in bar mode (exactly 2.60 bar is selectable) and 5-kPa steps in kPa mode instead of converted 0.5-psi steps that skipped them; psi mode is unchanged. Reported by a tester who couldn't select their door-placard 2.6 bar.  Thanks Roland!

### DID Range Scan: multi-frame responses fixed on clone adapters
Multi-frame DIDs no longer silently return nothing on clone adapters: the scanner left the flow-control header pointed at whichever ECU normal polling touched last, so multi-frame responses died after their first frame. OBDLink adapters were never affected.

### Parking sensors toggle now gates polling
With Parking sensors (Experimental) off — the default — the parking-sensor ECU is skipped entirely by the polling loop and no longer appears in Scan Status, the Connection Report and its CSV, or CarPlay's Scan Status, so 2022-2024 IONIQ 5 trims without the hardware stop showing a permanently failing entry. Turning it on starts polling on the next poll cycle — no reconnect needed.

### Charging chart shading fix
Pack Voltage and AC Input Voltage session charts no longer shade a full-width wedge whose top edge matches no plotted line. Shading now always hugs the visible line, in the app and on share cards.

---
## Build 118 — New: Adjustable SoC gauge colors, Dashboard and CarPlay values appear sooner, "Battery Warmer" rename completed

NOTE TO TESTERS:   Thanks to everyone who helped with the BCM and VCU scans.   If you have not already done a scan -- please hold for now.  I have not found a winning solution yet and I am contemplating next steps.  The VCU signal I was chasing turned out to be another location where the 12V/AUX voltage is reported (from the VCU in addition to the ICCU - an inadvertent discovery).  I'm on this search to solve a couple of experiential bugs that have emerged (unplug reminder not firing and driving sessions ending with BLE Lost), both traced to the same root cause.  The app currently uses the HVAC ECU to determine if the vehicle is ON or OFF -- this had worked well, but in the Kia EV9 (and perhaps other vehicles) the HVAC ECU can remain ON when the vehicle is turned OFF.

### New: SoC Range Colors
Settings → CarPlay has a new "SoC Range Colors" section: the state-of-charge gauge's color thresholds are now adjustable. Pick the percentage below which the gauge turns red (alert) and orange (warning) in 1% steps, optionally add a green "well charged" color at its own threshold, or turn the coloring off entirely. Applies to the CarPlay SoC gauge and — via an "Apply to Dashboard" toggle — the Dashboard gauge too. Defaults match the previous behavior (red below 20%, orange below 40%, no green), and CarPlay repaints the gauge immediately as you adjust. 

### Dashboard and CarPlay begin appearing slightly faster
Values now show up faster after starting the vehicle, especially with CarPlay connected. Three compounding fixes landed together: adapter communication moved off the UI thread, so screen drawing can never delay it; CarPlay chip images now draw a few per screen refresh instead of all at once; and a silent ~1.4-second stall before the first data request — traced to oversized placeholder images built while constructing the CarPlay tabs — was eliminated. Measured on-vehicle: the odometer now appears about half a second after the polling loop starts (previously ~2 seconds with CarPlay connected, and 4–8 seconds before Build 117's ordering fix), with state of charge arriving in under a second.

### "Battery Warmer" everywhere
Build 117 renamed the CarPlay chip; this build completes the transition everywhere "Preconditioning" appeared in the app: the Dashboard Battery · Temperatures section header, status chip, and time-series graph; the History → Signals list and its signal chart; the History → Sessions detail graph band; the in-progress charging-session status line ("Battery Warmer…"); and the charging-session share card. All languages updated; stored history data and export formats are unchanged.

---
## Build 117 — Improved vehicle speed signal, 4x more frequent tire pressure updates, two CarPlay fan favorites brought back

NOTE TO TESTERS:   This is RC4 for Version 2.2.  Thanks for everyone who helped with yesterday's BCM testing - including those of us sweltering in our cars due to the high temps!   The results were consistent across the fleet.  I want to explore one other possible signal source (the VCU) which I believe would be ideal for a number of reasons.  A new test protocol has been posted here -- please don't feel like you need to do everything on the list - even a simple OFF-ON-OFF test will be very helpful:   https://www.theburl.com/ioniq-app/charging-state-test/

### Vehicle speed now comes from the VCU
Speed previously came from the climate-control module's coarse 1 km/h rebroadcast, polled every 5 seconds. It now comes from the VCU's own high-resolution speed signal, carried in a response the app already polls every 2.5 seconds for the gear indicator — so speed is finer-grained and twice as fresh at zero added polling cost. One quirk worth knowing: the raw signal goes negative in reverse, which shows as a small below-zero dip in History speed charts; max-speed tracking ignores it.   Please let me know if you see any issue with the speed signal in your Driving Session histories.

### CarPlay Tires chip: the combined view is back
The Tires chip has a third page: the composite pressure + temperature layout (pressure large, temperature smaller beneath), rescaled for the current larger quadrants.  Tapping the chip now cycles pressure → temperature → both, shown by three page dots, and your selected page still persists across launches.

### Brake Light Indicator: solid red is back
A fourth option restores the original solid bright-red chip background from build 53 (requested by a tester). The picker now reads Off / Red Text / Red Glow / Red Background — the glow rendering formerly labeled "Red Background" is now "Red Glow". Existing saved selections are unaffected.

### CarPlay "Precondition" chip renamed "Battery Warmer"
This chip has been renamed to avoid confusion with the more general precondition feature which on 2025+ model year vehicles can mean either warming or cooling -- currently only warming preconditioning is supported

### Polling headroom panel rebuilt
The Polling headroom info panel refreshed with three defined tiers — High (above 50%), Normal (10–50%), and Low (under 10%) — plus notes that the number settles toward a session average and can vary with the wireless environment. The dashboard chip's gauge icon is now tinted by the same tiers.

### Advanced Tools scanners reskinned
Every screen under Settings → Diagnostics → Advanced Tools — the DID Range Scan, ECU Finder, Create Curated DID List, and the full Curated Scan flow — now uses the shared aurora backdrop with Liquid Glass cards and buttons. These were the last utilitarian-looking pages in the app. Visual only; scanner behavior is unchanged.

### Polling and housekeeping
Three background poll intervals were retuned: tire pressures/temps refresh every 30 seconds (was 120), while two charge-controller reads that return nothing when the car isn't charging slow from every 5 seconds to every 15 — freeing polling time for fresher data elsewhere. The Experimental "CarPlay updates per second" control now caps at 4 (the 6 and 8 presets are removed; prior selections clamp to 4). And diagnostic logs no longer include the CarPlay load-estimate lines left over from earlier tuning work.

---
## Build 116 — Predictable startup values, IONIQ 6 tire fix, Turkish fixes

NOTE TO TESTERS:  This is RC3 for Version 2.2.  I have a test protocol ready that I need your help with (https://www.theburl.com/ioniq-app/car-on-off-test/).  I believe I have figured out a more reliable method of detecting ignition state, but I need your help running an ~5 minute protocol using Advanced Tools before I feel comfortable deploying it to the fleet.  I need testers from all E-GMP vehicle types.  If you have 5 minutes to spare -- please run the protocol and send me the results via email.    Link here:  https://www.theburl.com/ioniq-app/car-on-off-test/    THANK YOU!

### Dashboard values now appear in a consistent order at startup
The polling loop previously fetched some ECUs — notably the instrument cluster that supplies the odometer — in an order that varied run-to-run and adapter-to-adapter, so the odometer could take anywhere from ~4 to ~8 seconds to first appear. The startup poll order is now pinned, with the odometer fetched first, so it and the other Overview values populate quickly and predictably every time.

### IONIQ 6 tire-pressure targets corrected
Build 115 shipped the IONIQ 6 placard targets as a symmetric 36/36 psi; the correct values are 36 psi front / 37 psi rear. IONIQ 6 now shows distinct front vs. rear warning bands, like the other asymmetric variants. Thanks David!

### Dashboard Climate honors Driver Position
The Dashboard Climate section now respects the Driver Position setting (Settings → International), matching CarPlay's Climate chip. When set to Right, the driver's Vent/Floor temperatures move to the right column and the passenger's to the left, mirroring the seating position; Left (the default) is unchanged. Both surfaces now share one rule, so they can't drift apart.

### Advanced Tools page redesign
The Advanced Tools page (Settings → Diagnostics → Advanced Tools) now uses the same polished Liquid Glass card design as the Inspect chooser. Each tool is a full-width glass card with a glowing tinted icon medallion, an "Advanced" badge, a bold title, and a one-line summary, replacing the plain grouped-list rows.

### Turkish translation fixes
More Turkish wording fixes from the translator, on the Dashboard charging section. The "Charging" section header now reads "Şarj" (the plain noun) instead of "Şarj ediliyor" ("charging in progress"), which was misleading on a static header — the same shared label also corrects the History charging category. And the charging-type value "Not Charging" now reads "Şarj edilmiyor" instead of "Şarj olmuyor" (the latter reads like a failed attempt to charge). Turkish only; no other language changed. Thanks Burak!

---
## Build 115 — Driver Position (LHD/RHD), tire-pressure warning rework, translation fixes

NOTE TO TESTERS: This is RC2 for Version 2.2   There's a new Driver Position setting under Settings → International. Set it to Right and the CarPlay Climate vent page swaps its columns so your own vent and floor temperatures sit on the right, where you sit. Right-hand-drive testers: please let me know if this matches your car. Two more things to watch: some of the tire-pressure warning colors were reworked from each vehicle's door-placard pressures, so your green/orange/red thresholds may have shifted slightly — flag anything that looks off.  And international testers, please confirm your language's high-voltage battery labels make sense.

### New: Driver Position (left / right-hand drive)
A new Settings → International section holds the app Language selector (moved out of Display) plus a new Driver Position setting (Left / Right, default Left). Set to Right, for right-hand-drive vehicles, the CarPlay Climate chip's vent page swaps its columns so the driver's vent and floor temperatures appear on the right, where the driver sits. Left-hand drive is unchanged, and the iPhone Dashboard — which already labels each vent — is unaffected.   Thanks to Dave, Brian, Chris, and  John for checking this!

### Tire-pressure warnings reworked
Tire-pressure warning colors now derive from each vehicle's door-placard target pressures, with one rule everywhere: red below −20% of target, green from −10% to +10%. Per-axle targets were set from verified placards — e.g. 2024 IONIQ 5 = 34 psi, 2025+ IONIQ 5 = 38, IONIQ 9 = 38 front / 39 rear, GV60 = 36 / 39, Kia EV9 = 38, IONIQ 6 and Kia EV3 = 36.  All of these values can be customized under Settings / Tires

Also fixed a tire-pressure chip that could briefly flash "0" before the real value reappeared. When a TPMS sensor momentarily drops out, the chip now holds the last known pressure (greyed) instead of recording the zero — so the fallback no longer shows 0, and tire-pressure history charts no longer dip to zero.   Thanks John for flagging this!

### CarPlay Driving layout
On the CarPlay Driving dashboard, the Compass/Odometer chip now sits between the Tires and Climate chips instead of beside them. Both Tires and Climate are 2×2 grids of tiles, and side by side they read as one cluttered block; separating them with the simpler Compass/Odometer chip makes each easier to scan at a glance.  Thanks Burak!

### Translation fixes
Fixed mistranslated high-voltage battery labels in seven languages. The traction-battery terms ("Pack", "Pack SoC", and the Power / Current / Voltage / Peak readings) had been machine-translated as the word for a shipping parcel (German *Paket*, Dutch *Pakket*, Italian *Pacco*). They now use each language's proper battery word — de *Batterie*, fr *Batterie*, it *Batteria*, es *Batería*, nl *Accu*, sv *Batteri*, ko *배터리*. Affects the CarPlay chips and the Dashboard/History labels.   Thanks Manfred!

Turkish also got a wording polish: the CarPlay "Colorize Climate Chip" setting and its description, and the "Start Recording Diagnostics" button, now use more natural and consistent Turkish terms.  Thanks Burak!

---
## Build 114 — Tappable CarPlay Climate & Tires chips, Dashboard AC charging panel, clearer Climate labels

NOTE TO TESTERS:  This is RC1 for Version 2.2.  More CarPlay polish in this one — both the Climate and Tires chips are now tappable, so you can flip between vent temperatures, cabin readings, tire pressures, and tire temperatures right from the car screen.  The vent and floor outlet temperaturs default to being colorized, you can turn this off in Settings / CarPlay if that's what you prefer. Testers where the driver is on the right side of the vehicle (opposite USA) -- I'm wondering if I should add an option to reverse the driver/passenger vents -- I'm not sure if the vehicle does this already.   Please let me know.

### Tappable CarPlay Climate & Tires chips
The Climate and Tires chips in CarPlay are now tappable, each with two pages and a two-dot indicator showing which page you're on. Both chips toggle on the Driving and Charging tabs, and the page you pick is remembered across app launches.

- Climate — tap to switch between the four vent/floor air temperatures (driver/passenger × vent/floor) and the Cabin / Exterior / Humidity readings. The vent page draws the four temperatures as a 2×2 of color-coded tiles on a cold→hot scale (blue → green → red), so you can see at a glance which vents are blowing cold or warm.
- Tires — tap to switch between tire pressures and tire temperatures, each shown as a 2×2 of larger tiles with bigger numbers than before. The tile color still reflects tire-pressure status (the existing green / orange / red evaluation) on both pages — only the displayed value changes.

A new Settings → CarPlay "Colorize Climate Chip" toggle (default on) turns the vent-page color coding on or off.

### Clearer Climate labels
Climate readings are renamed across the iPhone Dashboard and CarPlay for clarity: "IAT Sensor" → "Cabin Temp", "AAT Sensor" → "Exterior Temp", and "Relative Humidity" → "Cabin Humidity". The Dashboard's Climate info bubble was rewritten in plain language and now also explains the per-zone vent temperatures.

### AC charging on the Dashboard
The Dashboard Charging view now reflects AC charging the way CarPlay already does. While AC charging, the Session panel becomes an "AC Draw" panel with three chips — Voltage, Current, and Power — sourced from the ICCU's measured AC input (input voltage × AC current). A new "AC Draw" chart plots wall-side AC input power over the session, above the power chart (renamed "Charging Power" → "Pack Power", which has always plotted pack-side power). The gap between the two lines is the onboard-charger conversion loss. DC charging is unchanged.

The elapsed-session timer moved up to the Status panel as a full-width chip below the Charging/Type chips, for both AC and DC. The Requested Current chart is now shown for DC only — it carries a BMS-requested DC charge current that is unrelated to AC input.

### Odometer hidden until a real reading arrives
The odometer now shows no value until a valid reading arrives instead of defaulting to 0. On the Dashboard the Odometer chip is hidden until the car reports a real odometer, and stays hidden on vehicles that never report one (for example the international IONIQ 5 N). This mirrors how State of Charge shows "--" until it has a real value.

---
## Build 113 — Fixed App Crash in Background, Climate vent temps in History, ICCU Information polish, OBDLink CX odometer fix

NOTE TO TESTERS:  I believe I have figured out why many of you were sometimes experiencing an app crash notification when it was in the background.   Please let me know if you continue to experience that issue -- but hopefully it is now squashed!   We're getting close to RC1 for Version 2.2.   Just a few more things to get done.  As always -- thank you for your support, testing, logs, and constructive feedback -- thank you!

### Climate vent & floor temperatures in History
History → Signals now records the four cabin climate temperatures — driver and passenger vent, driver and passenger floor — under a new Climate section. Each has a tap-through detail chart, and every value (row, hero number, stats, and chart axis) respects your selected temperature unit (°C/°F).

### OBDLink CX odometer fix
Fixed the odometer (and other signals) occasionally reading as a phantom error on OBDLink CX adapters. When an ECU replied with a "response pending" frame before its real answer, the app mistook that frame for the response. The pending frame is now correctly skipped so the real value comes through.  Thanks Tom!

### ICCU Information polish
- The ICCU's software version (0xF1B1) now appears as a named "Software Version" field in the results, CSV export, and share card, instead of being buried in the raw "Additional data discovered" section.  Thanks Brian!
- The share card no longer lists named fields that didn't respond during the scan. Empty placeholder rows (e.g. MODULE, DATASET, BOOT SW, CALIBRATED) are now omitted, matching the in-app results view, which only shows fields that actually answered.

### Driving Session chart wording
On the Driving Session detail screen, the State-of-Charge chart's pending message now reads "Buffering chart data" / "The first readings will appear shortly." The old "No charted signals" / "Waiting for the first SoC sample to land." wording wrongly implied nothing was charting even when some signals (such as brake light) had already begun appearing. Fully localized.

### Stability
Fixed the background-task guard that protects History database saves (and the CloudKit mirror's export window) when iOS suspends the app. The guard had been silently inert since it was introduced, so it now reliably acquires its background grace period before the app is suspended. This is aimed at reducing a class of background termination; real-world impact will be confirmed over the next build cycles -- please send in crash reports if you experience one!

---
## Build 112 — New ICCU Information tool, 50% faster time to dashboard, OBDLink CX improvement, Connection Report polish

NOTE TO TESTERS:  In today's build, the time to dashboard has improved by almost 50% .  I measured <4 seconds with the Gate iCar Pro 2S.   The ICCU feature has been moved out of the Dashboard and into the Inspect panel.   Your ICCU information is available after a manual Inspect run -- but in exchange for that shift, you will have much more complete and in depth information -- along with a much faster time to dashboard.   

### New ICCU Information tool in the Inspect tab
ICCU details have moved off the Dashboard into a dedicated "ICCU Information" tool in the Inspect tab.  This shortens the time to the Dashboard — the app no longer reads the charging control unit's identification at startup. The new tool sweeps the ICCU's full identification range slowly and thoroughly, then shows everything that responds: part numbers, software, build date, serial, and any additional identification data the module reports. Only fields that actually answer are shown — there's no longer a "fields not reported" warning. The old ICCU panel on the Dashboard and the ICCU row in the CarPlay status tab have been removed.  Results can be exported as CSV.

### Faster connection when the vehicle is off
Removed a startup "prime" step that broadcast a generic OBD-II query and then waited up to 3 seconds for a reply.  That dead time is gone — after adapter setup the app proceeds straight to polling. 

### OBDLink CX error message fix
Automatic connection attempts that involve an iOS/adapter negotiaon failure no longer flash a red "Connection failed" error.  The app now treats those background failures quietly — the Adapter row simply stays at "Disconnected" and keeps retrying on its own with a short, growing backoff until the link comes up. A real error is still shown when you tap Connect or pick an adapter and that attempt fails, so a genuine problem you started is never hidden.

### Scan Status polish
- Fixed a rare blank screen (a lone yellow warning triangle on black) that could appear after opening Scan Status → Connection Report when the vehicle was then turned off or the adapter disconnected. The report now stays readable across that transition instead of collapsing to the empty placeholder.
- The Connection Report now uses the app's Liquid Glass appearance — its sections render as frosted glass panels over the themed aurora backdrop

---
## Build 111 — Updated Scan Status with export to CSV for troubleshooting, tweaks to multi-frame handling, front-motor RPM for Kia EV3, IONIQ 9 VIN fix

NOTE TO TESTERS: There have been a few instances of vehicles with very fast ECUs, which outpace the ability of some adapters to respond in time.   In this build, I have made a pretty big change that *SHOULD* fix that problem, without breaking anyone else -- but please pay close attention to what you see in the next few days.   Please also keep an eye on the iPhone Scan Status (in Dashboard/ Overview) which does a much better job tracking and surfacing any communication issues.  Please let me know if you see anything that looks strange/not right (colored RED).

KNOWN ISSUE:  Many of you have written in about a background crash -- this is a benign issue caused by iOS shutting down the app in the background which it does with apps from time to time.   I'm looking into any ways to suppress this particular report.

### Connection Report: a clearer view of the app-to-vehicle link
The Dashboard's "Scan Status" panel has been redesigned into a compact summary card that opens a full Connection Report. The report describes the live link between the app and your vehicle: an at-a-glance Summary of how many modules are reporting, the Bluetooth Link (connection state and how long it's been connected), the Adapter (name, firmware, protocol, and capabilities), Polling stats (polling headroom and transaction totals), and a per-module Coverage list showing which data IDs each module is answering, with success rates and sample counts. A collapsible Events timeline records connects, disconnects, and any module that drops out or recovers mid-session — flagging drop-outs in red and auto-expanding any module with a problem. The whole report exports as a CSV to attach to a support request, making it far easier to see why a reading is missing on a particular car or adapter.

### Improved multi-frame handling
Some adapters on some vehicles/ECUs have been getting outpaced by the car -- that's because some ECUs respond faster than the adapters can handle.  In this build I have added a coountermeasure - the app will now ask ECUs to slow down so they don't outpace the adapter's capabilities -- the adapter sends a flow-control frame that paces the incoming frames.  This change does take a way from polling headroom, so plesae keep an eye on your headroom.     

### Dashboard & CarPlay: motor RPM now works on front-wheel-drive vehicles
Front-wheel-drive vehicles (Kia EV3, and any future FWD model) now show live motor RPM on the Dashboard and in CarPlay. The single-motor gauge was reading the rear-motor signal — always 0 on a front-motor car — so it showed no reading. It now reads the front-motor signal for FWD drivetrains.

### IONIQ 9 now correctly identified from the VIN
Korea-built IONIQ 9 vehicles (sold in Europe) share a VIN prefix with the IONIQ 6, so the app was loading the IONIQ 6 profile — which polls the wrong module and left the 12 V / Auxiliary Battery readings blank. The decoder now tells the two apart using a later VIN position, so an IONIQ 9 loads the correct profile and the 12 V / Auxiliary Battery panel populates. US IONIQ 9s were unaffected, and IONIQ 6 identification is unchanged.  Thanks new tester Rene!

---
## Build 110 — Tire-pressure overhaul, HVAC vent temperatures, Kia EV3 support, DTC scan CSV export

NOTE TO TESTERS:  I added a new DID to everyone's polling loops today for expanded climate signals.  Please check the climate section of the app and let me know if you see driver/passenger vent and floor temp readouts.  It's important that I hear from owners across the fleet to make sure this these signals are available on all vehicles.   (before I extend CarPlay and add them into Signal History).   Also, please check-out the newly expanded Tire Pressure feature.  

### Tires: redesigned pressure card and a new Tires settings section

- NEW: Temperature compensation (on by default): warning colors now account for tire temperature, so hot tires after a drive — or very cold tires on a winter morning — no longer trip a false low/high warning. The pressure shown is always the real measured value; only the warning color is normalized to a cold reference temperature. 
- Separate front/rear pressures: the front and rear axles can now carry different targets and warning ranges, with correct built-in defaults for vehicles that ship asymmetric specs (Kia EV6 GT, Hyundai IONIQ 5 N).
- Custom pressures (Settings → Tires): a new Tires settings section lets you set each axle's target pressure and warning thresholds per vehicle, with reset-to-defaults. 
- Last-known reading: when a wheel's TPMS sensor isn't reporting, the tire chip now shows the last-known pressure greyed out instead of a blank dash. (Temperature is not shown stale.)
- Info panel: the (ⓘ) button on the Dashboard's Tires card explains temperature compensation, what a gray tile means (the wheel sensors sleep when parked and wake once you're rolling), and how the car automatically matches each sensor to its wheel using wheel-speed data. 

### Dashboard Climate: HVAC vent and floor discharge temperatures
The Climate section now shows the four HVAC vent discharge temperatures — driver and passenger, for the face and floor outlets — in a dual-zone grid below the existing inside / ambient / humidity sensors. Available across the supported E-GMP vehicles (IONIQ 5/6/9, EV6/EV9, GV60).

### Kia EV3 support
The app now recognizes the Kia EV3 (E-GMP 400 V), beginning the process of onboarding the Kia EV3 into the app - the first 400V vehicle.  Welcome aboard Brian!

### Battery cell-voltage grid: no more dropped cells
The per-cell voltage grid (Dashboard, and the CarPlay "Cell Δ" chip) now shows every cell on packs whose cell count isn't a multiple of 12. The grid previously dropped trailing cells silently — the Kia EV9 was missing 6–8 cells and the Kia EV3 two. Evenly-divisible packs (IONIQ 5/6/9, EV6) are unchanged.

### DTC scans: export results to CSV
The J1979 and Enhanced DTC Scan result screens now offer "Export Data (CSV)" alongside "Share as Image" in a share menu. The CSV carries a metadata header (VIN, scan times, outcome, coverage counts) and one row per trouble code, plus a roster row for every clean module/ECU so the table doubles as a coverage list. J1979 additionally includes per-ECU identity (self-reported VIN, calibration IDs, CVNs).

### Enhanced DTC Scan: two more modules identified by name
Two modules that previously showed as "Unidentified module" are now named: ECU 0x733 as Charging Management System (VCMS ASSY) — a second VCMS node that appears alongside the main VCMS at 0x744 on some E-GMP cars — and ECU 0x7C3 as Passenger Occupant Detection (PODS), the passenger-seat occupant sensor. Surfaced from a Kia EV6 tester scan.  Thanks David!

---
## Build 109 — Export session data to CSV, 12V current direction by color, charging-history & DTC report fixes

NOTE TO TESTERS:  Build 108 was skipped.  If you already ran an enhanced DTC scan report and found trouble codes, please re-run it with Build 109.  I improved the the identification of "unknown" ECUs based on information they report back.  Please share the results with me -- thank you!

### Export a session's data to CSV
You can now export a charging or driving session's full data to a CSV file. Open a session in History and tap the share button — now a menu — then choose "Export Data (CSV)". The file contains all of the session's stored details plus the complete time-series of every signal recorded during the session, ready to open in a spreadsheet or send along for support.

### 12V battery: current direction now shown by color
The 12V (auxiliary battery) current now uses color to show which way power is flowing — green when the battery is charging, amber when it's discharging — on both the Dashboard and CarPlay. The value no longer carries a +/− sign; the Charging/Discharging label and the color tell you the direction. The Dashboard and CarPlay previously disagreed on the sign of this reading, and now match.  Thanks David for pointing this out! 

### Kia EV9 - Charging history: no more phantom "DC Fast" session at AC plug-in
Fixed a spurious "DC Fast" charging session that appeared in History — and immediately showed as finished — every time you started an AC charge. AC charges now log a single, correct session.  Thanks Stephen!  https://github.com/gburlingame/ioniq-app/issues/73

### History → Signals: values in your units
The History → Signals list now shows each signal's unit in the units you've selected (e.g. °F, psi, mph, mi) instead of the raw stored metric unit. This matches what the detail and chart views already showed.   Thanks Tom and Mike!   https://github.com/gburlingame/ioniq-app/issues/74

### Enhanced DTC Report: best-guess identity for unnamed modules
When the Enhanced DTC scan finds a module the app can't name, the report now shows a best-guess identity in its title (e.g. "Front Camera (MFC) · best guess") along with the identity details captured during the scan — system name, spare-part number, and supplier ID — instead of a bare placeholder. The two different placeholders that both meant "unknown" are now a single "Unidentified module" label, and the shared report never prints a module's VIN or serial number.

---
## Build 107 — New Themes picker, increased OBDLink polling headroom (+15-20%), Dashboard & onboarding polish

CARPLAY MUSIC NOTES ISSUE:  Unfortuantely, the attempted mitigation for the CarPlay music notes bug has not helped - in fact, paradoxically it appears it may have actually increased the frquency of this happening with some testers.  If you run into this problem one of two things may happen:  1) After 10 seconds a watchdog timer will fire, which will restore normal operation or 2) the watchdog will not fire and you will need to power cycle your phone to restore normal operation.  I continue to investigate what I can do to mitigate this on my side.  Today I created a synthetic stress test that blasts CarPlay and I was glad to see it actually recreated the problem so many of you have experienced.  

### New Themes setting
As promised in Build 106 — if the Liquid Glass aurora colors weren't to your taste, you can now pick your own. Settings → Themes lets you choose a palette, or turn the aurora off entirely. Please try them in both Light and Dark mode and tell me which you like.  Because the Liquid Glass surfaces refract whatever's behind them, your choice recolors the whole app — and the picker previews each theme live as you tap it. Every theme has its own Light- and Dark-mode palette and still follows your system appearance.  You can also turn this background off if you prefer.

### Dashboard: more room for the dials
The Regeneration and Power dials no longer sit flush against the top of their panels — there's now breathing room above each one. Each panel's info (ⓘ) button moved from the bottom-right to the top-right corner to fill that space.

### Dashboard → Scan Status: see each ECU's address
Every ECU row now shows the module's CAN address next to its name (e.g. "BMS (0x7E4)", "VCMS (0x744)"), so you can tell at a glance which address each module is being polled at. The address shown is the one actually in use for your vehicle, so VCMS correctly reads 0x744 or 0x7E1 depending on the fitted unit. The DID line beneath it is unchanged.

### Faster OBD polling on OBDLink / STN adapters
OBDLink polling is noticeably quicker on OBDLink and other STN-based adapters. These adapters now assemble multi-frame responses themselves, so the app no longer needs the cautious timing mode that had been protecting those reads and instead lets the adapter return each reading as soon as it's ready — about a third less time per reading on a test OBDLink CX.  Please let me know if you experience any new issues.

### Onboarding polish
The "Already Connected Adapter Found" panel — shown during setup when an OBD-II adapter is already paired to your phone — now uses the same Liquid Glass treatment over the aurora as the rest of the Welcome flow, instead of rendering as a plain grey card. The "Set up a different adapter" button, previously hard to read over the aurora in both Light and Dark mode, is now legible in both while still reading as a secondary action.

---
## Build 106 — Liquid Glass on Dashboard, History & Inspect; CarPlay tab fix

NOTE TO TESTERS: This build continues the Liquid Glass design exploration from Build 105, now extending the frosted "aurora" look to the Dashboard, History, and Inspect screens. I'd love your read on it — especially how legible everything stays in Light/Dark mode.  I'm planning on adding a theme selector if this color pallette is not to your liking - so please don't panic!

### Liquid Glass comes to the Dashboard, History, and Inspect
The Dashboard, History (both Sessions and Signals), and Inspect screens now render as translucent "glass" cards and rows floating over a soft, slowly-shifting aurora backdrop. The Dashboard has a consistent card → panel → chip depth so related readings group visually, and Dark mode was tuned so metric chips (VIN, State of Charge, etc.) stay legible instead of reading as flat dark blocks.

### Dashboard Climate: a grouped Sensors panel
The ambient air, intake air, and humidity readings are now grouped in a labelled "Sensors" panel, with the info button tucked into its top-right corner. "Sensors" is translated in all eight supported languages.

### CarPlay: Driving and Charging tabs missing
Fixed a bug that could lead to the Driving and Charging tabs vanishing in CarPlay — leaving only Status and EVSE — this could happen after the OBD adapter dropped and reconnected while CarPlay stayed connected (for example, stepping away to plug in at a charger, then getting back in and reconnecting). The CarPlay tab bar is now rebuilt from a single source of truth, so it can no longer get stuck showing an incomplete set of tabs.

### CarPlay: translated cell-voltage delta chip
The cell-voltage delta chip ("Cell Δ") on the Driving and Charging tabs now appears translated. It previously bypassed the translation path and showed in English in every language; it now shows in all eight supported languages.

### Inspect tab: new icon
The Inspect tab icon is now a diagnostic waveform instead of a magnifying glass, so the tab reads as "check your vehicle's health" rather than "search."

---
## Build 105 — Redesigned Inspect tab, whole-bus Enhanced DTC Scan, richer ECU Finder, broader adapter support

NOTE TO TESTERS: This build overhauls the Inspect tab and the diagnostic scans behind it. Please try out the all Enhanced DTC Scan and let me know what you think - I'm very curious to hear what codes it finds across the fleet, and what people think about this new design aesthetic I am exploring, leveraging Liquid Glass. 

### Redesigned Inspect tab
The Inspect tab is rebuilt around two diagnostic scans, each a tappable card: the legacy quick J1979 crawl and a thorough Enhanced DTC Scan. Each card now explains what it does and how deep it reaches. The whole flow — the chooser, each scan's detail page, the live scan, and the results — shares a new frosted-glass "aurora" look for Light and Dark.

### Enhanced DTC Scan now finds every module on the bus
The Enhanced DTC Scan sweeps the entire diagnostic bus, identifies every control module that responds, and reads each one's stored fault codes — reaching body, chassis, airbag, and comfort modules a standard OBD-II scan never sees. 

### J1979 crawl reskinned, with a clear verdict
The J1979 Diagnostic Crawl's live-scan and results screens now share the same aurora-glass look. 

### Richer ECU Finder
ECU Finder (Advanced Tools) now identifies each module far more completely. It reads the full standardized identification block — part number, hardware/software numbers, serial, manufacturing date, system name — adds the OBD-II Mode 09 ECU name, and labels common modules (front camera, radar, brake, airbag, steering, head unit) from their part numbers, all in a readable per-ECU report. A new optional "Extended-session retry" toggle (off by default) re-reads values that don't answer normally by briefly switching each ECU into its extended diagnostic session — the screen warns this can trigger temporary dashboard lights or messages.

### Corrected, friendlier ECU names
Diagnostic tools now show corrected names with their codes (e.g. "Front Camera (MFC)", "Integrated Body Unit (IBU)"). Several long-standing mislabels are fixed across the ECU Finder, DID Scanner, and Complete ECU Scan — e.g. 0x7A0 is now the IBU (was "TPMS"), 0x7C6 the Instrument Cluster (was "AUX"), and 0x730 the ADAS Drive ECU (was "Wheel Speed"). In History, the source chip on tire-pressure and odometer signals now follows the corrected modules.

### Lifetime Efficiency chart: no more spurious low readings
Fixed a possiblethat issue that would have resulted in spurious low readings (e.g. mid-80%) after the adapter reconnects or switches vehicles. Round-trip efficiency is now derived atomically from a single battery poll, so a fresh "charged" value can no longer pair with a stale "discharged" one.

---
## Build 104 — Consistent battery gauge colors, more reliable charging info, more screens localized

NOTE TO TESTERS: Version 2.1 is now live in the App Store!  This is the first build of Version 2.2 — thank you all! The big visible change here is the battery gauge colors (see below).   I implemented a possible fix (more like a band-aid) for the CarPlay music icons issue.  If you encounter that issue (you see musical notes) from this build forward - PLEASE, PLEASE, PLEASE let me know, there is a hidden tuning adjustment under Experimental Features that we can experiment with.  The default setting prevents CarPlay from being asked to update any more frequently than the specified rate -- the default is 4Hz, i.e., 4 times per second (once every 250msec).   This is approximately the same speed it has always been, but ther was a possibility some unusual burst pattern to leak through previously which crashed CarPlay's CarPlayTemplateUIHost library.  Hopefully (fingers crossed) this mitigates the issue -- we will only know through soak testing in the field.  

SPECIAL NOTE FOR STANDARD RANGE / TURKEY-MARKET TESTERS: If your charging and EVSE details previously read blank while plugged in, please connect, start a charge, and confirm the charging-state and EVSE readouts now populate. Thanks Burak!

SPECIAL NOTE FOR TURKISH TESTERS: More screens and labels that were still showing English are now translated. Please check the Dashboard Climate chips (humidity, AAT/IAT sensors), the CarPlay charging tab, and the Complete ECU Scan / J1979 diagnostic tools. Thanks Burak x2!

### Consistent battery gauge colors
Battery state-of-charge gauges no longer turn green above 80%. Green previously implied "good/full," the gauge now stays neutral (white) from 40% up, with orange between 20–40% and red below 20%. This applies to both the CarPlay HV pack gauge and the Dashboard state-of-charge gauge, which now match each other. The CarPlay Pack chip (volts / amps / kW) also stays white when energy flows into the pack during regen or charging, instead of briefly flashing green. The Driving tab was getting a bit too busy for my liking - thanks Sean for the suggestion!

### Experimental: a possible fix for disappearing CarPlay gauge icons
On some drives the CarPlay gauge icons can disappear and show a generic placeholder (musical note). Settings → Experimental Features now offers a "CarPlay updates per second" control: lowering it slows how often the CarPlay screen redraws, which eases the load on the car's display system that appears to trigger the issue. This is an early, still-being-evaluated mitigation — if you hit the problem from this build forward, please let me know and we can experiment with this setting together.  By default, the setting is 4 times per second (4Hz).  

### More reliable charging information across vehicles
Some cars ship a charging controller (VCMS) that reports at a different internal address than others of the same model — first seen on a Turkey-market Standard Range IONIQ 5 — which previously left the charging-state and EVSE readouts blank on those cars. The app now detects the correct address automatically when it connects, so charging details appear regardless of which variant your vehicle was built with.

### More screens localized
Several labels that were still showing English in other languages now translate: the Dashboard Climate "Relative Humidity", "AAT Sensor", and "IAT Sensor" chips, the vehicle "Model" chip, the "Forget Saved Device" button, and the "Couldn't import scan log" alert. In Advanced Diagnostics, the J1979 "ECU aborted" row, the Complete ECU Scan selection and results headers and counts, and the Dashboard parking-bytes readout are now localized too. In Turkish, the CarPlay charging tab now reads the short noun "Şarj" instead of "Şarj ediliyor".

---
## Build 103 — Kia EV6 GT 12V fix, more screens localized - App Store Version 2.1

NOTE TO TESTERS:  This is RC5 for Version 2.1 -- I'm sending this over to Apple later today for App Store approval!   Thanks everyone for the ongoing support -- from all around the world! 

SPECIAL NOTE FOR KIA EV6 GT (2022–2024) TESTERS: Your 12V / Auxiliary Battery panel should now show live values (voltage, current, temperature, state of charge) instead of reading blank. This is a follow-up to the Build 102 GT profile fix — thanks again to JH for the live logs that pinned it down.

SPECIAL NOTE FOR TURKISH TESTERS: A number of screens that were still showing English are now translated. Please open the OBD-II adapter screen, the About screen, the battery Module Temperatures / Battery Configuration readouts, and the ECU/J1979 diagnostic tools and confirm they read in Turkish. Thanks Burak!

### Kia EV6 GT (2022–2024): 12V / auxiliary-battery panel fixed
Fixed the 12V / auxiliary-battery panel reading blank on 2022–2024 Kia EV6 GT — a follow-up to the Build 102 GT profile fix. These earlier GTs read this value from a different controller location than 2025+ GTs, one the app wasn't yet polling. The Auxiliary Battery panel (voltage, current, temperature, and state of charge) now populates.

### More screens localized
Several screens were still showing English text even in other languages — the OBD-II adapter screen ("Device"), the About screen ("Registry"), the battery Module Temperatures header and Battery Configuration readout, and the ECU/J1979 diagnostic tools ("Copy All", "ECUs Found", the "Scan 0x700 – 0x7FF" button, "Broadcast"/"Physical probe"). These now translate in all supported languages. The VIN label is also clearer in Turkish — now "Araç Şasi No" (vehicle chassis number), the term Turkish drivers and technicians actually use — and the "Batt Heater"/"Batt Temp" and "Lifetime Max/Min" labels are shorter so they fit their tiles.

---
## Build 102 — Live scan health gauge, more reliable "Vehicle On" detection, Kia EV6 GT lights fix, IONIQ 5 Standard Range battery fix, Turkish polish

NOTE TO TESTERS: There are some key (and possibly disruptive) changes in this build.  Please verify a few things with your vehicles - does the app correctly detect the vehicle turning on?  The app now realtime monitors polling activity -- please send me a screenshot of your Scan Status panel (phone app/Dashboard/Overview)  

SPECIAL NOTE FOR KIA EV6 GT (2022–2024) TESTERS: Please confirm your brake-light and headlight indicators now light up correctly. These earlier GTs were reading the wrong locations before. Thanks to new beta tester JH for the live data.

SPECIAL NOTE FOR IONIQ 5 STANDARD RANGE TESTERS: Please open Cell Voltages and the Battery Configuration readout and confirm it now shows the full pack ("144 series x 2 parallel") rather than only 96 cells. Thanks to Turkish tester Burak for his help on this and the Turkish translations!

### Live scan health gauge
The Scan Status panel (Dashboard) and the CarPlay scan rows now show a live per-signal health gauge instead of the static "found" count left over from the removed training phase. Each signal shows what fraction of its recent polls returned data; signals that stop responding float to the top, and the panel/CarPlay header summarizes "N not reporting." NO DATA and negative-response replies are shown separately and never counted as faults — so normally-quiet signals (asleep parking sensors, charging-only data) don't read as problems.

### More reliable "Vehicle On" detection
The app now confirms the vehicle's main controller is awake (a VIN read) before switching to the on state, instead of relying on the climate module alone. This prevents the app from briefly treating the vehicle as on while it's in accessory mode or still waking up after you connect — a state that could previously load the wrong vehicle profile or skip controller identification.   Thanks new tester Tim for his help!

### Kia EV6 GT (2022–2024): brake-light and headlight indicators fixed
Fixed brake-light and headlight indicators not appearing on 2022–2024 Kia EV6 GT. These earlier GTs use a different body-control-module layout than 2025+ GTs; the app was reading the newer locations, which the older car doesn't answer, so the indicators stayed dark. Pre-2025 GTs now load a matching vehicle profile. Their AC-charging input voltage and frequency readouts are corrected by the same change.

### IONIQ 5 Standard Range: full battery pack
Fixed the battery pack reading wrong on IONIQ 5 Standard Range models. The Cell Voltages view and "Battery Configuration" readout previously showed only 96 of the pack's cells and mislabeled it as "96 series"; the app now reads the full pack and correctly shows "144 series x 2 parallel".

### Turkish (Türkçe) translation polish
Improved Turkish translations across the app from a translator's review pass: clearer Diagnostics wording, corrected Light/Dark appearance labels, a clearer "Adapter Idle Check" name, and shorter battery-pack gauge labels that fit on small dashboard tiles and CarPlay chips.

---
## Build 101 — Kia EV9 auto headlights found!, Faster connection to live data, CarPlay onboarding + crash fix, adapter setup improvements, Gear chart

SPECIAL NOTE FOR KIA EV9 TESTERS:   Please verify that your low beam indication comes on correctly two ways:  If you turn the stalk to ON, do you see the low beam indicator?   If you have the stalk in AUTO and its dark (or you cover the ambient light sensor), do you see the low beam indicator?   Please share your experiences with me so I can know if this issue is closed or not.  

NOTE TO TESTERS: This is RC3 for Version 2.1 - the final RC?  A big win today for the treasure hunting for the Kia EV9.  The time to dashboard has improved by 31% in my testing - your Driving tab should appear more rapidly than ever before.  This build also includes lots of changes to help new folks onboard smoothly -- likely not things most of you will experience.  If you're feeling adventerous, and have some time, it would be great if you could forget your adapters and stress test the new flows, that would be very appreciated -- please let me know if you run into any friction adding your adapter back in.   I added the Gear chart to driving-session history, and added a new Wh/km efficiency unit that had been requested by some customers.

### EV9 low-beam indicator fix
Fixed the EV9 low-beam indicator which now responds to both manual stalk control and automatic activation.  Special thanks to tester Jaka from Slovenia for the time he spent mapping the Kia EV9 BCM, and for tester Stephen Y for using this map to find gold!    

### Faster connection to a live dashboard
The app no longer runs a per-connect "training" pass that probed every ECU before polling started.  In my testing a >31% improvement.

### CarPlay: onboarding screen and a mid-drive crash fix
- A first-time customer with no saved adapter now sees a clear "Set Up Your Adapter" screen in CarPlay instead of diagnostic Status rows. The new screen tells you to select an adapter in the app on your iPhone
- Fixed a crash caused by a transient CarPlay/vehicle link drop - a complicated chain reaction that led to the app writing to its database just as iOS was suspending it — a situation that lead to iOS terminating the app because it holds a write lock. The driving-session close is now debounced by a 20-second grace window (think loose USB-C cable).

### Adapter setup and Settings
- When scanning for an adapter, any adapter **already connected to your iPhone** (for example, held by another OBD app) now shows up marked "In Use." Previously a scan couldn't see these at all — a connected Bluetooth device stops advertising. Selecting one shows the same slide-to-confirm reminder as first-time setup before adopting it.
- Settings → OBD-II Adapter: status and error messages now wrap to as many lines as needed instead of being cut off with an ellipsis at larger text sizes.
- Settings → OBD-II Adapter: when Bluetooth itself is the problem, the section now offers a one-tap fix. If Bluetooth is off, a **Turn On Bluetooth** button brings up iOS's prompt; if the app's Bluetooth permission is denied, an **Open Settings** button jumps to the app's permission page. 

### Dashboard
- **State of Charge** no longer flashes a red **0%** for a moment when the adapter first connects. Until the battery is actually polled, the Dashboard and CarPlay SoC gauges now show a neutral "—" on an empty ring instead of an alarming red zero
- **Efficiency Unit** adds **Wh/km** as a fifth option, alongside mi/kWh, km/kWh, kWh/100km, and Wh/mi. It's a metric consumption unit (energy per distance, lower is better) that many EU drivers prefer over kWh/100km. It flows through the Dashboard efficiency chip and History session cards automatically.

### Driving session history
- New **Gear** chart showing P/R/N/D shifter position across the drive, in both the in-app session detail and the shareable session card.
- Session share cards now render every chart panel at the same height

---
## Build 100 — Curated DID List testing fixes, steadier Bluetooth reconnection, charging chart fix

NOTE TO TESTERS:  This is RC2 for Version 2.1.  This build smooths out the Curated DID List testing flow, makes Bluetooth reconnection more reliable when the adapter briefly drops, and fixes a small glitch in the charging-session charts.

### Curated DID List testing: a smoother flow
Three fixes to the "ABC test with Curated DID List" tool:
- Aborting a session no longer drops you on a duplicate "Pick a curated list" screen.
- Sessions now close the tool when you tap Done (on the results) or Abort (mid-capture), instead of leaving you on the picker.
- Opening a curated-list file someone shared with you now jumps straight to that list's checklist, ready to start — instead of dropping you on the picker to find it.

### Steadier Bluetooth reconnection
More reliable reconnection when the adapter briefly drops and returns — for example at the edge of Bluetooth range, or as a parked car wakes and sleeps overnight. The app no longer keeps trying to poll a link that has gone away, and recovers cleanly once the adapter is back and re-initialized.

### Charging session chart fix
Fixed a small rendering glitch in the EVSE Current chart on a charging session's detail screen, where the Requested and Delivered lines could show a brief horizontal spur during the charging ramp. Shared session images are corrected too.

---
## Build 99 — Korean and Turkish, localization fixes, session chart cleanup, crash fixes

NOTE TO TESTERS: I'm labeling this RC1 for App Store Release 2.1.  Please let me know if you find anything unusual.  The app now adds Korean and Turkish — 9 languages total. Alongside the new languages, a localization sweep fixed dozens of strings that had been showing English no matter which language you used, so if you run the app in German, Dutch, Spanish, French, Italian, or Swedish, expect several screens to look properly translated for the first time. This build also carries a session chart cleanup and two crash fixes (very rare, but good to fix anyway)

### Two new languages: 한국어 and Türkçe
Korean and Turkish join German, Spanish, French, Italian, Dutch, and Swedish. Every string in the app is translated — Dashboard, CarPlay, History, Diagnostics, Settings, and the share cards. Switch in Settings → Display → Language, or leave it on System Default to follow your phone.

### Localization fixes in every language
A sweep of the string catalog found 32 strings that had never been hooked up for translation and silently showed English in all languages. They're now translated in all 8: the CarPlay scan-status chips, the J1979 crawl statuses, the Complete ECU Scan screen, the History storage rows in Settings, and the "No data" chart placeholders. A further set of live strings that the tooling had wrongly marked as unused — "Looking for adapter", the parking-sensor footnotes, the ECU scanning status, the motor gauge labels — are covered in the new languages too. Six existing translations were also corrected, including German and Dutch wording that didn't match the rest of the app.

### Session charts: aligned, anchored, labeled
Three fixes to the charts on a session's detail screen (and the share card):
- All charts in the driving and charging stacks now share one plot width, so the time gridlines line up vertically down the whole stack. Previously each chart sized its Y-axis gutter to its own widest label, so plots came out slightly different widths.
- The State of Charge chart now fills from the left edge of the session instead of opening with a blank gap. SoC is only recorded when it changes (with a periodic heartbeat), so the first sample often lands a minute or more into the session; the chart now carries the last pre-session value back to the session-start line, the same way the other charts already did. The fix is in chart rendering, so all your existing sessions are fixed retroactively.
- The binary signal bands (Brake Light, AC/DC Charging, Preconditioning) no longer paint full-bleed under the column where the sibling charts draw their Y axes — they now show a real On/Off axis, both in the app and on the share card.

### Two crash fixes from the crash dashboard
- Fixed a Bluetooth crash (4 events across 3 devices): if the adapter disconnected at exactly the wrong moment during connection setup, the app could later touch freed connection state and crash. The typical trigger was overnight parked-car auto-reconnect churn. Connection events are now handled immediately instead of deferred, closing the window.
- Fixed a crash in the OBD response decoder (5 events): a corrupted response line that was cut off after its first byte crashed the decoder. It now treats the line as a failed read and moves on.

### Settings polish
The OBD-II Adapter card's status row now draws a full-width separator like every other Settings row. It previously showed no line at all — the default rendering aligned the separator to the Connect button, leaving just a stub, so it had been hidden outright.

---
## Build 98 — Settings redesign, Headlight Indicator, background stability

NOTE TO TESTERS: Settings has a new iOS-style layout — every control is still there, now organized into categories that open their own screens. Note that the 5-tap Build unlock now lives in Settings → About. Also new: a Headlight Indicator option.  I added protection against a class of silent background terminations that could interrupt History recording -- this is a substantive change, so please pay close attention to anything involving the History panel that looks odd.

### Settings reorganized into categories
Settings now works like the iOS Settings app: the OBD-II Adapter card stays at the top, and everything else is grouped into colored category rows — Units, Display, CarPlay, Notifications, History, Diagnostics, Advanced Tools, and About — each opening its own screen. All controls behave exactly as before; they just have new homes:
- Auto-Connect now lives inside the OBD-II Adapter card itself.
- Appearance, Language, Dashboard Charts, and Keep Screen Awake are grouped under Display.
- The Unplug Reminder is under Notifications.
- Reset Onboarding is at the bottom of About.
- The 5-tap-on-Build unlock for Experimental Features moved with the Build row into About. When unlocked, Experimental Features appears as its own row on the main Settings screen.

### New: Headlight Indicator setting
Settings → CarPlay has a new Headlight Indicator setting on vehicles that report headlight status, with three options. Off hides the headlight chip in both the Dashboard and CarPlay. Icons is the behavior you have today (and the default). Text replaces the symbols with words — "Low" in the green of the low-beam telltale and "High" in the familiar high-beam blue. The Brake Light Indicator setting moved into the same CarPlay section (same options as before), and the Dashboard brake light chip's On/Off value is now translated in all languages.

### Fewer silent interruptions to History recording
Crash reports showed iOS could terminate the app while it was saving History data in the background — the system would suspend the app mid-write. All background History writes (snapshots, drive/charge sessions, storage-cap cleanup, and launch-time database setup) are now protected by a background-task assertion, so the save completes before the app suspends. This was invisible in normal use but was the largest crash cluster in the dashboard, and it could cost the tail end of a drive or charge.

### History fixes after Delete All History
Running Delete All History while a session's detail screen was open could leave the History tab showing a black screen with a lone warning triangle; that's fixed. A session removed out from under an open screen (a purge, or a deletion syncing in from another device) now shows a proper "Session unavailable" message instead of an endless spinner, and a deleted photo under an open full-screen preview now shows "Photo unavailable" with a Done button instead of an undismissable black screen.

---
## Build 97 — Lifetime Efficiency history cleanup, AC charging session charts

NOTE TO TESTERS: A one-time cleanup of old Lifetime Efficiency readings, new AC charging charts, and chart polish.  There is a database schema change with this release, so please give me a shout out if you have any issues viewing things under HISTORY. 

### Old "Lifetime Efficiency" history cleaned up automatically
Build 93 fixed the bug that recorded a false 0% at the start of each recording window in History → Signals → Lifetime Efficiency. This build cleans up what was already recorded: a one-time background pass removes those spurious 0% points from your existing history, so older charts read correctly too. It runs quietly shortly after launch — you don't need to do anything — and it runs only once per iCloud account, with the cleaned-up history syncing to your other devices.

### AC charging sessions: AC Input Current and Voltage charts
AC (Level 2) charging session details now include AC Input Current and AC Input Voltage charts, shown between State of Charge and Charging Power — both in the session detail and on the shared report card.

### AC charging sessions no longer show Preconditioning
Preconditioning is battery prep for DC fast charging and doesn't apply to AC (Level 2) charging, so the Preconditioning strip no longer appears on AC charging sessions. DC sessions are unchanged.

### Preconditioning strip is a continuous line again
The Preconditioning strip in a session's History detail renders as one continuous line with sample dots, instead of breaking into segments across data gaps — restoring its pre-Build-96 look. The AC/DC Charging strips keep their Build-96 treatment (dots plus cross-hatched "unknown" regions).

---
## Build 96 — Charging session end-time fix, clearer charging History charts

NOTE TO TESTERS: A charging-history accuracy fix plus some chart polish.

### Charging sessions no longer run long when you walk away
If your phone (or the app) was away from the car as a charge finished, there was a possibility for a charging session to be recorded as lasting far longer than the actual charge — a ~3-hour charge could show as ~27 hours, with the charts and Duration stretched across the whole span. The app now records the true end of the charge the moment it sees charging stop, so the session length, average power, and charts stay accurate even if the connection drops or the app is closed right afterward.

### Charging History — dots and "unknown" regions
On the AC and DC Charging strips in a session's History detail (and on the shared report card), each captured data point is now marked with a dot, so it's easy to see exactly where readings landed. Where no data was captured for a stretch — for example because the phone was away — that span is now drawn as a cross-hatched "unknown" region in the signal's color, instead of a flat line that implied we knew the state the whole time. Added dots to Preconditioning as well.

### Two-day sessions show both dates
When a session spans midnight, the date now shows both the start and end dates. Previously the end time could appear under the start date with no sign it actually finished the next day. This applies to the in-app session view and the shared report card.

### Shared report — header matches the Duration stat
On the shared charging report card, the duration in the header line now matches the Duration stat below it.

---
## Build 95 — Power panel and CarPlay power gauge, French CarPlay charging chip fix

NOTE TO TESTERS:  A few new features and bug fixtures

### New Power panel
The Dashboard has a new Power panel, just below Regeneration. It shows a live output-power dial that fills from zero up to the battery pack's peak power capability, along with a Pack Peak reading and an info bubble explaining what you're looking at. Like the app's other power readouts, the value follows your chosen power unit in Settings (kW, HP, or PS), and it's fully translated.

### Power readouts follow your unit setting
The Dashboard panel now respects your Settings power unit (kW, HP, or PS). Previously it always showed kilowatts regardless of your preference.

### CarPlay power gauge
On the CarPlay power chip, the output side of the dial now scales to the battery's live peak-power capability reported by the car, instead of an estimate based on the vehicle's horsepower rating. A small "PEAK" label below the dial shows that maximum, in your chosen power unit.

### IONIQ 5 N and Kia EV6 GT recognized correctly
2024-model-year IONIQ 5 N cars and Kia EV6 GT cars were being misidentified and loading the wrong (AWD Long Range) profile. Both are now recognized from their VIN and load the right vehicle profile

### French charging-status chip
The CarPlay charging-status chip no longer renders as a clipped "Charg…" in French. It now uses "Recharge" for the charging section name and "Charge" for the live status.

### Charging — Status layout
The two chips in the charging Status row now expand to fill the full row width.

---
## Build 94 — Kia EV9 detection fix

NOTE TO TESTERS: Getting this build out to support an EV9 tester in the field - thanks Jaka!

### Kia EV9 detection fix

Some Korea-built Kia EV9s were still being misidentified as an IONIQ 5. EV9 VINs whose WMI third character isn't `D` — for example those starting with `KNAA` — were slipping through and getting polled as an IONIQ 5. EV9 detection now covers the full set of EV9 VIN prefixes, so these vehicles are recognized correctly and load the right battery and drivetrain profile.

(This is the same kind of VIN-prefix gap that was fixed for the Kia EV6 in Build 93, one model over.)

---
## Build 93 — Signals chart multi-touch fixes, Kia EV6 detection, lifetime efficiency 0% fix

NOTE TO TESTERS:  The History / Signals experience is much improved -- I think it's pretty amazing, but I'm a little biased.  I plan on adding some instructions to help people navigate the capabilities of this tool because there is so much that may not be discovered.  I plan on releasing a maintenance build to the Apple App Store (version 2.1) later this week due to the VIN decoding issues with the Kia EV6.   Also noteworthy -- the app has a new marketing landing page, with inspiration from forum member DH (a talented graphic designer), check it out here:  https://www.theburl.com/ioniq-app/.   And finally, the app surged to #3 in the App Store Utilities this weekend -- woohoo!

### Kia EV6 detection fixes

A couple of Kia EV6 variants were being misidentified. Some Korea-built EV6s — VINs starting with KNAC and similar — were slipping through and being treated as an IONIQ 5; EV6 detection now covers the full set of EV6 VIN prefixes, so they're recognized correctly. Separately, the EV6 RWD Standard Range is now identified as its own variant, loading the right battery and drivetrain profile and hiding the front-motor gauge instead of defaulting to the AWD Long Range.

### History → Signals chart: smoother panning and zooming

The Signals charts got a big multi-touch overhaul:

- Prior/Next now move the view by the amount of time you have on screen (with a slight overlap) and skip empty stretches to land on the next real data for that signal — no more jarring auto-zoom to each data cluster. Jump-to-Earliest/Latest keep your current zoom and snap to the start or end of recorded history, and all the transport controls go inactive once you're already viewing the entire time range.
- Pinch-to-zoom now "sticks" — dragging right after a pinch no longer snaps the chart back to fully zoomed out. Pinch, pan, and the scrub crosshair are now mutually exclusive, so a two-finger zoom is never undone by the next one-finger drag. (The accidental double-tap-to-reset gesture is gone too.)
- Scrub — press and hold to read a value — now takes a deliberate hold instead of firing on the lightest touch, the crosshair appears immediately under your finger, and it's a full crosshair now (horizontal + vertical). The horizontal line hides automatically when you're scrubbing over a stretch with no recorded data.

### Lifetime Efficiency 0% fix

Fixed the History → Signals "Lifetime Efficiency" series recording a spurious 0% at the start of each recording window (and the Dashboard's battery-efficiency tile briefly flashing 0%). Efficiency is computed from the battery's lifetime charged and discharged counters; right after reconnecting, the discharged counter hadn't been read yet, so the first reading briefly computed as 0 before correcting itself. It's now recorded only once both counters are available.  I will be pushing a change in the next build (hopefully) that cleans out the erroneous values from everyone's databases.

---
## Build 92 — Start of Kia EV9 support

NOTE TO TESTERS:  Version 2.0 has been released!

NOTE TO EV6 TESTERS:  To all the Kia EV6 testers -- thank you for your help brining the EV6 online.   I've been reaching out to all of you with the promised promo codes -- if you don't hear from me by the weekend -- please don't hesitate to reach out in case I've missed you.

### Kia EV9 now supported

The app now recognizes the Kia EV9 instead of treating it as an IONIQ 5. All three variants are covered — Standard Range RWD, Long Range RWD, and Long Range AWD — each with the correct battery capacity, cell configuration, and drivetrain (the front-motor gauge is hidden on the rear-wheel-drive trims). The vehicle now identifies itself as "Kia EV9" throughout the app.

Welcome to our first EV9 tester, Jeremy — thanks for the logs that made this possible!

---
## Build 91 — Phantom Charging Session cleanup - App Store Version 2.0

NOTE TO TESTERS:  One last minute bug came in, and has been fixed.  This build is going over to Apple as Version 2.0.  (Build 91 / RC8)

### No more stray empty Charging Sessions

Fixed a History bug where preconditioning the battery without then charging could leave behind a stray, empty "Charging Session" in History. Such a session is now reliably removed about 30 minutes after preconditioning ends without plugging in. The cleanup also survives the app being suspended or relaunched in the meantime, which previously could let the phantom session linger.  Thanks to Kåre for his rigorous testing!

---
## Build 90 — CarPlay tire-pressure chip readability

NOTE TO TESTERS: This is RC7.  I'm submitting this build to Apple later today for Version 2.0.  Thank you to everyone for all the support -- I'm looking forward to sharing this version with the rest of the world!

### CarPlay tire-pressure chip readability

The pressure and temperature values on the CarPlay tire-pressure chip now use black text on the colored (green / orange / red) tiles, instead of white text with a drop shadow.  The "no data" gray tile keeps its white text.

---
## Build 89 — Faster History detail, improved Signals chart controls, BLE robustness

NOTE TO TESTERS:  This is RC6 for Version 2.0.  This build includes a database schema update and a one-time local index upgrade.  After updating, navigate to the History tab and you'll see this process working.   After it is done, you will see a huge performance improvement opening historical recordings.  If you have attached any photos to sessions, those will also now properly sync across your devices if you have iCloud sync turned on.  Thanks as always for the feedback. Please let me know if you see anything unusual -- I'm really hoping this is the final build for Version 2.0.

### Faster History detail

Opening a History detail is now much faster. Tapping a charging or driving session, or an individual signal, used to stall for roughly a second to a second and a half before anything appeared. Now the screen shows up promptly with its headline content — the session summary, or a signal's latest value — and the charts and secondary stats fill in a moment later instead of holding up the whole screen. The difference is largest on signals with a lot of recorded history.

### One-time index upgrade on first launch

On the first launch after updating, History performs a one-time, automatic upgrade of its local index — you may briefly see "Building local index" in History → Signals while it runs. Once it's done, opening an individual signal is consistently fast, including repeat opens, which previously could lag noticeably the second and later times you opened the same one.

### Signals chart controls

You can now navigate historical signals in either the collapsed view or expanded view.   Added a jump to the beginning button, to make it easier to see the earliest recordings.

### CarPlay Connect/Disconnect improvement

On the CarPlay Status screen, the adapter's Connect/Disconnect button now reflects whether the app is actually connected, not just what you last asked for. Previously, if the connection failed or dropped on its own (e.g. a hiccup right as you started the car), the button could still read "Disconnect" while the adapter was disconnected — so to reconnect you had to tap Disconnect first just to make the "Connect" button appear, then tap Connect. Now it reads "Connect" whenever you're not connected, so a single tap retries. While it's actively connecting, it reads "Disconnect" so you can cancel a stuck attempt.

### BLE robustness

Hardened the adapter auto-recovery shipped in Build 87 against one more case. If the Bluetooth link dropped at the very start of talking to the adapter — during the brief warm-up before the first command — the app could still get stuck showing "Not connected to OBD adapter" with a red icon, needing a manual connection.  The app now lets an automatic reconnection happen on its own.   Thanks Mark for the patience and logs!

---
## Build 88 — First-connect reliability, background resume, storage cleanup, and a Cell Voltages explainer

NOTE TO TESTERS:  This is RC5 for Version 2.0 — reliability and housekeeping fixes plus a new Cell Voltages explainer. Thanks as always for the feedback. Please let me know if you see anything unusual.

### More reliable first connection

Some adapters — notably the VGate iCar Pro 2S — could fail the very first connection attempt right after launch, flashing a brief error and silently reconnecting before succeeding. The first attempt is now reliable.

### "Looking for adapter" while connecting

The adapter connection status now reads "Looking for adapter" while the link is being established (matching CarPlay), instead of "Connecting…". The app is really waiting for iOS to confirm the Bluetooth link rather than actively working, and the new wording reflects that.

### Resumes after the app is terminated in the background

If iOS terminates the app in the background (for example under memory pressure) while it's connected to your adapter, the app can now relaunch itself in the background on the next adapter activity and resume on its own — reducing lost recording time across app terminations. (This doesn't prevent gaps caused by iOS suspending a backgrounded app between polls — see the Keep Screen Awake note below.)

### Energy added recorded the instant a charge ends

Charging sessions now also record the energy added (kWh) from a fresh reading taken the moment the session ends, alongside the ending battery %. Because it's captured while the car is still awake, the figure stays accurate even on sessions the car ends on its own (e.g. reaching your set charge limit) and powers down moments later.

### Reclaims leftover storage

The app now reclaims roughly 30 MB of leftover storage on devices that updated through an earlier version — a duplicate copy of the history database a past update left behind. It happens once, automatically, the next time the app launches, and writes a one-time "History Storage Cleanup.txt" note into the app's Files folder confirming how much space was freed. New installs are unaffected.

### Cell Voltages explainer

The Battery → Cell Voltages section now has an info button. The explainer covers what the view shows: the Min/Avg/Max and Delta stats, that each square in the grid is one cell colored by how far it strays from the pack average (not its absolute voltage), what the green/yellow/red bands mean, and how to read it — an even field of green is ideal, brief shifting deviations are normal, and the same few cells holding a wider gap consistently over time is the pattern worth watching.

### Clearer "Keep Screen Awake" note

The "Keep Screen Awake" setting's footer now states that when it's off, your device may dim or lock and the app may be suspended by iOS, which will introduce gaps in the recorded data — replacing the previous wording that implied recording always continues.

---
## Build 87 — Charging History: data-gap notice and single-sample chart fix

NOTE TO TESTERS:  This is RC4 for Version 2.0 - a couple of visualiztion tweaks/fixes for https://github.com/gburlingame/ioniq-app/issues/41

### "Data gaps detected" notice on charging sessions

If a charging session loses its connection to the app partway through — for example you start a charge, then walk away with your phone and reconnect later — the charts fill in the missing stretch by carrying the last known reading forward. Charging sessions that had a gap like this now show a "Data gaps detected" notice on the session detail screen and on the shared session card, so it's clear that the values across the gap are inferred rather than measured. The notice only appears when a gap is actually present.

### Charging-session charts with a single reading now show a scale

Fixed the Charging Power and EVSE Current charts collapsing to a bare flat line with no vertical scale when a session captured only a single reading — which can happen when the adapter disconnects right after a charge starts. These charts now always draw a proper kW / A axis and fill, both in the app and on shared session cards.

---
## Build 86 — Net efficiency, charging accuracy fixes, refreshed info sheets, tappable CarPlay Compass

NOTE TO TESTERS:  This is RC3 for Version 2.0.  Thanks to everyone sending in feeddback -- I couldn't do this without everyone's support -- thank you!  Enjoy the driving this weekend, and please let me know if you see anything unusual.

### Driving efficiency now counts net energy

Driving-session efficiency now reflects net energy use — energy recovered through regenerative braking is no longer counted against you, so the figure tracks the car's own trip computer more closely. Sessions recorded before this build keep their old values, so expect a step in the efficiency trend at this build.  Thanks James for figuring this out!

### New efficiency units

Settings → Units now lets you show efficiency as kWh/100km (the standard in Canada and much of Europe) or Wh/mi, in addition to mi/kWh and km/kWh. Metric regions now default to kWh/100km — so if you're in a metric locale and haven't changed your units, the efficiency figure switches from km/kWh to kWh/100km; set it to whatever you prefer. Applies to the drive detail screen and shared session cards.   Thanks Denis for this idea!

### Charging fixes

- Charging sessions now record the battery percentage the car actually finishes at. Previously a session the car ended at a set limit (e.g. 80%) could be saved a half-percent low because the last reading was slightly stale — the app now takes a fresh reading the instant a session ends, while the car is still awake.
- Fixed AC charging staying shown as "active" after the car ends a charge on its own (e.g. reaching your charge limit) with the cable still plugged in. The app now confirms AC charging against live battery current, so it only shows AC charging while current is actually flowing. The History "AC Charging" band shows the real on/off bursts instead of one continuous block.
- Renamed the charging-session History badge from "Unplugged" to "Finished" — accurate whether or not the cable was pulled.
- Fixed the Pack Voltage (and Battery Temp) lines briefly drawing outside the chart area near the left edge during a live charging session; these charts now clip cleanly.

### Adapter reconnects automatically after a hiccup

Fixed the app sometimes showing a stuck red error on the adapter (e.g. "Adapter disconnected") with no obvious way to retry — typically after launching the app before getting in the car, then starting it. A brief Bluetooth hiccup during the first connection was being treated as a hard error; the app now reconnects automatically instead.  Thanks Mark!

### Refreshed in-app info sheets

The in-app info sheets got a more modern look — a hero icon and title over grouped cards. New info buttons: the driving-session efficiency figure (explaining how short drives can skew it, since trip distance comes from the car's whole-mile/km odometer), and the Dashboard Regeneration dial (the green arc, Available, and Pack Peak). The Polling Headroom sheet adds a tip: two devices sharing one adapter can cut headroom by 30–40%.

### Tappable Compass on CarPlay

The CarPlay Driving-tab Compass chip now shows a small info badge and, when tapped, opens a Compass screen with the live compass and a note: for an accurate heading, the phone must be lying flat with the top of the phone pointed toward the front of the vehicle.

### History stays available if its database can't open

If the saved-data database ever fails to open at launch, the app now launches normally with everything else working and shows a clear "History isn't available" message (plus a log file you can send for support) instead of risking a crash.

---
## Build 85 — Faster launch, brake-light regen fix

NOTE TO TESTERS:  This is RC2 for Version 2.0 - we are back on track!  The brake light "fix" in build 84 broke the brake light for everyone when the car's one pedal light-up algorithm turned the light on -- it was only responding to the physical brake pedal.

### Faster app launch

The app no longer rebuilds its entire Signals history index every time it launches. On devices with a large history this caused a multi-second processing spike at startup that could feel like a brief hang. Launch now updates the index incrementally — doing nothing when there's nothing new — and only performs a full rebuild once, the first time you launch after installing. Found and confirmed with Instruments.

### Brake Light — now catches regenerative / one-pedal braking

The Brake Light indicator now tracks all braking, not just the physical brake pedal. Build 84 only responded to the brake-pedal switch, so on 2022–2024 EV6 and IONIQ 5 the chip stayed dark during one-pedal slowdowns and stops.

---
## Build 84 — Gear history, brake-light fix, CarPlay compass/odometer toggle

NOTE TO TESTERS:  Not quite ready to call this RC2.  Owners of 2022-2024 Kia EV6 and IONIQ 5's -- please play extra close attention to the brake light chip behavior.   Does it behave correctly?   No interaction with the left or turn signals?

### Brake Light indicator fix — 2022–2024 EV6 and IONIQ 5

Fixed the Brake Light indicator falsely turning on in sync with the right turn signal on 2022 Kia EV6's -- and possibly others. On this model the indicator was reading a shared rear stop/turn lamp that lights for both braking and that side's turn signal; it now reads a brake-only signal, confirmed against brake-only, left-turn, and right-turn captures.  2025 and newer models use a different source and are unchanged.

### Gear is now saved in History

The shifter position (P/R/N/D) is now a recorded Historical Signal. Find it in the History tab's Signals list under Drive, with a tap-through chart that steps between P, R, N, and D over time. It syncs across your devices via iCloud like every other signal.

### CarPlay — choose Compass or Odometer on the Driving tab

New setting under Settings → CarPlay: "Replace Odometer with Compass," on by default. Leave it on for the live compass that's on the Driving tab today, or turn it off to show the odometer in that spot instead. The compass only uses location while it's the chip you've selected.

---
## Build 83 — Driving sessions gated on gear; CarPlay performance pass

NOTE TO TESTERS:  Thanks to everyone who tested the new Gear chip in Build 82 — it's confirmed working across the fleet.   I did a bunch of performance profiling today, and discovered a startup issue that's going to require a database schema migration in order to fix.   I worked on that for most of today, I hope to deploy that tomorrow.   I'm holding off calling this RC2 as a result.

### Driving sessions only start in Drive or Reverse

Until now, the app started a new driving session the moment HVAC responded (ignition on).  This was creating issues for folks who AC charge and happen to leave their OBD-II adapters plugged in -- lots of short aborted Drive sessions were being created.

Now the gate is: ignition on AND gear in Drive or Reverse. The session-start moment (odometer, SOC, pack temps on the Session row) reflects when you actually start driving, not when the car turned on.

End behavior is unchanged — ignition off, plugging in mid-trip, and BLE disconnect all close the session exactly as before. Mid-drive shifts (D→N at a stop, D→R for parking) do NOT end the session.

Applies to both fresh ignition cycles and the auto-restart after a mid-trip charging session ends.

### CarPlay — Dashboard and Status tabs are faster

Cached registry signal-flag lookups and the localized-string bundle so they're no longer recomputed on every view re-evaluation. Time Profiler shows the targeted hot paths drop ~94% over a 60-second trace.

### CarPlay — Status tab skips redundant cell reconfigures

The Status tab now skips the underlying text-update call when the rendered string hasn't changed, avoiding redundant CarPlay framework cell reconfigures.

### CarPlay — Precondition and Heater Temp chips stop re-rendering unchanged content

When these chips were showing inactive state, they were re-rendering the same image every ~5 seconds because their snapshot keys included BMS sample counts that advance on every poll regardless of the chip's actual state. Snap keys are now state-branched.

---
## Build 82 — Gear chip on Dashboard, Isolation chip restyled

NOTE TO TESTERS: Sorry for two builds in one day - but I need to ask everyone to help out with this one - please open the phone app, and check out the new Gear indicator chip in the Overview section.   PLEASE verify this is working on your vehicle -- P, N, R, D -- and let me know.  An issue has emerged with the Driving Session feature and I see an easy solution if this gear indicator works across the fleet.  IONIQ 5, 5 N, 6, 9 -- Kia EV6, Genesis GV60, etc...

### Dashboard → Overview — new Gear chip

Shows the current shifter position: P, R, N, or D. Sits next to Isolation Resistance on a single row. Updates within 2.5 seconds of a shift.

### Dashboard → Overview — Isolation Resistance chip restyled

The chip now matches the visual style of the other Overview chips (VIN, Model, Odometer, etc.)

---
## Build 81 — App crash fix when manually connecting/disconnecting, Auto-Connect updated, new haptics

NOTE TO TESTERS:  Thank you for all your continued support!  This is Release Candidate 1 (RC1) for Version 2.0.   Please report anything unusual -- if you're unsure if something is a bug, please don't hesitate to reach out.   Thank you to tester Paul for sending in a crash report via TestFlight that made me aware of the app crash issue when manually connecting/disconnecting.

### CarPlay — vehicle-tab tear-down debounced (crash fix)

Fixes the `Array index out of range` crash some testers had encountered when connecting and disconnecting from the adapter manually

### Settings → OBD-II Adapter — Auto-Connect reworked as a pure preference

- **Turning Auto-Connect OFF no longer drops a live link.** Only the Disconnect button does that.
- **Turning OFF mid-attempt cancels it** — no more hanging in "Connecting…" when out of range.
- **Turning ON kicks an immediate reconnect** when not already linked.
- **Adopting an adapter** (Scan → tap, or claiming an already-connected one) flips Auto-Connect to ON automatically.

### Settings → OBD-II Adapter — section split into two

Now two sections with one focused footer each:

- **OBD-II Adapter** — status row + Disconnect / Scan / Connect button.
- **Auto-Connect** — toggle + reconnect-behavior footer.

The Disconnect button is text-only (red `bolt.slash` icon gone), and the muted-red bordered style coordinates with the text color instead of layering brighter red over dimmed background.

### Dashboard — adapter panel is informational only

"Disconnected" / "Error" panels no longer carry Connect / Retry buttons — those live in Settings. The "Is your OBD-II adapter plugged in, and are you in range?" footer stays.

### Welcome onboarding — simplified OBD-II Adapter step

Stripped variant of the Settings section. Auto-Connect toggle, Forget Saved Device, and reconnect footer are hidden during onboarding. Status row, Scan button, and discovered-devices list are unchanged.

### Reset Onboarding — reliably returns to Welcome on first try

Previously the connected-adapter probe raced the reset and re-routed you into the "Adopt this already-connected adapter" sheet, requiring a second reset to see Welcome 1-2-3. First reset now works.

### CarPlay — status row shows scan progress

During startup, the status row reads `Scanning ECUs · N/M`, ticking up as each ECU comes online (typically 1/8 → 8/8 over ~4-5 seconds) so it's visible the scan is making progress instead of hanging.

### History → Signals — haptics on chart scrub

Tap-and-hold to start scrubbing now produces a light haptic bump.

### Dashboard — haptics on section expand/collapse

A soft haptic bump has been added, a bit of polish

### J1979 Crawl — cleaner post-crawl action row

Start New Crawl is now the single prominent button; Share Report demoted to a tint-colored link beneath it.

### Quick Look preview of `.iqlist` curated DID lists

Hint now reads "Tap [share icon] below. Select IONIQ 5 Companion on the next screen that appears." with an inline share-sheet SF Symbol, fully localized into all six non-English locales. The hint follows the in-app language picker.

---
## Build 80 — CarPlay Driving tab update and *New* compass feature, *New* setting to let the screen sleep, History session improvements

NOTE TO TESTERS:  Happy Memorial Day!  I added something new -- a Compass chip to the driving tab.   I'd love to hear what you think about this.  Compass uses your iPhone for the source of the signal, so the top of the phone needs to be pointed in the direction the car is headed.  I think that should be OK due to the way the charging pad is aligned.  I also added a lot of polish all over the place.  We're getting close to RC1 for Version 2.0, so please keep sending your feedback! 

### CarPlay → Driving tab — new Power chip, new Compass chip, Precondition redesign

- **New Power chip** — bidirectional circular gauge. White arc fills clockwise for power drawn (scales to vehicle peak); green arc fills counter-clockwise for regen (scales to BMS pack peak). Centre shows unsigned magnitude with one decimal; green for regen, white for draw.

- **New Compass chip** (replaces the standalone Regeneration chip) — heading-up rose with N / E / S / W and an orange tick at 12 o'clock marking direction of travel. Centre shows bearing in degrees. Cardinals localized for all six locales. First connect prompts for "While Using" location; declining leaves a placeholder dash.

- **Precondition chip merged with Heater Temp** — when active, shows the heater-temp sparkline with the current temperature as an orange pill, plus the "Time to 70°F / 21°C" ETA. The standalone Battery Heater Temp chip is gone.

### Settings → Units — new Power unit preference

kW (default), HP, or PS for the the Power chip on the Driving tab

### Settings → Keep Screen Awake

New toggle between Dashboard and History. Defaults to ON. When off, the device may dim or lock while the app is open — BLE polling, charging, and CarPlay continue in the background.

### CarPlay → Charging tab — row 1 redesigned around inlet-vs-pack power

DCFC active row 1 now reads SoC · Charging · Requested · Supplied · Pack Power · Pack · Timer with three side-by-side green sparklines:

- **Requested** — what the BMS asked the EVSE for.
- **Supplied** — what the EVSE is delivering at the inlet (matches the car's dashboard kW; runs ~10-12% higher than Pack Power because of inlet/contactor/cabling losses).
- **Pack Power** — what's entering the cells.

### CarPlay — tab switches redraw immediately

Tabs used to briefly show stale row images on switch. Each tab now clears its cache on entry.

### CarPlay — "Precondition" spelling unified

Was "Pre-Condition" on Driving/Charging tabs. Now matches the rest of the app.

### History → Sessions — driving sessions no longer span charging

When you stop to charge, your drive ends, the charging session runs, and a new drive begins after you unplug. The first drive ends on actual AC/DC charging start (preconditioning alone doesn't end a drive); the second starts when charging ends if ignition is still on.

### History → Sessions — status badges

All closed sessions now show a badge: Ignition Off (gray), Plugged In (teal), Unplugged (teal), BLE lost (orange), Recovered (gray), or Superseded (gray). Active sessions keep the green Active badge. Charging titles now read "DC Charge" / "AC Charge".

### History → Sessions — final charging SoC matches the car

Was up to 0.5% low. The endSOC is now overwritten by the next BMS sample within a 35-second finalize window after session close — latest-wins.

### History → Sessions — opening a live charging session is snappy

Per-poll writes used to cascade through the detail view and chart stack. The hero/stats sections are now their own subviews, so per-poll updates only re-render the small live numbers.

### History → Driving Session detail — hero handles short and live drives

New states: "Too short / Less than 1 mi tracked" for short drives that don't have enough data and "— / Drive in progress" while live. The Distance chip also shows "< 1 mi" instead of hiding.

---
## Build 79 — Session photo preview fix, Storage cap fix, Settings → History simplified, Dashboard localizations

NOTE TO TESTERS: 

### Session photo preview opens fit-to-screen

Tapping an attached photo in a History → Session detail used to open it zoomed-in, requiring pinch-out to see the whole image. The full-screen preview now opens at fit-to-screen; pinch / double-tap zooms in (up to 5×), drag pans while zoomed, pinch-out / double-tap resets.

### Storage cap fix

Fixed a bug that would have manifested if someone had a large data store, and selected a much smaller data cap that required a lot of data pruning.   The app would have appeared frozen for an extended period.  

### Settings → History — simplified

Simplified this secton.  The storage gauge above already communicates how much room History is using; the counters duplicated that while being the dominant source of UI stalls during eviction. The Delete All History button is now always enabled (a no-op on an empty store), and the confirmation sheet no longer shows record counts — just the slide-to-delete control to make sure someone really wants to delete all their data.

### Dashboard localization fixes

Thank you Gérald for the report of a number of missed localizations, fixed in build 79

### "Preconditioning" — spelled the same everywhere

The Dashboard had four labels variously rendered as "Pre-conditioning" / "Pre-Conditioning". All consumers now share one key spelled "Preconditioning" (one word, no hyphen) — translations already in place for all 6 locales.

---
## Build 78 — *New* Session photo + Session share sheet, DC EVSE chips + EVSE Current chart, IONIQ 9 cell-count fix

NOTE TO TESTERS: This build leans into making completed sessions feel like a finished story. Pick a photo, share a card, and (for DC charging) see the EVSE handshake spelled out.  Still building out the AC charging sheet - not done yet.  In my morning DC charging test today, the live/active session view (History / Sessions) was a bit slugglish.   I made some improvements to make it more snappy -- if you happen to run a DC charging session, please let me know if that issue is resolved.  

### *New* Photo per session

Open any completed driving or charging session and you'll see a 110pt photo slot next to the hero metric. Tap the empty box to pick a photo from your library; tap an existing photo to view it full-screen with Replace and Remove in the toolbar menu. Photos are downscaled to ~2000 px JPEG before storage so iCloud sync stays light, attached to the Session record, sync across your Apple devices, and cascade-delete with the session.

### *New* Share sheet for completed sessions

A share button now sits in the top-right of any completed driving or charging session. Tap to generate a branded JPEG report.  The headline uses charging-active duration (excludes preconditioning) so it reads as actual charge time rather than total session time. Active sessions don't show the button.

### DC charging session — EV Supply Equipment chips

History → Charging Session detail (DC) gets a new **EV Supply Equipment** card showing Max Power / Max Voltage / Max Current from the CCS handshake. Same labels and source data as the live Dashboard EVSE section and the CarPlay EVSE tab — now preserved in the history record so you can see what the charger advertised at handshake.

### DC charging session — EVSE Current chart

New **EVSE Current** chart plots Requested (BMS) vs. Delivered (VCMS) current on a shared axis, so the BMS's request curve and what the EVSE actually delivers can be eyeballed side-by-side throughout the charge.

### Charging session chart improvements

- **AC / DC bands gated by session type** — only the band matching the session's charge type is shown. Previously both rendered, with the irrelevant one as an empty strip.
- **EVSE Current chart** stops cleanly at the edges of each DC-charging window instead of bridging through preconditioning. Mirrors the gating used by Charging Power.
- **Charging Power dots** are now as dense as Pack Voltage samples. Linear interpolation between pack-current recordings fills the V × I pairing gaps with time-accurate estimates, instead of dropping most voltage samples.
- **Pack Voltage** and **Battery Temp** charts now auto-scale to the actual data range instead of starting at 0. The meaningful variation (e.g., 440–810 V, or 50–100 °F) is no longer compressed into the top fraction of the chart.

### IONIQ 9 — Battery Configuration chip stable

The Battery Configuration chip on the IONIQ 9 dashboard now locks to "168 series x 3 parallel" instead of flickering between 168, 169, and 170 as the BMS reported the same data different ways. Thanks to Sean for reporting this one!

---
## Build 77 — Brake Light polling 3x faster, Change to AC charging detection, Charging Session expanded, *New* History storage cap, iCloud sync fix

NOTE TO TESTERS: A lot has landed in Build 77.  The brake light now polls 3x faster - please let me know your polling headroom after this change.   AC charge detection:  Please let me know if you run into any issues with preconditioning or AC charge detection - there was a significant change for Hyundai vehicles that improves AC charge detection.  

### Brake light — 3× faster polling

Brake light polling rate increased 3× for closer-to-realtime behavior. Polling headroom drops ~6-10%.

### Fresh-install iCloud sync fix

Signal charts no longer stay empty after a fresh install on you iPhone, iPad or MAC -- view your data across all your Apple devices

### AC charge detection — harmonized across the fleet

AC charge detection now harmonized across all E-GMP vehicles.  V2L usages no longer mischaracterized as AC charging; end-of-AC-session detection is instantaneous instead of a 40-second delay.  Thanks to Kare in Norway ("the coffee bug") and the EV6 testers.

### Charging Session detail charts

Open any charging session from History → Sessions and you'll see a new chart stack below the SoC chart: Charging Power (cyan, V × I, gated to AC or DC active intervals so pre-charge driving is excluded), Ambient Temp, Pack Voltage, Battery Min/Max Temp (dual-line), AC Charging (yellow), DC Charging (green), Preconditioning (orange)

### History storage cap

Settings → History gets a "Maximum storage" picker (100 MB / 250 MB / 500 MB / 1 GB / 2 GB / 5 GB / Unlimited) plus a linear gauge with percent readout (blue → orange at 80% → red at 95%). When the on-disk total exceeds the cap, a background sweep deletes the oldest records first. Open sessions are never evicted. CloudKit propagates deletions to other devices.

### Three new History signals

History → Signals → Charging adds AC Charging, DC Charging, and Preconditioning as time-series signals. These power the new bands on the Charging Session view, and are tap-throughable in the Signals list.

### Driving session detail charts

Open any driving session — six new inline charts below the SoC chart: Speed, Distance Travelled, Brake Light (Gantt strip), Pack Current (regen-green / draw-red split), Cabin Temp, Cabin Humidity. Each hides itself if no samples were recorded.

### Driving session max speed fix

Completed drives now report peak speed correctly (Builds 71–76 showed "max 0 mph" regardless of actual speed; distance was correct). Forward-only fix; historical sessions stay at 0 mph but raw speed data is preserved on disk for a future backfill.

### Charging kWh added / Avg Power fix

Charging sessions that started before app connect now report kWh added and Avg Power correctly. 

### Driving session detail polish

SoC summary on driving sessions now reads end ← start (e.g., "51.0% ← 62.6%") with an SF Symbol left-arrow (mirrors in RTL locales). Charging keeps start → end. Uniform 1-decimal precision. VoiceOver labels added.

### J1979 crawl — confirmation alert

The J1979 Scanner's Start button now opens a confirmation alert before kicking off the crawl, warning that it pauses live polling and ends any in-progress session. Cancel is the default action.

### Lifetime Efficiency — new History signal

History → Signals → Battery adds a Lifetime Efficiency row tracking the round-trip efficiency value from the Dashboard's Battery Odometer card.

### CarPlay Battery Temp source

The CarPlay Battery Temp sparkline now reads from the BMS pack max/min temps, matching the Dashboard pack-temp chart and History "Battery Max/Min Temp".

---
## Build 76 — Snapshot detail views, polling polish, chart gap-band fix

NOTE TO TESTERS:  Some under the hood changes today -- please let me know if anythign new seems awry -- getting closer to Version 2.0 release

### Cell Voltages and Module Temperatures — full detail views

Cell Voltages (Snapshots) and Module Temperatures (Snapshots) in History → Signals now use the same full per-signal detail view as every other signal: hero value, lifetime stats grid, focus mode, multi-touch pan/zoom/scrub chart, time-range pills, and jump-to-prior/next nav. A new slider (with tick marks at module boundaries for cells) selects which channel to chart; the chart updates as you slide. Replaces the previous bare slider + dots view.

Titles read "Cell N Voltage" / "Module N Temp"; slider readouts read "Cell N" / "Module N". 1-indexed, no zero-padding.

### Battery snapshots — 3× the resolution

Cell voltages and module temperatures are now captured every 5 minutes during polling, up from every 15 minutes. 3× the data density on snapshot detail charts

### Polling loop wakes exactly when the next slot is due

The polling loop now wakes precisely when the next signal slot becomes due.

### Chart gap bands no longer paint over real data points

Two fixes to the History → Signals gap-band rendering: for legacy per-signal data whose timestamps don't align to V2 bucket boundaries, the band's left edge is now pulled in to the latest sample inside the gap region; the band's right edge is extended to align with the first actual reading in the next bucket. Closes a long-standing "blue dot drawn just inside the grey zone" issue most visible on the SoC (BMS) chart.

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
## Build 62 — Polling Paused state, diagnostic back-button guards, Curated Scan polish, Scan status panel change, updated brake light chip - App Store Version 1.1

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
## Build 52 — App rename and first-launch defaults polish — App Store Version 1.0

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
