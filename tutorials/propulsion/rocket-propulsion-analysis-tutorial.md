---
description: 'An intro to RPA: how/what to download, important components, etc.'
---

# Rocket Propulsion Analysis Tutorial

## Basics & d**ownload instructions:**

This YouTube video covers the basics of using the Rocket Propulsion Analysis\(RPA\) Software. This doesn't cover how to model the thrust chamber for the intro project, but it will help you become more familiar with the program:[ https://www.youtube.com/watch?v=F3W3zZj4zX4](https://www.youtube.com/watch?v=F3W3zZj4zX4)

**NOTE**: This YouTube video uses the RPA Lite version. In order to model the thrust chamber you must **download the RPA Standard Edition Trial Version.** \(The C++ one is not needed\)

Trial version of RPA Standard Edition v.2.3.2 has the following functional limitations:

* The user may run the analysis 3 times without restarting the software. To continue with evaluation, the application has to be restarted.

RPA downloads can be found here:[ http://propulsion-analysis.com/RPA/download.htm](http://propulsion-analysis.com/RPA/download.htm)

Complete User Manual\(v2.3\): [Rocket Propulsion Analysis - User Manual \(rocket-propulsion.com\)](https://www.rocket-propulsion.com/downloads/2/docs/RPA_2_User_Manual.pdf) 

## **Important Concepts:**

* Engine Definition: 
  * define the parameters for the combustion chamber and nozzle sizing
    * Nominal thrust, nominal mass flow rate, or throat diameter must be specified
  * switching on the flag for performing the thrust chamber thermal analysis
    * specify additional heat transfer and chamber cooling parameters on the screens Heat Transfer Parameters and Thrust Chamber Cooling.
  * Can define the type of engine feed system
    * parameters for cycle analysis can be specified on the screen Propellant Feed System
* Propellant Specification:
  * Define propellant type\(s\) and mixture ratio. The mixture ratio can be specified either as an O/F ratio \(ratio of "oxidizer flow rate" to "fuel flow rate"\), or as an oxidizer excess coefficient, given as ratio of desired O/F to stoichiometric O/F.
  * Click Add Oxidizer/Fuel. You can filter the list in the dialog window, using a regular expression\(ex “oxygen”\). The filter pattern is applied to both columns of the table.
* Nozzle Flow Model:
  * Nozzle Conditions: If you are solving the nozzle flow problem, you have to define at least nozzle exit conditions, specifying one of three parameters: nozzle exit pressure, nozzle expansion area ratio, or nozzle expansion pressure ratio.

