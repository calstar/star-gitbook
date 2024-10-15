---
description: 'Instrumentation, Control, and Communications: On the Ground and In-Flight'
---

# Avionics

### Instrumentation Requirements:

| Name                | Purpose          | Base Quantity | <p>Total </p><p>(w/ Redundancy)</p> |
| ------------------- | ---------------- | ------------- | ----------------------------------- |
| Pressure Transducer | Pressure data    | 5             | 6                                   |
| Thermocouple        | Temperature data | 2             | 4                                   |
| Power Switches      | Actuate valves   | 4             | 8 (2x red.)                         |
| ESP32               | Microcontroller  | 1             | 1                                   |
| SD Card             | Data storage     | 1             | 1                                   |

\


### Command/Communications Structure

<div data-full-width="true">

<figure><img src="../../.gitbook/assets/ALULA_Commnad.png" alt=""><figcaption><p>ALULA Command Structure</p></figcaption></figure>

</div>

### Control State Structure

<div data-full-width="true">

<figure><img src="../../.gitbook/assets/ALULA_STATE_MACHINE (1).png" alt=""><figcaption><p>ALULA Control State Diagram</p></figcaption></figure>

</div>

### Flight Avionics: Stackable Sub-Module Array

<div>

<figure><img src="../../.gitbook/assets/avcad.png" alt=""><figcaption><p>Flight Module Assembly</p></figcaption></figure>

 

<figure><img src="../../.gitbook/assets/pcb.png" alt=""><figcaption><p>Core Board PCB Design</p></figcaption></figure>

</div>

