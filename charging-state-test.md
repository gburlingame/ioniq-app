---
layout: default
title: Charging-State Test (VCU)
permalink: /charging-state-test/
nav_exclude: true
search_exclude: true
---

# Help Test a Better "Car On/Off" Signal

Thanks for helping! This test checks whether the **VCU** (the module the app reads the VIN from at
startup) can reliably tell the app the difference between **ON — ready to drive *or* charging** —
and **OFF**. We need it run across the fleet and, ideally, while charging.

**You need:** your OBD adapter connected in EV Dashboard, and ideally access to an **L1 or L2
charger** and/or a **DC fast charger**. Do whichever tests you can — please don't feel like you
need to run all of them. Even just the easy **OFF / ON / OFF** run is incredibly helpful! And I
know the summer heat makes sitting in the car rough, so thanks to everyone melting alongside me.

## Step 1 — Get the scan file

On your **iPhone**, tap the link below and choose **Open in "EV Dashboard."** It opens
automatically in **Advanced Tools → ABC test with Curated DID List**.

[**Download the scan file (iqlist_VCU_state_probe.iqlist)**]({{ '/assets/downloads/iqlist_VCU_state_probe.iqlist' | relative_url }})

## Step 2 — Run whichever scenarios you can

Each scenario is a full A/B/C. Set the car to the state, capture the slot, type the label, wait for
the green check.

**Scenario 1 — Normal (OFF / ON / OFF)**
- A: car **fully off** → label `OFF` (+ your car model & year)
- B: **ready to drive** (press the brake + Start button) → label `ON`
- C: car **fully off** again → label `OFF`

**Scenario 2 — AC charging (OFF / AC CHARGING / OFF)**
- A: car **off, not plugged in** → label `OFF` (+ your car model & year)
- B: car **off, AC charging** — plug in, wait until it's actually charging, then capture → label `AC CHARGING`
- C: car **off, not plugged in** → label `OFF`

**Scenario 3 — DC fast charging (OFF / DC CHARGING / OFF)**
- A: car **off, unplugged** → label `OFF` (+ your car model & year)
- B: car **off, DC fast charging** — plugged in and charging → label `DC CHARGING`
- C: car **off, unplugged**, session ended → label `OFF`

## Step 3 — Send it back

For each finished scenario, tap **Share findings…** and **email it to greg@theburl.com**. Send any
scans you're able to run — thank you!
