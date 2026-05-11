---
layout: default
title: Home
nav_order: 1
---

# IONIQ 5 Companion

A real-time diagnostics app for the Hyundai IONIQ family. Connect an ELM327-compatible Bluetooth OBD-II adapter to monitor your battery, charging sessions, temperatures, and more — right from your iPhone or CarPlay.

## Features

### CarPlay

* **Driving tab** — Two rows of live chips: pack state of charge, pack power, odometer, 12V state, cell delta, motor RPM, headlights — and tire pressures, climate, preconditioning, battery heater, battery temperature, brake light
* **Tire-pressure tile** — Pressure and temperature
* **12V chip** — State of charge, voltage, and current
* **Dynamic Charging tab** — Appears during EVSE sessions, with a session timer to keep track of your charge time at a quick glance
* **Dynamic EVSE tab** — Appears during charging with session details — see what capabilities the EVSE has communicated to your vehicle

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
* **Battery temperature charts** — Time series history of BMS max/min, heater, and coolant inlet temperatures
* **Battery heater status during preconditioning**
* **Battery Odometer** — Lifetime energy charged vs. discharged with round-trip efficiency percentage
* **Battery Health** — BMS-reported State of Health with explanatory info
* **Tire pressures and temperatures**
* **Motor RPM, ignition state**
* **12V auxiliary battery** — State of charge, voltage, current, temperature, plus DC-DC converter telemetry
* **Outside and cabin temperature, relative humidity**
* **Indicators for headlights** (low and high beams) and brake lights
* **ICCU details share card** — VIN-redacted share sheet for easy sharing

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

### Languages and notifications

* **Multi-language support** — English, Nederlands, Deutsch, Español, Français, Svenska, with an in-app language picker
* **Unplug reminder** — Notification when the car turns off reminding you to unplug the adapter
* **OBD-II adapter compatibility** — Works with inexpensive ELM327-compatible Bluetooth LE adapters

## Supported vehicles

The app ships per-vehicle registries with full or partial coverage:

**Verfified Full Support**

* **IONIQ 5** — model years 2022–2026
* **IONIQ 5 N** — model year 2025

**Partial support**

* **IONIQ 6** — model years 2023–2025
* **IONIQ 9** — model year 2026

**Under construction**

* **Genesis GV60** - model years 2021-2025

## Support

If you have a question, found a bug, or want to request a feature, please [open an issue](https://github.com/gburlingame/ioniq-app/issues) on GitHub.

## Links

* [Should I Unplug My OBD-II Adapter?](unplugging-your-adapter)
* [Why Some Features Are Hard](why-some-features-are-hard)
* [Privacy Policy](privacy)
* [Support](support)
* [Version History](versions)
