---
description: Radio module with a powerful AT86RF215 transceiver
---

# CAS Radio Revised

The radio-revised board is still in development. The plan for this board is to use an AT86RF215 module as the radio transciever, which can transcieve over two channels independently at different frequencies.The core board will communicate with the AT86RF215 through LVDS signals, which are output by the FPGA on the core-revised board and travel over LVDS pins on the cas-bus.&#x20;

Most of the design for this module is directly copied from the cariboulite radio board design (which also uses an AT86RF215) here: [https://github.com/cariboulabs/cariboulite/blob/main/hardware/rev2/schematics/CaribouLite.PDF](https://github.com/cariboulabs/cariboulite/blob/main/hardware/rev2/schematics/CaribouLite.PDF)
