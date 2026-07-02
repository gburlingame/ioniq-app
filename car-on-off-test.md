---
layout: default
title: Car On/Off Detection Test
permalink: /car-on-off-test/
nav_exclude: true
search_exclude: true
---

# Help Improve Car On/Off Detection

Thanks for helping test a better "car on / car off" detector! This takes about 5 minutes,
parked in your driveway. You'll capture your vehicle in **3 states**: Off, On with lights off,
and On with lights on.

**You need:** your OBD adapter plugged in and connected in IONIQ 5 Companion.

## Step 1 — Get the scan file

On your **iPhone**, tap the link below and choose **Open in "IONIQ 5 Companion."** The app
imports the list and opens its **A / B / C** capture screen.

[**Download the scan file (iqlist_BCM_ignition_fleet.iqlist)**]({{ '/assets/downloads/iqlist_BCM_ignition_fleet.iqlist' | relative_url }})

To reopen it later, go to **Settings → Advanced Tools → ABC test with Curated DID List** and tap
the list that starts with **iqlist_BCM**.

> **Tip:** each capture is **one steady state** of the car. Get the car into the state first,
> *then* start the capture. Don't change anything (brake, lights, start button) while a capture
> is running.

## Step 2 — Capture the three states

**Capture A — CAR OFF**
- Sit in the driver's seat, car **fully off** (do **not** press Start).
- Wait ~10 seconds, then tap **Begin** on row A.
- For the label, type: `A OFF — <your car & year>` (e.g. `A OFF — 2025 IONIQ 5 RWD`)
- Wait for the green checkmark.

**Capture B — CAR ON, LIGHTS OFF**
- Foot on the brake, press **Start** until the dash shows **Ready**. Take your foot off the brake.
- Put the headlight switch to **OFF**.
- Wait ~10 seconds, tap **Begin** on row B. Label: `B ON lights-off`
- Wait for the green checkmark.

**Capture C — CAR ON, HEADLIGHTS ON**
- Still **Ready**. Turn the headlight switch to **ON** (low beams on).
- Wait ~10 seconds, tap **Begin** on row C. Label: `C ON lights-on`
- Wait for the green checkmark.

After the third capture the app jumps to a **Results** screen.

## Step 3 — Send it back

Go back to the ABC test list (**Settings → Advanced Tools → ABC test with Curated DID List**),
tap **Share findings…** on the scan you just finished, and **email the file to greg@theburl.com**.

That's it — thank you!

---

No personal data leaves your phone — this scan reads only body-control lamp/status bytes; no VIN
or location is included in the shared file.
