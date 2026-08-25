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
    n: ""
    label: "Part 1 — What the app shows you"
  - id: s3
    n: ""
    label: "The Range & Efficiency tile"
  - id: s4
    n: ""
    label: "Estimated arrival state of charge"
  - id: s5
    n: ""
    label: "Your efficiency for a drive"
  - id: s6
    n: ""
    label: "Which number answers which question"
  - id: s7
    n: ""
    label: "Part 2 — How the numbers are calculated"
  - id: s8
    n: "1"
    label: "Notation and units"
  - id: s9
    n: "2"
    label: "Three efficiency values, one of them invisible"
  - id: s10
    n: "3"
    label: "Trip efficiency"
  - id: s11
    n: "4"
    label: "Rolling efficiency"
  - id: s12
    n: "5"
    label: "Range"
  - id: s13
    n: "6"
    label: "Arrival state of charge"
  - id: s14
    n: "7"
    label: "What the model does not do"
  - id: s15
    n: "8"
    label: "Constants reference"
  - id: s16
    n: "9"
    label: "Reading the drive recorder log"
---

<!-- =========================================================
     GENERATED FILE — DO NOT EDIT.
     Edits here are lost on the next build.
     Source:  docs/efficiency-and-range/efficiency-and-range.src.md
     Rebuild: cd docs/efficiency-and-range && node render.mjs
     ========================================================= -->
# How EV Dashboard measures efficiency and estimates range

*A walkthrough of the math, written for owners and testers who want to know exactly what the numbers on screen are made of.*

**Version:** 2026-08-25 · **Applies to:** app version 3.0 (build 146) and later

---

## Overview {#s1}

Your vehicle already shows a range distance and rolling efficiency on the instrument cluster, but I have found that very often these values do not match what I attained in real-world driving. I wanted to see if I could improve upon this, plus I wanted to enable some new features such as estimating your arrival state of charge (SoC) during a journey.

*A caveat while it is fresh: the range estimates in my new 2026 IONIQ 5 seem better — my early impression is that they land closer to actual obtained range than I experienced with my 2024 IONIQ 5 — though I need to spend more time with the 2026 to form a more informed opinion.*

Several new capabilities have been added to EV Dashboard. The app derives range and efficiency from signals it polls out of the battery management system (BMS) and the vehicle control unit (VCU), combined with GPS signals from your mobile device. Part 1 shows each of them on screen; Part 2 works through the math behind them.

This paper explains what the app's numbers actually mean and how they are calculated, so you can judge which one is answering the question you are asking.

---

## Part 1 — What the app shows you {#s2}

## The Range & Efficiency tile {#s3}

Most of the app's driving work ends up on one tile. It lives on the CarPlay dashboard, in whichever slot you have put it.

![The Range and Efficiency tile ringed in green in the top-right slot of the CarPlay dashboard, among fifteen other tiles]({{ '/assets/images/efficiency-and-range/dashboard-where.png' | relative_url }})

It is carrying three things at once: how far you can go, how efficiently you are going, and how that efficiency has been trending.

![The Range tile enlarged, with five labels. One, the range remaining. Two, your efficiency right now. Three, green marks stretches better than your recent average. Four, the dashed line is that average. Five, the dot is the present moment, amber here because you were fractionally worse than your average while still returning a healthy 3.4 miles per kilowatt-hour]({{ '/assets/images/efficiency-and-range/range-tile.png' | relative_url }})

### The trend line compares you against yourself

The green-and-amber trend line is the part most worth explaining.

The dashed line running across it is **your own average over the fifteen minutes on display**. It is not a factory figure, not a target, and not your lifetime average. Green marks the stretches where you were beating that average and amber the stretches where you were not — and that holds whichever efficiency unit you have chosen. If you display miles per kWh, better means higher, so green sits above the line; if you display Wh/km or kWh/100km, better means lower, and green sits below it. Green always means *better than you had been doing*, so you never have to remember which direction is good for your unit.

Two things are worth knowing before you read too much into the shape:

- **There is no fixed scale, and no zero.** The trend line stretches vertically to fit whatever is currently in it, so a very steady drive and a wildly varying one can look about equally dramatic. Read the trend line for the pattern — am I trending better or worse, and where did that turn? — and read the number above it for the value.
- **The average you are measured against moves.** Because the dashed line is the average of the very stretch being coloured, there is always some green and some amber. You cannot drive your way to an all-green trend line, and a long, efficient descent will drag the average down far enough to turn ordinary cruising amber.

What reliably moves it: hills, speed, outside temperature, cabin heating or cooling, and stop-and-go traffic. A long descent on regenerative braking can push it deep into green.

If the trend line is blank, it simply has not collected enough yet. It needs a couple of minutes of driving, fills in from the left, and a short stop does not wipe it.

---

## Estimated arrival state of charge {#s4}

Set a destination and the app will tell you what it expects to be left in the pack when you get there.

![The CarPlay navigation map with three labels. One, the estimated arrival state of charge capsule reading 67 percent. Two, the Range tile showing the near-term efficiency the projection is built from. Three, the remaining trip distance of 2.8 miles]({{ '/assets/images/efficiency-and-range/arrival-soc.png' | relative_url }})

The arithmetic is deliberately plain: the app takes the pace you have actually been driving, carries it forward over the distance still to go, and subtracts the result from what is in the pack now. There is no route lookahead behind it — no elevation model, no speed limits, no weather.

That has a practical consequence worth internalising. The estimate is at its weakest at the very start of a journey whose character is about to change — a mountain pass immediately after city driving is the classic case — and it corrects itself as you go, because the pace it is extrapolating from catches up with the new road while the distance it is extrapolating over shrinks. A number that looks alarming in the first mile is usually worth re-reading five miles later.

---

## Your efficiency for a drive {#s5}

When a drive ends, the app records it. Opening it in History gives you the whole-drive figure.

![A completed driving session on the phone with four labels. One, the efficiency for the whole drive, 3.9 miles per kilowatt-hour. Two, the state of charge at the start and the end. Three, the distance measured by the app. Four, the energy read from the pack]({{ '/assets/images/efficiency-and-range/drive-summary.png' | relative_url }})

This is a different number from the one the tile was showing while you drove, and the difference is the point. The tile answers *how am I driving right now*, over roughly the last few miles. The session answers *how efficient was that drive*, over all of it. A drive that started cold and finished on a warm highway will show a session figure somewhere between the two extremes the tile passed through.

One detail that trips people up: the three numbers here are rounded independently for display, and the efficiency is worked out before any of that happens. Above, 4.0 mi divided by 1.0 kWh looks like it should read 4.0 — but the drive used a little over 1 kWh, which displays as "1.0", while the efficiency is calculated from the full figure. Rounding once at the end is deliberate: working from the already-rounded numbers would make the efficiency itself less accurate. The gap only shows on very short drives, where a hundredth of a kWh is a large share of the total.

---

## Which number answers which question {#s6}

There are three efficiency figures which represent different things.

<div class="tablewrap" markdown="1">

| Number | Where you see it | What it answers |
|---|---|---|
| **Trip efficiency** | History ▸ a driving session | "How efficient was *that drive*?" |
| **Near-term efficiency** | The Range tile and its trend line | "How efficient am I driving *right now*?" |
| **Long-term efficiency** | *Nowhere — it divides into Range and arrival SoC* | "What should I expect over the miles ahead?" |

</div>

The third one never appears on screen anywhere, and it is the one that moves your range. Part 2 explains why the app keeps two horizons of the same measurement rather than one.

---

## Part 2 — How the numbers are calculated {#s7}

## 1. Notation and units {#s8}

The app works internally in **metric canonical units** and converts only at display time.

<div class="tablewrap" markdown="1">

| Symbol | Meaning | Canonical unit |
|---|---|---|
| <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>E</mi></mrow><annotation encoding="application/x-tex">E</annotation></semantics></math></span> | Energy | kilowatt-hours (kWh) |
| <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>d</mi></mrow><annotation encoding="application/x-tex">d</annotation></semantics></math></span> | Distance | kilometres (km) |
| <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi></mrow><annotation encoding="application/x-tex">P</annotation></semantics></math></span> | Pack power | kilowatts (kW) |
| <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>e</mi></mrow><annotation encoding="application/x-tex">e</annotation></semantics></math></span> | Near-term efficiency (consumption form) | watt-hours per kilometre (Wh/km) |
| <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>e</mi><mtext>long</mtext></msub></mrow><annotation encoding="application/x-tex">e_{\text{long}}</annotation></semantics></math></span> | Long-term efficiency — the range divisor (§4.4) | watt-hours per kilometre (Wh/km) |
| <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span> | State of charge | percent (%) |
| <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span> | Available pack energy | kWh |

</div>

The single conversion constant used throughout:

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mn>1</mn><mtext> mile</mtext><mo>=</mo><mn>1.609344</mn><mtext> km</mtext><mspace width="2em"/><mspace width="2em"/><mn>1</mn><mtext> km</mtext><mo>=</mo><mn>0.621371</mn><mtext> miles</mtext></mrow><annotation encoding="application/x-tex">1\ \text{mile} = 1.609344\ \text{km}
\qquad\qquad
1\ \text{km} = 0.621371\ \text{miles}</annotation></semantics></math></span>
</div>

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

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mtable rowspacing="0.25em" columnalign="right left right left" columnspacing="0em 1em 0em"><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mtext>mi/kWh</mtext></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>621.371</mn><mo>÷</mo><mn>185</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>3.4</mn></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mtext>km/kWh</mtext></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>1000</mn><mo>÷</mo><mn>185</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>5.4</mn></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mtext>kWh/100km</mtext></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>185</mn><mo>÷</mo><mn>10</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>18.5</mn></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mtext>Wh/mi</mtext></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>185</mn><mo>×</mo><mn>1.609344</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>298</mn></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mtext>Wh/km</mtext></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>185</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>185</mn></mrow></mstyle></mtd></mtr></mtable><annotation encoding="application/x-tex">\begin{aligned}
\text{mi/kWh}    &amp;= 621.371 \div 185   &amp;&amp; = 3.4 \\
\text{km/kWh}    &amp;= 1000 \div 185      &amp;&amp; = 5.4 \\
\text{kWh/100km} &amp;= 185 \div 10        &amp;&amp; = 18.5 \\
\text{Wh/mi}     &amp;= 185 \times 1.609344 &amp;&amp; = 298 \\
\text{Wh/km}     &amp;= 185                &amp;&amp; = 185
\end{aligned}</annotation></semantics></math></span>
</div>

The two "rate" forms (distance per energy) improve as they rise; the three "consumption" forms (energy per distance) improve as they fall.
The app tracks that polarity so the CarPlay trend line tints green for "better than your recent average" in whichever unit you picked.

Rounding: Wh/mi and Wh/km display as whole numbers; the other three display to one decimal.

---

## 2. Three efficiency values, one of them invisible {#s9}

Part 1 set out the three figures and where each one appears. Two of them you can see; the third never appears on screen, but it is the one that moves your range.

All three are consumption figures (energy per distance), and all three read energy from the same place — the battery's own account of how much usable energy it has left.
They differ only in the span they cover: one whole drive, the last few miles, or a horizon several times longer than that.
Near-term and long-term are computed from exactly the same measurements and differ by a single constant; §4.4 explains why the app keeps both.

---

## 3. Trip efficiency {#s10}

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

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mi>A</mi><mtext> </mtext><mo stretchy="false">(</mo><mtext>kWh</mtext><mo stretchy="false">)</mo><mo>=</mo><msub><mtext>raw</mtext><mrow><mn>16</mn><mtext>-bit</mtext></mrow></msub><mo>×</mo><mn>2</mn><mo>÷</mo><mn>1000</mn></mrow><annotation encoding="application/x-tex">A\ (\text{kWh}) = \text{raw}_{16\text{-bit}} \times 2 \div 1000</annotation></semantics></math></span>
</div>

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

**Worked micro-example.** Cursor anchored at <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>t</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">t = 0</annotation></semantics></math></span> with <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>v</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">v = 0</annotation></semantics></math></span>; times in seconds, speeds in m/s:

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mtable rowspacing="0.25em" columnalign="right left right left" columnspacing="0em 1em 0em"><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mi>t</mi><mo lspace="0em" rspace="0em">=</mo><mn>1.0</mn><mo separator="true">,</mo><mtext> </mtext><mi>v</mi><mo lspace="0em" rspace="0em">=</mo><mn>8.0</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>→</mo><mtext> </mtext><mover accent="true"><mi>v</mi><mo>ˉ</mo></mover><mo>=</mo><mstyle scriptlevel="0" displaystyle="false"><mfrac><mrow><mn>0</mn><mo>+</mo><mn>8.0</mn></mrow><mn>2</mn></mfrac></mstyle><mo>=</mo><mn>4.0</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>→</mo><mtext> </mtext><mn>4.0</mn><mo>×</mo><mn>1.0</mn><mo>=</mo><mn>4.0</mn><mtext> m</mtext></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mi>t</mi><mo lspace="0em" rspace="0em">=</mo><mn>2.0</mn><mo separator="true">,</mo><mtext> </mtext><mi>v</mi><mo lspace="0em" rspace="0em">=</mo><mn>9.0</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>→</mo><mtext> </mtext><mover accent="true"><mi>v</mi><mo>ˉ</mo></mover><mo>=</mo><mstyle scriptlevel="0" displaystyle="false"><mfrac><mrow><mn>8.0</mn><mo>+</mo><mn>9.0</mn></mrow><mn>2</mn></mfrac></mstyle><mo>=</mo><mn>8.5</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>→</mo><mtext> </mtext><mn>8.5</mn><mo>×</mo><mn>1.0</mn><mo>=</mo><mn>8.5</mn><mtext> m</mtext></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mphantom><mo>→</mo><mtext> </mtext></mphantom><mtext>total</mtext><mo>=</mo><mn>12.5</mn><mtext> m</mtext><mo>=</mo><mn>0.0125</mn><mtext> km</mtext></mrow></mstyle></mtd></mtr></mtable><annotation encoding="application/x-tex">\begin{aligned}
t{=}1.0,\ v{=}8.0
  &amp;\rightarrow\ \bar{v} = \tfrac{0 + 8.0}{2} = 4.0
  &amp;&amp;\rightarrow\ 4.0 \times 1.0 = 4.0\ \text{m} \\[2pt]
t{=}2.0,\ v{=}9.0
  &amp;\rightarrow\ \bar{v} = \tfrac{8.0 + 9.0}{2} = 8.5
  &amp;&amp;\rightarrow\ 8.5 \times 1.0 = 8.5\ \text{m} \\[4pt]
  &amp; &amp;&amp;\phantom{\rightarrow\ } \text{total} = 12.5\ \text{m} = 0.0125\ \text{km}
\end{aligned}</annotation></semantics></math></span>
</div>

### 3.3 Coverage, and when the odometer gets a vote

At session close the app computes how much of the drive it actually measured:

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mtext>coverage</mtext><mo>=</mo><mfrac><mrow><msub><mi>t</mi><mtext>doppler</mtext></msub><mo>+</mo><msub><mi>t</mi><mtext>wheel</mtext></msub><mo>+</mo><msub><mi>t</mi><mtext>stationary</mtext></msub></mrow><mrow><msub><mi>t</mi><mtext>doppler</mtext></msub><mo>+</mo><msub><mi>t</mi><mtext>wheel</mtext></msub><mo>+</mo><msub><mi>t</mi><mtext>stationary</mtext></msub><mo>+</mo><msub><mi>t</mi><mtext>gap</mtext></msub></mrow></mfrac></mrow><annotation encoding="application/x-tex">\text{coverage} = \frac{t_{\text{doppler}} + t_{\text{wheel}} + t_{\text{stationary}}}
{t_{\text{doppler}} + t_{\text{wheel}} + t_{\text{stationary}} + t_{\text{gap}}}</annotation></semantics></math></span>
</div>

Then a single decision:

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mtable rowspacing="0.25em" columnalign="right left right left" columnspacing="0em 1em 0em"><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mrow><mtext mathvariant="bold">if</mtext><mtext> </mtext></mrow><mtext>coverage</mtext><mo>≥</mo><mn>0.80</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>→</mo><mtext> use the integral</mtext></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mrow><mtext mathvariant="bold">else</mtext><mtext> </mtext><mtext mathvariant="bold">if</mtext><mtext> </mtext></mrow><mtext>odometer delta</mtext><mo>&gt;</mo><mn>0</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>→</mo><mtext> use end odometer</mtext><mo>−</mo><mtext>start odometer</mtext></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mtext mathvariant="bold">else</mtext></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>→</mo><mtext> use the partial integral</mtext></mrow></mstyle></mtd></mtr></mtable><annotation encoding="application/x-tex">\begin{aligned}
&amp;\textbf{if } \text{coverage} \ge 0.80
  &amp;&amp; \rightarrow\ \text{use the integral} \\
&amp;\textbf{else if } \text{odometer delta} &gt; 0
  &amp;&amp; \rightarrow\ \text{use end odometer} - \text{start odometer} \\
&amp;\textbf{else}
  &amp;&amp; \rightarrow\ \text{use the partial integral}
\end{aligned}</annotation></semantics></math></span>
</div>

**Worked example.** A 37-minute drive attributes 1,510 s to Doppler, 240 s to vehicle speed, 380 s stationary, 95 s gap:

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mtable rowspacing="0.25em" columnalign="right left" columnspacing="0em"><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mtext>coverage</mtext></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mo stretchy="false">(</mo><mn>1510</mn><mo>+</mo><mn>240</mn><mo>+</mo><mn>380</mn><mo stretchy="false">)</mo><mo>÷</mo><mo stretchy="false">(</mo><mn>1510</mn><mo>+</mo><mn>240</mn><mo>+</mo><mn>380</mn><mo>+</mo><mn>95</mn><mo stretchy="false">)</mo></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>2130</mn><mo>÷</mo><mn>2225</mn></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>0.957</mn><mspace width="1em"/><mo>→</mo><mspace width="1em"/><mn>95.7</mn><mtext> </mtext><mi mathvariant="normal">%</mi><mtext> </mtext><mo>≥</mo><mtext> </mtext><mn>80</mn><mtext> </mtext><mi mathvariant="normal">%</mi><mspace width="1em"/><mo>→</mo><mspace width="1em"/><mtext>the integral is used</mtext></mrow></mstyle></mtd></mtr></mtable><annotation encoding="application/x-tex">\begin{aligned}
\text{coverage} &amp;= (1510 + 240 + 380) \div (1510 + 240 + 380 + 95) \\
                &amp;= 2130 \div 2225 \\
                &amp;= 0.957 \quad\rightarrow\quad 95.7\ \% \ \ge\ 80\ \%
                   \quad\rightarrow\quad \text{the integral is used}
\end{aligned}</annotation></semantics></math></span>
</div>

**Why the odometer is inadequate as the primary source.** The car’s odometer signal reports in whole miles or whole kilometers.
A real-world short 1.443 km errand quantizes to 1.609 km — an 11 % error on that trip, and much worse on shorter ones.
Measured on one verification drive (2026-07-21), the integral gave 1.443 km against a 1.609 km odometer delta, with 98 % coverage.
The odometer is therefore a coverage-gated *fallback*, never an arbiter of a well-measured drive.

### 3.4 Putting it all together

**Sample trip.** Available energy 61.4 kWh when the car was put into gear, 53.3 kWh at ignition-off; the integral measured 42.0 km at 96 % coverage.

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mtable rowspacing="0.25em" columnalign="right left right left" columnspacing="0em 1em 0em"><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mi>E</mi></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>61.4</mn><mo>−</mo><mn>53.3</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>8.1</mn><mtext> kWh</mtext></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mi>d</mi></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>42.0</mn><mtext> km</mtext></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mphantom><mo>=</mo></mphantom><mtext>  (coverage</mtext><mo>≥</mo><mn>80</mn><mtext> </mtext><mi mathvariant="normal">%</mi><mo separator="true">,</mo><mtext> integral used)</mtext></mrow></mstyle></mtd></mtr></mtable><annotation encoding="application/x-tex">\begin{aligned}
E &amp;= 61.4 - 53.3 &amp;&amp; = 8.1\ \text{kWh} \\
d &amp;= 42.0\ \text{km} &amp;&amp; \phantom{=}\ \ \text{(coverage} \ge 80\ \%,\ \text{integral used)}
\end{aligned}</annotation></semantics></math></span>
</div>

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mtable rowspacing="0.25em" columnalign="right left right left" columnspacing="0em 1em 0em"><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mtext>km/kWh</mtext></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>42.0</mn><mo>÷</mo><mn>8.1</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>5.2</mn></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mtext>mi/kWh</mtext></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mo stretchy="false">(</mo><mn>42.0</mn><mo>×</mo><mn>0.621371</mn><mo stretchy="false">)</mo><mo>÷</mo><mn>8.1</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>3.2</mn></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mtext>kWh/100km</mtext></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>8.1</mn><mo>÷</mo><mn>42.0</mn><mo>×</mo><mn>100</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>19.3</mn></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mtext>Wh/km</mtext></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>8.1</mn><mo>×</mo><mn>1000</mn><mo>÷</mo><mn>42.0</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>193</mn></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mtext>Wh/mi</mtext></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>8.1</mn><mo>×</mo><mn>1000</mn><mo>÷</mo><mo stretchy="false">(</mo><mn>42.0</mn><mo>×</mo><mn>0.621371</mn><mo stretchy="false">)</mo></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>310</mn></mrow></mstyle></mtd></mtr></mtable><annotation encoding="application/x-tex">\begin{aligned}
\text{km/kWh}    &amp;= 42.0 \div 8.1                            &amp;&amp; = 5.2 \\
\text{mi/kWh}    &amp;= (42.0 \times 0.621371) \div 8.1          &amp;&amp; = 3.2 \\
\text{kWh/100km} &amp;= 8.1 \div 42.0 \times 100                 &amp;&amp; = 19.3 \\
\text{Wh/km}     &amp;= 8.1 \times 1000 \div 42.0                &amp;&amp; = 193 \\
\text{Wh/mi}     &amp;= 8.1 \times 1000 \div (42.0 \times 0.621371) &amp;&amp; = 310
\end{aligned}</annotation></semantics></math></span>
</div>

During the drive the app shows the running integral live; the coverage gate is applied once, when the session ends.

---

## 4. Rolling efficiency {#s11}

Rolling efficiency is a *rate* that reflects how you are driving now rather than how you drove an hour ago.
This is a separate estimator with its own energy and distance measurements.

Everything in §4.1 to §4.3 describes a single measurement pipeline: one window, one sample, one plausibility band.
Section 4.4 is where that single stream becomes the **two** figures of §2 — near-term and long-term — which differ only in how quickly each forgets.

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

**When a window is abandoned.**
A window is only abandoned when *both* the phone's GPS and the car's speed signal go quiet at once.

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

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mtable rowspacing="0.25em" columnalign="right left right left" columnspacing="0em 1em 0em"><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><msub><mi>e</mi><mtext>old</mtext></msub></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>200</mn><mtext> Wh/km</mtext></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mtext>sample</mtext></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>0.5</mn><mo>×</mo><mn>1000</mn><mo>÷</mo><mn>2.0</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>250</mn><mtext> Wh/km</mtext></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mi>k</mi></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><msup><mn>0.5</mn><mrow><mtext> </mtext><mn>2.0</mn><mo>÷</mo><mn>8.0</mn></mrow></msup></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>0.8409</mn></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><msub><mi>e</mi><mtext>new</mtext></msub></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>0.8409</mn><mo>×</mo><mn>200</mn><mo>+</mo><mn>0.1591</mn><mo>×</mo><mn>250</mn></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>168.18</mn><mo>+</mo><mn>39.78</mn></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>207.96</mn><mtext> Wh/km</mtext><mspace width="1em"/><mo stretchy="false">(</mo><mo>≈</mo><mn>208</mn><mo stretchy="false">)</mo></mrow></mstyle></mtd></mtr></mtable><annotation encoding="application/x-tex">\begin{aligned}
e_{\text{old}} &amp;= 200\ \text{Wh/km} \\[4pt]
\text{sample}  &amp;= 0.5 \times 1000 \div 2.0 &amp;&amp; = 250\ \text{Wh/km} \\
k              &amp;= 0.5^{\,2.0 \div 8.0}     &amp;&amp; = 0.8409 \\[4pt]
e_{\text{new}} &amp;= 0.8409 \times 200 + 0.1591 \times 250 \\
               &amp;= 168.18 + 39.78 \\
               &amp;= 207.96\ \text{Wh/km} \quad (\approx 208)
\end{aligned}</annotation></semantics></math></span>
</div>

**How the exponential moving average works.**
The obvious way to average recent driving would be to take the last few miles and average them evenly — but that has an awkward edge.
A measurement counts fully right up until it falls out of the window, then counts for nothing at all.
Drive past that boundary and the display lurches, for no reason connected to how you are driving.

An exponential moving average has no window and no boundary.
Instead of storing past measurements, it keeps a single running number and **nudges** it toward each new measurement:

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mtext>new estimate</mtext><mo>=</mo><mo stretchy="false">(</mo><mtext>old estimate</mtext><mo>×</mo><mi>k</mi><mo stretchy="false">)</mo><mo>+</mo><mo fence="true" stretchy="true" minsize="1.2em" maxsize="1.2em">(</mo><mtext>new measurement</mtext><mo>×</mo><mo stretchy="false">(</mo><mn>1</mn><mo>−</mo><mi>k</mi><mo stretchy="false">)</mo><mo fence="true" stretchy="true" minsize="1.2em" maxsize="1.2em">)</mo></mrow><annotation encoding="application/x-tex">\text{new estimate} = (\text{old estimate} \times k) + \bigl(\text{new measurement} \times (1 - k)\bigr)</annotation></semantics></math></span>
</div>

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

### 4.4 Two horizons from one measurement

Everything above produces one sample per closed window.
That sample is folded **twice**, into two running averages that differ only in half-life:

<div class="tablewrap" markdown="1">

| | Half-life | Where it goes |
|---|---|---|
| **Near-term** <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>e</mi></mrow><annotation encoding="application/x-tex">e</annotation></semantics></math></span> | 8 km | The efficiency number on the Range tile, and the trend line beneath it |
| **Long-term** <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>e</mi><mtext>long</mtext></msub></mrow><annotation encoding="application/x-tex">e_{\text{long}}</annotation></semantics></math></span> | 60 km | The range figure (§5) and arrival state of charge (§6) |

</div>

There is no second measurement and no second window — the same energy, the same distance, the same plausibility band and limit.
Only the blending constant differs.

**Why two.**
An efficiency readout and a range estimate are answering different questions, and the honest answer to each has a different shape.
"How am I driving?" is about the last few miles, and should move when the road changes.
"How far can I get?" is about the miles ahead, and a figure that lurches every time you crest a hill is not describing them.

A round trip on 1 August 2026 made the cost of conflating them concrete.
The two legs covered the same road within a few hours of each other, and their true whole-drive efficiencies were **169 and 168 Wh/km** — the same drive, twice.
The 8 km average *finished* those legs reading **147 and 202 Wh/km**, because one ended on a highway descent and the other on town streets.
Neither reading was wrong about the miles it described.
Both were poor divisors for the pack.

Dividing by them produced a range figure that rose by a total of **462 km** on the outbound leg and **346 km** on the return, in individual jumps as large as **85 km** — while the car was being driven steadily in one direction.
On the same drives, the 60 km average holds those totals to **49 km** and **40 km**, with worst jumps of **4 km** and **11 km**.

**What it costs.**
A genuine, sustained change of conditions — a mountain pass, a headwind, winter — takes about 60 km to half-register in the range figure.
That is the deliberate trade: the near-term number still shows such a change within a few miles, so the information is on screen immediately, just not in the division.

**A consequence worth expecting.**
The efficiency number and the range can now move independently, and sometimes visibly disagree — efficiency dropping while range holds steady.
That is the design working, not a fault.

### 4.5 Where the estimate starts

The estimator is seeded from **your own last drive**, stored per vehicle (keyed by VIN) and saved every 10 seconds while driving:

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mtable rowspacing="0.25em" columnalign="right left right left" columnspacing="0em 1em 0em"><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mrow><mtext mathvariant="bold">if</mtext><mtext> </mtext></mrow><mtext>stored value within </mtext><mn>60</mn><mo>…</mo><mn>600</mn><mtext> Wh/km</mtext></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>→</mo><mtext> seed from it</mtext></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mtext mathvariant="bold">else</mtext></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>→</mo><mtext> seed from </mtext><mn>207</mn><mtext> Wh/km</mtext></mrow></mstyle></mtd></mtr></mtable><annotation encoding="application/x-tex">\begin{aligned}
&amp;\textbf{if } \text{stored value within } 60\ldots600\ \text{Wh/km}
  &amp;&amp; \rightarrow\ \text{seed from it} \\
&amp;\textbf{else}
  &amp;&amp; \rightarrow\ \text{seed from } 207\ \text{Wh/km}
\end{aligned}</annotation></semantics></math></span>
</div>

The stored seed is applied when nothing has been measured this drive (less than 0.2 km), so a VIN that resolves mid-drive cannot overwrite live measurement with yesterday's number.
The fixed 207 Wh/km baseline is only used as the first-ever-drive starting point.

### 4.6 One measurement, two spans

Both efficiency figures are built from the same two ingredients: the battery's available-energy reading and the distance engine.
The only thing that differs is the span each one covers.

<div class="tablewrap" markdown="1">

| | Trip efficiency | Near-term efficiency |
|---|---|---|
| Energy | Available-energy delta | Available-energy delta |
| Distance | The totalizer of §3.2 | The totalizer of §3.2 |
| Span | The whole drive, start to finish | A rolling weighted average of roughly the last 5 miles |
| Long-term twin | — | The same stream at a 60 km half-life (§4.4) |
| Incomplete stretches | Accounted for and reported as coverage; the odometer can stand in | The affected window is abandoned |

</div>

That means the two numbers cannot disagree about *what was measured* — only about *how much of the drive they are describing*.
Finish a drive that started in city traffic and ended on the highway, and the trip figure will report the average of the whole thing while the near-term figure ends up near the highway portion. Both are right; they are answering different questions.

---

## 5. Range {#s12}

### 5.1 The formula

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mtext>range (km)</mtext><mo>=</mo><mfrac><mrow><mi>A</mi><mo>×</mo><mn>1000</mn></mrow><msub><mi>e</mi><mtext>long</mtext></msub></mfrac></mrow><annotation encoding="application/x-tex">\text{range (km)} = \frac{A \times 1000}{e_{\text{long}}}</annotation></semantics></math></span>
</div>

where <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span> is the BMS's reported available pack energy in kWh and <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>e</mi><mtext>long</mtext></msub></mrow><annotation encoding="application/x-tex">e_{\text{long}}</annotation></semantics></math></span> is the **long-term** efficiency in Wh/km — the 60 km average of §4.4, not the number shown beside the range.
In miles, multiply by 0.621371 — which the app does at display time, rounding to a whole unit.

**Worked example.** Available energy 52.0 kWh, long-term efficiency 185 Wh/km:

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mtable rowspacing="0.25em" columnalign="right left right left" columnspacing="0em 1em 0em"><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mtext>range</mtext></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>52.0</mn><mo>×</mo><mn>1000</mn><mo>÷</mo><mn>185</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>281.1</mn><mtext> km</mtext></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>281.1</mn><mo>×</mo><mn>0.621371</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>174.7</mn><mtext> mi</mtext></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>→</mo><mtext> displayed as “175 mi”</mtext></mrow></mstyle></mtd></mtr></mtable><annotation encoding="application/x-tex">\begin{aligned}
\text{range} &amp;= 52.0 \times 1000 \div 185 &amp;&amp; = 281.1\ \text{km} \\
             &amp;= 281.1 \times 0.621371     &amp;&amp; = 174.7\ \text{mi} \\[2pt]
             &amp;                            &amp;&amp; \rightarrow\ \text{displayed as ``175 mi&#x27;&#x27;}
\end{aligned}</annotation></semantics></math></span>
</div>

### 5.2 When the number updates

Range has two independent inputs, and each refreshes it on its own schedule:

- **Long-term efficiency** changes only while the vehicle is moving, and at most once a minute (§4.3). Each update moves it slightly, because a single window is a small fraction of a 60 km half-life (§4.4).
- **Available energy** changes on every BMS poll — roughly every 30 seconds — including while parked and while charging.

Between the two, available energy is now the faster-moving term, which is why the range figure reads as a countdown: most of what you see is the pack draining, not the model changing its mind.

So the range figure is live from the first BMS poll after the app connects, without needing any location data, and it climbs while you charge. If the BMS has not reported energy yet (or reports 0.1 kWh or less), range renders as a dash rather than a guess.

---

## 6. Arrival state of charge {#s13}

When a route is active, the app shows the one number the car's own navigation cannot: the state of charge you should arrive with.

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><msub><mi>E</mi><mtext>needed</mtext></msub><mo>=</mo><mfrac><mrow><msub><mi>d</mi><mtext>remaining</mtext></msub><mo>×</mo><msub><mi>e</mi><mtext>long</mtext></msub></mrow><mn>1000</mn></mfrac><mtext> kWh</mtext></mrow><annotation encoding="application/x-tex">E_{\text{needed}} = \frac{d_{\text{remaining}} \times e_{\text{long}}}{1000}\ \text{kWh}</annotation></semantics></math></span>
</div>

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><msub><mi>S</mi><mtext>arrive</mtext></msub><mo>=</mo><mi>max</mi><mo>⁡</mo><mrow><mo fence="true">(</mo><mn>0</mn><mo separator="true">,</mo><mtext> </mtext><msub><mi>S</mi><mtext>now</mtext></msub><mo>×</mo><mrow><mo fence="true">(</mo><mn>1</mn><mo>−</mo><mfrac><msub><mi>E</mi><mtext>needed</mtext></msub><mi>A</mi></mfrac><mo fence="true">)</mo></mrow><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">S_{\text{arrive}} = \max\left(0,\ S_{\text{now}} \times \left(1 - \frac{E_{\text{needed}}}{A}\right)\right)</annotation></semantics></math></span>
</div>

The derivation is simple proportionality: <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>E</mi><mtext>needed</mtext></msub><mi mathvariant="normal">/</mi><mi>A</mi></mrow><annotation encoding="application/x-tex">E_{\text{needed}}/A</annotation></semantics></math></span> is the fraction of your remaining usable energy the trip will consume, so <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn><mo>−</mo><msub><mi>E</mi><mtext>needed</mtext></msub><mi mathvariant="normal">/</mi><mi>A</mi></mrow><annotation encoding="application/x-tex">1 - E_{\text{needed}}/A</annotation></semantics></math></span> is the fraction left, and scaling today's SoC by it gives the arrival SoC.

Arrival SoC uses <span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>e</mi><mtext>long</mtext></msub></mrow><annotation encoding="application/x-tex">e_{\text{long}}</annotation></semantics></math></span> for the same reason range does: it is a projection across every remaining mile of the route, so it takes the long-horizon figure rather than the one describing the last few (§4.4).

**Worked example.** SoC 68 %, available energy 52.0 kWh, 120 km remaining, efficiency 185 Wh/km:

<div class="eq">
<span class="katex"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mtable rowspacing="0.25em" columnalign="right left right left" columnspacing="0em 1em 0em"><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><msub><mi>E</mi><mtext>needed</mtext></msub></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>120</mn><mo>×</mo><mn>185</mn><mo>÷</mo><mn>1000</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>22.2</mn><mtext> kWh</mtext></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mtext>fraction</mtext></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>1</mn><mo>−</mo><mn>22.2</mn><mo>÷</mo><mn>52.0</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>0.5731</mn></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><msub><mi>S</mi><mtext>arrive</mtext></msub></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>68</mn><mo>×</mo><mn>0.5731</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>=</mo><mn>38.97</mn></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow></mrow></mstyle></mtd><mtd><mstyle scriptlevel="0" displaystyle="true"><mrow><mrow></mrow><mo>→</mo><mtext> displayed as “39 %”</mtext></mrow></mstyle></mtd></mtr></mtable><annotation encoding="application/x-tex">\begin{aligned}
E_{\text{needed}} &amp;= 120 \times 185 \div 1000 &amp;&amp; = 22.2\ \text{kWh} \\
\text{fraction}   &amp;= 1 - 22.2 \div 52.0       &amp;&amp; = 0.5731 \\
S_{\text{arrive}} &amp;= 68 \times 0.5731         &amp;&amp; = 38.97 \\[2pt]
                  &amp;                          &amp;&amp; \rightarrow\ \text{displayed as ``39 \%&#x27;&#x27;}
\end{aligned}</annotation></semantics></math></span>
</div>

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

## 7. What the model does not do {#s14}

These are some things the model does not factor in, but may be explored in the future.

- **No route lookahead.** The estimate extrapolates "how you have been driving" over "the distance that remains".
  There is no elevation model, no speed-limit model, no weather model.
  It is least accurate at the start of a trip whose character differs sharply from the last few miles, e.g., a mountain pass right after city driving — and it self-corrects as the moving average absorbs the new pace and the remaining distance shrinks.
- **No odometer in the rolling estimate.** Whole-mile/kilometer quantization is uselessly coarse against an 8 km averaging window: an entire half-life fits inside one odometer tick.
- **No reading of the car's own range estimate.** This is not a known signal over the OBD-II port.

---

## 8. Constants reference {#s15}

Every tunable that affects a number in this paper.

**Rolling efficiency estimator (near- and long-term)**

<div class="tablewrap" markdown="1">

| Constant | Value | Meaning |
|---|---|---|
| Cold-start baseline | 207 Wh/km | First-ever-drive seed (≈ 3.0 mi/kWh) |
| Seed plausibility band | 60–600 Wh/km | A stored value outside this is discarded |
| Seed cutoff | 0.2 km | Past this measured distance, a late seed is not applied |
| Persist cadence | 10 s | How often the estimate is saved while driving |
| Near-term half-life | 8.0 km | The newest ~5 miles carry half the displayed figure |
| Long-term half-life | 60 km | The range and arrival-SoC divisor (§4.4) |
| Confidence threshold | 1.6 km | Internal flag only; not surfaced |
| Unmeasured time allowed | 5 s | More than this inside a window abandons it |
| Minimum window time | 60 s | The estimate updates no more often than this |
| Minimum window distance | 0.3 km | Below this the window stays open |
| Minimum window energy | 0.05 kWh | Below this the window stays open |
| Plausibility band | −200 to 5000 Wh/km | Readings outside this cannot be real |
| Efficiency limit | 40 Wh/km | Bounds the running average so the range division always has an answer |

</div>

**Trip distance engine**

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
| Available energy | BMS diagnostic ID 0x0105 | 30s | 0.002 kWh |
| State of charge | BMS diagnostic ID 0x0105 | 30s | 0.5 % |
| Vehicle speed | VCU | ~2.5–3s | 1/64 km/h |
| GPS fixes | Mobile device | ~1 Hz while a drive session is active | — |

</div>

---

## 9. Reading the drive recorder log {#s16}

Everything described in this paper writes to one file, and you do not have to remember to start it.
The **Drive Diagnostics Recorder** (Settings ▸ Diagnostics) is on by default and writes a separate flight-recorder file for each drive; the newest ten are kept, and **Share Drive Diagnostics** hands you the most recent one.

### The line format

Every line is one event:

```console
t=+842.113 [ENERGY] evt=energy eff=185 range=281 conf=1 distKm=42.30 …
```

- `t` is seconds since the recording started — the absolute start time is in the file header, so every line in the file shares one clock
- `[TAG]` names the subsystem, the same bracketed convention the app's other logs use
- `evt` names the record type, and everything after it is `key=value`

Values never contain spaces, so the whole file can be read with a text editor's search, or split on spaces by any script.

Four tags appear:

<div class="tablewrap" markdown="1">

| Tag | Covers |
|---|---|
| `[GPSDIST]` | The distance engine — GPS fixes, wheel-speed samples, odometer readings, and the close decision |
| `[ENERGY]` | Near- and long-term efficiency, range, and arrival state of charge |
| `[NAV]` | Turn-by-turn guidance — routing, maneuvers, reroutes |
| `[TRACE]` | The recording itself — start, end |

</div>

The point of one file rather than several is that these share a timeline.
When an efficiency window is discarded you can read straight across to the fixes that caused it, instead of correlating two logs by wall-clock time.

### The efficiency record

`[ENERGY] evt=energy` — one state line every 30 seconds while moving, every 5 minutes while stopped:

```console
t=+842.113 [ENERGY] evt=energy eff=185 rangeEff=178 range=292 conf=1 distKm=42.30
pendKm=0.180 pendKWh=0.031 soc=68.0 availE=52.014 folds=37 reanch=4 clamps=0 gaps=2
```

- `eff` — near-term efficiency in Wh/km: the number on the Range tile
- `rangeEff` — long-term efficiency (§4.4), the value `range` was actually divided by.
  The gap between `eff` and `rangeEff` *is* the smoothing; on a steady drive they converge, and on a changing one they should differ
- `range` — in km, before any unit conversion for display
- `conf` — whether the 1.6 km confidence threshold has been passed (the internal flag in §8)
- `distKm` — measured distance this drive, taken from the shared totalizer that also builds the trip figure (§4.2)
- `pendKm` / `pendKWh` — the window currently open: how much distance and energy have accrued toward the next update
- `folds` — how many windows have closed and entered the moving average
- `reanch` — windows excluded by the distance engine (gap, or before drive start)
  A high count relative to `folds` means the drive was measured in fragments — worth knowing before trusting the figure
- `clamps` — readings that fell outside the plausibility band
- `gaps` — unmeasured stretches that forced a re-anchor

`availE` is logged to three decimals because that is the signal's real resolution.

Four one-off `[ENERGY]` records fill in the rest: `energy_params` stamps every constant in §8 at the start of the drive, so an old file stays interpretable after the constants are retuned; `energy_reanchor`, `energy_clamp`, and `energy_confident` each record the moment they happen, with the values that caused them.

### The distance record

`[GPSDIST] evt=close` — one line per drive, recording the distance decision:

```console
t=+2431.007 [GPSDIST] evt=close endReason=ignition_off integKm=42.031 cov=0.960
odoDeltaKm=41.843 chose=INTEGRAL distanceKm=42.031 startSoC=84.0 endSoC=68.0 energyKWh=7.79
```

The choice between the integral and the odometer is always recorded (§3.3), alongside the start and end values the trip figures are built from.

Before it, `evt=fix` carries every GPS fix with its stated confidence and crediting verdict, `evt=wheel` every vehicle-speed sample, and `evt=buckets` the final four-way attribution of §3.2 — so the coverage figure in the close line can be checked against the seconds that produced it.
