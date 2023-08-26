---
description: This version created in Fall 2023 by Dulanya Cooray. Subject to revision.
---

# Avionics (in-progress)

## What is avionics anyway?

Avionics involves working with all the electronics and software we need to launch rockets. Sensors? Power? Communication? GPS Tracking? Remote engine control? That's all avionics!&#x20;

We welcome members of _**all majors and all levels of prior technical experience**_. The goal of this intro project is to go over some fundamental concepts and techniques from the ground up. All we ask is that you're interested in learning about, and eventually contributing to, the work we do at STAR

## Introduction

This intro project is separated into modules, each of which is expected to take about a week long to complete. You can complete most of the intro project at your own pace—however, you will need to **attend workshops/ events synchronously.** (Exceptions on a case-by-case basis, make sure you inform the avionics lead to make other arrangements.)&#x20;

#### Navigation

We will use a spreadsheet to give you the instructions for the intro project. A copy of this sheet will be assigned to each prospective member.&#x20;

> **Each prospective member should receive a copy of the Intro Project spreadsheet, and be able to edit it. If you did not receive a copy, message the Avionics lead ASAP!!**

<figure><img src="../../.gitbook/assets/Screen Shot 2023-08-25 at 11.20.11 AM.png" alt=""><figcaption></figcaption></figure>

* **Task:** The intro project is made up of individual tasks you need to complete. You need to complete all tasks (except the ones marked \[OPTIONAL]) to complete the intro project.&#x20;
* **Status:** There are 3 options for status: Complete, In-progress, and N/A (not applicable). Use 'N/A' if you decide not to complete an _optional_ task. Use 'In-progress' after you have begun working on a task. Use 'Complete' only once the task is fully completed.&#x20;
* **Check Off By:** For tasks marked 'Prospective', you must update the status of that task by yourself. This lets us keep track of how you're doing on the intro project! Some tasks are marked 'Mentor' or 'Lead', you are _not_ allowed to update the status of that task until a mentor or lead approves it.&#x20;
* **Notes:** These may include some additional information or resources that might help with the task. Some notes cells will have a border around them, this indicates that there's some information you need to fill in there. (Instructions should be included in the corresponding task.)

## Section 1: Orientation and Setup

| <p>Join the STAR discord, know how to navigate to the channels relevant to you. </p><p>Fill out the new members form.</p>                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Attend an orientation (or make arrangements with the avionics lead)                                                                                                                                                                                          |
| Read through the General Info tab and make sure you understand everything on there. Make sure to ask questions if you have any!                                                                                                                              |
| Get Google Drive access - make sure you are able to view items in the drive. Reach out to the avionics lead or a mentor if you are having trouble.                                                                                                           |
| Complete the RFS safety training. Follow the intructions linked here.                                                                                                                                                                                        |
| Create a GitHub user profile if you do not already have one. Add your username in "Notes" so you can be added to the STAR organization.                                                                                                                      |
| Mark as 'complete' once you have been added to the STAR organization.                                                                                                                                                                                        |
| Download Git on your laptop - follow the instructions linked here                                                                                                                                                                                            |
| Download and install Arduino 2.0 (or later)                                                                                                                                                                                                                  |
| Download the ESP32 drivers.                                                                                                                                                                                                                                  |
| Follow the linked tutorial to add the ESP32 module on Arduino. Make sure to also test that the install was successful.                                                                                                                                       |
| Download KiCad 6.0.11 (DO NOT DOWNLOAD KICAD 7.0). After selecting your OS, you will need to scroll down to "Previous Releases" and click the link given there to find the correct version.                                                                  |
| \[OPTIONAL] If possible, enroll in the HOPE DeCal (most of the prerequisite knowledge will be covered in this intro project). While we will go over PCB design, the HOPE DeCal is a great experience! We strongly reccomend enrolling, but this is optional. |

## Section Two: Soldering

| Attend Soldering Workshop - include date attended in the 'Notes' column                  |
| ---------------------------------------------------------------------------------------- |
| Practice through-hole soldering until you feel confident                                 |
| Practice surface mount soldering (for size 0602 and larger) until you feel confident     |
| Practice soldering using the PCB oven until you feel confident                           |
| Practice de-soldering (solder wick, solder sucker, hot air gun) until you feel confident |
| \[OPTIONAL] Complete the entire soldering practice board                                 |

## Section Three: Coding Basics (C++/ Arduino)

| <p>Read the following sections of the Arduino Getting Started Guide (you can skim them):<br>- Anatomy of an Arduino Board<br>- Basic Operation<br>- Memory<br>- Arduino API (and all subsections)<br>- Arduino Software Tools: A Typical Workflow<br><br>Come to Office Hours or post on Discord if you have questions.<br>(Feel free to look through more of their resources if you'd like!)</p> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Attend coding workshop (or make arrangements with the avionics lead) - include date attended in the 'Notes' column                                                                                                                                                                                                                                                                                |
| Write code to control the LEDs on your soldering practice board. Your code must follow the attached specs. Show to a mentor to be checked off.                                                                                                                                                                                                                                                    |

## Section Four: Electronics Basics

| <p>Read the following sections of the Arduino Getting Started Guide (you can skim them):<br>- Circuit Basics<br>- Electronic Signals<br>- Sensors and Actuators<br>- Serial Communication Protocols<br><br>Come to Office Hours or post on Discord if you have any questions.<br>(Feel free to look through more of their resources if you'd like!)</p> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Read the following sections of DC Circuit Theory (you can skim them):<br>- DC Circuit Theory<br>- Ohm's Law and Power<br>- Kirchoff's Current Law<br>- Kirchoff's Voltage Law (14)<br>- Nodal Voltage Analysis<br>- Thevenin's Theorem<br>- Voltage Sources<br>- Current Sources<br>- Voltage Dividers<br>- Electrical Energy and Power</p>          |
| Attend electronics workshop - include date attended in the 'Notes' column                                                                                                                                                                                                                                                                               |

## Section Six: Choosing a Project

| <p>Have a one on one chat with the Avionics Deputy for that project, make sure you understand the requirements and workload of the project. Add the deputy's name in the 'Notes' column.<br><br>(You don't have to meet with both deputies, but you do have to have met with the deputy for the project you will be working on. You can meet with the relevant deputy after you have selected which project you want to work on, although this is not recommended.)</p> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Attend a work session for that project (communicate with the respective deputies to find out when that will be!) Add the name of the project and the date of the work session you attended in the 'Notes' column.                                                                                                                                                                                                                                                       |
| Choose which project you would like to join and inform the avionics lead.                                                                                                                                                                                                                                                                                                                                                                                               |

## Section Seven: PCB Design



{% content-ref url="avionics/pcb-design-mini-project.md" %}
[pcb-design-mini-project.md](avionics/pcb-design-mini-project.md)
{% endcontent-ref %}

| Read the KiCad Tutorial                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Attend Intro to KiCad workshop - include the date attended in the 'Notes' column                                                                                                                                          |
| PCB Dev Mini-Project: Find Instructions & Materials at the link                                                                                                                                                           |
| Finish making the schematic and receive 0 ERC errors.                                                                                                                                                                     |
| Finish making the layout and receive 0 DFM errors.                                                                                                                                                                        |
| Generate the Manufacturing Files and upload to Bay Area Circuit's instant DFM (linked). DO NOT PURCHASE THE BOARDS. THIS IS SIMPLY SO THAT YOU CAN PRACTICE THE PROCESS OF GENERATING AND VALIDATING MANUFACTURING FILES. |

