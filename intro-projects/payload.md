---
description: >-
  The payload intro-project is designed to be a comprehensive and interesting
  way of introducing new members to the common tasks done by the team.
---

# Payload

![A simple rover chassis](../.gitbook/assets/simple_chassis.png)

![A more complicated Payload rover for NASA SL 2018](../.gitbook/assets/picture2.png)

## Introduction

The intro project is designed with two main parts: 1. Design, and 2. Manufacturing. This closely emulates the major stages of a payload project cycle. \(Assembly of course is also a major component, but it is better to teach that during our actual payload projects.\)

The intro project may seem daunting, but don’t worry! In addition to the existing resources on GitBook, all the returning payload members will available to help. 

To encourage intra-team communication new members are encouraged to ask for help from a designated returning member, as part of our mentorship program. Furthermore, do not hesitate to ask questions on the \#payload Discord channel or PM Jason Xu or other payload members. 

We will also hold a series of intro project workshops throughout the next weeks, giving an opportunity for hands-on help. Details will be announced here and on the \#payload channel.

Above all, we hope that the intro project will be a fun and rewarding experience.

Checkpoints Schedule:

* By week of 2020-02-25 - Design Stage Complete
* By following meeting - Manufacturing files complete

### Objective Outline

Our goal is to build a mini robotic rover that fits inside a 4” diameter payload tube. Another team has already done the task of picking out the electronics, sensors, motors, and wheels. Your task is to design and prototype the rover’s chassis– a structure to mount all of sensors, motors, wheels, and the [microcontroller](https://electronics.howstuffworks.com/microcontroller1.htm).

### Requirements

> Engineering is defined by requirements!

_**Components to Integrate**_

* 1x [Arduino Nano](https://store.arduino.cc/usa/arduino-nano)
* 2x [40mm wheels](https://www.pololu.com/product/1452/specs)
* 1x [ball caster wheel](https://www.pololu.com/product/952/resources)
* 2x [motors](https://www.pololu.com/product/2367/resources)
* 1x [motor driver board](https://www.pololu.com/product/2130) \(optional\)
* 1x [distance sensor](https://www.pololu.com/product/2474)

_**Detailed Design Requirements:**_

1. All components must fit within the space of a cylinder, 4" in diameter and 8" in length.
2. All components must be mounted by non-permanent means. For example, you may not glue the Arduino to the frame. One method could be to use zip ties/Velcro; if you choose this option, be sure to include slots/holes for the ties/velcro. For parts with mounting holes, screws and nuts are preferred.
3. The distance sensor must be mounted to the front of the rover, facing forward.
4. The wheels may be arranged in any _reasonable_ format. \(Tricycle-like approach recommended\).
5. You do not have to worry about wiring the electronics or mounting the rover to the tube.

Your frame may be as elaborate or simple as you'd like, but it should adhere to the above requirements.

## Stage 1: Design

{% hint style="info" %}
**Checkpoint: Week of 10/01 \| Workshop 1: 09/22 @ Etcheverry CAD Lab, see \#announcements on Discord for more information**

**\(Dates subject to modification according to scheduling\)**
{% endhint %}

We will use CAD \(computer aided design\) software in order to model our 3D frame. STAR has standardized in using [SolidWorks ](www.solidworks.com)as our preferred CAD software. If have used CAD software other than SolidWorks, such as Fusion 360, Inventor, or Creo, then SolidWorks should not be too difficult to pick up. 

If you have never used CAD software before, don’t worry! We will hold a intro project training class during Workshop 1, most likely on the week of 9/15**.** If you are not able to attend, there are also great online resources:

{% embed url="https://www.youtube.com/watch?v=qtgmGkEPXs8" %}

{% hint style="info" %}
There will also be example PDFs for each section located at the end of each stage. Use them if you are really stuck!
{% endhint %}

### 1.1 Installing SolidWorks

The first challenge of this stage is installing SolidWorks. The GitBook has a very helpful “SolidWorks Installation” page to help you with this.

{% page-ref page="../tutorials/software/solidworks.md" %}

{% hint style="warning" %}
**SolidWorks is only compatible with Windows!** If you use MacOS or Linux you have three options: 

1. Use the on-campus CAD lab in Etcheverry 1XXX or Jacobs 10 both of which have SolidWorks pre-installed.
2. Install Windows and then install SolidWorks.
3. **Only if the above is not feasible,** you may use a compatible CAD program of your choice \(Fusion 360 is recommended as it has many online resources\).
{% endhint %}

### 1.2 Working with given hardware

Assume another team has already picked out the motors and electronics necessary for a rover. As a design engineer, your task is to cohesively incorporate all the given components into a \(hopefully\) functioning rover.

A good place to start is by looking at the physical dimensions of each component. Attached are 2D dimensioned engineering drawings of all the parts.

{% file src="../.gitbook/assets/dimensions.zip" caption="Component dimensions" %}

{% hint style="info" %}
You do not have to 3D model the provided components. However, 3D models of major components are provided below should you want to make a SolidWorks assembly in the end \(NOT REQUIRED\).
{% endhint %}

{% file src="../.gitbook/assets/models.zip" caption="Component models" %}

### 1.3 Working with the tube

The most challenging \(and annoying\) constraint placed on many payload projects is the size of the payload tube \(the part of the rocket that the payload is stored in\). Learning to work with the size limits of a cylinder is essential. 

In this project, your tube space is limited to 4" in diameter and 8" in length, a common size for a medium-scale rocket. It is often convenient to work with space envelopes limited by a rectangle, so the foremost important fact to understand is that **a 4" diameter circle will not fit a 4x4" square.** Your usable space is limited to what you can fit \(or [inscribe](http://www.moomoomath.com/inscribed-polygon.html)\) within a circle.

![](../.gitbook/assets/annotation-2019-07-08-185531.png)

Keep this in mind when designing your chassis!

### 1.4 Start designing!

That's all the essentials to get you started on your design. Remember, you can come up with anything as long as it meets the detailed design requirements. The rest of this sub-section lists a few tips.

{% hint style="info" %}
Any non-permanent mounting method is acceptable. If a part comes with screw holes, you are encouraged to design for screw fasteners. However, zip ties and Velcro are also acceptable \(and are the only possible options for parts without mounting holes\). 
{% endhint %}

{% hint style="info" %}
To design screw holes that fit, visit the [Tolerancing GitBook page](../tutorials/manufacturing/tolerancing.md)! 
{% endhint %}

{% hint style="info" %}
If you are really stuck, or just want to see an example of a simple chassis design process step-by-step, there is a detailed PDF in the additional design resources section.
{% endhint %}

### 1.5 Additional resources

A detailed step-by-step design guide will be out by 9/10. \(Although I heavily encourage you to try it out yourself first & ask any Payload member for help before consulting the guide\)

## Stage 2: Manufacturing

Since it is logistically challenging to have everyone manufacture their designs, the task will be to export your CAD components as appropriate manufacturing files. For a 3D printed part, an appropriate file will be .stl \(SolidWorks -&gt; Save As -&gt; STL\). For laser-cutting, Adobe Illustrator .ai files or AutoCAD .dxf files are accepted. We have resources on manufacturing in the GitBook tutorials section.

Please reach out on Discord if you have any concerns with this section.

{% page-ref page="../tutorials/manufacturing/laser-cutting.md" %}

## Project Submission

Please upload your SolidWorks/other CAD files here, along with manufacturing files:

{% embed url="https://forms.gle/x4N125Xg1EVt1uba9" %}



