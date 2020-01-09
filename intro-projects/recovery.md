---
description: >-
  This page is currently under construction and will undergo multiple changes.
  The finalized version will be noted as such.
---

# Recovery

## **Introduction**

Welcome to the Recovery sub-team's intro/returning project page! Glad you're here.

The recovery team is tasked with safely landing the launch vehicle. This responsibility requires working with constraints set by other sub-teams, attention to detail, and producing creative and efficient solutions. We work on numerous different components that  are essential to the safe landing of the rocket including but not limited to: parachute size and geometry selection, parachute deployment altitude selection, ejection and separation mechanics, and avionics sled design. We require a general understanding of mechanics, electronics, simulations, physics, and more.

For any questions/help please feel free to reach out to recovery sub-team lead Cheljea at officer hours or online through Discord or email. We also have Evan Borzilleri on as an advisor this year so feel free to contact him with any questions. Office Hour times/locations for both are listed below. OH are highly encouraged if you need help!

* Cheljea Jang \| Recovery Team Lead
  * OH: Monday 5 - 6:30 pm, 7:30 - 9 pm \(Kresge or tba each day\) 
  * Email:  cheljea.jang@berkeley.edu
* Evan Borzilleri \| Advisor
  * Email: evanjborzilleri@berkeley.edu

{% hint style="info" %}
**\[Workshop\]** = indicates that a workshop will be provided for the fundamentals of this task. Workshops are mandatory, and will make accomplishing the tasks much more simple. Workshop times are listed below:

* **\[OpenRocket\]** \| \[When\] \[Where\]
* **\[Solidworks\]** \| TBA
{% endhint %}

## **New Member Project** _**\(14 hrs\)**_

The new member project for the recovery sub-team is intended to:

1. Introduce a **strong technical foundation** for the critical components of the recovery subsystem to new members
2. Learn to work with constraints, similar to **industry**
3. Encourage **collaboration/asking for help** to accomplish these tasks

The deliverables of the project should be presented at the recovery subteam meeting **\(TBA\)** in the form of a .ppt slide deck containing snapshots of the various project pieces. Remember! This project is meant to be challenging, but attainable, especially if you ask for help. So please ask questions, come to workshops, and come to office hours!

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### **Task 1 \| Jacob's Trainings** _**\(3 hrs\)**_

**Due: October 7**

**Deliverable:** Screenshots of completed trainings from Bcourses.

The majority of our manufacturing will be done in the Jacob's Hall Makers space. It is a great space to work on a variety of projects with numerous tools and super helpful staff. We would like you to complete laser cutter training and electronics lab training as we will be using those the most often. After this introduction to the Jacobs makerspace, you will no doubt use your pass for projects outside of CalSTAR including personal projects and also some classwork.

**We would like you to complete Jacob's Hall general training, laser cutter training, and electronics lab training.** Screenshot the completed trainings from bcourses and include it into your final presentation.

{% hint style="warning" %}
**Note:** A maker's pass costs $100 for the semester. CalSTAR does offer club maker's passes if you sign up early enough. If you have any concerns, please contact Evan or Cheljea and we be more than happy will work something out. 
{% endhint %}

{% hint style="info" %}
**Link:** [http://jacobsinstitute.berkeley.edu/our-space/makerpass/get-maker-pass/](http://jacobsinstitute.berkeley.edu/our-space/makerpass/get-maker-pass/)
{% endhint %}

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### **Task**  2 **\| Parachute Selection** _**\(3 hrs\)**_

**Due: September 30**

**Deliverable:** Filled out chart with calculations and work. What you think the best option is given the constraints provided and justification of your choice.

**Workshops:  \[Recovery\] \[OpenRocket\]**

Select the best combination of parachutes that satisfies the constraints below:

* Drogue is deployed at apogee \(maximum altitude\)
* Main is deployed at 600 ft above ground level \(AGL\)
* Drogue Cd \(Coefficient of Drag\): 1.5
* Main Cd: 2.2
* Each component must not land with greater than 75 ftlb of Force
* Drift radius must be less than 2500 ft in 20 mph wind

Fill out the chart below with all of the calculations and relevant information obtained from open rocket.

| **Parachute Options** | Drogue Deployment Velocity \(ft/s\) | Drogue Terminal Velocity \(ft/s\) | Main Deployment Velocity \(ft/s\) | Main Terminal Velocity \(ft/s\) | KE of Upper Section before Landing \(ft-lbf\) | KE of Avionics Bay before Landing \(ft-lbf\) | KE of Lower Section before Landing \(ft-lbf\) | Drift in 20mph wind \(ft\) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| _Option 1:_ Main - 72", Drogue - 12" |  |  |  |  |  |  |  |  |
| _Option 2:_ Main - 72", Drogue - 24" |  |  |  |  |  |  |  |  |
| _Option 3:_ Main - 60", Drogue - 24" |  |  |  |  |  |  |  |  |

{% hint style="info" %}
**Hint:** First calculate the **masses** of the upper, lower, and avionics bay sections using the given OpenRocket File for Arktos. In this case, the upper section is referring to all components above the avionics bay while lower section refers to all components below the avionics bay.
{% endhint %}

{% file src="../.gitbook/assets/sl-full-scale-v6.ork" caption="OpenRocket File for Arktos" %}



{% hint style="success" %}
**BONUS:** Play around with OpenRocket and select your own combination of sizes that would be even better than the best option listed above.
{% endhint %}

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### **Task 3 \|  Avionics Bay Assembly** _**\(6 hrs\)**_

**Due: October 7**

**Deliverable**: A brief write up presenting your design \(include pictures of the full assembly\) and explaining your design methodology and decisions.

**Workshops: \[PDM\] \[Recovery\] \[Solidworks\]**

Creating CAD models is a skill every engineer should have down and recovery is no exception. It is important to model things before manufacturing to avoid wasted materials due to poor design. Recovery designs and manufactures the avionics bays for all the rockets so proper documentation is needed. The avionics bay houses the altimeters and other necessary hardware that enables proper parachute deployment which is often mounted to an accessible sled. A typical avionics bay \(av-bay\) consists of the following:

* Altimeters
* Altimeter Sled  
* Bulkheads
* Alignment Rods
* Access Hatch 
* Batteries

**You are tasked to create a full CAD model of a usable avionics bay to house 2 altimeters and 2 9V batteries**. We have provided the appropriate airframe and altimeter models that we frequently use below. You should create models for the altimeter sled, bulkheads, and alignment rods. Once you have completed all of the above models, make an assembly of the entire avionics bay with all the components inside and properly constrained. 

* **Outter**
  * **Inner Diameter:** 3.900" \(9.91 cm\)
  * **Outer Diameter:** 4.014" \(10.2 cm\)
* **Coupler**
  * **Inner Diameter:** 3.786" \(9.80 cm\)
  * **Outer Diameter:** 3.900" \(9.91 cm\)

{% hint style="info" %}
**Link for File Download:** [https://drive.google.com/open?id=1YP8dbC0DgkeTvMOsvlSa2kKPlNZkGhRv](https://drive.google.com/open?id=1YP8dbC0DgkeTvMOsvlSa2kKPlNZkGhRv)
{% endhint %}

{% hint style="warning" %}
**NOTE:** This is a open, free-form project. There is no single way to create an avionics bay. As long as you can defend your design choices, we will accept your assembly. This is certainly one of the more difficult parts of the intro project, especially if you do not have prior CAD experience. Please see Evan or Cheljea if you have any questions; we want to help! 
{% endhint %}

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

