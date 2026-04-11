---
layout: default
title: Version History
nav_order: 4
---

# Version History

---
## Build 27 — Training reliability, Scan Status dark mode fix, CarPlay Scan Status grouping

### Fix: ECU Training Reliability

The startup ECU scan occasionally failed to detect the VCMS (charging system) and other ECUs, especially when CarPlay was connected. Multiple improvements:

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
