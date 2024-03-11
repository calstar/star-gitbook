---
description: >-
  The description of the Cosmic Watch, a pocket-sized detector that counts the
  number of muons that hits it. It also measures temperature and time. It will
  be merged with IRIS for IREC 2020.
---

# Muons - Archived

* PLEASE learn how to solder printed circuit boards. Though it is not hard to pick up, learning understandably still takes time. At Cal, you can either practice soldering in the Chen-Ming Hu Lab in Cory Hall Second Floor (aka SuperNode), or in the Electronics Lab in Jacobs Hall. Here's a tutorial to get you started: [https://www.youtube.com/watch?v=Qps9woUGkvI](https://www.youtube.com/watch?v=Qps9woUGkvI)&#x20;
* Find a way to machine the scintillator if the one you bought is not already machined. The manufacturing drawing is attached below: [https://github.com/spenceraxani/CosmicWatch-Desktop-Muon-Detector-v2/blob/master/CAD/Scintillator%20CAD%20file.pdf](https://github.com/spenceraxani/CosmicWatch-Desktop-Muon-Detector-v2/blob/master/CAD/Scintillator%20CAD%20file.pdf)
* After you purchase the SiPM and it arrives, PLEASE place it somewhere safe and load-free. Do NOT crush the SiPM as it is very delicate (and expensive!)

### **Assembly Instructions**

1. Buy all required electrical components
2. For the Arduino Nano, be sure to upload the coincidence.ino code to it, as this ensures a muon will be counted! Refer to pdf attached below for specific detail.&#x20;
3. Solder the electrical components onto the 3 PCBs (Main Board, SiPM Board, SD Card Board). Use this as the guide to know where to solder the components: [https://github.com/spenceraxani/CosmicWatch-Desktop-Muon-Detector-v2/blob/master/PCB\_Files/SMT\_reference.pdf](https://github.com/spenceraxani/CosmicWatch-Desktop-Muon-Detector-v2/blob/master/PCB\_Files/SMT\_reference.pdf)
4. Drill 4 mounting holes into SiPM PCB. Polish it afterwards.&#x20;
5. Wrap the scintillator in reflective foil.&#x20;
6. Put optical gel on SiPM board and mount it to scintillator using the mounting holes on the SiPM board.&#x20;
7. Wrap both with electrical tape to make light tight. Important! Carefully wrap or else "light-leak" will occur. This will distort your results!
8. Plug the SiPM PCB into the Main PCB through the header pins.&#x20;
9. Finally, upload the SDCard.ino code to the Arduino Nano.&#x20;
10. Plug in a 5V power bank to the detector and make sure that the HV pin on the Main Board delivers 29.5 V.&#x20;

For greater detail, read the entire instruction manual: [https://github.com/spenceraxani/CosmicWatch-Desktop-Muon-Detector-v2/blob/master/Instructions.pdf](https://github.com/spenceraxani/CosmicWatch-Desktop-Muon-Detector-v2/blob/master/Instructions.pdf)

## (Please Read!) Miscellaneous Files/Instructions

* **Please make sure you have access to the STAR GrabCAD! If you do not, you will be unable to locate any of these files**\*
* **Also make sure you have SolidWorks 2019 and Ultimaker Cura 4.4.1!**\*
* **Please also purchase a Makerpass for Jacobs Hall Access. It will make your life so much easier for assembly**\*
* After you obtain your Makerpass, get training on the Wood Laser Cutters, Ultimaker 3D Printers, Electronics Lab, and FabLight metal laser cutter (this last one isn't really necessary but it's so fun that I think you should still do it!).&#x20;
* The detector CAD is located in the IREC 2020 GrabCAD under:&#x20;
  * Upper\_Section -> Payload -> Muons\_IRIS -> Detector\_CADs -> IREC20\_PAY\_MuonDetector.&#x20;
* Under the Muons\_IRIS folder, the other folder called "STL Files". These are the CAD files in the Detector\_CADs folder but translated into .stl files which can be passed in Ultimaker Cura and in turn be 3D printed.&#x20;

## Plan for IREC 2020

While we did collect data from our AirBears launch, it correlated only time with muon count. Furthermore, 4 separate SD files were created, meaning we had no idea at which height did the counts correspond to, making the data not as useful.&#x20;

To combat this, our beloved payload lead Jason Xu (Woo!) is working to merge IRIS and Muons together as IRIS records height (through pressure) which allows us to see how muon count correlates with other parameters besides time. Excited events to come!

## Sources

1. [https://www.space.com/32644-cosmic-rays.html](https://www.space.com/32644-cosmic-rays.html)
2. [https://www.pnnl.gov/main/publications/external/technical\_reports/PNNL-20693.pdf](https://www.pnnl.gov/main/publications/external/technical\_reports/PNNL-20693.pdf)&#x20;
3. [https://www.radioactivity.eu.com/site/pages/Cosmic\_Muons.ht](https://www.radioactivity.eu.com/site/pages/Cosmic\_Muons.htm)&#x20;
