---
description: >-
  Here are some general tolerancing tips, picked up from work experience, in no
  particular order. Anyone is welcome to add to these or correct them if you see
  something inaccurate.
---

# Tolerancing

* Tolerances should always be as **large as possible for the part to still function**
  * Overly tight tolerances are expensive, time consuming, and unnecessary
* **3D printed parts will shrink. A lot.**
  * Online estimates are ~8% for ABS and ~3% for PLA but the actual amount will vary drastically based on the printer, settings, and the part itself.
* If possible, part corners should be chamfered or filleted, especially for sharp/hard materials
* For machined parts, a surface finish of 125 microinches \(3.175 micrometers\) is standard
* Any holes to be tapped should be first made one size smaller than the tap size
  * I.e. for a \#6 screw, one should drill a \#5 hole before tapping with a \#6 tap
* Holes should be **larger** than the fasteners that go in them. The smallest diameters for a "normal" fit by ASME standards are listed below.
  * See ASME standard 18.2.8 for more information, or go to: [https://mechanicalc.com/reference/fastener-size-tables    ](https://mechanicalc.com/reference/fastener-size-tables    )

| Designation | Nom. \(in\) | Nom. \(mm\) | Min. \(in\) | Min. \(mm\) |
| :--- | :--- | :--- | :--- | :--- |
| \#0 | **0.060** | 1.524 | **0.076** | 1.930 |
| M1.6 | 0.063 | **1.600** | 0.071 | **1.800** |
| \#1 | **0.073** | 1.854 | **0.089** | 2.261 |
| M2.0 | 0.079 | **2.000** | 0.094 | **2.400** |
| \#2 | **0.086** | 2.184 | **0.102** | 2.591 |
| M2.5 | 0.098 | **2.500** | 0.114 | **2.900** |
| \#3 | **0.099** | 2.515 | **0.116** | 2.946 |
| \#4 | **0.112** | 2.845 | **0.128** | 3.251 |
| M3.0 | 0.118 | **3.000** | 0.134 | **3.400** |
| \#5 | **0.125** | 3.175 | **0.156** | 3.962 |
| \#6 | **0.138** | 3.505 | **0.170** | 4.318 |
| M4.0 | 0.157 | **4.000** | 0.177 | **4.500** |
| \#8 | **0.164** | 4.166 | **0.196** | 4.978 |
| \#10 | **0.190** | 4.826 | **0.221** | 5.613 |
| M5.0 | 0.197 | **5.000** | 0.217 | **5.500** |
| \#12 | **0.216** | 5.486 | N/A | N/A |
| M6.0 | 0.236 | **6.000** | 0.260 | **6.600** |
| 1/4" | **0.250** | 6.350 | **0.281** | 7.137 |
| M8.0 | 0.315 | **8.000** | 0.354 | **9.000** |

GD&T should be added at some point

