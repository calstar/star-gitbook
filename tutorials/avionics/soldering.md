---
description: How to solder/populate a PCB
---

# Soldering

{% hint style="danger" %}
If you are at a soldering station, do **NOT** eat or drink there whether you're soldering or not. Ever. Here is what the CDC and WHO have to say about lead poisoning: [CDC](https://www.cdc.gov/niosh/topics/lead/health.html); [WHO](http://www.who.int/news-room/fact-sheets/detail/lead-poisoning-and-health).
{% endhint %}

{% hint style="info" %}
Please note that there should be a through-hole and surface mount soldering workshop roughly every semester; ask on Discord for a date and time. It is highly recommended that you attend this workshop, as this page is more of a supplement than a stand-alone tutorial.&#x20;
{% endhint %}

## Getting Started

Now that you have a PCB, you are ready to solder. Make sure you have the following supplies:

* Soldering iron
* Solder
* The board that needs soldering
* Components to solder onto the board
* Flux (either liquid in syringe or pen form)
* Tweezers (for surface mount soldering)
* Solder wick (not necessary, but useful)
* Solder sucker (not necessary, but useful)

When putting together your board, remember to test as you solder. This will make sure that you have a better idea of where a bug is if you run into one. This means soldering on a module and then testing that module before moving on to soldering another module. Refer to ["Using Lab Equipment](https://calstar.gitbook.io/docs/tutorials/avionics/lab-equipment)" on information relevant to testing. An example of how to break up soldering a board into modules is as follows:

1. Voltage regulator/power input. Test with a multimeter (and by power LED).
2. Microcontroller. Test by writing a simple program to verify that you can use digital input/output pins. Can also verify by flashing a program that uses the debug UART port.
3. Sensors/actuators (one component at a time). Verify the component works by interfacing with the microcontroller. This may require having some code ready to communicate over I2C or SPI!

Remember to put away **all** tools you used when you are done. Keep whichever space you are working in clean.

## Through-Hole Soldering

Through-hole soldering steps (repeat these steps for each joint):

1. Place your circuit element into the PCB.&#x20;
2. Melt a small blob of solder on the tip of the soldering iron. This is called “tinning the tip” and it improves the transfer of heat from your soldering iron to the component you want to solder. **Make sure to do this to avoid oxidation and permanently ruining the tip.**
3. If necessary, apply flux to the metal ring on your PCB. Flux is usually more important for surface mount soldering.&#x20;
4. Touch the tip of your soldering iron to the metal ring and component leg (of a through-hole component) at the same time. (See diagram below)
5. Feed solder **into the joint** (not the soldering iron) while this is happening. It should only take a couple of seconds at most to fill the joint with a proper amount of solder.
6. After enough melted solder is present, stop feeding solder and remove the tip from the joint.
7. Clean the tip of the soldering iron by dabbing the tip on a wet sponge.
8. Let the joint cool down for at least 5 seconds and then trim the ends of the wire(s).

![Soldering tips](../../.gitbook/assets/wk1\_soldering\_tips.png)

The following tutorial is for through-hole soldering:

{% embed url="https://www.youtube.com/watch?v=Qps9woUGkvI" %}
Basic soldering steps and through-hole
{% endembed %}

## Surface Mount Soldering

Surface mount soldering is a bit more difficult. The components are small, and it's easy to short pads (the metal parts that you're soldering onto) and components together. But all it takes is practice!

The steps to do surface mount soldering is similar to through-hole:

1. Place your circuit element onto the PCB.&#x20;
2. Tin the tip. **Very important.**&#x20;
3. This is when it's good practice to use flux! Apply some to the pad before soldering. After you're done, put some flux on the solder blob and apply heat with the soldering iron to flatten peaks.
4. While soldering, touch the tip of your soldering iron to the metal pad and edge of the component leg at the same time.
5. Feed solder **onto the pad** (not the soldering iron) while this is happening. It should only take a couple of seconds at most to cover the component and pad with the right amount of solder.&#x20;
6. After enough melted solder is present, stop feeding solder and remove the tip from the pad.
7. Clean the tip of the soldering iron by dabbing the tip on a wet sponge or brass sponge.
8. Let the joint cool down for at least 5 seconds and then refer to the flux step above.
9. The following tutorial is for surface mount soldering:

{% embed url="https://www.youtube.com/watch?v=5uiroWBkdFY" %}
Surface mount soldering
{% endembed %}

## Conclusion - _practice_

There are many free through-hole components around [Supernode](https://supernode.berkeley.edu/), and you can just ask someone for surface mount components. It's important that you practice. Please ask for help if necessary.&#x20;
