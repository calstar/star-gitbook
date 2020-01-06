---
description: Setting up ground station software to run on laptop
---

# Ground Station Software

## Installation

First, install `npm`. Then, run `$ npm install`. This will take a while as there are many dependencies for the ground station software. 

If your terminal fails on 

```text
prebuild-install --tag-prefix @serialport/bindings@ || node-gyp rebuild
```

try uninstalling and reinstalling node.js.

If you are getting a git error such as

```text
npm WARN addRemoteGit Error: Command failed: git -c core.longpaths=true config - -get remote.origin.url
```

try running `npm cache clear` .

{% hint style="warning" %}
If you are on Windows and are installing `npm` in WSL, `npm` will likely fail if you have `npm` also installed in Windows itself. Install `npm` in only one of the two.
{% endhint %}

To run the program, you will first have to plug in the ground station and then determine which device the ground station is. 

## Running

On Windows, open `Device Manager`, look under `COM Ports`. Remember which are listed, and then unplug ground station. The Device Manager will refresh and, if the ground station was correctly detected by Windows, one of them will have disappeared. You can plug ground station back in for it to reappear. It should have a name in the format `COMx` where `x` is a number. If you installed npm in Windows, you will run the ground station software with the command `npm start COMx`. If you install npm in WSL, you will run the ground station software with the command `npm start /dev/ttySx` where `x` is the same number as in Device Manager.

{% hint style="warning" %}
Make sure you have `logs` folder in that directory or else this will fail!
{% endhint %}

Open up a web browser and go to [http://localhost:8080](http://localhost:8080). If opening this gives you a blank page, `inspect element` . If the error says something along the lines of `cannot find dist/openmct` then...we really don't know. For now, contact someone who has it working to email you their `openmct` package. Then from `ground_station_openmct/node_modules` run `rm -rf openmct`  then unzip the emailed openmct package into `ground_station_openmct/node_modules` .

