---
layout: default
title: Support
nav_order: 2
---

# Support

## Contact Us

For questions, bug reports, or feature requests, email us at [greg@theburl.com](mailto:greg@theburl.com). We typically respond within 24 hours.

You can also [open an issue on GitHub](https://github.com/gburlingame/ioniq-app/issues).

## Getting Started

1. **Plug in your OBD-II adapter** — Insert an ELM327-compatible Bluetooth LE adapter into your car's OBD-II port (usually below the dashboard on the driver's side)
2. **Open the app and scan** — Tap Scan to find your adapter. If it doesn't appear, tap "Filter by name" to show all nearby Bluetooth devices
3. **Start the car** — Turn on your vehicle. The dashboard will begin populating with live data automatically
4. **Explore** — Swipe through the dashboard sections: Overview, Battery, Charging, Temperatures, and Tires

## Adapter Compatibility

The app works with any ELM327-compatible Bluetooth Low Energy (BLE) adapter. Tested adapters include:

* **Veepeak OBDCheck BLE**
* **VGate vLinker MC+**
* **Vgate iCar Pro**
* **OBDLink CX**
* **Carista**

**Important:** The adapter must be Bluetooth LE (not classic Bluetooth or Wi-Fi). 

## CarPlay

CarPlay support is automatic — when your iPhone is connected to CarPlay and the app is running, you'll see Driving, Charging, and (during charging) EVSE tabs in the CarPlay interface with live-updating data.

## Capturing Diagnostics

If you're experiencing connection issues or unexpected behavior:

1. Go to **Settings** and tap **Start Recording Diagnostics**
2. Reproduce the issue (connect to adapter, drive, etc.)
3. Tap **Stop**, then **Share Diagnostics** to send the log to the developer

## Frequently Asked Questions

**Q: Which OBD-II adapters work with this app?**
A: Any ELM327-compatible Bluetooth LE adapter. Make sure it's Bluetooth Low Energy (BLE), and not classic Bluetooth or Wi-Fi.

**Q: My adapter isn't connecting.**
A:   First, verify that you are using a ELM327-compatible Bluetooth LE adapter.  Next, check to make sure that Bluetooth permissions are enabled for IONIQ 5 Companion.  Check Settings / Apps / IONIQ 5 Companion.  If you continue to have trouble connecting, please reach out to the developer.

**Q: The BLE connection keeps disconnecting.**
A:  Check to make sure that no other OBD-II apps (like Car Scanner, Torq, or ABRP) are running in the background. IONIQ 5 Companion and these other apps can only be run one at a time.  If you are not sure if another app is running, you can use the Adapter Quiet Check Feature.   This will run a one minute diagnostic check to verify that no other apps are running.  Settings / Diagnostics / Adapter Quiet Check.  After checking, if you still have a problem, please reach out to the developer for support.

**Q: Which vehicles are supported?**
A: The IONIQ 5 (RWD SR/LR and AWD LR, model years 2024–2026), the IONIQ 5 N (2025), the IONIQ 6 (RWD SR/LR and AWD LR, model years 2023–2024), and the IONIQ 9 (2026). See the [home page](.) for the up-to-date list.

**Q: How does CarPlay work?**
A: Connect your iPhone to CarPlay as usual. The app appears automatically with Driving, Charging, and (during charging) EVSE tabs showing live data.

**Q: How do I capture a diagnostic log?**
A: See the "Capturing Diagnostics" section above. 

**Q: Will the adapter drain my 12V battery?**
A: Probably not in the dramatic "your car won't start" sense — your IONIQ has a DC-DC converter that quietly tops the 12V back up from the high-voltage traction battery whenever it dips. The more honest concern is wear: continuous accessory draw causes extra charge cycling on the 12V battery and shortens its life over time. See [Should I Unplug My OBD-II Adapter?](unplugging-your-adapter) for the full breakdown, including a switched-extension-cable middle path and what the app does on its end to keep the polling cadence quiet when the car is off.

## Links

* [IONIQ 5 Companion Home](.)
* [Privacy Policy](privacy)
* [Version History](versions)
