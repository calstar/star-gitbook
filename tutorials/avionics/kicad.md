---
description: >-
  Installing and using KiCAD for editing schematics, layouts, symbols, and
  footprints.
---

# KiCad

## Installation

Download KiCad from here: [http://kicad-pcb.org/download/](http://kicad-pcb.org/download/)

This also contains instructions for each system.

## General

The KiCad tutorial is actually pretty good, so in general refer to it. The Avionics intro project (on Gitbooks) guide also walks through usage of KiCad.

{% embed url="https://docs.kicad-pcb.org/5.1/en/getting_started_in_kicad/getting_started_in_kicad.html" %}

To jump right in, go to [Draw Electronic Schematics](https://docs.kicad-pcb.org/5.1/en/getting\_started\_in\_kicad/getting\_started\_in\_kicad.html#draw-electronic-schematics) and then [Layout Printed Circuit Boards](https://docs.kicad-pcb.org/5.1/en/getting\_started\_in\_kicad/getting\_started\_in\_kicad.html#layout-printed-circuit-boards).

## Schematic Symbols

Use the following link to learn how to make new symbols for components when you can't find an existing symbol for it in the KiCad libraries.

{% embed url="http://docs.kicad-pcb.org/5.1.2/en/getting_started_in_kicad/getting_started_in_kicad.html#make-schematic-symbols-in-kicad" %}

Often, it can be worth finding an existing symbol that is similar (for example, an older version of a sensor), copying it, and modifying it.

Try to make symbols following a functional pattern of placing pins. Symbols don't need to look like the footprint of an IC. Often, symbols of ICs will have all Vdds/Vccs/Vddios at the top, all Vss's at the bottom, and pins on the sides of the symbol.

STAR has has a repository `hardware-sch-blocks` which contains a library of symbols, `star-common-lib`. Create your symbols in this repository on a new branch, add them to the library, and when ready submit a pull-request. Make sure to update the datasheet link and description!

## Component Footprints

If you've made your own schematic symbol for a component, you will likely have to make a footprint for it as well. Footprints are described [here](https://calstar.gitbook.io/docs/tutorials/avionics/board-design#making-a-layout). The following link will show you how to make new component footprints.

{% embed url="http://docs.kicad-pcb.org/5.1.2/en/getting_started_in_kicad/getting_started_in_kicad.html#make-component-footprints" %}

As with schematic symbols, try finding an existing footprint and then modifying it according to the actual component's datasheet. Datasheets will have drawings and dimensions of the footprint, often under a section such as 'Packaging'.

Many ICs come in standard packages (such as SOT-8). KiCad includes footprints for these standard packages, so often one can select one of these and then ensure with the datasheet that it matches--unfortunately, different manufacturers may use the same name but actually have slightly different footprints.&#x20;

As with symbols, all STAR footprints go in `star-common-lib` in `hardware-sch-blocks`. Create your footprints on a new branch (makes sense to put them on the same branch as the new symbols), and submit a pull-request. Please let the current Avionics lead know when you submit a pull-request so it doesn't slip through their email.
