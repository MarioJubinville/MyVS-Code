# Tester

Now the operating point is: **1τ drain, 1τ charge, steady-state oscillation** — and there's a gift hiding in this configuration that makes the whole thing come out clean. Let me show you the gift first, because it changes how you read the answer.

## The gift: the node voltages don't depend on the resistors at all

Drain for one τ₂: V_low = V_high·e⁻¹. Charge for one τ₁: V_high = V_low + (5 − V_low)(1 − e⁻¹). The only way this can repeat cycle after cycle is:

$$V_{high} = \frac{5}{1+e^{-1}} = 3.655\ \text{V}, \qquad V_{low} = e^{-1}V_{high} = 1.345\ \text{V}$$

The e-folding is set by *running exactly one time constant*, which is dimensionless — the actual values of R₁, R₂ cancel. So **every cycle moves the same charge, 154.3 pC = C_t·(3.655 − 1.345) V**, whatever resistors you pick. The resistors set only the clock speed and the peaks. (Verify the invariant that keeps the peaks symmetric: 5 − V_low = V_high *exactly*, so at R₁ = R₂ both FETs see identical peak currents.)

What the resistors *do* set:

$$T = (R_1+R_2)C_t, \qquad I_{peak,drain} = \frac{V_{high}}{R_2}, \qquad I_{peak,charge} = \frac{V_{high}}{R_1}, \qquad I_{avg} = \frac{2.3105\ \text{V}}{R_1+R_2}$$

Notice: **the average current cares only about the sum R₁+R₂.**

## Applying the 100 mA constraint

Drain FET (BSS138): V_high/R₂ ≤ 100 mA → **R₂ ≥ 36.6 Ω**.

One flag before we commit: you constrained the *discharge* FET, but the charge-side BSS84 has the *same* 100 mA rating, and at R₁ = R₂ it sees the same 100 mA peak. The symmetric choice is exactly the point that respects both — if you shrink R₁ below 36.6 Ω to push the average higher, you're billing the BSS84 for the excess.

## The achievable design (R₁ = R₂)

| | Ideal, at the limit | Standard 5% value |
|---|---|---|
| **R₁ = R₂** | **36.6 Ω** | **39 Ω** |
| Peak current, drain FET | **100.0 mA** | 93.7 mA |
| Peak current, charge FET | 100.0 mA | 93.7 mA |
| **Average current** (each path & supply) | **31.6 mA** | 29.6 mA |
| Frequency (T = 2τ) | **205 MHz** (4.88 ns) | 192 MHz (5.21 ns) |
| **Peak power** (per path, at the switch) | **365 mW** | 343 mW |
| **Average power** (per path) | **79 mW** | 74 mW |
| **Average power** (total) | **158 mW** | 148 mW |
| FET channel power (peak / avg) | ~0.4 mW / ~80 µW | ~0.3 mW / ~74 µW |
| Node swing | 3.66 ↔ 1.34 V | (same) |
| Charge per cycle | 154.3 pC | (same) |

The averages come from the per-cycle energies, which the geometry also fixes: ½C_t(V_high² − V_low²) = 385 pJ dissipated in each path per cycle, × 205 MHz = 79 mW per path; the supply sees 5 V × 31.6 mA = 158 mW, closing conservation exactly.

If you want the family rather than the point: I_avg = 2.3105/(R₁+R₂) — e.g. R₁=R₂=47 Ω gives 24.6 mA at 158 MHz; 68 Ω gives 17.0 mA at 110 MHz. And the "constrain only the discharge FET" variant: swap the high side to a Si2301 (220 mA) and R₁ can drop to 16.6 Ω, lifting the average to 43.5 mA at 282 MHz — if you're willing to let the part choice, not the resistor, carry that constraint.

## The 200 MHz reality check — this is no longer the same kind of circuit

1. **The FETs are still the bored ones.** Peak 100 mA is 45% of the BSS138's rating and a 2.4 ns pulse; the channel power is a fraction of a milliwatt. The *resistors* are now the hot parts: 79 mW each, so use ½ W metal-film, not ¼ W, and keep them away from the gate wiring.
2. **The gate drive becomes the design.** Phases are 2.44 ns. To be fully on in a third of that, a 2 nC gate wants ~6 A of gate current in a nanosecond — that is dedicated-fast-gate-driver, tight-loop, PCB territory, not a 74LVC buffer on a breadboard. The saving grace is the same one as always: R₁/R₂ cap the *channel* current at 100 mA no matter how sloppy the turn-on, so a slower gate degrades the timing but can't blow the current budget.
3. **The layout is the third component.** At 205 MHz, keep the 5 V rail decoupled at the FET pins, keep node N and the ground return short (a stray nH is harmless to the 2.4 ns RC envelope — L/R ≈ 27 ps — but it will ring the switching edges), and route the two gate loops so they don't pick each other up.
4. **The sphere voltage spec moved.** Your spheres now peak at **3.66 V**, not 5 V — that's the price you already accepted ("skip fully charged"), and at 1τ the price is high: 63% of the charge never leaves the drain path's reach in a given cycle. If some downstream requirement actually needs the 5 V peak, this operating point doesn't meet it, however beautifully it runs.

## Where this lands in the series

| Design | f | I_avg | Peak | P_avg |
|---|---|---|---|---|
| 3 MHz original (4.9τ phases) | 3 MHz | 1.0 mA | 9.8 mA | 5 mW |
| 2τ/2τ steady state | 7.3 MHz | 1.87 mA | 8.6 mA | 9.3 mW |
| **1τ/1τ at 100 mA limit** | **205 MHz** | **31.6 mA** | **100 mA** | **158 mW** |

Cutting the tail from 4.9τ to 1τ while riding the current up to the 100 mA wall bought a **32× average current** — and your intuition held at every step: the peaks are what you set them to be (100 mA, 365 mW), and the average is just the area you stopped throwing away. The one new truth at this end of the dial: the resistors and the layout now do the work; the BSS138 merely supervises at 100 mA and 80 microwatts.
