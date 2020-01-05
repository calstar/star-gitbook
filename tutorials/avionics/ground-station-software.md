---
description: Setting up ground station software to run on laptop
---

# Ground Station Software

## Installation

First, install `npm`. Then, run `$ npm install`. This will take a while as there are many dependencies for the ground station software. 

{% hint style="warning" %}
If you are on Windows and are installing `npm` in WSL, `npm` will likely fail if you have `npm` also installed in Windows itself. Install `npm` in only one of the two.
{% endhint %}

To run the program, you will first have to plug in the ground station and then determine which device the ground station is. 

## Running

On Windows, open `Device Manager`, look under `COM Ports`. Remember which are listed, and then unplug ground station. The Device Manager will refresh and, if the ground station was correctly detected by Windows, one of them will have disappeared. You can plug ground station back in for it to reappear. It should have a name in the format `COMx` where `x` is a number. If you installed npm in Windows, you will run the ground station software with the command `npm start COMx`. If you install npm in WSL, you will run the ground station software with the command `npm start /dev/ttySx` where `x` is the same number as in Device Manager.

