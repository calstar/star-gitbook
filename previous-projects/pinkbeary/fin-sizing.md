---
description: How the fins geometries were determined
---

# Fin Sizing

### Before PDR

1. Material Choice: Fiberglass (Balsa wood too weak given geometry and speed)
2. Geometry Options
   1. Best Performance: Triangular
      1. Root chord: 8 in.
      2. Tip chord: 0 in.
      3. Height: 5.5 in.
      4. Max rocket speed is 92% max fin flutter speed
      5. Highest apogee: 8460 ft.
   2. Best Choice: Trapezoidal
      1. Root chord: 8 in.
      2. Tip chord: 3 in.
      3. Height: 5.2 in.
      4. Max rocket speed is 65% max fin flutter speed
      5. Highest apogee: 8344 ft.
   3. Viable: Elliptical
      1. Root chord: 8 in.
      2. Height: 5.2 in.
      3. Highest apogee: 8282 ft - consistently outperformed by trapezoidal fins with comparable stability, geometry
3. Thickness Choice: 1/8” (Thinnest option that could withstand max speeds)
4. Stability
   1. Ranges from 1.31 - 1.5 on design view
   2. Consideration of high speeds shift this stability to around 1.8-1.9 according to simulations, so this meets the recommended requirements
   3. For lower stage fins, a range of 1.5 - 2.5 should be used, which of course means a change of geometry

### Between PDR and CDR

1. Decided on trapezoidal over elliptical based on OpenRocket data
2. Increased thickness of both sets of fins to 3/16” based on FinSim data because FinSim accounts for fin divergence also
3. Adjusted the geometries based on the most recent (version 2.0.1) ork to work with stability margins and updated to version 2.0.2 ([All ork versions](https://drive.google.com/drive/u/0/folders/13vuME98Goo64ToEPxMPIjDIPy4-IvKFT))&#x20;
   1. Upper Stage
      1. Root Chord: 8”
      2. Tip Chord: 3”
      3. Height: 5.5”
      4. Stability: 1.27 cal
   2. Lower Stage
      1. Root Chord: 10”
      2. Tip Chord: 3.5”
      3. Height: 5.7”
      4. Stability: 2.19 cal

### Files Used

{% embed url="https://docs.google.com/document/d/1ZdZ9ba6mTG7DJOrrNZseG0eMA0PXnZb6bWlU0I1rweY/edit" %}

[**Spreadsheet**](https://docs.google.com/spreadsheets/d/1UudalR3tthVuBF3Y9PU93paA0vcJeHNFAKbkoaKNTLI/edit#gid=0) **- Used for fin flutter calculations**
