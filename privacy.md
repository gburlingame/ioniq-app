---
layout: default
title: Privacy Policy
nav_order: 3
---

<div style="text-align: right; margin-bottom: 16px;">
  <strong>English</strong> · <a href="privacy-nl">Nederlands</a> · <a href="privacy-de">Deutsch</a> · <a href="privacy-fr">Français</a> · <a href="privacy-es">Español</a> · <a href="privacy-sv">Svenska</a> · <a href="privacy-it">Italiano</a> · <a href="privacy-ko">한국어</a> · <a href="privacy-tr">Türkçe</a> · <a href="privacy-ja">日本語</a>
</div>

# Privacy Policy

**Last updated: November 9, 2026**

EV Dashboard ("the app") is developed by Greg Burlingame. This privacy policy describes how the app handles your data.

## Data Collection

EV Dashboard has no backend, no account, and no login. It contains no analytics, advertising, or tracking of any kind. The developer never receives your data, and nothing is sold.

Your data leaves your device only in these cases, each described below:

* **ABRP sharing** — off until you turn it on and link a vehicle; it sends that vehicle's live data directly to ABRP.
* **iCloud sync** — your settings and history sync to your own private iCloud account.
* **Apple Maps** — address searches, contact addresses you pick, and route requests go to Apple's MapKit.
* **Files you share** — logs, recordings, exports, and share cards leave your device only when you tap Share.

The Internet Connection tile and charger database updates also make network requests. They carry no information about you or your vehicle.

## Data Stored on Your Device

The app stores the following data locally on your device:

* **Vehicle diagnostic data** — Battery status, cell voltages, temperatures, charging data, tire pressures, and other sensor readings from your vehicle are stored in memory while the app is running. This data is not persisted between app launches unless you use a recording feature.
* **Driving and charging history** — When you use the History feature, summaries and recorded signal samples from your drives and charging sessions (state of charge, energy, temperatures, and other readings) are saved on your device so you can review them later. A charging session may store the location where it took place. A drive stores its route — your location about once a second while you drive — so it can be shown on its Journey map. You can turn this off under **Settings → Drive Sessions → Record Journey**, or remove a drive's route from its Journey map.
* **Session photos** — A photo you add to a charging or driving session is stored with that session.
* **App settings** — Your preferences (units, language, appearance, themes, chart settings, adapter selection, CarPlay tile layouts, charger filters, tire settings, and vehicle names) are stored on your device and synced through iCloud while Sync to iCloud is on.
* **Saved destinations** — Addresses you save for navigation, and your recent destinations, are stored on your device and synced with your settings.
* **Bluetooth device information** — The identifier and name of your paired OBD-II adapter is stored locally so the app can reconnect automatically.
* **ABRP link token** — If you link a vehicle to ABRP, the token you paste from the ABRP app is stored in your device's Keychain. Unlinking the vehicle deletes it.
* **App Activity Log** — A log file recording app lifecycle, Bluetooth connection, adapter interference, and history storage events. It is only shared when you explicitly use the Share button.
* **Drive Diagnostics Recorder** — A per-drive log file containing GPS fixes (position, heading, speed, and altitude), vehicle speed samples, and distance calculations, used to troubleshoot distance, elevation, and navigation accuracy. It is only shared when you explicitly use the Share button.
* **Diagnostic recordings and snapshot logs** — If you use the diagnostic recording or snapshot comparison features, a log file is saved locally containing Bluetooth events, adapter commands, and raw vehicle data. It is only shared when you explicitly use the Share button.

## Location

EV Dashboard uses your location to show your position on the CarPlay map, provide turn-by-turn directions, measure trip distance and efficiency, record a drive's Journey route, show your elevation, and find nearby chargers.

The app requests "When In Use" location access only. It never requests "Always" access. Location updates may continue while the app is in the background or while you are using another app: if you open the app while it is connected to your vehicle, it keeps a background location session until the vehicle turns off or the adapter is out of Bluetooth range, and iOS shows the location indicator while it does. GPS readings for trip distance and the Journey route are taken only while you drive.

Your location is not sent to the developer, and it is not profiled or sold. It is stored on your device in the history and files described above, which leave your device through iCloud sync or when you choose to share them. If you turn on ABRP sharing, your vehicle's location is sent to ABRP (see Sharing with ABRP).

## Maps and Navigation

Maps, address search, and route calculation are provided by Apple's MapKit. When you search for an address, pick a contact's address, or start navigation, the necessary query and location information is sent to Apple to return a result, and is handled under [Apple's privacy policy](https://www.apple.com/legal/privacy/). This information is not sent to the developer.

## Contacts

If you turn on **Show Contacts in Search** while adding a destination on your mobile device, the app asks for access to your contacts and shows their addresses as you type, in the app and in CarPlay. When you pick one, its address is sent to Apple's MapKit to place it on the map, and the contact's name is saved as the destination's tag. The app does not store your contacts or send them anywhere else.

## Camera and Photos

Tapping a session's photo square lets you take a photo with the camera or choose one from your library. A photo you take is stored with the session, and the full-resolution original is also saved to your Photos library. For that, the app asks for add-only access: it can add photos to your library but cannot see the photos in it. When you choose a photo from your library, iOS's own picker gives the app only the photo you choose.

## Motion & Fitness

The app uses your device's barometer to follow climbs and descents for the CarPlay Elevation tile and the Journey map, which matters most on vehicles whose CarPlay system does not report altitude. It asks for Motion & Fitness access to do so. Barometer readings are used on your device and are not sent anywhere.

## Sharing with ABRP (Optional)

ABRP (A Better Routeplanner) is a route-planning service operated by Iternio. Sharing is off until you turn on **Share Live Data with ABRP** under **Settings → Data Sharing → ABRP** and link a vehicle with the token from your ABRP app. When you link, the app sends the token to ABRP to check it.

While a linked vehicle is on, the app sends its live data directly from your device to ABRP's servers (api.iternio.com): the time; state of charge, battery energy, and state of health; power, current, and voltage; speed; location (latitude, longitude, elevation, and heading); whether it is charging, DC fast charging, or parked; the odometer; battery, cabin, and outside temperatures; and tire pressures. The VIN is not sent. Readings that could not be sent are held in memory, up to a limit, until the connection returns, and are discarded if the app closes.

This data does not pass through the developer. ABRP handles it under its own privacy policy. To stop sharing, turn the switch off or unlink the vehicle.

## Internet Connection Tile

The CarPlay Internet Connection tile measures your connection. While the tile is on your CarPlay screen, the app requests an empty test page about every 30 seconds, alternating between Cloudflare (cp.cloudflare.com) and Google (connectivitycheck.gstatic.com). These requests carry no information about you or your vehicle, although, like any internet request, they reveal your network address to those services. No requests are made while the tile is not on screen.

## Charger Database Updates

The list of DC fast-charge sites is included inside the app and works offline. No network connection is needed to browse or navigate to a charger.

If you tap **Settings → Navigation → Check for Update**, and only then, the app downloads a newer charger database. This makes two requests: one for a manifest file hosted at theburl.com, and one for the data file it names, hosted on GitHub Releases. Both are ordinary static file downloads, verified against a checksum. No information about you, your device, or your vehicle is sent with these requests, and there is no automatic or periodic update check.

## iCloud Sync

Both kinds of sync are on by default and can be turned off under **Settings → iCloud**.

* **Settings** — While **Sync to iCloud** is on, your app settings, saved destinations, tire settings, and vehicle names are synced through Apple's iCloud key-value storage to your own iCloud account, so they match across your devices. Whether to reconnect to an adapter automatically is set on each device and is not synced.
* **History** — While History sync is on, your driving and charging history — including session photos, the location stored with a charging session, and each drive's Journey route — is synced through Apple's CloudKit to your own private iCloud account, so it stays consistent across your iPhone, iPad, and Mac.

Both are stored in your personal iCloud, are governed by Apple's privacy policy, and are never sent to the developer or any third-party server — the developer has no access to them. If you turn both off, all data stays only on your device.

## Bluetooth

The app communicates with your OBD-II adapter over Bluetooth: Bluetooth Low Energy (BLE) for most adapters, and Bluetooth Classic, through Apple's External Accessory framework, for the OBDLink MX+, Vgate vLinker FS, and Vgate vLinker MS. All Bluetooth communication occurs directly between your device and the adapter. No Bluetooth data is transmitted to any server or third party.

## Vehicle Data

The app reads diagnostic data from your vehicle's onboard computer via the OBD-II port. This data includes battery status, temperatures, voltages, tire pressures, and other sensor readings. It is displayed and stored on your device, and it is not transmitted anywhere except to your own iCloud while History sync is on, and to ABRP if you turn on sharing.

## Notifications

If you enable the unplug reminder, the app uses local notifications to remind you to unplug the OBD-II adapter when the car turns off. No notification data is sent to any server.

## Data Retention

All data is stored on your device. Log files and recordings can be deleted through the iOS Files app. Uninstalling the app removes all locally stored data including settings, saved destinations, and saved adapter information. Photos the app saved to your Photos library stay there until you delete them. If you enabled iCloud sync, your history also remains in your iCloud account until you delete it from within the app or turn off sync. Data already sent to ABRP is kept by ABRP under its own policy.

## Children's Privacy

The app does not knowingly collect any data from children under 13.

## Changes to This Policy

If this privacy policy is updated, the revised version will be posted on this page with an updated date.

## Contact

If you have questions about this privacy policy, please [open an issue](https://github.com/gburlingame/ioniq-app/issues) on GitHub or email [greg@theburl.com](mailto:greg@theburl.com).
