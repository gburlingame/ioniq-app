---
layout: default
title: Version History — Ioniq 5 Diagnostics
---

# Version History

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
