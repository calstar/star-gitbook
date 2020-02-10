---
description: Intro Project 2020 due TBA
---

# Propulsion

![Ignition Testing for LE-165](../.gitbook/assets/ignitiontesting.PNG)

## Introduction

The purpose of this project is to ensure that new and returning members research various parts of a rocket propulsion system from both theoretical and practical engineering points of view.

The project consists of two parts: an in-person component and a project component.

### Returning Members

Returning members have no special requirements for Spring 2020. It is highly recomended to attend workshops and the Feed System Presenations hosted by Trevor.

If you are interested in contributing to a workshop \(highly encouraged\), please contact Trevor via Discord.

### Contact

If you have any questions about any part of the question at any time \(even if it's 4AM on a weekend\), do not hesitate to reach out to the propulsion lead \(Trevor\) or the propulsion deputy \(Sam\). Discord is preferred, but if you are having difficulty getting started with Discord, Email is fine.

* Trevor's Discord: zat15 \(accessible through CalSTAR discord\)
* Sam's Discord: Sam\_Phillips  \(accessible through CalSTAR discord\)
* Discord: in the \#propulsion channel
* Trevor's Email: tzinky@berkeley.edu
* Sam's Email: 
* Office Hours:
  * Trevor's OH: 4:5:30 PM in Kresge Engineering Library

    \(exact location may vary, will be announced on Discord\)

  * Sam's OH: TBA

    \(exact location may vary, will be announced on Discord\)

{% hint style="warning" %}
This project is intended to challenge you a little bit! You are not expected to know everything you need for this project going in, and it will almost certainly be necessary for you to ask questions and interact with the team lead and propulsion members. This is by design, and is intended to get you familiar with our workflow and asking for help when needed. If you feel intimidated by the intro project, please please please reach out to others! Everybody wants you to succeed!
{% endhint %}

## 1. In-Person Component

To satisfy the in-person component, you must attend **one** of the following events:

* Safety Workshop \(Will be 2 dates, TBA\)

In addition to attending a safety session, you are required to attend **one** of the following events. If you have time to attend more than one, you are encouraged to do so.

* Manufacturing workshop \(TBA\)
* Quantitative Analysis workshop \(TBA\)

Lastly, once you believe you have finished your intro project, you should schedule a time with Trevor during office hours to go over your submission. If you are super busy and can't find a time, then talk to me and we can sort something out.

## 2. Project Component

You may choose any of the two project components to complete. Both are intended to be of about the same difficulty, and should give you insight about the various engineering tasks that we undertake.

### 2.1 Fluids

This task involves assorted tasks related to fluids design in propulsion systems.

#### 2.1.1 - Injectors

Injectors serve to mix and atomize the propellants flowing into the thrust chamber. Injectors also help regulate the flow of propellants and ensure efficient combustion.

* Describe 4 types of injectors, and explain their pros and cons
* Design an injection system for the given engine.
  * Your design should consist of the following:
    * The selected injector type, and a justification for its selection
      * Factors to consider here are manufacturability/machinability and efficiency of mixing, among others
    * If there are multiple injection elements, describe their layout on the injection plate
    * The orifice area for each injection element. This can be calculated using an equation found in chapter 8 of Sutton \(9th ed.\)
  * The engine parameters are:
    * 1000psi chamber pressure
    * Mass flow rates are 0.17 kg/s for LOX, 0.08 kg/s for RP-1
    * 250 psi pressure drop across the injector
    * Injection plate diameter is 2”

#### 2.1.2 - Feed System Analysis

The following Piping and Instrumentation Diagram \(P&ID\) is for a simplified gas-fed system. For each component labelled, describe its function, and what would happen if that component were not included in the system. Note that this is not the entire feed system, just one side of it. There are 2 fluids in the system, N2 and RP-1.

{% hint style="info" %}
To get an idea of what some components are used for, consider walking through a cycle of filling the tank from the Fill/Vent, then feeding through either the injector or the vent in R3B2
{% endhint %}

![A simplified P&amp;ID diagram](../.gitbook/assets/capture.PNG)

In the diagram, all ball valves are "L-port".

The following page will be very useful in interpreting this diagram:

{% page-ref page="../tutorials/propulsion/propulsion-pipes-+-adapters.md" %}

#### 2.1.3 - Testing Procedures

The testing propulsion engages in necessitates the use of detailed procedures to ensure safe and effective testing. Procedures are written to be technically adaquate, but can be hard to read and understand. Here is an example procedure written for the P&ID system above with comments in red to aid in your understanding.

[https://docs.google.com/document/d/1JVZ57ZGFRJqKUsU6c2CBqbC9tXLGUoygCTmqfX7sT-w/edit\#](https://docs.google.com/document/d/1JVZ57ZGFRJqKUsU6c2CBqbC9tXLGUoygCTmqfX7sT-w/edit#)

After each step in this process, think about what lengths of pipe become pressurized or depressurized. What lengths of pipe are still pressurized when this process is completed? \(you dont need to present this at all, just think about it\)

#### 2.1.4 - Testing the Injector

The following problem is based off work that was done in Fall and Spring 2019.

The injector design in use in this problem is a pintle injector. The flow rate of fluid through the injector is proportional to the diameter of the manufactured pintle. Using a simulation, a pintle diameter was determined and a pintle manufactured to that diameter. The initial pintle design was tested, and determined to not produce the correct and expected flow rate.

A new pintle was produced with the aid of improved simulations. This pintle must now be tested to ensure that its flow rate is what is expected based off of the simulation.

Create a procedure that can be used to test the pintle, and when done send a message to Trevor on Discord that includes your new testing procedure. This new procedure will reference the piping system presented above. Trevor will review your procedure, and if the procedure is adaquate you will recieve the flow rate results from the test.

**Deliverables**

* A procedure to test the pintle 
* The final diameter of the pintle that produces the correct flow rate
  * Justification for why this final diameter is correct based on results from the test 

#### 2.1.5 - Flow coefficient

The flow coefficient of a component, often denoted Cv, is a very useful measure of its behaviour in the feed system.

Describe what the flow coefficient is, and explain why it is important to look at the flow coefficient of components when selecting them.

Then, showing your work, derive the pressure drop across this swagelok check valve \([https://www.swagelok.com/en/catalog/Product/Detail?part=SS-4C-1/3](https://www.swagelok.com/en/catalog/Product/Detail?part=SS-4C-1/3)\) when carrying RP-1 at a _mass_ flow rate of 0.08 kg/s. Discuss your answer, particularly whether this pressure drop is significant in the context of the feed system \(which operates at 1250-1800 psi\).

**Deliverables**

* Your injector design and area calculations
* Your interpretation of the P&ID diagram
* Your solution to the question in part 2.1.3

{% hint style="info" %}
All deliverables should be compiled into a powerpoint/google slides presentation
{% endhint %}

### 2.2 Thrust Chamber Design and Testing

This project involves design of a thrust chamber for a liuquid rocket engine, and design of a testing setup for a solid rocket motor.

#### 2.2.1 - Thrust Chamber Design

A thrust chamber is to be designed for a 1000lbf engine using Kerosene and Liquid Oxygen.

* Design constraints:
  * O/F ratio = 2.5
  * The feed system can supply up to 1200psi feed pressure, and an injection pressure drop of 250psi will be used.
    * Based on these parameters, decide on a reasonable chamber pressure.
  * The thrust chamber must fit in a 7.5” diameter airframe.
  * Ambient pressure will be 1atm

**Deliverables:**

* Chamber geometry: Using the Rocket Propulsion Analysis \(RPA\) software, determine the thrust chamber size and shape.
* Tank analysis: A total impulse of 30,000 N\*s is desired. Using the mass flow rates derived in RPA, determine the mass of each propellant required, as well as the associated volume.
* Material analysis: Pick three materials that are commonly used as thrust chamber materials and describe the pros and cons of each material in this application
  * A good analysis should include comparisons between quantitative material properties such as yield strength, thermal conductivity, and thermal expansion as well as qualitative material properties such as brittleness, machinability, cost, and corrosion resistance
  * If a metal is one of the materials chosen, it must be a specific grade i.e. 1018 steel vs just steel, or 316 stainless steel vs just stainless steel

{% hint style="info" %}
All deliverables should be compiled into a powerpoint/google slides presentation
{% endhint %}

#### 2.2.2 - Test Stand Mechanical Design/CAD

Just like any other subteam, our work requires the design and construction of many mechanical systems, often for a very specialized task. In the past, these have included structures to house the propulsion system in the rocket or on the test stands, testing jigs for various components, mounting brackets, and more.

In this task, you will design a test stand for testing small solid motors. Test stands are used to fire the motor while it is static on the ground. Test stands help verify motor design and test key features of any propulsion systems. Common features of test stands include thrust measuring devices, safety features, and, obviously, motor systems. In this project, you will design a small test stand intended to test fire solid model rocket motors up to a “G” class. Your design of this should ideally maximize safety and measurement accuracy, while minimizing costs and complexity.

![A small solid rocket motor of the type to be tested on your stand](../.gitbook/assets/image%20%2853%29.png)

{% hint style="info" %}
This is an intentionally open-ended mechanical design task. The purpose is to exercise your ability to think about problems and create mechanical solutions. If you don’t know where to start, try searching online for rocket motor test stands to get some inspiration.
{% endhint %}

**Design Constraints**

* Must be able to safely test fire up to a “G” class solid motor
* Must be able to handle various motor diameters up to 29mm
* Must be able to measure the thrust produced by the motor

**Deliverables:**

* You must make a visual representation of your test stand in some form. This can be using a CAD software program like Solidworks, Inventor, or Fusion 360. If you have no experience with any of these programs, you can create a clean and understandable hand drawing of your design. 
* A bill of materials including all part names, order links \(www.mcmaster.com is a great website for ordering pretty much any part you can think of, plus they have CAD’s on the website which is pretty great\), and prices. A template is provided here.
* A justification of your design. Factor of Safety calculations, while optional, would be nice. This can be just a quick paragraph or two explaining your thinking, possibly improvements, possible failure modes, etc.

{% hint style="warning" %}
**SolidWorks is only compatible with Windows!** If you use MacOS or Linux you have three options:

1. Use the on-campus CAD lab in Etcheverry 1st floor which has SolidWorks pre-installed.
2. Install Windows and then install SolidWorks.
3. **Only if the above is not feasible,** you may use a compatible CAD program of your choice \(Fusion 360 is recommended as it has a lot of resources online\).
{% endhint %}

#### 2.2.3 Engine testing

You now take your engine and put it into a feed system \(the feed system supplies fuel and oxidiser to the combustion chamber at the correct flow rates and pressures\). A very simplified P&ID \(piping and instrumentation\) diagram for the feed system is shown below:

%%&lt;&lt;&lt;&lt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;

The ball valves essentially act as on off switches - assume they all start in the ‘off’ position. The gauges display the pressure at the location they are in. The igniter produces a spark in the engine when you press a button.

Develop a procedure \(very precise step by step guide\) for how to test the engine and measure it’s thrust output on your test stand. You may assume that no modifications to your test stand are necessary to accommodate the new feed system.

Some example steps you will need to include are: opening the ball valves, checking the readings on gauges, closing ball valves, sparking the igniter.

Consider the safety aspects of each step, and the order they should be done in. Putting on safety glasses, for example, should be included in the procedure. Also consider a basic bit in the procedure for what to do if it goes wrong. We are not expecting this procedure to be perfect, but want to see how you tackle the problem.

Once you have completed the procedure, send it to Trevor or Sam before moving on to the next part of this problem.

Next, you run your test and acquire the thrust curve below. \(The thrust curve shows the thrust output of an engine as a function of time\). Is the motor suitable to use in a rocket with a total mass of 25kg \(assume this mass is constant throughout flight\), given you are launching from a 10ft long guide rail,? \(Your rocket needs to be travelling at least 50 ft/s by the end of the guide rail, and should have at least a 5:1 thrust to weight ratio\). Explain your answer with words and calculations and send it to Trevor or Sam.

&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;

**Helpful equations:**

F=ma \(Force = mass \* accelaration\) &lt;&lt;&lt;&gt;&gt;&gt;&gt;

**Deliverables:**

* A procedure for testing the engine on the test stand using the provided feed system
* An explanation on why the thrust curve does or does not work assisted by calculations

## Resources

{% file src="../.gitbook/assets/george-p.-sutton-oscar-biblarz-rocket-propulsion-elements-2016-wiley.pdf" caption="Rocket Propulsion Elements" %}

{% embed url="http://www.braeunig.us/space/propuls.htm" caption="" %}

