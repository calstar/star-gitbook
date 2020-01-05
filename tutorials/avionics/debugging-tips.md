---
description: How to debug hardware and firmware problems
---

# Debugging Tips/Testing

## Hardware

Start with these steps to avoid common mistakes: 

1. Make sure the PCB is powered \(either by power supply or by battery\). Indicator LEDs are generally helpful for this \(if they were placed correctly\).
2. Check for correct DC voltages with a multimeter at all input pins.
3. Check for continuity on nets. You can also inspect solder joints.
4. Check regulator outputs with a DC multimeter AND an oscilloscope.
5. Check input voltage at all ICs with both DC multimeter AND an oscilloscope.
6. Check for amplitude and frequency of all external oscillators with an oscilloscope.
7. Check bus signals with an oscilloscope.

After you determine that the PCB is powered correctly and connections are intact, see the firmware debugging to determine more complex problems.

## Firmware

Prior to checking firmware, make sure the hardware is functioning as expected using the hardware debugging steps. 

Then,

* Sanity check you can control GPIO pins by flashing a simple program that sets GPIO pins high, and another program that sets GPIO pins low. Check output using a multimeter.
* Check the fuse bits are what you expect them to be.
* Check the microcontroller is running at the rate you expect it to using UART. This may be a fuse bit issue as well.

Once you have confirmed basic control of the board and microcontroller, test your firmware by adding status LEDs to show general state of code \(particularly useful to check control flow in a state machine\). Add additional output at critical points in the code. Forms of output include GPIO pins, radio, UART, and LEDs. This should allow you to see where your program is going wrong.

Modularize the code as much as possible and test modules from simplest to most complex. Reduce complexity in the code.

