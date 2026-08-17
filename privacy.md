---
layout: default
title: Privacy Policy
nav_order: 3
---

<div style="text-align: right; margin-bottom: 16px;">
  <strong>English</strong> · <a href="privacy-nl">Nederlands</a> · <a href="privacy-de">Deutsch</a> · <a href="privacy-fr">Français</a> · <a href="privacy-es">Español</a> · <a href="privacy-sv">Svenska</a> · <a href="privacy-it">Italiano</a> · <a href="privacy-ko">한국어</a> · <a href="privacy-tr">Türkçe</a> · <a href="privacy-ja">日本語</a>
</div>

# Privacy Policy

**Last updated: August 17, 2026**

EV Dashboard ("the app") is developed by Greg Burlingame. This privacy policy describes how the app handles your data.

## Data Collection

EV Dashboard does **not** collect, transmit, or sell any personal data to third parties. The app has no backend, no account, and no login. It contains no analytics, advertising, or tracking of any kind, and it never uploads your data anywhere.

## Data Stored on Your Device

The app stores the following data locally on your device:

* **Vehicle diagnostic data** — Battery status, cell voltages, temperatures, charging data, tire pressures, and other sensor readings from your vehicle are stored in memory while the app is running. This data is not persisted between app launches unless you use a recording feature.
* **Driving and charging history** — When you use the History feature, summaries and recorded signal samples from your drives and charging sessions (state of charge, energy, temperatures, and other readings) are saved on your device so you can review them later. A session may also store the location where it took place, so it can be shown on a map.
* **App settings** — Your preferences (units, language, appearance, themes, chart settings, adapter selection, CarPlay tile layouts) are stored locally using UserDefaults.
* **Saved destinations** — Addresses you save for navigation, and your recent destinations, are stored locally on your device.
* **Bluetooth device information** — The identifier and name of your paired OBD-II adapter is stored locally so the app can reconnect automatically.
* **App Activity Log** — A log file recording app lifecycle, Bluetooth connection, adapter interference, and history storage events. It is only shared when you explicitly use the Share button.
* **Drive Diagnostics Recorder** — A per-drive log file containing GPS fixes, vehicle speed samples, and distance calculations, used to troubleshoot distance and navigation accuracy. It is only shared when you explicitly use the Share button.
* **Diagnostic recordings and snapshot logs** — If you use the diagnostic recording or snapshot comparison features, a log file is saved locally containing Bluetooth events, adapter commands, and raw vehicle data. It is only shared when you explicitly use the Share button.

## Location

EV Dashboard uses your location to show your position on the CarPlay map, provide turn-by-turn directions, measure trip distance and efficiency while you drive, and find nearby chargers.

The app requests "When In Use" location access only. It never requests "Always" access. Because trip distance is measured continuously during a drive, location updates may continue while the app is in the background or while you are using another app — this stops when the drive ends.

Your location is used on your device and is not sent to the developer. It is not collected, profiled, or sold. Location may be written to the on-device files described above (the Drive Diagnostics Recorder, and the location stored with a history session), which leave your device only if you choose to share them.

## Maps and Navigation

Maps, address search, and route calculation are provided by Apple's MapKit. When you search for an address or start navigation, the necessary query and location information is sent to Apple to return a result, and is handled under [Apple's privacy policy](https://www.apple.com/legal/privacy/). This information is not sent to the developer.

## Charger Database Updates

The list of DC fast-charge sites is included inside the app and works offline. No network connection is needed to browse or navigate to a charger.

If you tap **Settings → Navigation → Check for Update**, and only then, the app downloads a newer charger database. This makes two requests: one for a manifest file hosted at theburl.com, and one for the data file it names, hosted on GitHub Releases. Both are ordinary static file downloads, verified against a checksum. No information about you, your device, or your vehicle is sent with these requests, and there is no automatic or periodic update check.

## iCloud Sync (Optional)

If you turn on iCloud sync, your driving and charging history — including any location stored with a session — is synced through Apple's CloudKit to your own private iCloud account, so it stays consistent across your iPhone, iPad, and Mac. This data is stored in your personal iCloud, is governed by Apple's privacy policy, and is never sent to the developer or any third-party server — the developer has no access to it. If you leave iCloud sync off, all data stays only on your device.

## Bluetooth

The app communicates with your OBD-II adapter via Bluetooth Low Energy (BLE). All Bluetooth communication occurs directly between your device and the adapter. No Bluetooth data is transmitted to any server or third party.

## Vehicle Data

The app reads diagnostic data from your vehicle's onboard computer via the OBD-II port. This data includes battery status, temperatures, voltages, tire pressures, and other sensor readings. This data is displayed on your device and is not transmitted anywhere.

## Notifications

If you enable the unplug reminder, the app uses local notifications to remind you to unplug the OBD-II adapter when the car turns off. No notification data is sent to any server.

## Data Retention

All data is stored on your device. Log files and recordings can be deleted through the iOS Files app. Uninstalling the app removes all locally stored data including settings, saved destinations, and saved adapter information. If you enabled iCloud sync, your history also remains in your iCloud account until you delete it from within the app or turn off sync.

## Children's Privacy

The app does not knowingly collect any data from children under 13.

## Changes to This Policy

If this privacy policy is updated, the revised version will be posted on this page with an updated date.

## Contact

If you have questions about this privacy policy, please [open an issue](https://github.com/gburlingame/ioniq-app/issues) on GitHub or email [greg@theburl.com](mailto:greg@theburl.com).
