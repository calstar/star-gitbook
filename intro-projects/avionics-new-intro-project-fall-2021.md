---
description: A new intro project for avionics members updated for Fall 2021.
---

# Avionics \(new intro project Fall 2021\)

## Overview

This intro project serves as an introduction to the Kicad software suite, which is used by the avionics team to design circuit boards for STAR projects. The projects is split up into two paths--one path is for students who are more interested in schematic design, and the other path is for students more interested in PCB layout. Schematic design and PCB layout are both fundamental parts of using Kicad. The primary goal of both intro projects is for students to learn how board design is done on the avionics subteam, and gain experience on a project that is very similar to "real" avionics projects.

The schematic-focused path of the intro project is called "CAS-Core Revision" and it consists of adding two new parts \(a raspberry pi compute module, and an FPGA\) to our current CAS-Core board. The layout-focused path of the intro project is called "CAS-Radio Revision" and it consists of adding one new part \(a dual radio transmitter-reciever\) to our current CAS-Radio board. Both CAS-Core and CAS-Radio will be explained in more detail later on.

## What is Kicad?

The circuit design process in Kicad follows a relatively predictable structure, which is separated into two main phases: schematic design, and PCB layout. Schematic design involves deciding which components and pins are connected to which, and PCB layout involves actually drawing the physical wires that will connect the components together. Each component on a circuit board has one symbol \(a diagram showing which pins it has, and what their names are\) and one footprint \(a diagram showing the exact size and shape of its pins\). Symbols are used in the schematic design stage, and footprints are used in the PCB layout stage. 

Kicad has tools that you can use to create your own symbols and footprints for any circuit element, but we will not be using those tools in the intro project \(all symbols and footprints are pre-made for you\). Even outside the intro project, these tools are not always necessary because Kicad has thousands of well-known circuit elements pre-loaded with symbols and footprints. Even if it is not included in Kicad, there are also symbols and footprints publicly available on the web for many different circuit elements \(for example, at [snapeda.com](https://www.snapeda.com)\)

Another core feature of Kicad is Libraries, which are used to store symbols and footprints. Every symbol or footprint must be in a library. You can create your own libraries to store symbols and footprints in, and these libraries can either be global or project-specific. Creating project-specific libraries is generally simpler and easier to manage.

A typical Kicad project proceeds as follows:  
1: Decide on the main components you are planning to use on your circuit board.  
2: Create schematic symbols for these components, unless they already exist in Kicad.  
3: Create footprints for these components, unless they already exist in Kicad.  
4: Create connections between pins in the schematic design stage  
5: Associate symbols with footprints \(tell Kicad which symbol corresponds to which footprint\)  
6: Draw the physical traces between footprints in the PCB layout stage  
7: Generate gerber files \(gerber files are the end stage of PCB design\)  
  
Here is a convenient cheatsheet that explains this process in full:

![](../.gitbook/assets/kicad_flowchart.png)

You can get started with Kicad by downloading and installing it here: [https://www.kicad.org/download/](https://www.kicad.org/download/)

If you have no prior experience with Kicad, then I _highly_ recommend watching this tutorial video series by Digikey. It is useful both as a first look to get familiar with Kicad, and as a refresher to brush up on the details. Following along with their practice project is completely optional--the tutorial is still very helpful even when just passively watching.

Basics: [https://www.youtube.com/watch?v=vaCVh2SAZY4](https://www.youtube.com/watch?v=vaCVh2SAZY4)  
Schematic symbol editor: [https://www.youtube.com/watch?v=c2niS9ZRBHo](https://www.youtube.com/watch?v=c2niS9ZRBHo)  
Schematic design: [https://www.youtube.com/watch?v=4Gtd7xY6zS4](https://www.youtube.com/watch?v=4Gtd7xY6zS4)  
Footprint editor: [https://www.youtube.com/watch?v=ZHH4G\_EWhm0](https://www.youtube.com/watch?v=ZHH4G_EWhm0)  
Associate footprints with symbols: [https://www.youtube.com/watch?v=Ghv0bGiZFL8](https://www.youtube.com/watch?v=Ghv0bGiZFL8)  
PCB Layout 1: [https://www.youtube.com/watch?v=Ghv0bGiZFL8](https://www.youtube.com/watch?v=Ghv0bGiZFL8)  
PCB Layout 2: [https://www.youtube.com/watch?v=jaQPr7PgImk](https://www.youtube.com/watch?v=jaQPr7PgImk)  
Generate gerber files: [https://www.youtube.com/watch?v=ENmDnoKs2hM](https://www.youtube.com/watch?v=ENmDnoKs2hM)  
Generate BOM & Order parts \(optional\): [https://www.youtube.com/watch?v=I7GUiGoD1w8&t=642s](https://www.youtube.com/watch?v=I7GUiGoD1w8&t=642s)  
Solder components to board \(optional\): [https://www.youtube.com/watch?v=Zkn\_Au5aeLA](https://www.youtube.com/watch?v=Zkn_Au5aeLA)

## CAS

CAS stands for Common Avionics Stack and it is one of our most recent avionics projects. The fundamental idea behind CAS is that the entire system is organized into modular boards, each of which are about 3 inches by 3 inches in area. Each board has one general purpose, and the boards are all connected together in a 'stack.' The boards can exchange data because each board has an identical 80-pin header. The pins of one board contact the pins of every other board--so, for example, once the stack is arranged, pin X of one board is connected to pin X of every other board. but pin X of one board isn't necessarily connected to pin Y of the same board.

The CAS board that already exist are: Core \(main function: performing computations\), Pyro \(main function: igniting fuses\), Radio \(main function: sending and recieving radio\), and Prop \(main function: regulating the rocket's propulsion system\). The files for the boards can be found on cadlab \([https://cadlab.io/star](https://cadlab.io/star)\) and github \([https://github.com/calstar](https://github.com/calstar)\).

Most of the boards on CAS are 4-layer, but in this intro project we will only cover 2 layer boards. 2 layer and 4 layer boards have many similarities, but the main difference about 4 layer boards is that the middle two layers are generally designated as power and ground planes, respectively, while the topmost and bottomost layers serve the same function they would on a 2-layer board.

## Intro Project A: CAS-Core Revision

#### Step 0: Getting started

* Download the starter files for the project from github \(provide instructions to do so\)
* The project starts with symbol & footprint libraries for Raspberry Pi Compute Module 4 & ICE40HX4K-TQ144 FPGA.
* The project starts with the entirety of the CAS-Core schematic, except without the STM32 Micro-controller

#### Step 1: Add Raspberry Pi Compute Module To Schematic

* Create a subcircuit to contain the Raspberry Pi Compute Module \(the intro project on gitbooks will describe what the correct subcircuit should look like\)
* Add the Raspberry Pi Compute Module’s symbol to the schematic
* Add any required minor components to the schematic near the compute module, such as resistors and capacitors \(the intro project on Gitbooks will list what is needed\)
* Connect the pins on the Rapberry Pi Compute Module to all other relevant components on the board \(the intro project on Gitbooks will list which pins should be connected to which\).

#### Step 2: Add ICE40 FPGA To Schematic

* Create a subcircuit to contain the ICE40 FPGA \(the intro project on gitbooks will describe what the correct subcircuit should look like\)
* Add the ICE40 FPGA’s symbol to the schematic
* Add any required minor components to the schematic near the FPGA, such as resistors and capacitors \(the intro project on Gitbooks will list what is needed\)
* Connect the pins on the ICE40 FPGA to all other relevant components on the board \(the intro project on Gitbooks will list which pins should be connected to which\).

#### Step 3: Associate Components With Footprints

* Perform electrical rules check using debugger tab to ensure there are no errors
* Open the CVPCB tool from the toolbar
* Search for each board component and associate it with a footprint
* Generate the netlist
* Open PCBNew and read in net-list

#### Step 4: Layout PCB

* Organize footprints into clean positions on top of the CAS-Stacking board
* Calculate proper trace width using an online trace width calculator, and set the trace widths in KiCad \(go to the track width tab on the toolbar, click on ‘edit pre-defined sizes’ in the dropdown menu, and input the new sizes\)
* Draw traces on the front copper layer connecting all of the ‘air wires’, using vias to draw traces on the back copper layer if necessary
* Create a ground pour with the copper fill tool
* Generate gerber files once the layout is finished

## Intro Project B: CAS-Radio Revision

#### Step 0: Getting started

* Download the starter files for the project from github \(provide instructions to do so\)
* The project starts with symbol & footprint libraries for AT86RF215 Radio Transceiver
* The project starts as an almost empty project, with only the 80-pin CAS-Bus included

#### Step 1: Add Radio Transceiver To Schematic

* Add the Radio Transceiver’s symbol to the schematic
* Add any required minor components to the schematic near the transceiver, such as resistors and capacitors \(the intro project on Gitbooks will list what is needed\)
* Connect the pins on the Radio Transceiver to all other relevant components on the board \(the intro project on Gitbooks will list which pins should be connected to which\).

#### Step 2: Associate Components With Footprints

* Perform electrical rules check using debugger tab to ensure there are no errors
* Open the CVPCB tool from the toolbar
* Search for each board component and associate it with a footprint
* Generate the netlist
* Open PCBNew and read in net-list

#### Step 3: Layout PCB

* Organize footprints into clean positions on top of the CAS-Stacking board
* Calculate proper trace width using an online trace width calculator, and set the trace widths in KiCad \(go to the track width tab on the toolbar, click on ‘edit pre-defined sizes’ in the dropdown menu, and input the new sizes\)
* Draw traces on the front copper layer connecting all of the ‘air wires’, using vias to draw traces on the back copper layer if necessary
* Create a ground pour with the copper fill tool
* Generate gerber files once the layout is finished

