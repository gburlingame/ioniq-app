---
layout: default
title: Support — Ioniq 5 Diagnostics
---

# Support

## Contact Us

For questions, bug reports, or feature requests, email us at [greg@theburl.com](mailto:greg@theburl.com). We typically respond within 24 hours.

You can also [open an issue on GitHub](https://github.com/gburlingame/ioniq-app/issues).

## Getting Started

1. **Plug in your OBD-II adapter** — Insert an ELM327-compatible Bluetooth LE adapter into your car's OBD-II port (usually below the dashboard on the driver's side)
2. **Open the app and scan** — Tap Scan to find your adapter. If it doesn't appear, tap "Filter by name" to show all nearby Bluetooth devices
3. **Start the car** — Turn on your Ioniq 5. The dashboard will begin populating with live data automatically
4. **Explore** — Swipe through the dashboard sections: Overview, Battery, Charging, Temperatures, and Tires

## Adapter Compatibility

The app works with any ELM327-compatible Bluetooth Low Energy (BLE) adapter. Tested adapters include:

* **Veepeak** — Most popular choice among testers
* **Carista** — Works well
* **Vgate** — Works well

**Important:** The adapter must be Bluetooth LE (not classic Bluetooth or Wi-Fi). Wi-Fi OBD adapters are not supported on iOS.

## CarPlay

CarPlay support is automatic — when your iPhone is connected to CarPlay and the app is running, you'll see Driving and Charging tabs in the CarPlay interface with live-updating data.

## Capturing Diagnostics

If you're experiencing connection issues or unexpected behavior:

1. Go to **Settings** and tap the **Build** number **5 times** to enable the hidden Diagnostics section
2. Tap **Start Recording Diagnostics**
3. Reproduce the issue (connect to adapter, drive, etc.)
4. Tap **Stop**, then **Share Diagnostics** to send the log

## Frequently Asked Questions

**Q: Which OBD-II adapters work with this app?**
A: Any ELM327-compatible Bluetooth LE adapter. We recommend the Veepeak OBDCheck BLE+. Make sure it's Bluetooth, not Wi-Fi.

**Q: My adapter isn't connecting.**
A: Close any other OBD apps (Torque, Car Scanner, Carista, etc.) — ELM327 adapters only allow one connection at a time. If that doesn't help, unplug the adapter from the OBD port, wait 10 seconds, and plug it back in.

**Q: Which Ioniq 5 models are supported?**
A: All model years and all variants (Standard Range, Long Range, AWD, RWD, Project 45) are supported.

**Q: Does it work with the Ioniq 6 or Ioniq 9?**
A: We're starting with the Ioniq 5 to build a great experience there first. Support for other Ioniq models is planned — if you'd like to help test, reach out.

**Q: How does CarPlay work?**
A: Connect your iPhone to CarPlay as usual. The app appears automatically with Driving and Charging tabs showing live data.

**Q: How do I capture a diagnostic log?**
A: See the "Capturing Diagnostics" section above. Enable the hidden Diagnostics section by tapping the Build number 5 times in Settings.

**Q: Will the adapter drain my 12V battery?**
A: The adapter draws a small amount of power from the 12V battery when plugged in. The app sends an unplug reminder notification when the car turns off. We recommend unplugging the adapter when not in use.

## Links

* [Ioniq 5 Diagnostics Home](.)
* [Privacy Policy](privacy)
