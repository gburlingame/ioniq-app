---
layout: default
title: Why Some Features Are Hard
nav_order: 3
---

# Why Some Features Are Hard

## There's no user manual for this

When people ask "can the app show me X?", the honest answer is often "maybe — if we can find the signal." Hyundai doesn't publish documentation for the data flowing across the car's diagnostic bus. There's no API. There's no dealer manual that says "brake lights are at location Y." What you see on your dashboard today exists because someone — often several someones — sat with their car, compared raw bytes against what the car was doing, and worked out the pattern.

That reality shapes everything. A request like "can you tell me when my daytime running lights are on?" might be trivial once the signal is found, or the state might not exist on the bus at all. Until we go look, we don't know. I try to be honest about that rather than promise things we might never be able to deliver.

## The hunt — how we found the brake light

The brake light indicator is a good example of why this work takes a village — and why the first fix is often close but not quite right. It had been working on 2022-2024 IONIQ 5s for a while, with the signal sitting at a specific byte-and-bit position in a message broadcast by the Body Control Module.

Then an IONIQ 9 tester came on board and reported the indicator wasn't firing on their car. Comparing snapshots between a 2024 IONIQ 5 and the new IONIQ 9 revealed that Hyundai had relocated the signal in the newer platform. We found the new location, pushed a fix, and it worked on the IONIQ 9.

Not long after, a 2025 IONIQ 5 tester reported the same problem on their car. We tried the IONIQ 9 fix on the 2025 i5 — it mostly worked, but produced false positives: the indicator lit up at moments when the pedal clearly wasn't pressed. Something was almost right, but not quite. More snapshots came in, from more cars, and the precise answer emerged: the brake flag isn't the whole byte we'd been watching — it's a single bit within that byte (bit 3, for the curious). Narrow the watch to that one bit, and the false positives disappeared.

Three cars, two model years, several testers' worth of snapshots — and we still needed one more iteration after we thought we had it.

This is the normal pace of discovery, not an exceptional feat. Most signals move between model years. Most signals hide. And even once you've found one, the first guess is often close but not right. The only way to work through it is to have enough eyes on enough cars.

## Why some things feel sluggish

Even when we've found a signal, physics puts a floor on how fast we can show it. Your OBD-II adapter talks to the app over Bluetooth Low Energy, and the ELM327 chipset inside the adapter can only ask the car one question at a time. Each question takes roughly 100-200 milliseconds: send the request, wait for the car to respond, parse the answer, move on.

The app tracks more than 40 values across the battery, motors, climate system, parking sensors, and more. Multiply that out and a full polling cycle takes several seconds. The brake light indicator can feel a beat behind because it's standing in line with the rest of them.

This isn't a bug — it's the nature of the hardware. Faster buses exist inside the car. The IONIQ 5's CAN FD bus carries real-time motor and driving data at much higher rates, and those signals *are* exposed on the OBD-II connector — they're just not reachable through a Bluetooth ELM327 adapter. Reading them requires a different category of hardware: a wired CAN FD adapter, generally connected to a laptop or a dedicated diagnostic device.

The Bluetooth pipe itself also imposes a ceiling. In my experience, the highest sustained payload rate achievable over Bluetooth Low Energy is around 16 kilobytes per second — enough for periodic polling of dozens of values, but nowhere near what a continuous stream of real-time driving data would need. Even a hypothetical BLE adapter that could speak CAN FD would still run into that wall.

## Become a treasure hunter

If any of this sounds intriguing rather than discouraging, there are tools built into the app that let you join the hunt. You'll find them in **Settings → Advanced Tools** — no secret handshake required; they're available to everyone.

- **DID Range Scan** walks one controller across a range of data identifiers and tells you which ones respond. Think of it as mapping the map. Running it on two cars of different model years is how we've spotted signals that Hyundai quietly relocated.
- **ECU Finder** probes the bus and lists every controller that answers, naming the ones we recognize. It's a quick way to see whether your car and someone else's have the same set of modules on board — a difference there is often the first hint that the data layout differs too.
- **ABC test** (the A-B-C snapshot) is the workhorse of signal hunting. Take a baseline with a condition off, change one thing, take a second snapshot, revert, take a third. The app shows you exactly which bytes flipped. This is how the brake light trail got picked up across multiple cars — press the pedal, take a snapshot, let it up, take another.

Beyond the app, hidden knowledge shows up in unexpected places: forum threads, Hyundai technical service bulletins, a passing comment in a Facebook group, a conversation at a DC fast charger. If any of it might point at a signal we haven't found — or might explain something we don't yet understand — pass it along. Every crumb shortcuts weeks of guessing, and the features people ask for are a lot more likely to ship when the community hands me the map.
