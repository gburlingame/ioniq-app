---
layout: default
title: Home
nav_order: 1
---

# IONIQ 5 Companion

A real-time diagnostics app for the Hyundai IONIQ family. Connect an ELM327-compatible Bluetooth OBD-II adapter to monitor your battery, charging sessions, temperatures, and more — right from your iPhone or CarPlay.

## Features

* **Real-time battery monitoring** — State of charge, pack voltage, current, and power updated every 3 seconds
* **Per-cell voltage grid** — Color-coded cell health visualization with min/max/avg/delta statistics
* **Battery temperature charts** — Time series history of BMS max/min, heater, and coolant inlet temperatures
* **Battery Odometer** — Lifetime energy charged vs. discharged with round-trip efficiency percentage
* **Battery Health** — BMS-reported State of Health with explanatory info
* **12V (auxiliary) battery panel** — State of charge, voltage, current, and temperature for the 12V battery, plus DC-DC converter temperature, output voltage, output current, and HV pack input voltage
* **Charging session monitoring** — Real-time power, voltage, current, SoC, and elapsed time during AC and DC charging, with EVSE info (max voltage, max current, present voltage/current, max power, Control Pilot duty cycle)
* **Tire pressure and temperature** — All four tires with color-coded pressure ranges
* **Outside temperature** — Ambient air temperature from the vehicle's sensor
* **Dashboard status chips** — Pre-conditioning (with ETA), Battery Heater, brake light indicator (configurable), headlights, and motor RPM
* **CarPlay integration** — Driving, Charging, and EVSE tabs with live-updating gauges, sparklines, and data chips
* **Multi-language support** — English, Nederlands, Deutsch, Español, Français, Svenska with in-app language picker
* **OBD-II adapter compatibility** — Works with ELM327-compatible Bluetooth LE adapters (Veepeak, Carista, OBDLink CX, vLinker MC-IOS, and others)
* **Unplug reminder** — Notification when the car turns off reminding you to unplug the adapter
* **Advanced Diagnostics** — Hidden behind a 5-tap unlock in Settings: ECU scans, J1979 DTC scans with reassurance for known-benign codes (e.g. P0C17), Curated DID Scans with `.iqlist` sharing between testers, A-B-C Snapshots for discovering new sensor signals, Adapter Quiet Check for detecting foreign-app interference on the shared BLE adapter, and full diagnostic recording

## Supported vehicles

The app ships per-vehicle registries covering:

* **IONIQ 5** — RWD SR/LR and AWD LR, model years 2024–2026
* **IONIQ 5 N** — model year 2025
* **IONIQ 6** — RWD SR/LR and AWD LR, model years 2023–2024
* **IONIQ 9** — model year 2026

## Support

If you have a question, found a bug, or want to request a feature, please [open an issue](https://github.com/gburlingame/ioniq-app/issues) on GitHub.

## Links

* [Should I Unplug My OBD-II Adapter?](unplugging-your-adapter)
* [Why Some Features Are Hard](why-some-features-are-hard)
* [Privacy Policy](privacy)
* [Support](support)
* [Version History](versions)
