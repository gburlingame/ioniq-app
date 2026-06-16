---
layout: default
title: Should I Unplug My OBD-II Adapter?
nav_order: 4
---

# Should I Unplug My OBD-II Adapter?

This comes up often, and there's no single right answer — it's a personal decision.
It comes down to weighing four things against each other:

- **12V battery drain** — how much current the adapter pulls while the car is off
- **Connector wear** — the OBD-II port isn't built for daily plug/unplug
- **Security** — the adapter is a wireless device wired to the diagnostic port
- **Convenience** — never having to think about it

Here are the facts on each.

## How much power the adapter draws

Most vendors don't publish idle-current figures, so this is harder to pin down than it
should be. Two data points we have asked about directly:

- **Veepeak** told us their adapter draws about **35 mA**.
- **VGate** told us the **iCar Pro 2S** has a low-power sleep state of about **3 mA**,
  which it enters when nothing is connected to it over Bluetooth.

For context against a roughly **60 Ah** 12V battery:

- 3 mA over a full day is about **72 mAh** (0.072 Ah) — a tiny fraction of the battery.
- 35 mA over a full day is about **840 mAh** (0.84 Ah) — still small day to day, but it
  adds up on a car that sits unused for weeks.

On top of that, your vehicle has a large high-voltage traction battery and a DC-DC
converter that quietly tops the 12V back up whenever it dips. So the common fear — "the
adapter will drain my 12V and I won't be able to start" — overstates the risk for a
healthy system that gets driven regularly. The figure that matters is *your* adapter's
draw, and they vary by more than 10×.

## Wear on the connector

The OBD-II port was designed to be plugged into occasionally — by a mechanic with a scan
tool — not connected and disconnected every single day. Each plug/unplug cycle puts a
little mechanical wear on the connector and its pins. Pull the adapter twice a day for a
couple of years and you've cycled that connector well over a thousand times to save a few
milliamps each time.

For that reason, we'd discourage making a habit of removing the adapter after every drive.
If draw or security is your concern, there's a better way to cut power (below) that leaves
the car's port alone.

## Security

An OBD-II adapter is a wireless (Bluetooth) device physically connected to your car's
diagnostic bus, and many adapters have weak or no pairing security. So the risk of someone
nearby connecting to it is greater than zero.

It's worth being honest about how large that risk actually is, though, and the answer is:
probably small, but not nothing.

- An attacker has to be within Bluetooth range of your car.
- When the car is off and asleep, most of its ECUs are powered down and simply won't
  respond, which sharply limits what a connection could do.

We don't want to overstate this — there's no known, demonstrated exploit we're pointing at.
But if the idea of a live, reachable device on your car's bus bothers you, especially when
you park in shared or public spaces, cutting its power when you're away closes that door
entirely.

## The switched extension cable

If you want the option to cut power — for drain, for security, or just for peace of mind —
without wearing out the car's port, use an inline OBD-II extension cable with a built-in
power switch. The adapter stays plugged into the extension, the extension stays in the car,
and you flip the switch off when you're done. The switch (not the car's connector) takes the
wear, the adapter draws nothing when it's off, and there's no powered device on the bus.

This is the option we'd point most people to. They're inexpensive and widely available. The
[iKKEGOL OBD-II extension with power switch](https://www.amazon.com/dp/B01EW83OCQ) we
previously linked is currently unavailable, but the
[Yeebline OBD-II extension with power switch](https://www.amazon.com/Yeebline-Extension-Diagnostic-Extender-Adapter/dp/B0CLTTSWG4)
is an equivalent substitute. Other vendors sell similar designs.

## The Unplug Reminder

If you do prefer to cut power, **Settings → Unplug Reminder** sends an iOS notification
shortly after the app detects the car has been turned off — a nudge to unplug the adapter,
or just flip the switch on your extension cable. Like any iOS notification, it depends on
you having granted notification permission.

## Bottom line

It's a personal decision. A low-draw adapter like the iCar Pro 2S, on a healthy 12V battery
in a regularly driven car, is fine to leave plugged in — and leaving it in spares your OBD-II
port the wear of daily reconnection. If drain or security concerns you, don't get in the habit
of yanking the adapter; fit a switched extension cable and let a flick of the switch do the
work.
