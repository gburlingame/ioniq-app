---
layout: default
title: Should I Unplug My OBD-II Adapter?
nav_order: 4
---

# Should I Unplug My OBD-II Adapter?

Most people unplug it. Some leave it in for months without trouble. Both camps have a defensible position, and the right answer depends on what you value: zero risk to your 12V battery, or the convenience of never thinking about it. This article lays out what's actually going on so you can make an informed call — and explains what the app does on its end to keep its footprint small.

## The case for unplugging

The mainstream advice from IONIQ owners is simple: when you're done driving, pull the adapter. It's worth being precise about *why*, though, because the popular framing — "an adapter will drain your 12V and you won't be able to start the car" — isn't really how the car works. Your IONIQ has an enormous high-voltage traction battery and a DC-DC converter that quietly tops the 12V back up whenever it dips. As long as the high-voltage system is healthy, the 12V isn't going to a dead-flat state from a few milliamps of accessory draw.

The more honest concern is wear. Every time the adapter pulls a small, continuous current, the 12V sags a little and the DC-DC converter wakes up briefly to bring it back up. Repeated thousands of times over weeks and months, that micro-cycling burns through the 12V battery's finite charge-cycle budget faster than it would otherwise. Unplugging when you're not actively using the app stops the cycling. If you're not sure, unplug.

## The case for leaving it in

The other camp is also reasonable. The honest truth is that nobody really knows how much current a typical Bluetooth ELM327 adapter actually draws — vendors don't publish it, the figure depends on the chipset, the BLE module, the voltage regulator, and whether there's a power LED that stays lit. If you've seen a measurement of your adapter's idle current, I'd love to hear it. What we *can* say empirically is that plenty of testers leave their adapters plugged in for weeks or months and have never reported a 12V issue traceable to the adapter.

If your 12V battery is healthy and you drive the car often enough to keep it topped up, the steady-state risk is genuinely small. The strongest argument for this camp isn't ideology, it's the OBD-II port itself: each plug/unplug cycle puts a little wear on a connector that wasn't designed for daily reconnection.

## A middle path: a switched extension cable

If you don't love unplugging but also don't love the idea of an always-on accessory, there's a tidy middle option: an inline OBD-II extension cable with a built-in power switch. The adapter stays plugged into the extension; you flip the switch off when you're done. No wear on the car's port, and the adapter draws nothing when the switch is off.

These are inexpensive and widely available — one example sold at the time of writing is the [iKKEGOL OBD-II extension with power switch](https://www.amazon.com/dp/B01EW83OCQ) on Amazon. Other vendors sell similar designs.

## What the app does to keep its footprint small

The app is aware that it's talking to a device that's drawing power from the car, and it changes how often it speaks based on what it knows.

When you first plug in and the app has never seen the ignition on, it sends an ignition-detection probe roughly every **500 milliseconds**. That's deliberately aggressive — the goal is for the dashboard to come alive within a second or two of you sitting down and turning the car on, rather than making you wait. This fast cadence only runs *until* the app sees ignition for the first time.

Once you've driven and turned the car off, the app drops to a much quieter cadence: a single probe every **5 seconds**. That's enough to detect the next key-on within a few seconds without keeping a continuous conversation going on the bus.

Honesty caveat: even at 5-second intervals, the app is still talking to the adapter, and the adapter is still talking to the car. The bus isn't fully asleep while you're connected. That's exactly why the next feature exists.

## The Unplug Reminder

Inside the app, **Settings → Unplug Reminder** is on by default. When enabled, the app sends you an iOS notification shortly after it detects the car has been turned off, nudging you to unplug the adapter (or flip the switch on your extension cable). It's a small thing, but it's the difference between "I forgot it was in there for a week" and "oh right, let me grab that on my way out."

The toggle is opt-out, and like any iOS notification it depends on you having granted notification permission to the app.

## Bottom line

If in doubt, unplug — or use a switched extension cable so the act of unplugging is just a flick of a switch. If you've been leaving yours plugged in for ages without trouble, you're probably fine; just keep an eye on your 12V battery's health, especially in cold weather or after long periods of not driving.
