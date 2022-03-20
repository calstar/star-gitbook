---
description: General tip
---

# Using ANSYS

## FEA (Finite Element Analysis)

## CFD (Computational Fluid-Dynamics)

![](../../.gitbook/assets/19989695\_829713397188027\_1815486438543530461\_n.png)

The latest ANSYS (19) contains **2** CFD **modules**: Fluent & CFX. While CFX is easier to set up, it yields few useful data - not even the drag force. Therefore, we usually use Fluent. Everything below will be about Fluent.

![](../../.gitbook/assets/18238719\_788784077947626\_189882273304562384\_o.png)

(with all due respect to our Testing sub-subteam)

{% embed url="https://www.youtube.com/watch?v=tVFq7EnesXU" %}

This is one of the best **tutorial videos** of Fluent we have found. Follow through it and you will be able to do all that the team needs now.

### Tips for (Be) Fluent

1. The **CAD model quality** is crucial. It doesn't necessarily need to be very detailed, but here are some qualities that will ease the simulation tasks:
   1. **Air-tight**. It should be a single continuous entity because _what we will simulate is not its interior, but a block of fluid with a rocket-shaped hole_ cut from it. Do not let air inside the rocket.
   2. **Aligned**. If it is radially symmetric (which is usually the case for a rocket), please make sure **the main axis **_**coincides**_** ** (not just parallel) **with one axis** (ie. the z-axis) so that the rocket sits on the origin of e.g. the x-y plane. A radially symmetric body is probably also axially symmetric. Make sure the CAD is **symmetric about the x-z plane** (or y-z plane) so that if you _slice_ it along the plane (see tip 6), it will fall into two identical parts.
   3. **Empty**. CFD is about the airframe only and does not need the interior like the pretty avionics, as long as the center of mass is set right. You can **save 'only the outer parts'** when you export **an Assembly** **to a Part** in Solidworks. You can also save only the outer surfaces, but we have not figured out how to meld the 2-D surfaces into a body that can be processed in ANSYS - it only takes 3-D bodies.
   4. **Blunt** (optional). Non-differentiable sharp points such as the nose cone tip may or may not yield errors in meshing. Still, you want some accuracy in the nose cone shape. Slice an infinitesimal amount off the tip, for example.
   5. **No overlap**. It may sound silly, but redundant parts may arise when different teams build separate CADs and piece them together. The overlap will become physical nonsense in ANSYS.
   6. **No surface**, only solid bodies. A tutorial for fix surfaces in ANSYS DesignModeller is below
2. If the full CAD does not work even after repaired with the tricks described later, to **make a** '**wind-tunnel model'** from scratch that has nothing except what is needed in CAD. Particularly, make **one single body** that has the body, fins, boat tail, etc. all in one piece. Made properly, the wind-tunnel model should look boringly monochromatic in SolidWorks.
3. How to improve the CAD after it is done? With **built-in CAD tools** in ANSYS, specifically **Design Modeller (DM,** round green icon**)** & SpaceClaim (SC, square blue icon). SC is the default and is newer, prettier, and more intuitive at first glance, but it is hard to be precise in SC. Therefore, we **usually use DM**. **Select DM from the right-click menu and do NOT double-click** - that will pull up the default SC (unless you have changed the options), which can freeze the program for long. Still, it is easiest to make a good CAD in Solidworks in the beginning. DM is for CFD-specific polishes, which are often unavoidable.
4. You may have realized that our usual SolidWorks .SLDPRT is not a valid **CAD format** for ANSYS, because SolidWorks is a licensed software not willing to work with ANSYS. Furthermore, SolidWorks' own CFD software less capable than ANSYS. The solution is to **convert the CAD file into** something compatible, **.x\_t** or .step for example. Usually .x\_t is the best because it conserves certain parameters and is well-compressed.
5. The **Repair** & **Merge** tools in DM's Tools menu & **Body Operation - simplify** in Create are very useful in **simplifying the model** for CFD - detail is trivial. Try them one by one on your CAD. Pls be aware that Merge can take very long on over 500 entities & cannot be paused or stopped, so save everything and ensure power supply beforehand.
6. **Cylindrical enclousres** are more useful for our radially symmetric rockets.
7. **Make a moderately-sized enclosure** to ease computations with the 'Details' options in the lower-left corner. The diameter of the cylinder is usually 3 times that of the rocket (fins included). Leave much more space on the hind than on the front
8. **Slice** axially symmetric models into halves/thirds/quarters because they would yield the same results anyway. It also helps you to see the interiors and check whether there are leaks. **Remember to multiply back certain results** like drag in the end.
9. **Name surfaces** in the right-click menu before you close DM - not only the inlet etc, but also where you want to take data (e.g. you may want to know the drag on the sides of the fins). Use Ctrl to select multiple surfaces and name them into a same Named Selection.
10. If meshing fails, **slice** different sections **to debug**, just as you would comment out sections of buggy code. However, it is better to go back to Tips 5 & 8 and simplify the model first. (We are trying to develop custom meshing code as a last resort)
11. Try **parallel** processing if you can, even locally. CFD is a computationally intensive tasks.
12. **Explore models for solution** and their options. We usually try Transient SST because we heard it is an eclecticism between k-omega and k-epsilon. The _Help_ button below the _Edit..._ button lists their pros, cons, and underlying science.
13. **Average over** iterations for Monitors, e.g. over 5 iterations. This is averaging not over time, but over calculations.
14. We usually need **around 500 iterations** for mere convergence. Yes, convergence of quantities is key (and the primary pain) in CFD. We usually decide whether it has converged by looking at the plot by eye.
15. Try **double precision** in the options when you start up Solving if the result does not converge or look realistic. U do not usu. need it tho
16. **Animating too many pathlines may freeze** the frail old computers in the CAD lab. Be cautious when you set the default setting for step size/number.
17. Like _@Turbulent CFD Memes for Aerodynamic Teens_ on FB. Most of the memes on this page are from there.

{% embed url="https://www.facebook.com/CFDMemes" %}

![](../../.gitbook/assets/18424025\_791987614293939\_1903621450240058390\_n.jpg)

## Fixing (Sewing) Surfaces

2D surfaces break the process of enclosing the model with a fluid domain. They can be identified in DM by the Surface ('flag') icon in the Bodies tree

To fix them:

1. **Create new part** and make a **Named Selection** for every cluster of surfaces that can make a solid
2. Tools > **Merge**. First the edges, then the faces
3. Tools > **Surface patch** to fill gaps in surface body
4. Use Create > **Body Operation** & select Sew in the options to convert the surface body to a solid body. Be sure to turn on **Create Solid**
5. **Supress original surfaces**. Select them from yr Named Selection, so that only the solid remains
6. **Body Operation** & select **Simplify** to make the solid sim-friendly

## Inlet Conditions

**Velocity inlet** boundary conditions are used to define the velocity and scalar properties of the flow at inlet boundaries.

**Pressure inlet** boundary conditions are used to define the total pressure and other scalar quantities at flow inlets.

**Mass flow inlet** boundary conditions are used in compressible flows to prescribe a mass flow rate at an inlet. It is _not necessary to use mass flow inlets in incompressible flows_ because when density is constant, velocity inlet boundary conditions will fix the mass flow.

**Pressure outlet** boundary conditions are used to define the _static pressure_ at flow outlets (and also other scalar variables, in case of back-flow). The use of a pressure outlet boundary condition instead of an outflow condition often results in a better rate of convergence when back-flow occurs during iteration.

**Pressure far-field** boundary conditions are used to model a free-stream compressible flow at infinity, with free-stream Mach number and static conditions specified. This boundary type is available only for compressible flows.

**Outflow** boundary conditions are used to model flow exits where the _details of the flow velocity and pressure_ are not known prior to solution of the flow problem. They are appropriate where the exit flow is close to a fully developed condition, as the outflow boundary condition assumes a zero normal gradient for all flow variables except pressure. They are **not appropriate for compressible** flow calculations.

**Inlet vent** boundary conditions are used to model an inlet vent with a specified loss coefficient, flow direction, and ambient (inlet) total pressure and temperature.

**Intake fan** boundary conditions are used to model an external intake fan with a specified pressure jump, flow direction, and ambient (intake) total pressure and temperature.

**Outlet vent** boundary conditions are used to model an outlet vent with a specified loss coefficient and ambient (discharge) static pressure and temperature.

**Exhaust fan** boundary conditions are used to model an external exhaust fan with a specified pressure jump and ambient (discharge) static pressure.

\--from [http://jullio.pe.kr/fluent6.1/help/html/ug/node177.htm](http://jullio.pe.kr/fluent6.1/help/html/ug/node177.htm)
