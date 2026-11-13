# SPHERE

**Formula for a spherical capacitor** (a = radius of inner conductor's outer surface, b = radius of outer conductor's inner surface):

$$C = 4\pi\varepsilon_0 \frac{ab}{b - a}$$

**Example:**
- a = 5 cm = 0.050 m
- b = 5.1 cm = 0.051 m
- b − a = 1 mm = 0.001 m

$$C = 4\pi\varepsilon_0 \frac{(0.050)(0.051)}{0.001} = 4\pi\varepsilon_0 \times 2.55\ \text{m}$$

$$C = 1.1127 \times 10^{-10} \times 2.55 \approx 2.84 \times 10^{-10}\ \text{F}$$

**C ≈ 284 pF**

The geometry is: inner shell outer surface at a = 10.0 cm, outer shell **inner** surface at b = 10.1 cm → gap = **1 mm** (the outer shell diameter doesn't affect C).

$$C = 4\pi\varepsilon_0\frac{ab}{b-a} = 4\pi\varepsilon_0 \times 10.1 = 1.1238 \times 10^{-9}\ \text{F}$$

**C_cap ≈ 1124 pF ≈ 1.12 nF** (not 562 pF)

The isolated sphere (R = 10 cm): **C_self = 4πε₀R ≈ 11.13 pF**

Using Q = CV and E = ½CV² (air dielectric, ε ≈ ε₀):

| V (V) | Q — spherical capacitor | E — spherical capacitor | Q — isolated sphere | E — isolated sphere |
|------:|------------------------:|------------------------:|--------------------:|--------------------:|
| 3.3   | 3.71 nC                 | 6.12 nJ                 | 36.7 pC             | 60.6 pJ             |
| 5     | 5.62 nC                 | 14.0 nJ                 | 55.6 pC             | 139 pJ              |
| 10    | 11.24 nC                | 56.2 nJ                 | 111 pC              | 556 pJ              |
| 12    | 13.49 nC                | 80.9 nJ                 | 134 pC              | 799 pJ              |
| 15    | 16.86 nC                | 126 nJ                  | 167 pC              | 1252 pJ             |
| 24    | 26.97 nC                | 324 nJ                  | 267 pC              | 3204 pJ             |
| 30    | 33.71 nC                | 506 nJ                  | 334 pC              | 5007 pJ             |

Notes:

- The ratio is exactly constant: C_cap/C_self = b/(b−a) = 101, so the capacitor stores **101× the charge and energy** of the isolated sphere at every voltage.
- Charge scales linearly with V; energy scales with V² — going 5 V → 30 V (6×) multiplies the stored energy by 36 (14 nJ → 506 nJ).
- At 30 V across a 1 mm gap the field is only 30 kV/m, far below air breakdown (~3 MV/m), so no corona or arcing concerns at any of these voltages.
