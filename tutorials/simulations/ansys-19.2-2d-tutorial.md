# ANSYS 19.2 2D CFD Tutorial

2D Tutorial

## ANSYS Download and Installation Instructions:

Instructions: [https://docs.google.com/document/d/1l5zS3rDZNhere1akOaFCs\_O0VW4Dil8Atkec5RnhjSo/edit](https://docs.google.com/document/d/1l5zS3rDZNhere1akOaFCs\_O0VW4Dil8Atkec5RnhjSo/edit?usp=sharing)

ISOs:\
[https://drive.google.com/drive/u/1/folders/1grdEHUKfftCNnkoH3mhTrcDQaJvqN3aE](https://drive.google.com/drive/u/1/folders/1grdEHUKfftCNnkoH3mhTrcDQaJvqN3aE)

## Introduction

This tutorial introduces the general ANSYS CFD workflow which can be summarized in four steps:

1. Geometry (SolidWorks)
2. Mesh (ANSYS Meshing)
3. Setup/Solve (Fluent)
4. Results (CFD-Post)

## Geometry

While geometry creation is possible in ANSYS with the Design Modeler module, we will\
primarily be using SolidWorks to create our geometries.\


For 2D simulations, our geometry consists of a surface that represents our fluid domain. This means that you will cut out the area of any objects (ex. Airfoils, Fin Profiles) from the whole domain. The picture below shows the example model that that we’ve already prepared for this tutorial (2D\_Test\_v2.SLDPRT).

![](https://lh6.googleusercontent.com/7xRn\_ylqzozIauof5wuSxQPzwhycSBgpCT9JM7ShGWGWwA17wu8Y6wWqvc9dWsDrxB3Nx5MMdndVzQueWsDdo4fZOg23eUsP8jpGNfigLeQmX7D8oHjYtPPe38rzy1A-96nM08AG)

Download the SLDPRT file to your computer first before going to your Start Menu and running Workbench 17.1/19.2, which looks like this by default:

![](https://lh5.googleusercontent.com/s4lADLH5SBQ30\_YUKsO6FoQKfa2DWzsOhuI0QptSSEpTpt2uYu\_\_82tJUNLNv3axWV7tfMb58TsDWrFnlbayhNUGzleDn-0\_SVKZczLenrkKjYWIRktk0Uuj2GIL-\_ZB7\_lPhYxj)

Workbench is the digital “workbench” where you set up simulations to run. The blank slate under “Project Schematic” is where you layout the different system blocks available to you in your Toolbox on the left.

Begin by dragging and dropping a Geometry block into the Project Schematic workspace. You may have to click the + next to Component Systems to expand the list.

![](https://lh5.googleusercontent.com/NR5nX-X8gbl7RYstfWF8wH-A2Ca7c6166LedxoeoAIaP6b3U1dZ7Hru0FOw\_2gI2xKb3TiflY1KAvzNKN3SH-DTgRoV0Gij\_4Jpg8jbOe3lYwXy8Cq5VYg6BVZRWf1ZRlmYk2olr)

Right click the cell of the Geometry block with the “?” and import the SolidWorks part.

## Mesh

The next step is meshing, which is the process of discretizing our fluid domain into elements and nodes. A high level view of how CFD works is that the solver takes your mesh and solves a set of fluid equations for each individual element.\


Element size can be considered the ”resolution” of the mesh. In general, we want more elements (aka smaller elements) in areas that we expect to see high changes in pressure and/or velocity. For example, we try to use inflation layers in areas where we expect a boundary layer to form. Areas further away from our interest areas are allowed to have larger element sizes because there will be less change within an element in those areas.\


Click and drag a Mesh block over the Geometry block you just created. A new Mesh block will appear, with a line connecting it to the Geometry block. This indicates that it is pulling geometry information from the Geometry block.

![](https://lh3.googleusercontent.com/NkOU3pr4zU9BJmdoSxetsVFcIDygy7DKh7w5i9nfKtF6tPDVsBHVrKG\_4VJmjN67icUlNeIh\_Isz0fCdx8yW6J9KmypPazXx6Mr1FzpDIEb8thnN1h7tcw8ubb8euMBhB2C0k3wn)

Double click the Mesh cell to open up ANSYS Meshing in a new window.\


In ANSYS Meshing, you will first need to make named selections. These will mainly be used in Fluent later to create boundary conditions.To create named selections, Ctrl+ left click to select all the edges you want to be grouped together. Then right click and select ”Create Named Selection.” If you’re unable to select edges, press Ctrl+E to switch to edge selection mode, or go to the top of the window and select the icon.

![](https://lh6.googleusercontent.com/ap8QcCEj9nZDOE9S8ED7gScl4mFRqiksDSDL16BgB499G0Jxe\_SBeLh-KMr9ORIIYNjPSCZcsU-td\_WJZ9kVLgtiIHLsj7dl7wQjeTYJhHOesNHMzgELpi9DeovL\_EJvUfl\_nKAf)

You may also find it useful to switch to Box Selection mode when selecting multiple edges at a time.

![](https://lh5.googleusercontent.com/PNuxb\_oUSrwQ1S0cPkm\_PMRSktct8gHqCjcqlia8AF1-wPt2bPzqWAB\_0WE-9ctlZPJAGDC3tQAEdAY1Y7T98vJRRmev44rZZCSuAdjasfAGHGmSIycQdATAooN-nUXJgPnXuCgd)

Create named selections for the wings (WINGS), ground (GROUND), left edge (VELOCITY-INLET), right edge (PRESSURE-OUTLET), and top surface (SYMMETRY). Then switch to surface selection mode, select the entire surface, and name it FLUID.\


Now we’ll specify our meshing settings. To enable meshing options, select ”Mesh” from the outline on the left. In the Details panel in the bottom left of your screen, expand the sizing options. Set the following settings:\


1\. Size Function: ”Proximity and Curvature”

2\. Relevance Center: Fine

3\. Smoothing: High

4\. Span Angle Center: Fine

5\. Num Cells Across Gap: 10

6\. Min Size: 0.001m

7\. Proximity Min Size: 0.001m\


Then use the Mesh Control menu to set local mesh parameters.

![](https://lh4.googleusercontent.com/4TjgYfmZ01I\_mh\_MHaIs1yE04ZPDc4VITHbh5h0OLcdF5l7VnuS7TGKDRt-L0sJT-QXBxZc-cVnAB-BvLmG2ryg1zTG3ugUKF88FWPRpJQGevJaFZiMoRSFhdhgM-0w5UhTOJevQ)

First select Sizing. Select the edges of the wing, then click ”Geometry” in the Details panel. Select the ”Apply” button to set the selection. Then set the element size to 0.0005m. After that, select Refinement from the Mesh Control menu. Select the surface for the geometry selection. Set the refinement to 1. After this is done, right click “Mesh” in the Project tree and select “Generate Mesh”. Once the mesh generates, you should be able to the outline of how the program divided the surface into individual elements. Save the project and close the ANSYS Meshing window.

## Setup/Solve

Now that we have our mesh, it’s time to read it into our solver. Click and drag the Fluent block over the Mesh block to add and connect. Double click Setup, and when the Fluent Launcher window opens up choose Parallel processing and input the number of processors your computer has under processes. You can find this by going to the Performance tab of Task Manager and seeing how many “Logical processors” your computer has. If your computer has graphics cards, you can enter them under GPGPUs.

![](https://lh3.googleusercontent.com/tfXiruksJLpju6FpD9fjmlB1Yr8lkCJArN0UNBeC0TCEcl\_WznKw1u\_\_SYvWXbnbVr3OCMgmwNkK5P-lBNJF9j2grU66S\_JaL8EdAVeAuJZol\_S7qEbzodTLlOdP13I38XACDsQQ)

Once Fluent loads the mesh, go to the Tree on the left side and:

1. Select Models. Select “Viscous” and click “Edit”. Under Models, select “Reynolds Stress (5 eqns)”. Keep everything at default values and press OK.
2. Select Boundary Conditions on the left Menu. If you did the named selections correctly, you should have named selections for the ground, interior-fluid, pressure-outlet, symmetry, velocity-inlet, outlet, and wings. Select velocity-inlet and make sure the type is also “velocity-inlet” (you should now be able to see why we named the selections the way we did). Click Edit and change Velocity Magnitude to 20 m/s. Then, select the ground, make sure the type is “wall”, and click Edit. Change the wall type to moving wall and change the speed to 20 m/s. Make sure the direction of the movement is in line with the inlet velocity (should be in the X direction). Then select the pressure-outlet and make sure the type is ’pressure-outlet.’ Click edit and make sure the pressure is 0 gauge pressure. For symmetry, make sure the type is “symmetry”.
3. Select Solution Methods from the Tree. Change the scheme to “Coupled”, and the Turbulent Kinetic Energy, Turbulent Dissipation Rate, and Reynolds Stresses all  to “Second Order Upwind”. Then check the box for “Pseudo Transient”.
4. Select Solution Controls from the Tree. Change the following values: Pressure to 0.5, Momentum to 0.5, Turbulent Kinetic Energy to 0.75, Turbulent Dissipation Rate to 0.75, and Reynolds Stresses to 0.75.
5. Select Monitors. Click “Residuals” and select “Edit”. Change Convergence Criterion to ’none.’ Click OK. Then, under ’Residuals, Statistic and Force Monitors,’ select lift from the create menu. Check the boxes for “Print to Console” and select wing as the wall zone. Make sure the force vector is the right direction (should be Y). This will create a plot of the coefficient of lift per iteration while running the simulation.
6. Select Solution Initialization from the Left Menu. Select Hybrid initialization and click initialize.

After the Console tells you that initialization is done, click Run Calculation on the Left Menu. Put in 50 iterations in the number of iterations and click calculate. Watch the convergence plot. Make sure the residuals and/or the CL is converging. For the residuals, this means that they are below 1e-02 times smaller than they were in the beginning. For the CL, it means that the plot ends up at approximately one value over many iterations. Continue calculating in 50 iteration sets until the simulation converges.

Once done with the simulation, click Reports from the left menu. Select “Forces” and click Set Up. Select the wings as the wall zone and specify the direction vector such that lift is shown. Press Print and the amount of downforce will be reported in the console.

## Results

While we can pull downforce numbers from Fluent quite easily as you just saw for yourself, in many cases we want to be able to visually see our flow to determine how the flow is actually behaving. Close the Fluent window and add a Results block to the Project Schematic. Double click the new block to open up CFD-Post.

First, let’s add a Contour to see what our velocity and pressure distributions look like. Click the Contour icon at the top of the screen.

![](https://lh3.googleusercontent.com/3vi-Fyt\_VN-PJ4GBdxm6U\_cRaMja8aQPJFcMU5oN1mEa7vJrtLvyiaY3\_dD4YBN3SrY5sFIEj\_ahRq6hDDclJ4ahEjQUi0H20X0JmqKV-8Pkqrtm0xiCbBwRz3-0Kx9ab2kkKDo2)

Then for Locations, choose symmetry 1. For # of contours, select 20. Press Apply to generate the plot. Play around with # of Contours to see how the visualization of the pressure distribution changes. Then, add another Contour but select Velocity as the variable instead.

Next, let’s add a Streamline to see flow behavior. Click the Streamline icon to the right of the Contour icon. Specify the streamlines to start from velocity inlet, and change the # of points to 50. Click Apply to generate the plot.
