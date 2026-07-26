---
layout: paper
title: How Range and Efficiency Are Calculated
nav_order: 6
description: How the app measures driving efficiency and turns it into a range estimate — every formula worked out.
sections:
  - id: s1
    n: ""
    label: "Overview"
  - id: s2
    n: "1"
    label: "Notation and units"
  - id: s3
    n: "2"
    label: "Three different efficiency values"
  - id: s4
    n: "3"
    label: "Trip efficiency"
  - id: s5
    n: "4"
    label: "Rolling efficiency"
  - id: s6
    n: "5"
    label: "Range"
  - id: s7
    n: "6"
    label: "Arrival state of charge"
  - id: s8
    n: "7"
    label: "Lifetime round-trip efficiency — a different number entirely"
  - id: s9
    n: "8"
    label: "What the model deliberately does not do"
  - id: s10
    n: "9"
    label: "Constants reference"
  - id: s11
    n: "10"
    label: "Reading the diagnostic log"
  - id: s12
    n: ""
    label: "Appendix — where this lives in the code"
---

<!-- =========================================================
     GENERATED FILE — DO NOT EDIT.
     Edits here are lost on the next build.
     Source:  docs/efficiency-and-range/efficiency-and-range.src.md
     Rebuild: cd docs/efficiency-and-range && node render.mjs
     ========================================================= -->
# How IONIQ 5 Companion measures efficiency and estimates range

*A walkthrough of the math, written for owners and testers who want to know exactly what the numbers on screen are made of.*

**Version:** 2026-07-25 · **Applies to:** app version 3.0 (build 137) and later

---

## Overview {#s1}

Your vehicle already shows a range distance and rolling efficiency on the instrument cluster, but more often than not these values do not match what is attained in real-world driving (at least not my driving).
IONIQ 5 Companion has added a new feature for calculating efficiency and range.   These values are  **computed by the app itself**.  They are based on signals it polls out of the battery management system (BMS) and the vehicle control unit (VCU), combined with GPS signals from your mobile device.
This paper explains what the app's numbers actually mean and how they are calculated, so you can judge which one is answering the question you are asking.

---

## 1. Notation and units {#s2}

The app works internally in **metric canonical units** and converts only at display time.

<div class="tablewrap" markdown="1">

| Symbol | Meaning | Canonical unit |
|---|---|---|
| <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>E</mi></mrow><annotation encoding="application/x-tex">E</annotation></semantics></math></span> | Energy | kilowatt-hours (kWh) |
| <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>d</mi></mrow><annotation encoding="application/x-tex">d</annotation></semantics></math></span> | Distance | kilometres (km) |
| <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi></mrow><annotation encoding="application/x-tex">P</annotation></semantics></math></span> | Pack power | kilowatts (kW) |
| <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>e</mi></mrow><annotation encoding="application/x-tex">e</annotation></semantics></math></span> | Efficiency (consumption form) | watt-hours per kilometre (Wh/km) |
| <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span> | State of charge | percent (%) |
| <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span> | Available pack energy | kWh |

</div>

The single conversion constant used throughout:

```
1 mile = 1.609344 km          1 km = 0.621371 miles
```

### Display units

You choose the efficiency unit in **Settings ▸ Units ▸ Efficiency**.
It is independent of your distance unit, so a metric driver can read distance in km and consumption in kWh/100km.
All five forms are conversions of the same underlying Wh/km value:

<div class="tablewrap" markdown="1">

| Selected unit | Formula from the canonical pair <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo stretchy="false">(</mo><mi>d</mi><mtext> km</mtext><mo separator="true">,</mo><mtext> </mtext><mi>E</mi><mtext> kWh</mtext><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">(d\ \text{km},\ E\ \text{kWh})</annotation></semantics></math></span> | From <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>e</mi></mrow><annotation encoding="application/x-tex">e</annotation></semantics></math></span> in Wh/km | Direction |
|---|---|---|---|
| mi/kWh | <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle scriptlevel="0" displaystyle="true"><mfrac><mrow><mi>d</mi><mo>×</mo><mn>0.621371</mn></mrow><mi>E</mi></mfrac></mstyle></mrow><annotation encoding="application/x-tex">\dfrac{d \times 0.621371}{E}</annotation></semantics></math></span> | <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>621.371</mn><mi mathvariant="normal">/</mi><mi>e</mi></mrow><annotation encoding="application/x-tex">621.371 / e</annotation></semantics></math></span> | higher is better |
| km/kWh | <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle scriptlevel="0" displaystyle="true"><mfrac><mi>d</mi><mi>E</mi></mfrac></mstyle></mrow><annotation encoding="application/x-tex">\dfrac{d}{E}</annotation></semantics></math></span> | <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1000</mn><mi mathvariant="normal">/</mi><mi>e</mi></mrow><annotation encoding="application/x-tex">1000 / e</annotation></semantics></math></span> | higher is better |
| kWh/100km | <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle scriptlevel="0" displaystyle="true"><mfrac><mi>E</mi><mi>d</mi></mfrac></mstyle><mo>×</mo><mn>100</mn></mrow><annotation encoding="application/x-tex">\dfrac{E}{d} \times 100</annotation></semantics></math></span> | <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>e</mi><mi mathvariant="normal">/</mi><mn>10</mn></mrow><annotation encoding="application/x-tex">e / 10</annotation></semantics></math></span> | lower is better |
| Wh/mi | <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle scriptlevel="0" displaystyle="true"><mfrac><mrow><mi>E</mi><mo>×</mo><mn>1000</mn></mrow><mrow><mi>d</mi><mo>×</mo><mn>0.621371</mn></mrow></mfrac></mstyle></mrow><annotation encoding="application/x-tex">\dfrac{E \times 1000}{d \times 0.621371}</annotation></semantics></math></span> | <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>e</mi><mo>×</mo><mn>1.609344</mn></mrow><annotation encoding="application/x-tex">e \times 1.609344</annotation></semantics></math></span> | lower is better |
| Wh/km | <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle scriptlevel="0" displaystyle="true"><mfrac><mrow><mi>E</mi><mo>×</mo><mn>1000</mn></mrow><mi>d</mi></mfrac></mstyle></mrow><annotation encoding="application/x-tex">\dfrac{E \times 1000}{d}</annotation></semantics></math></span> | <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>e</mi></mrow><annotation encoding="application/x-tex">e</annotation></semantics></math></span> | lower is better |

</div>

**Worked conversion.** An efficiency of <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>e</mi><mo>=</mo><mn>185</mn></mrow><annotation encoding="application/x-tex">e = 185</annotation></semantics></math></span> Wh/km displays as:

```
mi/kWh      = 621.371 ÷ 185        = 3.4
km/kWh      = 1000 ÷ 185           = 5.4
kWh/100km   = 185 ÷ 10             = 18.5
Wh/mi       = 185 × 1.609344       = 298
Wh/km       = 185                  = 185
```

The two "rate" forms (distance per energy) improve as they rise; the three "consumption" forms (energy per distance) improve as they fall.
The app tracks that polarity so the CarPlay trend band tints green for "better than your recent average" in whichever unit you picked.

Rounding: Wh/mi and Wh/km display as whole numbers; the other three display to one decimal.

---

## 2. Three different efficiency values {#s3}

This white paper will explain the details behind three different efficiency values that IONIQ 5 Companion presents. 

<div class="tablewrap" markdown="1">

| Number | Where you see it | What it answers | Energy signal source |
|---|---|---|---|
| **Trip efficiency** | History ▸ a driving session | "How efficient was *that drive*?" | BMS available-energy delta  |
| **Rolling efficiency** | CarPlay Range chip | "How efficient am I driving *right now*?" | BMS available-energy delta |
| **Lifetime round-trip efficiency** | Dashboard ▸ Battery Odometer | "How much energy does the pack *lose to heat*?" | Lifetime BMS counters |

</div>

The first two are consumption figures (energy per distance).
They differ only in the span they cover — one whole drive versus the last few miles — and both read energy from the same place, the battery's own account of how much usable energy it has left.
The third is a **percentage** and is a completely different physical quantity — it is not a driving statistic at all.  Section 7 covers it separately.

---

## 3. Trip efficiency {#s4}

This is the headline number on every completed driving session.
It is derived at display time from two values stored as part of the session record:

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mtext>efficiency</mtext><mo>=</mo><mi>f</mi><mrow><mo fence="true">(</mo><msub><mi>d</mi><mtext>session</mtext></msub><mo separator="true">,</mo><mtext> </mtext><msub><mi>E</mi><mtext>session</mtext></msub><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">\text{efficiency} = f\left(d_{\text{session}},\ E_{\text{session}}\right)</annotation></semantics></math></span>
</div>

where <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>f</mi></mrow><annotation encoding="application/x-tex">f</annotation></semantics></math></span> is whichever display formula from §1 you selected.

### 3.1 The energy term — read from the pack, not calculated

The app reads the BMS's own available-energy report at the start and end of the drive and takes the difference:

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><msub><mi>E</mi><mtext>session</mtext></msub><mo>=</mo><msub><mi>A</mi><mtext>start</mtext></msub><mo>−</mo><msub><mi>A</mi><mtext>end</mtext></msub></mrow><annotation encoding="application/x-tex">E_{\text{session}} = A_{\text{start}} - A_{\text{end}}</annotation></semantics></math></span>
</div>

<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span> is `availableEnergy`, decoded from BMS diagnostic identifier **0x0105** which is polled every 30 seconds.
Two raw bytes at offset 28, scaled:

```
A (kWh) = raw_16bit × 2 ÷ 1000
```

Three properties follow from using the BMS accounting:

- **Regeneration is netted automatically.** Energy recovered on a downhill run raises available energy, which shrinks the difference.  
- **Everything on the high-voltage bus is included** — traction motor drive, climate control, battery conditioning, the DC-DC converter feeding the 12 V system.  
- **Pack capacity, degradation, and temperature are already baked in**, because the BMS computes available energy against the real pack.

### 3.2 The distance term

Trip distance is measured as a **speed integral over the session timeline**:

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><msub><mi>d</mi><mtext>session</mtext></msub><mo>=</mo><munder><mo>∑</mo><mi>i</mi></munder><msub><mover accent="true"><mi>v</mi><mo>ˉ</mo></mover><mi>i</mi></msub><mo>⋅</mo><mi mathvariant="normal">Δ</mi><msub><mi>t</mi><mi>i</mi></msub><mspace width="2em"/><mtext>where</mtext><mspace width="2em"/><msub><mover accent="true"><mi>v</mi><mo>ˉ</mo></mover><mi>i</mi></msub><mo>=</mo><mfrac><mrow><msub><mi>v</mi><mrow><mi>i</mi><mo>−</mo><mn>1</mn></mrow></msub><mo>+</mo><msub><mi>v</mi><mi>i</mi></msub></mrow><mn>2</mn></mfrac></mrow><annotation encoding="application/x-tex">d_{\text{session}} = \sum_{i} \bar{v}_i \cdot \Delta t_i
\qquad\text{where}\qquad
\bar{v}_i = \frac{v_{i-1} + v_i}{2}</annotation></semantics></math></span>
</div>

That is a trapezoid rule: each new speed sample credits the time since the last one, at the average of the two speeds.

Two independent speed channels feed it:

1. **Doppler speed** from GPS fixes on your mobile device (~1 Hz).  A fix credits distance only if it passes a confidence gate: reported speed <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo>≥</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">\ge 0</annotation></semantics></math></span> **and** its stated speed accuracy is <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>0</mn><mo>&lt;</mo><msub><mi>σ</mi><mi>v</mi></msub><mo>≤</mo><mn>2.0</mn></mrow><annotation encoding="application/x-tex">0 &lt; \sigma_v \le 2.0</annotation></semantics></math></span> m/s.  This is the fix's *own reported speed*, never derived by differencing positions — so it does not jitter while parked and has no scale bias.
2. **Vehicle speed** from the VCU, polled roughly every 2.5–3 seconds.  It credits only the intervals Doppler has not already covered — specifically, when no confident fix has arrived within the last 2.5 seconds.  This carries the drive through tunnels, parking garages, dead GPS, or denied location permission.

Every second of the session is attributed to exactly one of four buckets — `doppler`, `wheel`, `stationary`, or `gap` — and nothing is silently dropped.
A single timeline marker guarantees no interval is ever counted twice.

Interval rules:

<div class="tablewrap" markdown="1">

| Rule | Value | Effect |
|---|---|---|
| Credit cap | 10 s | A sample arriving 14 s after the marker credits 10 s and books 4 s as `gap` — no data means no invented distance |
| Stationary floor | 0.15 m/s | Below this the interval is *verified stationary*: time counted, zero distance. A stopped car is a measurement, not a gap |
| Doppler freshness | 2.5 s | How long a confident fix suppresses the vehicle-speed channel |
| Doppler confidence gate | 2.0 m/s | Fixes with worse stated speed accuracy do not credit |

</div>

**Worked micro-example.** Cursor anchored at <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>t</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">t = 0</annotation></semantics></math></span> with <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>v</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">v = 0</annotation></semantics></math></span>:

```
t = 1.0 s, Doppler v = 8.0 m/s → v̄ = (0 + 8.0)/2 = 4.0 m/s → 4.0 × 1.0 = 4.0 m
t = 2.0 s, Doppler v = 9.0 m/s → v̄ = (8.0 + 9.0)/2 = 8.5 m/s → 8.5 × 1.0 = 8.5 m
                                                     running total = 12.5 m = 0.0125 km
```

### 3.3 Coverage, and when the odometer gets a vote

At session close the app computes how much of the drive it actually measured:

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mtext>coverage</mtext><mo>=</mo><mfrac><mrow><msub><mi>t</mi><mtext>doppler</mtext></msub><mo>+</mo><msub><mi>t</mi><mtext>wheel</mtext></msub><mo>+</mo><msub><mi>t</mi><mtext>stationary</mtext></msub></mrow><mrow><msub><mi>t</mi><mtext>doppler</mtext></msub><mo>+</mo><msub><mi>t</mi><mtext>wheel</mtext></msub><mo>+</mo><msub><mi>t</mi><mtext>stationary</mtext></msub><mo>+</mo><msub><mi>t</mi><mtext>gap</mtext></msub></mrow></mfrac></mrow><annotation encoding="application/x-tex">\text{coverage} = \frac{t_{\text{doppler}} + t_{\text{wheel}} + t_{\text{stationary}}}
{t_{\text{doppler}} + t_{\text{wheel}} + t_{\text{stationary}} + t_{\text{gap}}}</annotation></semantics></math></span>
</div>

Then a single decision:

```
if coverage ≥ 0.80                    → use the integral
else if odometer delta > 0            → use (end odometer − start odometer)
else                                  → use the partial integral
```

**Worked example.** A 37-minute drive attributes 1,510 s to Doppler, 240 s to vehicle speed, 380 s stationary, 95 s gap:

```
coverage = (1510 + 240 + 380) ÷ (1510 + 240 + 380 + 95)
         = 2130 ÷ 2225
         = 0.957  →  95.7 %  ≥ 80 %  →  the integral is used
```

**Why the odometer is inadequate as the primary source.** The car’s odometer signal reports in whole miles or whole kilometers.
A real-world short 1.443 km errand quantizes to 1.609 km — an 11 % error on that trip, and much worse on shorter ones.
Measured on one verification drive (2026-07-21), the integral gave 1.443 km against a 1.609 km odometer delta, with 98 % coverage.
The odometer is therefore a coverage-gated *fallback*, never an arbiter of a well-measured drive.

### 3.4 Putting it all together

**Sample trip.** Available energy 61.4 kWh when the car was put into gear, 53.3 kWh at ignition-off; the integral measured 42.0 km at 96 % coverage.

```
E = 61.4 − 53.3           = 8.1 kWh
d = 42.0 km               (coverage ≥ 80 %, integral used)

km/kWh     = 42.0 ÷ 8.1                      = 5.2
mi/kWh     = (42.0 × 0.621371) ÷ 8.1         = 3.2
kWh/100km  = 8.1 ÷ 42.0 × 100                = 19.3
Wh/km      = 8.1 × 1000 ÷ 42.0               = 193
Wh/mi      = 8.1 × 1000 ÷ (42.0 × 0.621371)  = 310
```

During the drive the app shows the running integral live; the coverage gate is applied once, when the session ends.

---

## 4. Rolling efficiency {#s5}

Rolling efficiency is a *rate* that reflects how you are driving now rather than how you drove an hour ago.
This is a separate estimator with its own energy and distance measurements.

### 4.1 Energy

Similar to trip efficiency, energy comes from the battery's own available-energy reading, differenced between the start and end of a measuring window:

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><msub><mi>E</mi><mtext>window</mtext></msub><mo>=</mo><msub><mi>A</mi><mtext>start</mtext></msub><mo>−</mo><msub><mi>A</mi><mtext>end</mtext></msub></mrow><annotation encoding="application/x-tex">E_{\text{window}} = A_{\text{start}} - A_{\text{end}}</annotation></semantics></math></span>
</div>

The reading resolves to **0.002 kWh (2 Wh)** and is polled every 30 seconds, so a minute of driving typically moves it by several dozen steps — fine enough to measure against, provided the window is long enough. §4.3 explains why that qualifier matters.

Idling still costs you, exactly as you would expect: sitting at a red light with the climate control running keeps draining the pack, so available energy keeps falling while the distance term does not grow. The window that eventually closes has that consumption in it.

### 4.2 Distance

Distance is measured the same as trip efficiency — the same running total, from the same two speed sources, produced by the same code.
The rolling estimate simply reads how far that total has advanced since its own measuring window opened.

**Why a window can be thrown away.**
There is one thing the rolling figure must do that the trip total does not, and it follows from the energy side rather than the distance side.
The distance totalizer tracks how much of the drive it could not account for.
When that unaccounted time grows during an open rolling efficiency time window, the app abandons that time window and starts a fresh one rather than including a distorted measurement.
**The two cases where a window is abandoned.**
Note that a window is always discarded whole — its distance *and* its energy together — so the two halves always describe the same span of driving.
Individual distance readings are never selectively dropped.

<div class="tablewrap" markdown="1">

| Case | Trigger | Why |
|---|---|---|
| Unmeasured driving | More than 5 s of the time window went unaccounted for | Energy is complete but distance is short, so the window would read falsely inefficient |
| A new drive begins | The app is told a driving session has started | The open window described a different drive |

</div>

The second case is also what handles charging.
Plugging in ends the driving session, so the reading taken before you charged is discarded when you next set off — the app does not watch for the charger separately.

**A stop does not abandon a window, deliberately.**
Sitting in traffic or idling with the climate running spends real energy over no distance, and that is exactly what your efficiency should reflect.
The energy keeps accruing against the open window and lands in the next measurement, so a long wait shows up as worse efficiency.
A rise in available energy while you are *moving* is regeneration — real driving data, and kept.

**This is rarer than it used to be.**
Because distance now comes from the shared totalizer, the car's own speed signal keeps measuring through tunnels and parking garages, which previously produced no distance at all and forced the window to be thrown away.
A window is now abandoned only when *both* the phone's GPS and the car's speed signal go quiet at once.

### 4.3 The blend — a distance-weighted exponential moving average

The estimator keeps one measuring window open at a time, accumulating distance <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="normal">Δ</mi><mi>d</mi></mrow><annotation encoding="application/x-tex">\Delta d</annotation></semantics></math></span> (km) and energy <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>E</mi><mtext>window</mtext></msub></mrow><annotation encoding="application/x-tex">E_{\text{window}}</annotation></semantics></math></span> (kWh). When the window is big enough it closes, produces one sample, and a fresh window opens:

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mtext>sample</mtext><mo>=</mo><mi mathvariant="normal">clamp</mi><mo>⁡</mo><mrow><mo fence="true">(</mo><mfrac><mrow><msub><mi>E</mi><mtext>window</mtext></msub><mo>×</mo><mn>1000</mn></mrow><mrow><mi mathvariant="normal">Δ</mi><mi>d</mi></mrow></mfrac><mo separator="true">,</mo><mtext> </mtext><mo>−</mo><mn>200</mn><mo separator="true">,</mo><mtext> </mtext><mn>5000</mn><mo fence="true">)</mo></mrow><mtext> Wh/km</mtext></mrow><annotation encoding="application/x-tex">\text{sample} = \operatorname{clamp}\left(\frac{E_{\text{window}} \times 1000}{\Delta d},\ -200,\ 5000\right)\ \text{Wh/km}</annotation></semantics></math></span>
</div>

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mi>k</mi><mo>=</mo><msup><mn>0.5</mn><mrow><mtext> </mtext><mi mathvariant="normal">Δ</mi><mi>d</mi><mi mathvariant="normal">/</mi><mn>8</mn></mrow></msup></mrow><annotation encoding="application/x-tex">k = 0.5^{\,\Delta d / 8}</annotation></semantics></math></span>
</div>

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><msub><mi>e</mi><mtext>new</mtext></msub><mo>=</mo><mi>max</mi><mo>⁡</mo><mrow><mo fence="true">(</mo><mn>40</mn><mo separator="true">,</mo><mtext> </mtext><mi>k</mi><mo>⋅</mo><msub><mi>e</mi><mtext>old</mtext></msub><mo>+</mo><mo stretchy="false">(</mo><mn>1</mn><mo>−</mo><mi>k</mi><mo stretchy="false">)</mo><mo>⋅</mo><mtext>sample</mtext><mo fence="true">)</mo></mrow><mtext> Wh/km</mtext></mrow><annotation encoding="application/x-tex">e_{\text{new}} = \max\left(40,\ k \cdot e_{\text{old}} + (1 - k)\cdot \text{sample}\right)\ \text{Wh/km}</annotation></semantics></math></span>
</div>

<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>k</mi></mrow><annotation encoding="application/x-tex">k</annotation></semantics></math></span> is the fraction of the old estimate retained.
The exponent's denominator is the **half-life: 8 km (about 5 miles)**.

**Update cadence:** All three of these must be true, so the estimate updates **at most once a minute**:

<div class="tablewrap" markdown="1">

| Condition | Value | What it prevents |
|---|---|---|
| Time since the window opened | ≥ 60 s | Updating so often that noise dominates the measurement |
| Distance measured | ≥ 0.3 km | Dividing a real energy reading by a few metres of GPS wobble |
| Energy moved | ≥ 0.05 kWh | Folding a zero while the battery's reading sits between updates |

</div>

The three conditions also mean the display simply holds its last value in stop-and-go traffic rather than reporting noise: if the car has not covered 300 meters, the window stays open until it does.

**Example calculation:**  Begin with a starting estimate of 200 Wh/km followed by the car covering 2.0 km with the the battery's available energy falling by 0.5 kWh:

```
starting estimate = 200 Wh/km

sample = 0.5 × 1000 ÷ 2.0        = 250 Wh/km
k      = 0.5 ^ (2.0 ÷ 8.0)       = 0.8409

e_new  = 0.8409 × 200 + 0.1591 × 250
       = 168.18 + 39.78
       = 207.96 Wh/km   (≈ 208)
```

**How the exponential moving average works.**
The obvious way to average recent driving would be to take the last few miles and average them evenly — but that has an awkward edge.
A measurement counts fully right up until it falls out of the window, then counts for nothing at all.
Drive past that boundary and the display lurches, for no reason connected to how you are driving.

An exponential moving average has no window and no boundary.
Instead of storing past measurements, it keeps a single running number and **nudges** it toward each new measurement:

```
new estimate = (old estimate × k) + (new measurement × (1 − k))
```

If <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>k</mi></mrow><annotation encoding="application/x-tex">k</annotation></semantics></math></span> were 0.9, each new measurement would move the estimate a tenth of the way toward itself and leave nine tenths of what was already there.
Nothing is ever dropped; older driving simply fades, its influence shrinking a little with every update.
That is what makes the display move smoothly instead of stepping.

**Why the nudge size depends on distance.**
A measurement covering 2 km deserves more say than one covering 300 m, so <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>k</mi></mrow><annotation encoding="application/x-tex">k</annotation></semantics></math></span> is not a fixed number — it is computed from the distance that window covered:

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mi>k</mi><mo>=</mo><msup><mn>0.5</mn><mrow><mtext> </mtext><mi mathvariant="normal">Δ</mi><mi>d</mi><mi mathvariant="normal">/</mi><mn>8</mn></mrow></msup></mrow><annotation encoding="application/x-tex">k = 0.5^{\,\Delta d / 8}</annotation></semantics></math></span>
</div>

Read it as: *every 8 km of driving cuts the influence of everything that came before it in half.* That is what "half-life" means here. Drive 8 km and the past counts half as much; drive another 8 and it counts a quarter as much. It never reaches zero — it just becomes too small to matter.

<div class="tablewrap" markdown="1">

| Distance since a measurement | Weight it still carries |
|---|---|
| 8 km (5 mi) | 50 % |
| 16 km (10 mi) | 25 % |
| 24 km (15 mi) | 12.5 % |
| 40 km (25 mi) | 3 % |

</div>

**What that looks like on the display.**
Suppose you have been driving in town at 150 Wh/km and you join the highway, where you settle at 200 Wh/km.
The figure does not jump to 200, and it does not wait and then snap — it slides:

<div class="tablewrap" markdown="1">

| After this much highway | Displayed |
|---|---|
| 0 km | 150 Wh/km |
| 4 km (2.5 mi) | 165 Wh/km |
| 8 km (5 mi) | 175 Wh/km |
| 16 km (10 mi) | 188 Wh/km |
| 24 km (15 mi) | 194 Wh/km |
| 40 km (25 mi) | 198 Wh/km |

</div>

Most of the change lands in the first ten miles, and the last few percent take a while — which is the intended behavior.
The number is meant to answer "how am I driving lately", so it should move decisively when your driving genuinely changes and ignore the fact that you just went up one hill.

**Why 8 km.**
It is long enough that a single hill, one traffic light, or a brief burst of acceleration cannot move the figure much, and short enough that a real change of road or driving style shows up within a few miles rather than at the end of the trip.

**Why weight by distance rather than time.** A 20-minute crawl through traffic and 20 minutes of highway cruising are not equally informative about the next 100 miles.
Distance weighting means a slow crawl cannot dominate the average, and a fast highway stretch is not underweighted just because it took less time.

**The plausibility band** (−200 to 5000 Wh/km) rejects readings that cannot be real.
The two ends guard different things, which is why they are not symmetric.
The low end is a physical limit on how much energy regeneration can return over a kilometer; anything beyond it is a data fault rather than a descent.
The high end has to be generous, because a genuinely large reading is easy to produce honestly: sit at a level crossing for twenty minutes with the climate running, then move off, and the first 300 meter carry twenty minutes' worth of energy.

**The 40 Wh/km limit** guards something different from the band above: the band bounds a single measurement, this bounds the running average itself.
Range is available energy divided by efficiency, so a long descent that dragged the average to zero would leave the division with no answer at all, and below zero it would produce a negative range.
The limit prevents that.

Whether it reads as a floor or a ceiling depends on your chosen unit — 40 Wh/km is the same limit as 15.5 mi/kWh — but on range it is always a ceiling: at that efficiency a 60 kWh pack would project around 1,500 km.

That figure is the point.
This is a mathematical guard, not a plausibility one: 40 Wh/km is about four times better than any production EV achieves, so if the average ever reaches the limit the range shown will be wildly optimistic — finite, but not to be relied on.
It recovers within a few miles of the road flattening out.

### 4.4 Where the estimate starts

The estimator is seeded from **your own last drive**, stored per vehicle (keyed by VIN) and saved every 10 seconds while driving:

```
if a stored value exists and is within 60…600 Wh/km  → seed from it
else                                                 → seed from 207 Wh/km (≈ 3.0 mi/kWh)
```

The stored seed is applied when nothing has been measured this drive (less than 0.2 km), so a VIN that resolves mid-drive cannot overwrite live measurement with yesterday's number.
The fixed 207 Wh/km baseline is only used as the first-ever-drive starting point.

### 4.5 One measurement, two spans

Both efficiency figures are built from the same two ingredients: the battery's available-energy reading and the distance engine.
The only thing that differs is the span each one covers.

<div class="tablewrap" markdown="1">

| | Trip efficiency | Rolling efficiency |
|---|---|---|
| Energy | Available-energy delta | Available-energy delta |
| Distance | The totalizer of §3.2 | The totalizer of §3.2 |
| Span | The whole drive, start to finish | A rolling weighted average of roughly the last 5 miles |
| Incomplete stretches | Accounted for and reported as coverage; the odometer can stand in | The affected window is abandoned |

</div>

That means the two numbers cannot disagree about *what was measured* — only about *how much of the drive they are describing*.
Finish a drive that started in city traffic and ended on the highway, and the trip figure will report the average of the whole thing while the rolling figure ends up near the highway portion. Both are right; they are answering different questions.

Earlier versions measured each of these two ways — the rolling estimate integrated volts × amps and summed GPS position hops, while the trip figure used the battery's reading and a speed integral.
Both differences have been removed, in that order.

---

## 5. Range {#s6}

### 5.1 The formula

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mtext>range (km)</mtext><mo>=</mo><mfrac><mrow><mi>A</mi><mo>×</mo><mn>1000</mn></mrow><mi>e</mi></mfrac></mrow><annotation encoding="application/x-tex">\text{range (km)} = \frac{A \times 1000}{e}</annotation></semantics></math></span>
</div>

where <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span> is the BMS's reported available pack energy in kWh and <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>e</mi></mrow><annotation encoding="application/x-tex">e</annotation></semantics></math></span> is the rolling efficiency in Wh/km.
In miles, multiply by 0.621371 — which the app does at display time, rounding to a whole unit.

**Worked example.** Available energy 52.0 kWh, rolling efficiency 185 Wh/km:

```
range = 52.0 × 1000 ÷ 185 = 281.1 km
      = 281.1 × 0.621371  = 174.7 mi   →  displayed as "175 mi"
```

### 5.2 Why the numerator is not SoC × capacity

A tempting alternative is <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mtext>range</mtext><mo>=</mo><mi>S</mi><mo>×</mo><msub><mi>C</mi><mtext>nominal</mtext></msub><mi mathvariant="normal">/</mi><mi>e</mi></mrow><annotation encoding="application/x-tex">\text{range} = S \times C_{\text{nominal}} / e</annotation></semantics></math></span>.
The app deliberately does not do this.
The BMS already publishes a matched SoC ↔ available-energy pair that embodies the pack's real capacity, its degradation over years of use, and its current temperature.
Multiplying a displayed percentage by a nameplate capacity discards all three and reintroduces a per-vehicle constant the app would have to maintain for every model and pack size it supports.

A useful consequence: because available energy comes from the pack, the range figure needs no per-vehicle capacity table at all.

**Both halves of the division use the same signal.** This is the quiet reason the range figure can be trusted. Efficiency is measured as *how fast available energy is falling per km* (§4.1), and range divides *available energy* by it. The question being answered is therefore exactly the right one: at the rate this number has actually been dropping, how far until it reaches zero?

Measuring the two halves against different definitions of energy — as an earlier version did, using volts × amps for efficiency — leaves whatever gap exists between those definitions sitting inside the range estimate. That gap was measured at −15 % to +11 % across recorded drives, and it varied by drive, so it could not have been calibrated out with a fixed correction. Sharing one signal removes it by construction rather than by adjustment.

### 5.3 When the number updates

Range has two independent inputs, and each refreshes it on its own schedule:

- **Efficiency** changes only while the vehicle is moving, and at most once a minute (§4.3).
- **Available energy** changes on every BMS poll — roughly every 30 seconds — including while parked and while charging.

So the range figure is live from the first BMS poll after the app connects, without needing any location data, and it climbs while you charge.
If the BMS has not reported energy yet (or reports 0.1 kWh or less), range renders as a dash rather than a guess.

---

## 6. Arrival state of charge {#s7}

When a route is active, the app shows the one number the car's own navigation cannot: the state of charge you should arrive with.

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><msub><mi>E</mi><mtext>needed</mtext></msub><mo>=</mo><mfrac><mrow><msub><mi>d</mi><mtext>remaining</mtext></msub><mo>×</mo><mi>e</mi></mrow><mn>1000</mn></mfrac><mtext> kWh</mtext></mrow><annotation encoding="application/x-tex">E_{\text{needed}} = \frac{d_{\text{remaining}} \times e}{1000}\ \text{kWh}</annotation></semantics></math></span>
</div>

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><msub><mi>S</mi><mtext>arrive</mtext></msub><mo>=</mo><mi>max</mi><mo>⁡</mo><mrow><mo fence="true">(</mo><mn>0</mn><mo separator="true">,</mo><mtext> </mtext><msub><mi>S</mi><mtext>now</mtext></msub><mo>×</mo><mrow><mo fence="true">(</mo><mn>1</mn><mo>−</mo><mfrac><msub><mi>E</mi><mtext>needed</mtext></msub><mi>A</mi></mfrac><mo fence="true">)</mo></mrow><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">S_{\text{arrive}} = \max\left(0,\ S_{\text{now}} \times \left(1 - \frac{E_{\text{needed}}}{A}\right)\right)</annotation></semantics></math></span>
</div>

The derivation is simple proportionality: <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>E</mi><mtext>needed</mtext></msub><mi mathvariant="normal">/</mi><mi>A</mi></mrow><annotation encoding="application/x-tex">E_{\text{needed}}/A</annotation></semantics></math></span> is the fraction of your remaining usable energy the trip will consume, so <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn><mo>−</mo><msub><mi>E</mi><mtext>needed</mtext></msub><mi mathvariant="normal">/</mi><mi>A</mi></mrow><annotation encoding="application/x-tex">1 - E_{\text{needed}}/A</annotation></semantics></math></span> is the fraction left, and scaling today's SoC by it gives the arrival SoC.
Because both terms come from the same BMS pair, **pack capacity cancels out** — the formula needs no capacity figure.

**Worked example.** SoC 68 %, available energy 52.0 kWh, 120 km remaining, efficiency 185 Wh/km:

```
E_needed = 120 × 185 ÷ 1000              = 22.2 kWh
fraction = 1 − 22.2 ÷ 52.0               = 0.5731
S_arrive = 68 × 0.5731                   = 38.97 →  displayed as "39 %"
```

<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>d</mi><mtext>remaining</mtext></msub></mrow><annotation encoding="application/x-tex">d_{\text{remaining}}</annotation></semantics></math></span> is the distance to the current turn plus the sum of all later steps, recomputed on every GPS fix by the app's own trip engine — so it keeps counting even when CarPlay's guidance panels are suspended.

**The projection is worked out once a minute, and what you see is an average of the last five.**

It is unusually sensitive to the efficiency figure: once a leg needs most of the pack, a 10 % change in efficiency moves the arrival estimate by around 5 percentage points.
Shown unsmoothed, that arrives as a single jump.
Averaging the last five minutes turns the same 5-point move into five 1-point steps.

The averaging costs less than it might appear, because **this figure does not drift as you drive**.
Drive at exactly the efficiency it assumes and it holds the same value the entire way: your state of charge falls, the energy left falls, and the distance still to go falls, and those changes cancel out.

<div class="tablewrap" markdown="1">

| After driving | Remaining | SoC now | Arrival SoC |
|---|---|---|---|
| 0 km | 120 km | 68 % | **39 %** |
| 40 km | 80 km | 58 % | **39 %** |
| 80 km | 40 km | 49 % | **39 %** |
| 120 km | 0 km | 39 % | **39 %** |

</div>

So the estimate only moves when your actual driving differs from what was predicted — which is exactly the change worth smoothing rather than reacting to instantly.
The real cost is response time: if conditions genuinely change, the arrival figure takes the full five minutes to catch up.

A new destination or a reroute starts a fresh average rather than blending two journeys.

The displayed value is tinted green at 20 % or above, amber from 10 % to 20 %, and red below 10 %.

---

## 7. Lifetime round-trip efficiency — a different number entirely {#s8}

On the phone Dashboard, under **Battery Odometer**, a percentage appears alongside two lifetime counters.
It is not a driving statistic:

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><msub><mi>η</mi><mtext>round-trip</mtext></msub><mo>=</mo><mfrac><msub><mi>D</mi><mtext>lifetime</mtext></msub><msub><mi>C</mi><mtext>lifetime</mtext></msub></mfrac><mo>×</mo><mn>100</mn><mtext> </mtext><mi mathvariant="normal">%</mi></mrow><annotation encoding="application/x-tex">\eta_{\text{round-trip}} = \frac{D_{\text{lifetime}}}{C_{\text{lifetime}}} \times 100\ \%</annotation></semantics></math></span>
</div>

where <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>D</mi></mrow><annotation encoding="application/x-tex">D</annotation></semantics></math></span> is `cumulativeEnergyDischarged` and <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>C</mi></mrow><annotation encoding="application/x-tex">C</annotation></semantics></math></span> is `cumulativeEnergyCharged`, both lifetime BMS counters from diagnostic identifier **0x0101**.

**Worked example.** 6,061 kWh discharged against 6,652 kWh charged:

```
η = 6061 ÷ 6652 × 100 = 91.1 %
```

This is the ratio of energy out to energy in over the pack's entire life.
The missing ~9 % is energy lost as heat inside the cells during charging and discharging — ordinary electrochemical loss, not a fault.
It tells you nothing about how you drive, and it is not used anywhere in the range calculation.

The figure appears only once both counters have been observed.
This matters more than it sounds: the two values arrive in the same message, with *charged* decoded first, so an unguarded calculation would compute <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>0</mn><mi mathvariant="normal">/</mi><mi>C</mi><mo>×</mo><mn>100</mn><mo>=</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">0 / C \times 100 = 0</annotation></semantics></math></span> on the first poll after every connection and record a spurious 0 %.

---

## 8. What the model deliberately does not do {#s9}

Being explicit about the limits is the honest way to present an estimate.

- **No route lookahead.** The estimate extrapolates "how you have been driving" over "the distance that remains".
  There is no elevation model, no speed-limit model, no weather model.
  It is least accurate at the start of a trip whose character differs sharply from the last few miles — a mountain pass right after city driving — and it self-corrects as the moving average absorbs the new pace and the remaining distance shrinks.
- **No odometer in the rolling estimate.** Whole-mile quantization is uselessly coarse against an 8 km averaging window: an entire half-life fits inside one odometer tick.
- **No SoC × nameplate-capacity arithmetic** anywhere (§5.2).
- **No reading of the car's own range estimate.** It is not available to the app.
- **Efficiency does not update while parked.** Only pack energy does.
  This is a design choice, not an oversight — nothing about your *driving* efficiency changes while stopped.
- **Efficiency updates at most once a minute, and only after 300 m.** Crawling in traffic, the figure holds its last value rather than reporting noise.
  A number that updated every second would look more responsive and mean less (§4.3).

---

## 9. Constants reference {#s10}

Every tunable that affects a number in this paper.

**Rolling efficiency estimator**

<div class="tablewrap" markdown="1">

| Constant | Value | Meaning |
|---|---|---|
| Cold-start baseline | 207 Wh/km | First-ever-drive seed (≈ 3.0 mi/kWh) |
| Seed plausibility band | 60–600 Wh/km | A stored value outside this is discarded |
| Seed cutoff | 0.2 km | Past this measured distance, a late seed is not applied |
| Persist cadence | 10 s | How often the estimate is saved while driving |
| EMA half-life | 8.0 km | The newest ~5 miles carry half the estimate |
| Confidence threshold | 1.6 km | Internal flag only; not surfaced |
| Unmeasured time allowed | 5 s | More than this inside a window abandons it |
| Minimum window time | 60 s | The estimate updates no more often than this |
| Minimum window distance | 0.3 km | Below this the window stays open |
| Minimum window energy | 0.05 kWh | Below this the window stays open |
| Plausibility band | −200 to 5000 Wh/km | Readings outside this cannot be real |
| Efficiency limit | 40 Wh/km | Bounds the running average so the range division always has an answer |

</div>

**Trip distance totalizer**

<div class="tablewrap" markdown="1">

| Constant | Value | Meaning |
|---|---|---|
| Doppler confidence gate | 2.0 m/s | Max stated speed uncertainty that still credits |
| Doppler freshness | 2.5 s | How long a good fix suppresses the vehicle-speed channel |
| Credit cap | 10 s | Max time one sample can retroactively claim |
| Stationary floor | 0.15 m/s | Below this: covered time, zero distance |
| Coverage floor | 0.80 | Below this, fall back to the odometer delta |

</div>

**Signals**

<div class="tablewrap" markdown="1">

| Signal | Source | Cadence | Resolution |
|---|---|---|---|
| Available energy | BMS diagnostic ID 0x0105 | 30 s | 0.002 kWh |
| State of charge | BMS diagnostic ID 0x0105 | 30 s | 0.5 % |
| Lifetime charged / discharged | BMS diagnostic ID 0x0101 | 3 s | 0.1 kWh |
| Vehicle speed | VCU | ~2.5–3 s | 1/64 km/h |
| GPS fixes | Mobile device | ~1 Hz while a drive session is active | — |

</div>

---

## 10. Reading the diagnostic log {#s11}

Testers who want to check the model against a real drive can record a diagnostic log (**Settings ▸ Diagnostics**).
Two tagged record types carry the whole story.

`[ENERGY]` — one state line every 30 seconds while moving:

```console
eff=185Wh/km (3.4 mi/kWh) range=281km conf=true dist=42.3km pendKm=0.18 pendKWh=0.031
soc=68.0% availE=52.014kWh folds=37 reanch=4 clamps=0 gaps=2 totKm=42.31
```

- `pendKm` / `pendKWh` — the window currently open: how much distance and energy have accrued toward the next update
- `folds` — how many windows have closed and entered the moving average
- `reanch` — windows abandoned because the distance half was spoiled (gap, long stop, or charging).
  A high count relative to `folds` means the drive was measured in fragments — worth knowing before trusting the figure
- `totKm` — the shared distance totalizer's running total, the same figure the trip distance is built from
- `clamps` — readings that fell outside the plausibility band.
  This should now be rare; it was routine when the estimate updated once per second
- `gaps` — tick gaps that forced a re-anchor

`availE` is logged to three decimals because that is the signal's real resolution.
An earlier version of this log rounded it to one decimal, which made the reading look far coarser than it is — a misreading that shaped the design until raw frames were decoded and checked.

A separate banner records every constant in §9 at the moment recording starts, so an old log stays interpretable after the constants are retuned.

`[GPSDIST]` — one line per session close, recording the distance decision:

```console
[GPSDIST] close integ=42.031km cov=96% odoDelta=41.843km chose=INTEGRAL → distanceKm=42.031
```

The choice between the integral and the odometer is never silent.

---

## Appendix — where this lives in the code {#s12}

For testers reading alongside the source:

<div class="tablewrap" markdown="1">

| Topic | File |
|---|---|
| Rolling efficiency, range, arrival SoC | `Ioniq5/CarPlayV2/EnergyPaceEstimator.swift` |
| Trip distance totalizer | `Ioniq5/Vehicle/DriveLocationPipeline.swift` (`DriveDistanceAccumulator`) |
| Trip energy, lifetime round-trip | `Ioniq5/Vehicle/VehicleDataService.swift` (`netEnergyUsedKWh`, `lifetimeEfficiencyPercent`) |
| Close-time distance policy | `Ioniq5/History/HistoryRecorder.swift` (`closedDistanceKm`) |
| Display-unit conversion | `Ioniq5/Views/SettingsView.swift` (`efficiencyValue`) |
| Design record for trip distance | `docs/adr/0023-drive-distance-gps-primary-via-location-pipeline.md` |
| Design record for range | `docs/2026-07-13-carplay-range-estimation-design.md` |

</div>
