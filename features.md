---
layout: default
title: Features
nav_order: 1
---

# EV Dashboard

A real-time diagnostics app for the Hyundai, Kia, and Genesis E-GMP family. Connect an ELM327-compatible Bluetooth OBD-II adapter to monitor your battery, charging sessions, temperatures, and more — right from your iPhone or CarPlay.

## Features

### CarPlay

* **Driving tab** — Two rows of live chips: pack state of charge, pack power, odometer, 12V state, cell delta, motor RPM, headlights — and tire pressures, climate, preconditioning, battery heater, battery temperature, regen power, brake light
* **Tire-pressure tile** — Pressure and temperature
* **12V chip** — State of charge, voltage, and current
* **Compass** — A live compass tile; tap it for a full-screen heading
* **Customize Tiles** — *New in Version 3.0:* Choose which tiles are visible and where they sit, with separate full-screen and split-screen layouts
* **Status page** — Connection state, ECU scan status, and polling headroom, available any time
* **Dynamic Charging page** — Appears on its own when a charging session begins

### Charging telemetry

* **Live AC and DC charging detection**
* **EVSE max voltage / current / power** — J1772 + CCS
* **Control Pilot duty cycle** — The EVSE's advertised max-current capability
* **ICCU input voltage and AC current**

### Preconditioning readiness ETA

* **Live "Time to 70°F / 21°C" battery-temperature ETA** — When your pack will be ready for optimal DC fast charging
* **Visible on the Dashboard and as a CarPlay chip during preconditioning** — Now also visible on the Driving tab for the drive to the station

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
* **ECU scan status** — See which of your vehicle's modules are responding
* **ICCU details share card** — VIN-redacted share sheet for easy sharing

### History and iCloud

* **Charging sessions** — Every charge recorded automatically: peak power, energy added, duration, EVSE max voltage / current / power, and a full set of charts
* **Driving sessions** — Distance, max and average speed, energy used, and net efficiency, with speed, current, state-of-charge, and gear charts
* **Signal history** — Long-term time-series for every recorded signal, with tap-through charts spanning your whole recording history
* **Session photos** — Attach a photo to any session
* **Share a session** — Export any session as an image, charts and all
* **iCloud sync** — Sessions, signals, and photos sync across your iPhone, iPad, and other Apple devices

### Inspect

* **J1979 OBD-II Scanner** — Standard mode 01-09 read-out for adapter compatibility checking
* **DTC reassurance** — Known-benign permanent codes (e.g. P0C17) come with a contextual explanation rather than an alarm

### Advanced Tools

Powerful tools to help enthusiasts learn more about their vehicles, with result sharing built in.

* **DID Range Scan** — Probe a single ECU across an address range to find which DIDs respond
* **ECU Finder** — A full scan to find all the ECUs your vehicle exposes
* **Curated DID List** — An in-depth scan of a single ECU across all 65535 addresses, with `.iqlist` sharing between testers
* **ABC test** — Use the curated list to hunt for interesting new signals
* **Adapter Quiet Check** — Detect foreign-app interference on the shared BLE adapter
* **Full diagnostic recording** — Capture sessions for later analysis

### Settings and customization

* **Units your way** — Independent preferences for temperature, distance, speed, pressure, power, and efficiency
* **Appearance** — Auto, Light, or Dark
* **Reorder the Dashboard** — Drag sections into the order you want, or hide the ones you don't use
* **Auto-Connect** — Reconnect to your adapter automatically on launch and after drops
* **Keep Screen Awake** — Keep recording without the screen dimming or locking
* **Quick Look for `.iqlist` files** — Preview a shared curated DID list before importing it

### Languages and notifications

* **Multi-language support** — Deutsch, English, Español, Français, Italiano, Nederlands, Svenska, Türkçe, 한국어, with an in-app language picker
* **Unplug reminder** — Notification when the car turns off reminding you to unplug the adapter
* **OBD-II adapter compatibility** — Works with inexpensive ELM327-compatible Bluetooth LE adapters

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
