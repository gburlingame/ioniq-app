---
layout: default
title: Tester Guide
nav_order: 5
---

# Tester Guide: Capturing Diagnostics

## Before You Start

**Close any other OBD apps** (Torque, Car Scanner, Carista, etc.) before using this app. ELM327 adapters only allow one active connection at a time — if another app is connected, the adapter will appear to connect but won't respond to commands.

If you're having connection issues, this is the first thing to check.

## Enabling the Hidden Diagnostics Menu

1. Open the app and go to the **Settings** tab
2. Scroll down to the **About** section
3. Tap the **Build** number **5 times** quickly
4. A prompt will appear asking to "Enable Diagnostics" — tap **Enable**
5. Two new sections will appear at the bottom of Settings: **Diagnostics** and **Advanced Diagnostics**

To hide them again later, tap the Build number 5 times again.

## Capturing a Diagnostic Log

Use this when you're experiencing connection issues, unexpected behavior, or when asked by the developer to capture a log.

1. Go to **Settings** and scroll to the **Diagnostics** section
2. Tap **Start Recording Diagnostics** — a red recording indicator will appear
3. **Now use the app normally** — connect to your adapter, drive, reproduce the issue you're reporting
4. When done, tap **Stop**
5. Tap **Share Diagnostics** and send the file (via Messages, email, AirDrop, etc.)

**Tip for connection issues:** Start recording *before* you connect to the adapter. The log will capture the entire connection and initialization process, which is exactly what we need to diagnose connection problems.

The log file captures:
- Bluetooth connection events (connect, disconnect, errors)
- Adapter initialization commands and responses
- All vehicle data received from the car

## Capturing an A-B-C Snapshot

Use this to help identify which sensor bytes change when something in the car changes (e.g., heater turns on/off, climate setting changes, etc.).

1. Go to **Settings > Advanced Diagnostics**
2. Set the car to the **baseline condition** (e.g., heater off)
3. Tap **Take Snapshot A (baseline)** — wait for it to complete (~20 seconds)
4. **Change the condition** you're testing (e.g., turn heater on)
5. Tap **Take Snapshot B (changed)** — wait for it to complete
6. **Revert the condition** back to baseline (e.g., turn heater off)
7. Tap **Take Snapshot C (reverted)** — wait for it to complete
8. Tap **Share ABC Log** and send the file

The log file contains all three snapshots and highlights exactly which bytes changed between A→B and B→C. This is invaluable for reverse-engineering what each sensor byte means.

**Note:** Live data polling pauses automatically while taking snapshots and resumes when complete. The snapshot reads data from all 12 vehicle ECUs (~45 data points), so each snapshot takes about 15-20 seconds.

## Unplug Reminder Notifications

The app sends a notification reminding you to unplug the OBD-II adapter when your car turns off. If you're not seeing this notification, check the following:

1. **In-app setting** — Go to Settings and make sure **Unplug Reminder** is turned on
2. **iOS notification permissions** — Go to iOS Settings → Notifications → Ioniq 5 and make sure **Allow Notifications** is enabled
3. **Focus mode** — If you're using a Focus mode (Do Not Disturb, Driving, etc.), notifications may be silenced. Check iOS Settings → Focus to see if the app is allowed
4. **Notification style** — In iOS Settings → Notifications → Ioniq 5, make sure **Banners** or **Alerts** is selected (not "None")
5. **Low Power Mode** — iOS may delay or suppress notifications when in Low Power Mode
6. **The car must actually turn off** — The reminder triggers when the app detects the ignition switching off. If you disconnect the adapter before turning off the car, the notification won't fire
