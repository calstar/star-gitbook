---
description: >-
  IRIS: IRIS Records Information via Sensors. By Jason Xu, Rajiv Govindjee,
  Bryant La, and Josh Alexander.
---

# IRIS Legacy - Archived

## Background

The IRIS journey started in 2018; IRIS v1 was conceived of as a project for the[ Hands-On PCB Engineering (HOPE) DeCal](https://ieee.berkeley.edu/hope/pcb.html). The board was assembled in Fall 2018 and found to be relatively functional, with difficulties arising mostly due to lack of software libraries for the ICM 20948. \
\
IRIS v2 was designed and assembled in early 2019, adding rounded corners, more sensors, options for breakout boards, test points, improved power electronics, and more. IRIS v2 was also more successful on the software front; all sensors tested worked nominally, including the ICM 20948. Code for IRIS v2 can be found at [https://github.com/calstar/Payload](https://github.com/calstar/Payload). While IRIS v2 was intended to fly on Spectre, STAR's ambitious entry for IREC 2019, Spectre was never constructed due to significant engineering challenges.

For a more detailed look at requirements and progression of IRIS v1 and v2, see the IREC 2019 documentation: [IRIS](broken-reference)

## AirBears Test Flight

IRIS v2 was flown on [AirBears on 2019-11-16](https://rocketry.gitbook.io/docs/history-of-the-team/launch-history). To prepare for this flight, the casing was significantly re-designed to integrate with the other payload (Muons) on the test flight. Software was completed to allow for continuous recording of IMU data to the on-board SD card on the Teensy.

Unfortunately, as a result of non-comprehensive assembly procedures and some time pressure to assemble the payloads, IRIS was flown while not in a recording state.

The following recommendations were made following this test flight:

* Implement some method for back-up power (capacitor, coin cell battery, etc.). This ensures writes to non-volatile memory have time to safely complete.
* Create robust procedures and test them entirely before launch. This includes all integration needed with other payloads. Add special notes if power may not be disconnected from the payload after a certain point.
* Perform as much assembly as possible beforehand. Ensure that no more than 30 minutes are needed at launch for assembly; time someone actually completing this assembly beforehand.

## Current Work

The team is currently working on physical design and manufacturing for IRIS to fly in the IREC 2020 payload suite as one of 5U worth of CubeSats. Work is also underway on a potential IRIS v4 board, although not required for competition readiness. Software is the largest hurdle for the competition; some development may be required to communicate with all sensors on multiple SPI buses at once (effectively).
