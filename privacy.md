---
layout: default
title: Privacy Policy
nav_order: 3
---

<div style="text-align: right; margin-bottom: 16px;">
  <strong>English</strong> · <a href="privacy-nl">Nederlands</a> · <a href="privacy-de">Deutsch</a> · <a href="privacy-fr">Français</a> · <a href="privacy-es">Español</a> · <a href="privacy-sv">Svenska</a>
</div>

# Privacy Policy

**Last updated: April 29, 2026**

IONIQ 5 Companion ("the app") is developed by Greg Burlingame. This privacy policy describes how the app handles your data.

## Data Collection

IONIQ 5 Companion does **not** collect, transmit, or sell any personal data to third parties. The app does not contain analytics, advertising, or tracking of any kind.

## Data Stored on Your Device

The app stores the following data locally on your device:

* **Vehicle diagnostic data** — Battery status, cell voltages, temperatures, charging data, tire pressures, and other sensor readings from your vehicle are stored in memory while the app is running. This data is not persisted between app launches unless you use the diagnostic recording feature.
* **App settings** — Your preferences (units, language, appearance, time chart settings, adapter selection) are stored locally using UserDefaults.
* **Bluetooth device information** — The identifier and name of your paired OBD-II adapter is stored locally so the app can reconnect automatically.
* **Diagnostic recordings** — If you use the "Start Recording Diagnostics" feature, a log file is saved to your device's local storage. This file contains Bluetooth events, adapter commands, and raw vehicle data. It is only shared when you explicitly use the Share button.
* **A-B-C Snapshot logs** — If you use the snapshot comparison feature, a log file is saved locally containing raw ECU data. It is only shared when you explicitly use the Share button.

## No Cloud Services

The app does not use iCloud, CloudKit, or any cloud storage. All data remains on your device.

## No Third-Party Integrations

The app does not integrate with any third-party services. There is no account creation, no login, and no data upload.

## Bluetooth

The app communicates with your OBD-II adapter via Bluetooth Low Energy (BLE). All Bluetooth communication occurs directly between your device and the adapter. No Bluetooth data is transmitted to any server or third party.

## Vehicle Data

The app reads diagnostic data from your vehicle's onboard computer via the OBD-II port. This data includes battery status, temperatures, voltages, tire pressures, and other sensor readings. This data is displayed on your device and is not transmitted anywhere.

## Notifications

If you enable the unplug reminder, the app uses local notifications to remind you to unplug the OBD-II adapter when the car turns off. No notification data is sent to any server.

## Data Retention

All data is stored on your device. Diagnostic recordings and snapshot logs can be deleted through the iOS Files app. Uninstalling the app removes all locally stored data including settings and saved adapter information.

## Children's Privacy

The app does not knowingly collect any data from children under 13.

## Changes to This Policy

If this privacy policy is updated, the revised version will be posted on this page with an updated date.

## Contact

If you have questions about this privacy policy, please [open an issue](https://github.com/gburlingame/ioniq-app/issues) on GitHub or email [greg@theburl.com](mailto:greg@theburl.com).
