---
description: >-
  Avionics introductory project designed to introduce new and returning members
  to the type of work done in this subteam.
---

# Avionics

## Introduction

You have been given a design for a very simple rocket flight computer that consists of six components: a battery, a voltage regulator, an ATMega328P microprocessor, an MPL3115A2 altimeter, and two black powder ports. You will be describing the system in more detail and writing firmware to control the rocket’s recovery system \(parachutes\) via the two black powder ports.



![](https://lh4.googleusercontent.com/mfFEtGNiHnTwU3RBe0HuG_s7x2uXXkwkNsBHaUWIQdsAe-3HrAts-Ln5fl-VhHxjfWl_34aZYZvBSzXhRN0ytLYm1HB_3A1bpP0pRjWHozd-Z_Wus2VLGqHo9adRo6KY5MRglTyQ)

{% hint style="info" %}
If you are confused, read the Avionics guides under the "Tutorials" tab!
{% endhint %}

## Details and Specifications

* The details of the battery and voltage regulator do not matter, but they must both be included in the final system diagram that you create.
* You have been provided with an interface for a HAL \(Hardware Abstraction Layer\). You will use its functions to write the firmware for the ATMega328P. The file is below, in the Files section.
  * The pinMode, digitalRead, and digitalWrite functions act as they would in Arduino.
  * The i2c\_\*\*\* functions act as they would in the Arduino Wire library.
  * The millis function returns time, in milliseconds, from program start.
  * Arduino reference materials and the HAL are listed below, in the Resources section.
* When configured correctly, the MPL3115A2 provides integer altitude data, in feet, via the I2C protocol.
  * Registers implemented in the simulator are: 
    * Pressure Data Out MSB/CSB/LSB \(OUT\_P\_XSB\)
    * System Mode \(SYSMOD\)
    * Control Register 1 \(CTRL\_REG1\)
    * Control Register 2 \(CTRL\_REG2\)
    * Who Am I  \(WHOAMI\)
    * Data Ready Status \(DR\_STATUS\)
    * Pressure/Temperature Data Config \(PT\_DATA\_CFG\)
  * Depending on how you use the altimeter, you may not need all of these registers.
* The simulation runs at 100 times real time, i.e. millis\(\) returns 100 \* \(milliseconds elapsed since start of program\). Be careful if using sleeps and while debugging.
* The two black powder ports are activated by two specific GPIO pins on the ATMega328P. To activate each one, turn on the pin for at least 50 milliseconds.
  * The drogue chute ignition pin is PB3.
  * The main chute ignition pin is PD7.
* The firmware must be written in C.
* The initial altitude reported by the MPL3115A2 will be somewhere within \[-100, +100\] feet in altitude \(inclusive\)
* The altitude will remain within \[-5, +5\] feet of an unspecified constant altitude between \[-100, +100\] feet -- the **ground altitude** -- for at least 30 seconds after flight computer startup and before launch. All altitudes following are in reference to this ground altitude. It is expected that there will be some inaccuracy in the timing of the ejections in your firmware due to the fluctuation of altitude readings while the rocket is on the ground.
* The black powder ignitions must happen at apogee, +/- 2 seconds, and at 600 feet of altitude during descent, +/- 2 seconds.
* Neither black powder ignition should happen unless the rocket has passed 200 feet in altitude.
* Determine and implement a proper strategy for the case in which the flight computer passes 200 feet in altitude, but does not reach an apogee of 600 feet in altitude.
* Describe at least three failure modes and how they are being mitigated or avoided.
* Describe test procedures you would use to verify correct functionality in the lab \(i.e. not at a launch\) and at a launch.
* Show how the microprocessor should be hooked up to the MPL3115A2 and any additional hardware added in order to mitigate failure modes and run test cases \(such as status LEDs or buttons\). This must be in the form of a wiring diagram or schematic.
* Add at least one feature to the code and/or schematic that is used for safety, such as beeping when black powder is connected. Describe the feature and explain any changes made to accommodate it. You are encouraged to look at how COTS \(Commercial Off-the-Shelf\) altimeters work for inspiration. Some examples are the Stratologger CF and the MissileWorks RRC3.

## Compiling and Testing

* The HAL you are provided is in fc.h. You are expected to write an fc.c file that defines fc\_setup and fc\_loop.
  * fc\_setup is called once, followed by fc\_loop called repeatedly until the simulation is complete.
  * All of the other functions declared in fc.h are defined by the simulation runner, in fc\_sim.mac.o or fc\_sim.win.o.
  * Download the appropriate fc\_sim.\*\*\*.o file from the Files section and rename it to fc\_sim.o \(if you want\).
* You are provided with a compiled, but not linked, simulation runner, called fc\_sim. You will compile your flight computer code and link it with fc\_sim to create an executable that, when run, will tell you how the launch went!
* To compile your flight computer:
  * ```text
    gcc -g fc_sim.o fc.c -o fc_sim
    ```

    The -g is to compile with debug symbols.

  *  Note: On linux you may have to add a "-lm" flag to link the math library.
* To test your flight computer, simply run fc\_sim.
* To debug your flight computer, use your favorite C debugging tool, such as gdb. You are not provided the code for the flight computer simulator, but you can debug your own code.
  * Tip: VSCode makes it very easy to write, build, run, and debug code once you have it set up!

## Resources

* [MPL3115A2 Datasheet](https://www.nxp.com/docs/en/data-sheet/MPL3115A2.pdf)
* [ATMega328P Datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42735-8-bit-AVR-Microcontroller-ATmega328-328P_Datasheet.pdf)
* [Arduino Function Reference](https://www.arduino.cc/reference/en/#functions)
* [Arduino I2C Reference](https://www.arduino.cc/en/Reference/Wire)
* [ATMega328P-Arduino Pin Mapping](https://www.arduino.cc/en/Hacking/PinMapping168)

{% file src="../.gitbook/assets/freescale\_mpl3115a2\_i2c\_reference.pdf" caption="MPL3115A2 I2C Reference" %}

## Additional Questions

1. One simple electrical system consists of a battery and a microcontroller with a single button connected with a pullup resistor and a single LED with current-limiting resistor, as shown below. Determine how long it will last on battery power. Explain your answer.
   * Vbatt = 15V, and its capacity is 1A-hr. For safety, only 80% of its full capacity should be used.
   * U1 outputs 5V, and is 90% efficient.
   * The microcontroller draws a constant 20mA.
   * R1= 10kΩ, and S1 is pressed 5% of the time.
   * R2 = 200Ω, D1's Vf = 2.1V, and D1 is on 50% of the time.

![](../.gitbook/assets/additional-question-1%20%281%29.png)

  


2. Write a short snippet of C code that, given an 8-bit register **r** and a bit index **b**:

1. Sets bit **b**.
2. Clears bit **b**.
3. Toggles bit **b**.
4. Assigns bit **b** to a boolean value **v**.

## Files

{% file src="../.gitbook/assets/fc.h" caption="Flight Computer HAL" %}

{% file src="../.gitbook/assets/fc\_sim.win \(5\).o" caption="Compiled Flight Computer Simulator \(Windows\)" %}

{% file src="../.gitbook/assets/fc\_sim.mac \(7\).o" caption="Compiled Flight Computer Simulator \(Mac\)" %}

{% file src="../.gitbook/assets/fc\_sim.linux \(1\).o" caption="Compiled Flight Computer Simulator \(Linux\)" %}

{% file src="../.gitbook/assets/fc\_sim.rv64.o" caption="Compiled Flight Computer Simulator \(RISC-V 64\)" %}

{% file src="../.gitbook/assets/fc\_sim.rv32 \(2\).o" caption="Compiled Flight Computer Simulator \(RISC-V 32\)" %}

## Submission

Please PM Jacob, the Avionics Lead \(Jashaszun\#9329\) a ZIP of the following files via Discord:

* Any C files you wrote that are required to compile and run your flight computer.
* A text file or PDF containing your answers to all other parts of the project.

