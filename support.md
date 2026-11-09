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

1. **Plug in your OBD-II adapter** — Insert a supported Bluetooth OBD-II adapter (see [Adapter Compatibility](#adapter-compatibility)) into your car's OBD-II port (usually below the dashboard on the driver's side)
2. **Open the app and scan** — Tap Scan to find your adapter. If it doesn't appear, tap "Filter by name" to show all nearby Bluetooth devices
3. **Start the car** — Turn on your vehicle. The dashboard will begin populating with live data automatically
4. **Explore** — Swipe through the dashboard sections — Overview, Battery, Charging, Temperatures, Tires, and more. Visit the **History** tab to see your recorded charging and driving sessions

## Adapter Compatibility

EV Dashboard works with all popular brand name ELM327-compatible Bluetooth Low Energy (BLE) adapters, and with three Bluetooth Classic adapters: the OBDLink MX+, the Vgate vLinker FS, and the Vgate vLinker MS.

These adapters have been tested and verified to work with EV Dashboard:

* **Vgate vLinker MC+**
* **Vgate iCar Pro 2S**
* **Veepeak OBDCheck BLE**
* **OBDLink CX**
* **Carista**
* **OBDLink MX+** (Bluetooth Classic)
* **Vgate vLinker FS** (Bluetooth Classic)

**Bluetooth Classic adapters** don't appear in the app's Bluetooth scan until they're paired. Pair the OBDLink MX+, Vgate vLinker FS, or Vgate vLinker MS once in **iOS Settings → Bluetooth**; it then appears in the app's adapter list labeled "Bluetooth Classic". Only one app at a time can use a Bluetooth Classic adapter, so close any other OBD app first.

**Not compatible:** Wi-Fi adapters, and Bluetooth Classic adapters other than the three named above.

**Important:**  The developer already bought and tested a blue-colored semi-translucent adapter labeled ELM327.  This was purchased on Amazon for approximately $5 USD and was found to be incompatible with EV Dashboard.  

## CarPlay

CarPlay support is automatic — when your iPhone is connected to CarPlay and the app is running, you'll see Driving and Status pages with live-updating data, plus a Charging page that appears on its own when a session begins. The Status page shows connection state, ECU scan status, and polling headroom.

## Capturing Diagnostics

If you're experiencing connection issues or unexpected behavior:

1. Go to **Settings / Diagnostics** and tap **Start Recording Diagnostics**
2. Reproduce the issue (connect to adapter, drive, etc.)
3. Tap **Stop**, then **Share Diagnostics** to send the log to the developer

## Unplug Reminder Notifications

The app sends a notification reminding you to unplug the OBD-II adapter when your car turns off. If you're not seeing this notification, check the following:

1. **In-app setting** — Go to Settings and make sure **Unplug Reminder** is turned on
2. **iOS notification permissions** — Go to iOS Settings → Notifications → EV Dashboard and make sure **Allow Notifications** is enabled
3. **Focus mode** — If you're using a Focus mode (Do Not Disturb, Driving, etc.), notifications may be silenced. Check iOS Settings → Focus to see if the app is allowed
4. **Notification style** — In iOS Settings → Notifications → EV Dashboard, make sure **Banners** or **Alerts** is selected (not "None")
5. **Low Power Mode** — iOS may delay or suppress notifications when in Low Power Mode
6. **The car must actually turn off** — The reminder triggers when the app detects the ignition switching off. If you disconnect the adapter before turning off the car, the notification won't fire

## History and iCloud

The app records your charging and driving sessions and long-term signal history in the **History** tab, and can sync them across your Apple devices.

* **First launch after updating** — The first time you open the app after a History update, you may briefly see "Building local index" in History → Signals while a one-time index upgrade runs. Let it finish; once it's done, opening individual signals is fast.
* **iCloud sync** — To sync your history across your iPhone, iPad, and other devices, go to **Settings → History** and turn on **iCloud Sync**. Sessions, signals, and any photos you've attached sync automatically. If iCloud is unavailable, the app will let you know.
* **Purging history** — To clear your recorded history, use the purge option in **Settings → History**. This is permanent.

## Frequently Asked Questions

**Q: Which OBD-II adapters work with this app?**  
A: Any popular brand name ELM327-compatible Bluetooth LE adapter, plus three Bluetooth Classic adapters: the OBDLink MX+, the Vgate vLinker FS, and the Vgate vLinker MS. Wi-Fi adapters don't work.

**Q: My adapter isn't connecting.**  
A: First, verify that you are using a supported adapter (see [Adapter Compatibility](#adapter-compatibility)). An OBDLink MX+, Vgate vLinker FS, or Vgate vLinker MS must be paired in iOS Settings → Bluetooth before the app can see it.  Next, check to make sure that Bluetooth permissions are enabled for EV Dashboard.  Check Settings / Apps / EV Dashboard.  If you continue to have trouble connecting, please reach out to the developer.

**Q: The BLE connection keeps disconnecting.**  
A: Check to make sure that no other OBD-II apps (like Car Scanner, Torq, or ABRP) are running in the background. EV Dashboard and these other apps can only be run one at a time.  If you are not sure if another app is running, you can use the Adapter Quiet Check Feature.   This will run a one minute diagnostic check to verify that no other apps are running.  Settings / Diagnostics / Adapter Quiet Check.  After checking, if you still have a problem, please reach out to the developer for support.

**Q: My recorded sessions have gaps.**  
A: When your device dims or locks, iOS may suspend the app between polls, which leaves gaps in the recording. To record continuously while you're watching, turn on **Keep Screen Awake** in Settings. With it off, your device may dim or lock and recording will pause until the app resumes.

**Q: Which vehicles are supported?**  
A: See the [home page](.) for the most up-to-date list.

**Q: How does CarPlay work?**  
A: Connect your iPhone to CarPlay as usual. The app appears automatically with Driving and Status pages showing live data, plus a Charging page that appears when a session begins.

**Q: How do I capture a diagnostic log?**  
A: See the "Capturing Diagnostics" section above.

**Q: Will the adapter drain my 12V battery?**  
A: Probably not in the dramatic "your car won't start" sense — your IONIQ has a DC-DC converter that quietly tops the 12V back up from the high-voltage traction battery whenever it dips. The more honest concern is wear: continuous accessory draw causes extra charge cycling on the 12V battery and shortens its life over time. See [Should I Unplug My OBD-II Adapter?](unplugging-your-adapter) for the full breakdown, including a switched-extension-cable middle path and what the app does on its end to keep the polling cadence quiet when the car is off.

## Links

* [EV Dashboard Home](.)
* [Privacy Policy](privacy)
* [Version History](versions)
