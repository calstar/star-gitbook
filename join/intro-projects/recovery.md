---
description: >-
  This is the most up to date version of our intro project but is subject to
  change.
---

# Recovery

## **Introduction**

Welcome to the Recovery specialty's intro/returning project page! Glad you're here.

The recovery specialty is tasked with safely landing the launch vehicle. This responsibility requires working with constraints set in each project, attention to detail, and producing creative and efficient solutions. We work on numerous different components that are essential to the safe landing of the rocket including but not limited to: parachute size and geometry selection, parachute deployment altitude selection, ejection and separation mechanics, and avionics sled design. We require a general understanding of mechanics, electronics, simulations, physics, and more.

For any questions/help please feel free to reach out to Recovery specialty lead Cassidy at office hours or online through Discord or email. We also have mentors you will be assigned to as advisors (and friends) this year so feel free to contact them with any questions. Office Hour times are listed below. OH are highly encouraged if you need help!&#x20;

* Cassidy Powers | Recovery Specialty Lead
  * OH: Mondays 5-7pm and Wednesdays 5:30-6:30pm or ping me on discord
  * Email: cassidypowers@berkeley.edu
  * Discord: cassidy\_powers

{% hint style="info" %}
**Workshops:** There will be these workshops during the onboarding period:\
1\. (09/15) - CAD (demonstration on how to use Solidworks computer modeling software)

2\. (09/19) - Openrocket/Parachute Sizing

3\. (09/26) - Visual demonstrations of the avionics bay, avionics bay wiring, and parachute harness (9/23/21)

4\. (10/03) - General manufacturing

5\. (TBD) - Mock Launch Day, Parachute packing, black powder weighing, ground test
{% endhint %}

## **New Member Project **_**(18 hrs)**_

The new member project for the recovery sub-team is intended to:

1. Introduce a **strong technical foundation** for the critical components of the recovery subsystem to new members
2. Learn to work with constraints, similar to **industry**
3. Encourage **collaboration/asking for help** to accomplish these tasks
4. **Connect** new Recovery members with returning Recovery members.

The deliverables of the project should be presented at the final GM of the onboarding period. Remember! This project is meant to be challenging, but attainable, especially if you ask for help. So please ask questions, come to workshops, and come to office hours!

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### **Task 1 | Jacob's Trainings **_**(Urgent!**_) (5 hours)

**Due: October 13th**

**Deliverable:** Screenshots of completed training from bCourses: Laser cutting training, electronics lab training, and general workshop training. Upload these into the google drive at this link, under a folder with your name.

The majority of our manufacturing will be done in the Jacob's Hall Maker Space. It is a great place to work on a variety of projects with numerous tools and super helpful staff. We would like you to complete laser cutter training, electronics lab training, water jet training, and metal shop training as these are the tools or sets of tools we use that require in person training. After this introduction to the Jacobs makerspace, you will no doubt use your pass for projects outside of STAR including personal projects and also some classwork. Steps to complete:&#x20;

1. Apply for a Maker Pass by September 12th at this link. This will not guarantee you a pass. Jacob's will let you know if you get a pass or not by TBD.&#x20;
2. After applying for a Maker Pass, you need to complete the "General Workshop Safety" (GWS) online module that will be linked when you complete the application.&#x20;
3. Then you will need to complete tool-specific online trainings (in the same bCourses class as GWS -> under Jacobs Hall -> Equipment) for each piece of equipment you want to use, including&#x20;
   1. Type A 3D Printers&#x20;
   2. Laser cutters&#x20;
   3. Electronics Lab&#x20;
4. In order to have access to the Electronics Lab and Laser cutters you will need to attend an in person training as well as completing the bcourses training. Trainings should not take more than 2 hours. Coordinate with your teammates to sign up for in person trainings together! Contact Cassidy if you are unable to get a Maker Pass. There are other makerspaces on campus so we can figure something out.

**Contact Cassidy if you are unable to get a Maker Pass. There are other makerspaces on campus so we can figure something out.**

{% hint style="info" %}
**Note:** A Maker Pass costs $125 per semester unless you are able to get a fee waiver for demonstrated financial need. If you have any concerns, please let me or Rocklin (Operations Lead) know and we can definitely work something out to help you purchase one!
{% endhint %}

{% hint style="info" %}
**Link:** [http://jacobsinstitute.berkeley.edu/our-space/makerpass/get-maker-pass/](http://jacobsinstitute.berkeley.edu/our-space/makerpass/get-maker-pass/)
{% endhint %}

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### **Task** 2 **| Stage Separation Flow Chart **_**(2 hrs)**_

**Due: September 29th**

**Deliverable:** Filled out flow chart breaking down each event of stage separation. Cover possibilities of both success and failure at each event and the resulting situation. Remember our main goal is safe recovery of the rocket. Feel free to display this however you would like. One example for how this may look is seen to the left. Upload these into the google drive at this link, under the same folder with your name from task 1.

You can assume all separation occurs due to "pyrogen ignition" regardless of mechanism or type or charge. Don't worry too much about how the separation is actually occurring as the mechanisms vary. I recommend checking out Apogee Rocketry's basic breakdown of events, but please keep in mind this does not cover stage separation.&#x20;

The basic idea with stage separation is that it is more efficient for the rocket to fly up without the extra weight of a used up motor and the surrounding airframe so the lower part or stage of the rocket is released at a certain altitude once the lower motor has burned out. Apogee has a good explanation of this process as well: How 2-Stage Rockets Work (although they initiated the staging with "headend ignition," which is different from the one implemented by our team but it is still relevant). Openrocket simulations are a good way to visualize the steps of our two stage recovery system. Download Openrocket (directions are in the gitbook under "Tutorials">"Software Setup">"Openrocket Installation") and then download the file linked below containing the most recent stage separation Openrocket file: stage\_sep\_v2\_7\_2.ork.&#x20;

Select "Flight simulations" and "plot" to get a sense of what is happening to each stage throughout the rocket's flight. The "Motors & Configuration" tab is useful for understanding when and where each parachute will deploy. Also in looking at the "Rocket Design" try to picture where in the rocket separation will occur.&#x20;

In understanding the recovery steps of Stage Separation, you will grasp the recovery steps of our single stage competition (IREC) rocket as well.

{% embed url="https://www.apogeerockets.com/Tech/Phases-of-a-Rockets-Flight" %}

{% hint style="warning" %}
**Stage Separation Openrocket File:** [**https://drive.google.com/file/d/1bbOjms46XsEmK8uuQKp6Asz5ojwOvLvK/view?usp=sharing**](https://drive.google.com/file/d/1bbOjms46XsEmK8uuQKp6Asz5ojwOvLvK/view?usp=sharing)
{% endhint %}

{% embed url="https://www.apogeerockets.com/Tech/How_2-Stage_Rockets_Work" %}

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### **Task** 3 **| Parachute Selection **_**(3 hrs)**_

**Due: October 6th**&#x20;

**Deliverable:** Filled out the chart below (this is easily done in excel/google sheets) with the proper calculations and information from open rocket. Include a short justification of the formulas used and steps followed. (Use the Arktos OpenRocket file attached at the bottom of this section). Upload these into the google drive at this link, under the same folder with your name from task 1.

Select the best combination of parachutes that satisfies the constraints below:&#x20;

* Drogue is deployed at apogee (maximum altitude)&#x20;
* Main is deployed at 800 ft above ground level (AGL)&#x20;
* Drogue Cd (Coefficient of Drag): 1.5&#x20;
* Main Cd: 2.2&#x20;
* Each component must not land with greater than 75 ft\*lbs of kinetic energy&#x20;
* Drift radius must be less than 2500 ft in 20 mph wind&#x20;

Fill out the chart below with all of the calculations and relevant information obtained from the open rocket.&#x20;

\~ Hint: Fill out the chart and do your calculations in google sheets so you can apply the same drift and kinetic energy equations to each box. Make sure you calculate kinetic energy in ftlbs not J. This link has a quick explanation on how to calculate kinetic energy in ftlbs. \~ Bonus: Play around with OpenRocket and select your own combination of sizes that would be even better than the best option listed above. Or check out the StageSep ork and check out options there!

\~ Bonus: Play around with OpenRocket and select your own combination of sizes that would be even better than the best option listed above. Or check out the StageSep ork and check out options there!

| **Parachute Options**                | Drogue Deployment Velocity (ft/s) | Drogue Terminal Velocity (ft/s) | Main Deployment Velocity (ft/s) | Main Terminal Velocity (ft/s) | KE of Upper Section before Landing (ft-lbf) | KE of Avionics Bay before Landing (ft-lbf) | KE of Lower Section before Landing (ft-lbf) | Drift in 20mph wind (ft) |
| ------------------------------------ | --------------------------------- | ------------------------------- | ------------------------------- | ----------------------------- | ------------------------------------------- | ------------------------------------------ | ------------------------------------------- | ------------------------ |
| _Option 1:_ Main - 72", Drogue - 12" |                                   |                                 |                                 |                               |                                             |                                            |                                             |                          |
| _Option 2:_ Main - 72", Drogue - 24" |                                   |                                 |                                 |                               |                                             |                                            |                                             |                          |
| _Option 3:_ Main - 60", Drogue - 24" |                                   |                                 |                                 |                               |                                             |                                            |                                             |                          |

{% hint style="info" %}
**Hint:** First calculate the masses of the upper, lower, and avionics bay sections using the given OpenRocket File for Arktos. In this case, the upper section is referring to all components above the avionics bay while lower section refers to all components below the avionics bay.&#x20;
{% endhint %}

{% file src="../../.gitbook/assets/sl-full-scale-v6.ork" %}
OpenRocket File for Arktos
{% endfile %}

{% hint style="info" %}
**Hint:** Fill out the chart and do your calculations in google sheets so you can apply the same drift and kinetic energy equations to each box. Make sure you calculate kinetic energy in ftlbs not J. This link has a quick explanation on how to calculate kinetic energy in ftlbs. \
[https://www.engineeringtoolbox.com/kinetic-energy-d\_944.html](https://www.engineeringtoolbox.com/kinetic-energy-d\_944.html)
{% endhint %}

{% hint style="success" %}
**BONUS:** Play around with OpenRocket and select your own combination of sizes that would be even better than the best option listed above. Or check out the StageSep ork and check out options there!&#x20;
{% endhint %}

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### **Task 4| Lines Diagram **_**(1 hrs)**_

**Due: October 13th**

**Deliverable**: Completed line diagram for dual-side dual-deployment (ie. one line diagram depicting main deployment and one depicting main deployment)

The image below is a line diagram for a single side dual deployment (meaning both the drogue and main are housed in the same part of the rocket). Use this image as a guide to understand the aspects that your line diagram should have. Such as: Shock cord Quick links Parachutes Parachute bags Rocket tubes U-bolt

5

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### **Task 5| Avionics Bay Assembly **_**(6 hrs)**_

**Due: October 13th**

**Deliverable**: A brief write up presenting your design (include pictures of the full assembly) and explaining your design methodology and decisions. Upload your write up and CAD files into the google drive at this link, under the same folder with your name from task 1. Please note that you must upload all parts contained within your final assembly file in order for me to be able to open your assembly file.

Creating CAD models is a skill every engineer should be knowledgeable about, and recovery is no exception. It is important to model things before manufacturing to avoid wasted materials due to poor design. Recovery designs and manufactures the avionics bays for all the rockets so proper documentation is needed. The avionics bay houses the altimeters and other necessary hardware that enables proper parachute deployment which is often mounted to an accessible sled. A typical avionics bay (av-bay) consists of the following:&#x20;

* Altimeters: tell the pyrogens for parachute deployment and stage separation when to deploy&#x20;
* Avionics Sled: secure the batteries and altimeters&#x20;
* Bulkheads- create sturdy and nearly airtight separations between different sections of the rocket allowing for pressure build up when the explosives ignite. This is critical for parachute deployment&#x20;
* Alignment Rods: orient the Av-Bay components such that the Avionics Sled can slide in and out&#x20;
* Access Hatch: the opening through which we can bring the altimeter sled in and out and we can connect wires to the altimeters on the altimeter sled&#x20;
* Batteries: power the altimeters&#x20;

You are tasked to create a full CAD model of a usable avionics bay to house 2 altimeters and 2 9V batteries. We have provided the appropriate airframe, batteries and altimeter part models that we frequently use below. Use these part files in your avionics bay assembly. You will have to create and design your own separate model parts for the altimeter sled, bulkheads, and alignment rods. Once you have completed all of the above part models, make an assembly of the entire avionics bay with all the components inside and properly constrained.&#x20;

* **Outer**
  * **Inner Diameter:** 3.900" (9.91 cm)
  * **Outer Diameter:** 4.014" (10.2 cm)
* **Coupler**
  * **Inner Diameter:** 3.786" (9.80 cm)
  * **Outer Diameter:** 3.900" (9.91 cm)

{% hint style="info" %}
**CADs of a 9V battery and a Stratologger Altimeter:** [**https://drive.google.com/drive/folders/1mKPF4cOOXk0YaSNkeCsWYUEElXhLPK8q?usp=sharing**](https://drive.google.com/drive/folders/1mKPF4cOOXk0YaSNkeCsWYUEElXhLPK8q?usp=sharing)
{% endhint %}

{% hint style="info" %}
**Help Starting:** Check out the STAR Internal page on the Avionics Sled for some helpful information. Join GrabCAD to see the CAD work for STAR's current projects. You should check out SSEP project's AvBays to see what AvBays can look like. SSEP contains three different av bays, one for the lower section parachute, one for the upper section main parachute, and one for the drogue parachute. By looking at these you can see how avionics bays can vary in size, shape and design.
{% endhint %}

{% hint style="info" %}
**NOTE:** This is an open, free-form project. There is no single way to create an avionics bay. As long as you can defend your design choices, we will accept your assembly. This is the most difficult part of the project especially if you do not have CAD experience. Please see Cassidy, Cassie, your mentors, or any of the other returning members if you have any questions; we want to help!
{% endhint %}

#### \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### Task 6| Mentorship (2 hours)

**Due: October 13th**

**Deliverable:** Upload a selfie with you and your mentor into the google drive at this link, under the same folder with your name from task 1.\
\
Meet for at least an hour with two returning recovery members. Ask for any help you need on your intro projects and get to know each other. This is both to promote the share of knowledge, but also for new members to meet and integrate with returning members.&#x20;

Once you decide to join Recovery, you will be assigned 2 returning members that you will meet with during the onboarding period. Meet at a coffee shop or somewhere else cool in Berkeley or on campus! If these meetings are not enough for you to get the help you need on your intro projects, you should definitely reach out to your mentors or other returning Recovery members for more help.

