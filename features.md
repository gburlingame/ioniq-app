---
layout: default
title: Features
nav_order: 1
---

# EV Dashboard

A real-time diagnostics app for the Hyundai, Kia, and Genesis E-GMP family. Connect an ELM327-compatible Bluetooth OBD-II adapter to monitor your battery, charging sessions, temperatures, and more — right from your iPhone or CarPlay.

## Features

### CarPlay

* **Driving page** — Two rows of live chips: pack state of charge, pack power, range, cell delta, 12V state, motor RPM, headlights, odometer — and tire pressures, climate, preconditioning, battery heater, battery temperature, regen power, brake light, nearest DC charger
* **Customize Tiles** — *New in Version 3.0:* Choose which of the 20 tiles appear and where they sit, with separate full-screen (2×8) and split-screen (2×4) layouts
* **Help for every tile** — *New in Version 3.0:* Each tile on your layout has its own authored Help page, illustrated with the live tile itself
* **Status page** — Connection state, ECU scan status, and polling headroom, available any time
* **Dynamic Charging page** — Appears on its own when a charging session begins
* **Apple Dashboard** — A live charger map with two tiles of your choosing beside it
* **Compass** — Driven by your car's own heading; tap it for a full-screen heading
* **Tire-pressure tile** — Pressure and temperature
* **12V chip** — State of charge, voltage, and current

### Chargers and navigation

* **DC fast-charge finder** — Roughly 60,000 sites, bundled with the app and searchable without a network connection
* **Data worth trusting** — U.S. and Canadian sites come straight from the U.S. DOE / NRCan Alternative Fuels Data Center; Open Charge Map covers the rest of the world. Stations only Teslas can use are excluded
* **Filters that apply instantly** — By minimum speed (≥50kW and up) and by charging network, anywhere in the world
* **Turn-by-turn navigation** — Route to a charger or a searched address, talked through every turn in a voice you pick
* **Saved destinations** — Keep the places you come back to
* **Estimated arrival SoC** — Your projected state of charge on arrival, averaged over recent projections so it settles instead of jumping
* **Updates without an App Store release** — Settings → Navigation → Check for Update swaps in a newer charger database in place

### Range and efficiency

* **Live range estimate** — Fed by a long-term efficiency average, so the number stays steady instead of swinging with the last hill
* **Recent-efficiency trend** — The smaller figure beneath the range tracks your recent driving instead
* **The whole method is published** — See [How Range and Efficiency Are Calculated](efficiency-and-range) for every formula worked out

### Charging telemetry

* **Live AC and DC charging detection** — Read from the vehicle's own charge-type flags
* **Three-phase AC power** — Measured per phase, so three-phase supplies read correctly
* **EVSE max voltage / current / power** — J1772 + CCS
* **Control Pilot duty cycle** — The EVSE's advertised max-current capability
* **ICCU input voltage and AC current**

### Preconditioning readiness ETA

* **Live "Time to 70°F / 21°C" battery-temperature ETA** — When your pack will be ready for optimal DC fast charging
* **On the Dashboard and in CarPlay** — Including the Driving page, so you can watch it the whole drive to the station

### Live Dashboard

* **State of charge, available energy, voltage, current**
* **Battery cell min/max temperature**
* **Battery cell voltages**
* **Module temperature grid** — Per-sensor pack temperatures with min/avg/max/delta
* **Battery temperature charts** — Time series history of BMS max/min, heater, and coolant inlet temperatures
* **Battery heater status during preconditioning**
* **Battery Odometer** — Lifetime energy charged vs. discharged with round-trip efficiency percentage
* **Battery Health** — BMS-reported State of Health with explanatory info
* **Tire pressures and temperatures**
* **Motor RPM, gear position, ignition state**
* **Regenerative braking dial** — Live regen power against the available ceiling and the pack's peak power
* **12V auxiliary battery** — State of charge, voltage, current, temperature, plus DC-DC converter telemetry
* **Outside and cabin temperature, relative humidity**
* **Indicators for headlights** (low and high beams) and brake lights
* **Isolation resistance and polling headroom** — With explanatory info
* **Connection Report** — Which modules are reporting, the adapter's name, firmware and protocol, polling statistics, per-module coverage, and a timeline of connects and drop-outs — exportable as CSV
* **ICCU details share card** — VIN-redacted share sheet for easy sharing

### History and iCloud

* **Charging sessions** — Every charge recorded automatically: peak power, energy added, duration, EVSE max voltage / current / power, and a full set of charts
* **Driving sessions** — Distance, max and average speed, energy used, and net efficiency, with speed, current, state-of-charge, and gear charts
* **Signal history** — Long-term time-series for every recorded signal, with tap-through charts spanning your whole recording history
* **Session photos** — Attach a photo to any session
* **Share a session** — Export any session as an image, charts and all
* **iCloud sync** — Sessions, signals, and photos sync across your iPhone, iPad, and other Apple devices

### Inspect

* **J1979 OBD-II Scanner** — Standard mode 01–09 read-out for adapter compatibility checking
* **Enhanced DTC Scan** — Manufacturer-specific trouble codes from every module the car exposes, with modules identified by name
* **Share or export any scan** — As an image, or as a CSV carrying a metadata header and one row per code
* **DTC reassurance** — Known-benign permanent codes (e.g. P0C17) come with a contextual explanation rather than an alarm

### Advanced Tools

Powerful tools to help enthusiasts learn more about their vehicles, with result sharing built in.

* **DID Range Scan** — Probe a single ECU across an address range to find which DIDs respond
* **ECU Finder** — A full scan to find all the ECUs your vehicle exposes
* **Curated DID List** — An in-depth scan of a single ECU across all 65535 addresses, with `.iqlist` sharing between testers
* **ABC test** — Use the curated list to hunt for interesting new signals
* **Adapter interference detection** — The app notices when another OBD-II app takes over the shared adapter; Adapter Quiet Check confirms it on demand
* **Full diagnostic recording** — Capture sessions for later analysis

### Settings and customization

* **Themes** — Eight palettes, chosen separately for the app and for CarPlay
* **Units your way** — Independent preferences for temperature, distance, speed, pressure, power, and efficiency
* **Appearance** — Auto, Light, or Dark
* **Reorder the Dashboard** — Drag sections into the order you want, or hide the ones you don't use
* **Auto-Connect** — Reconnect to your adapter automatically on launch and after drops
* **Keep Screen Awake** — Keep recording without the screen dimming or locking
* **Quick Look for `.iqlist` files** — Preview a shared curated DID list before importing it

### Languages and notifications

* **Multi-language support** — Deutsch, English, Español, Français, Italiano, Nederlands, Svenska, Türkçe, 日本語, 한국어, with an in-app language picker
* **Unplug reminder** — Notification when the car turns off reminding you to unplug the adapter
* **OBD-II adapter compatibility** — Works with inexpensive, popular brand name ELM327-compatible Bluetooth LE adapters

## Supported vehicles

The app ships per-vehicle registries with verified full support for:

* **IONIQ 5**
* **IONIQ 5 N**
* **IONIQ 6**
* **IONIQ 9**
* **Kia EV6**
* **Kia EV6 GT**
* **Kia EV9**
* **Kia EV3**
* **Genesis GV60**

## Support

If you have a question, found a bug, or want to request a feature, please [open an issue](https://github.com/gburlingame/ioniq-app/issues) on GitHub.

## Links

* [Should I Unplug My OBD-II Adapter?](unplugging-your-adapter)
* [Why Some Features Are Hard](why-some-features-are-hard)
* [Privacy Policy](privacy)
* [Support](support)
* [Version History](versions)
