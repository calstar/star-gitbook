# Schematic and Layout Review

### Overview

Reviewing is one of the most important parts of bringing up a board – we don’t want to waste money or time on a flawed design. Consequently, it can take practice to really know what to look for while reviewing a board; there’s no substitute for watching an experienced engineer at work. However, most boards we make have quite a bit in common, so a lot of failure modes are also shared. For anything simple, the below guide should be a good starting point; for anything analog/RF, high-speed, or high voltage/power, additional care should be taken.

In general, when reviewing a board, make notes and open issues on whatever issue tracking system you’re using \(GitHub, Jira, etc.\). Let the responsible engineer \(RE\) review those issues and make changes – don’t make changes on your own. Especially with schematics, merging changes from multiple people can get messy.

Reviews take time to be done thoroughly, so \(especially if a single person is doing the review\), alot time in terms of days, not hours. Additionally, do not think of a review as a 'final check' before a board is put out for fabrication. It may take weeks to make changes and update until a board passes review.

### Submitting your schematic or layout for review

Make sure you include the schematic file \(and layout if applicable\) as well as a bill of materials \(BOM\) that includes DigiKey part number \(or Mouser \#, or direct link if applicable\), name, quantity, and price for literally everything on the board.

### Schematic review

At the level of the board, one of the first steps is to ensure that all interfaces to other systems are met. This usually means that there should be power, a programming port \(per MCU\), and some combination of actuators + sensors + communication. Familiarize yourself with the function of the board within the system. The project page for the board or the system it is part of should contain the description of these functions against which you can compare the schematic.

Component level review should be exhaustive. This means pulling up a datasheet for every single component other than simple passives, and comparing side-by-side with the schematic. Things to look for:

* Reference designs \(in the datasheet\) are followed
* Directionality of I/O lines
* Acceptable voltage ranges
* Power lines
  * Every Vdd/GND pair should have a decoupling capacitor whose value matches what’s suggested in the datasheet
  * Analog power should be separated from digital power \(sometimes with additional filtering on the analog lines\).
* Certain types of I/O \(I2C buses, for example\) require pull-up or pull-down resistors. If you’re not sure where these are required, ask.
* Sometimes, components will have requirements on where they should be placed during layout \(for example, decoupling caps should always be placed near the IC being decoupled\). Make sure these are annotated on the schematic.

Lastly, at the system level, you should ensure that your power block can supply enough current/power to meet the peak needs of everything on the board, with overhead. Also ensure that top-level interfaces to other parts of the system are satisfied.

### Layout review

TBD

### Additional Resources

{% embed url="http://pcbchecklist.com/" caption="A very comprehensive, but not always applicable, PCB checklist" %}



