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
4. **Explore** — Swipe through the dashboard sections — Overview, Battery, Charging, Temperatures, Tires, and more. Visit the **History** tab to see your recorded charging and driving sessions

## Adapter Compatibility

IONIQ 5 Companion works with any ELM327-compatible Bluetooth Low Energy (BLE) adapter. The adapter must be Bluetooth LE (not classic Bluetooth or Wi-Fi).  

These adapter have been tested and verified to work with IONIQ 5 Companion:

* **Vgate vLinker MC+**
* **Vgate iCar Pro 2S**
* **Veepeak OBDCheck BLE**
* **OBDLink CX**
* **Carista**

**Not compatible:** Wi-Fi adapters, and any *Classic Bluetooth* adapter — including the **OBDLink MX+**. The app connects over Bluetooth Low Energy only. Note that OBDLink's BLE model, the **OBDLink CX**, is fully supported (listed above).

**Important:**  The developer already bought and tested a blue-colored semi-translucent adapter labeled ELM327.  This was purchased on Amazon for approximately $5 USD and was found to be incompatible with IONIQ 5 Companion.  

## CarPlay

CarPlay support is automatic — when your iPhone is connected to CarPlay and the app is running, you'll see Driving, Charging, a Status tab, and (during charging) an EVSE tab in the CarPlay interface with live-updating data. The Status tab shows connection state, ECU scan status, and adapter details when the car is parked.

## Capturing Diagnostics

If you're experiencing connection issues or unexpected behavior:

1. Go to **Settings / Diagnostics** and tap **Start Recording Diagnostics**
2. Reproduce the issue (connect to adapter, drive, etc.)
3. Tap **Stop**, then **Share Diagnostics** to send the log to the developer

## Unplug Reminder Notifications

The app sends a notification reminding you to unplug the OBD-II adapter when your car turns off. If you're not seeing this notification, check the following:

1. **In-app setting** — Go to Settings and make sure **Unplug Reminder** is turned on
2. **iOS notification permissions** — Go to iOS Settings → Notifications → IONIQ 5 Companion and make sure **Allow Notifications** is enabled
3. **Focus mode** — If you're using a Focus mode (Do Not Disturb, Driving, etc.), notifications may be silenced. Check iOS Settings → Focus to see if the app is allowed
4. **Notification style** — In iOS Settings → Notifications → IONIQ 5 Companion, make sure **Banners** or **Alerts** is selected (not "None")
5. **Low Power Mode** — iOS may delay or suppress notifications when in Low Power Mode
6. **The car must actually turn off** — The reminder triggers when the app detects the ignition switching off. If you disconnect the adapter before turning off the car, the notification won't fire

## History and iCloud

The app records your charging and driving sessions and long-term signal history in the **History** tab, and can sync them across your Apple devices.

* **First launch after updating** — The first time you open the app after a History update, you may briefly see "Building local index" in History → Signals while a one-time index upgrade runs. Let it finish; once it's done, opening individual signals is fast.
* **iCloud sync** — To sync your history across your iPhone, iPad, and other devices, go to **Settings → History** and turn on **iCloud Sync**. Sessions, signals, and any photos you've attached sync automatically. If iCloud is unavailable, the app will let you know.
* **Purging history** — To clear your recorded history, use the purge option in **Settings → History**. This is permanent.

## Frequently Asked Questions

**Q: Which OBD-II adapters work with this app?**  
A: Any ELM327-compatible Bluetooth LE adapter. Make sure it's Bluetooth Low Energy (BLE), and not classic Bluetooth or Wi-Fi.

**Q: My adapter isn't connecting.**  
A: First, verify that you are using a ELM327-compatible Bluetooth LE adapter.  Next, check to make sure that Bluetooth permissions are enabled for IONIQ 5 Companion.  Check Settings / Apps / IONIQ 5 Companion.  If you continue to have trouble connecting, please reach out to the developer.

**Q: The BLE connection keeps disconnecting.**  
A: Check to make sure that no other OBD-II apps (like Car Scanner, Torq, or ABRP) are running in the background. IONIQ 5 Companion and these other apps can only be run one at a time.  If you are not sure if another app is running, you can use the Adapter Quiet Check Feature.   This will run a one minute diagnostic check to verify that no other apps are running.  Settings / Diagnostics / Adapter Quiet Check.  After checking, if you still have a problem, please reach out to the developer for support.

**Q: My recorded sessions have gaps.**  
A: When your device dims or locks, iOS may suspend the app between polls, which leaves gaps in the recording. To record continuously while you're watching, turn on **Keep Screen Awake** in Settings. With it off, your device may dim or lock and recording will pause until the app resumes.

**Q: Which vehicles are supported?**  
A: See the [home page](.) for the most up-to-date list.

**Q: How does CarPlay work?**  
A: Connect your iPhone to CarPlay as usual. The app appears automatically with Driving, Charging, Status, and (during charging) EVSE tabs showing live data.

**Q: How do I capture a diagnostic log?**  
A: See the "Capturing Diagnostics" section above.

**Q: Will the adapter drain my 12V battery?**  
A: Probably not in the dramatic "your car won't start" sense — your IONIQ has a DC-DC converter that quietly tops the 12V back up from the high-voltage traction battery whenever it dips. The more honest concern is wear: continuous accessory draw causes extra charge cycling on the 12V battery and shortens its life over time. See [Should I Unplug My OBD-II Adapter?](unplugging-your-adapter) for the full breakdown, including a switched-extension-cable middle path and what the app does on its end to keep the polling cadence quiet when the car is off.

## Links

* [IONIQ 5 Companion Home](.)
* [Privacy Policy](privacy)
* [Version History](versions)
