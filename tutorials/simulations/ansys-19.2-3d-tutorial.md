# ANSYS 19.2 3D CFD Tutorial

### ANSYS Download and Installation Instructions

Instructions: [https://docs.google.com/document/d/1l5zS3rDZNhere1akOaFCs\_O0VW4Dil8Atkec5RnhjSo/edit](https://docs.google.com/document/d/1l5zS3rDZNhere1akOaFCs_O0VW4Dil8Atkec5RnhjSo/edit?usp=sharing)

ISOs:  
[https://drive.google.com/drive/u/1/folders/1grdEHUKfftCNnkoH3mhTrcDQaJvqN3aE](https://drive.google.com/drive/u/1/folders/1grdEHUKfftCNnkoH3mhTrcDQaJvqN3aE)

### Tutorial

3D Meshing & Fluent Guide v2

1. DesignModeler
   1. Notes:
      1. After pretty much every step, you will need to update your geometry by clicking “Generate”. For the sake of clarity, it’s not included in this guide.
      2. SAVE OFTEN
      3. Ansys defaults to metric, so all dimensions following this will be metric unless otherwise stated.
      4. If DM gives you errors/issues about your geometry, try Boolean uniting your imported CAD into one solid piece
      5. DM allows you to hide individual faces by right clicking on them and selecting “hide face”. This is useful for editing your model after it’s been subtracted from the fluid body.
   2. Import your STP or SW file: File -&gt; Import External Geometry File
   3. Create the fluid body: Create -&gt; Primitive -&gt; Box![Screenshot \(59\).png](https://lh4.googleusercontent.com/x9piIcvihJKaKnKh_3az9_Xfl3FHj9hWxTokUKethQSLm-zj1NpQwT3BVsS6A-WUBCKRfdJviFyAw64U1RK0VzIo_FMHe9cSH2yxaFRR1d0CD_3wGWzqrG3kr3s4-mW0GBuO4u_E)
      1. Tip: using the  “two points” box type is generally much much easier than 1 point and a diagonal ![Screenshot \(60\).png](https://lh3.googleusercontent.com/9zlFq_AhXpxHHT01I67C4a-SwFsOpRZmPDnxhs8uvHoYR2eVdFJ8UYEoIXAo5iM4RL1KMtBUgA6FQPcVQkJTkovaA3pda59e2i5MVo65mjAAPmZb_KHSActtVP7uHHKA26Rwkbag)  
      2. Again, this is possible in SolidWorks, this way is just less buggy.
   4. Create a box that contains everything you want to simulate and then some. For half car sims, we’ve generally been using the two points method with \(-8,-3,0\) and \(15,0,4\).
      1. You should see that this creates a box surrounding the car with one wall going down the centerline of the car.
   5. Boolean out your imported CAD model from your box: Create -&gt; Boolean
      1. Set Operation to “Subtract”
      2. Target Body -&gt; Fluid
      3. Tool Bodies -&gt; CAD model \(could potentially be multiple bodies\)
   6. At the base of anything protruding from the box, you should see rectangular-ish holes
      1. Put a fillet on the edge of this hole traditionally \(While not necessary, it can reduce errors\). Create -&gt; Fixed Radius Blend
         1. Before: ![dm holes.PNG](https://lh6.googleusercontent.com/4hWIX8hiaLhSKigbigtw6jWhabeNW15xYFiu3ME_V6Q8ldRsje3IbBRcjlzHwKHjn1YDeCUev1sjHXX1DGpzy3YlR_Z2XebAMs0xnJFt4DNyZ4fpRjWrq1ZYmkuUHlNBBAAVESI8)
         2. After:![dm\_fillet holes.PNG](https://lh3.googleusercontent.com/hivO_7SucXBQn63ZNz3UadVTiym7EuQTQJ3XTvsCb2VFretpUd3uCv7Sm1-MZoqyU4qrmgW8g23C5QJXjkSE15VBmzq1HpJfdkVicqLJ7qPPgKMCfTtWlhqlof9zXfRgzhBxbukC)
   7. Create your named selections: Tools -&gt; Named Selections or right click on a face -&gt; Named Selection
      1. Coloring by named selection will make this process way easier and prettier looking: View -&gt; Graphics Options -&gt; Face Coloring -&gt; By Named Selection
         1. Note: Colors will only display on one side of a face, so this can look a little confusing at times.
      2. Fillets will \(unfortunately\) create tons of little faces. Make sure you select all of them!
      3. You do not have to get every face in one pass. Right clicking on a named selection allows you to edit the selections
         1. Toggling visibility on a named selection also makes it extremely apparent if you’ve forgotten to select a part of it.
2. ICEM
   1. Tips:
      1. ICEM is very unforgiving, so be careful not to screw up
         1. no pressure
      2. For whatever reason, most of the icons aren’t named and instead you must solely rely on the little pictures. I’ve included names of what the icon looks like to try and make up for this.
      3. Selections are made by left-clicking and confirmed by middle mouse
         1. Right click deselects them in the reverse order of selection \(ie, newest to oldest\)
      4. Setting your background to all black makes it easier to view your geometry: Settings -&gt; Background Style
      5. SAVE OFTEN
   2. After importing your model, immediately repair your geometry: Geometry -&gt; Cube and wrench icon -&gt; Enter
      1. If you see any yellow lines/surfaces, those are suspected to cause holes in your mesh, a fatal error. Go back to your model in SW and clean up/thicken the areas where you saw them.
   3. Toggle the display of points and surfaces: Model Tree \(on left side of screen\) -&gt; Check off points and surfaces
      1. ![icem.PNG](https://lh5.googleusercontent.com/7bE6Lrt6spISEL5Z716Zf52g4m9USwlHTD5ifayXbH-EbUfHpcyLSrSFlb0pOB8hPy9wZuK1S0iULGFJ1TnDKI__juKagPWfoyZkSkDLMdZtYlhixOPdR1-1msDO9H4yxCb8TtLP)
      2. Deselecting curves can help declutter your screen
   4. Create fluid body: Geometry -&gt; Cube and pencil
      1. Change part name to fluid
      2. Select two opposite corners of your bounding box by clicking on them
   5. Set your mesh parameters:
      1. Mesh -&gt; Cube and two globes -&gt; Set Global element seed size -&gt; max element to 1 m
      2. Within the same dialog on the lower left, click on the orange triangular icon with the gears
         1. ![prism icon.PNG](https://lh6.googleusercontent.com/rxj3FPs0yXH3_hP6VAF3KZCB4Y_WCPRhgifv_1rsXnQ-4gxk9JLB2MfFNofOM3TyWNme6u6DMscDjAVTxBBpae_2eCpKUTrscPe018VjLq6vj-WdbBvMG4o_UT5iFZkYHg2LVCJA)
         2. Scroll all the way to the bottom and click on “Advanced Prism Meshing Parameters”
            1. Select “Do checks’ and “Do not allow sticking” and apply
      3. Set your part mesh parameters: Mesh -&gt; Cone, cylinder, and sphere
         1. See [here](https://docs.google.com/spreadsheets/d/14glI9kQquGwdVE2VhNbSxes4zF_oPPsIwhnScXuXLYQ/edit#gid=0) for the settings.
         2. Notes:
            1. Increasing number of layers and decreasing maximum size causes computing time to increase dramatically. Halving your maximum size will lead to far greater than two-fold increase in time. Make sure that you are only being as accurate as you need to be.
            2. Example pic:
   6. Create points for your mesh densities: Geometry -&gt; Three black dots and pencil
      1. You can place points using the following tools:
         1. Computer screen with dot places points wherever you click \(Quick, but inaccurate\)
         2. Circle with 3 dots allows you to place points at the center of a circle \(useful for wheels\)
         3. Two black dots and blue dot allows you to place points halfway between two other points
         4. Blue arrow allows you to put point a certain distance away from a known location
      2. Place points at the places specified in the [settings doc](https://docs.google.com/spreadsheets/d/14glI9kQquGwdVE2VhNbSxes4zF_oPPsIwhnScXuXLYQ/edit#gid=0).
   7. Create mesh densities: Mesh -&gt; Cube with rho
      1. See [settings doc](https://docs.google.com/spreadsheets/d/14glI9kQquGwdVE2VhNbSxes4zF_oPPsIwhnScXuXLYQ/edit#gid=0) again.
      2. Notes:
         1. To create a cylindrical density zone \(the ones that are specified as “connected” on the settings doc\), select both points before hitting apply.
         2. Be very careful of accidentally creating nested mesh densities; they will make a bajillion elements and take forever
         3. Large widths with small sizes will also take forever and make a bajillion elements
         4. You can edit/delete densities by right-clicking on densities in the
         5. left panel  ![Screenshot \(61\).png](https://lh3.googleusercontent.com/EVgZGj_hDw4y3hBDVssqcV2KqJ5lMtVKOMCtp_XxWFxYs8_fUhJFFG8vGDugbXkE-Ar8Yhp3LYiwSxX-NMHWetcNpBRYqWpApyJoZ9LuEDhm3m2oWqPjTxK6sk5Uq5yq005U7mEB)
   8. Doublecheck all your mesh settings
   9. If you’re simulating rolling wheels, copy down the locations of the centers of the wheels, you’ll need it during Fluent
      1. Left panel -&gt; Geometry -&gt; Left click on points -&gt; show point info
         1. Copy down the output from the console to a txt file or something
         2. It doesn’t matter where the point is, as long as it’s on the axis of rotation of your tire
   10. Now you’re ready to mesh! Don’t run this on a laptop. It will take a very long time and probably fail. Archive your wbpj \(in Workbench, click File -&gt; Archive\) and transfer it over Chrome Remote Desktop to one of the sim comps
   11. Unarchive it. Open Workbench -&gt; File -&gt; Restore Archive
   12. Open ICEM back up
   13. Go into Settings → General and make sure you put the appropriate number of processors \(32 for SC1 and SC2\)
   14. Now it’s time to actually mesh. Mesh -&gt; Blue icon with colored arrows on it \(on the far right\)
       1. Select create prism layers
       2. Click compute!
       3. Wait for meshing to finish
          1. NOTE: A prompt may pop up asking you if you want to save the geometry. This typically indicates that the initial meshing has finished and ICEM is about to move onto prisms meshing. Select “No”.
       4. After meshing has finished, scroll up in the console and ensure that ICEM has properly meshed prisms. You should be able to see lines of blue text that the prism mesher outputs.
   15. Check your mesh: Edit Mesh -&gt; Cube with red check mark. Hit apply.
       1. Multi-face errors will crash fluent on orientation
          1. This is different from multiple edge errors - Fluent seems to be fine with those.
       2. If fix is an option for the error message, choose that. If it’s not, choose subset.
       3. If your geometry has a hole in it, gg
   16. Smooth your mesh: Edit Mesh -&gt; Iron with multicolored background \(not the iron with brown background\)
       1. Freeze Tetra 4, Penta 6, and Pyra 5
          1. Set iterations to 20 and quality to 0.5 and smooth
       2. Set everything to smooth
          1. Lower quality to .2 and smooth
   17. Repeat step o to check mesh one more time.
3. Fluent
   1. Notes:
      1. Error troubleshooting
         1. Crashes before 1st iteration - remesh
         2. Segmentation error - remesh
         3. Floating point error - remesh
      2. Use as many cores as you again \(for most of our desktops, try 8\). Don’t use double precision unless single precision gives you convergence issues and you don’t want to remesh
   2. Models -&gt; Reynolds Stress \(7 eqn\)
   3. Boundary Conditions
      1. Set inlet velocity and ground to 20 m/s \(process is identical to 2D\)
      2. If using wheels:
         1. Wall motion -&gt; Moving Wall
         2. Motion -&gt; Rotational
            1. Set xyz coordinates to whatever you copied down from ICEM
               1. If you used the standard origin and orientation, you should be able to use the points on the [settings doc](https://docs.google.com/spreadsheets/d/14glI9kQquGwdVE2VhNbSxes4zF_oPPsIwhnScXuXLYQ/edit#gid=0).
            2. Rotation axis direction should be \(0,1,0\), unless you made your model funny.
            3. Speed: -87.5 rad/s
               1. Alternatively, you can set this to positive and flip the direction of your rotation axis
         3. Example:
         4. 
      3. Double check remaining zones \(symmetry, chassis, etc\)
   4. Solutions Method
      1. Scheme -&gt; Coupled
      2. Set Momentum, Turbulent Kinetic Energy, Turbulent Dissipation Rate, and Reynolds Stresses to 2nd order
      3. Note: If you have convergence issue, try running the first 50 iterations with 1st order, then switching to 2nd order after 50 iterations
      4. Enable Pseudo-transient
   5. Solution Controls
      1. Pressure: 0.65
      2. Momentum: 0.35
      3. Turbulent Kinetic Energy: 0.5
      4. Turbulent Dissipation Rate: 0.5
      5. Reynolds Stresses: 0.5
   6. Monitors
      1. Create lift and drag plots for whatever you’re modeling:
         1. For Ansys 19.2 Top menu: Solving → Reports → Definitions → New → Force Report →  Drag/Lift
         2. Ansys 17 options are still in Monitors
      2. Select residuals -&gt; edit -&gt; disable convergence criterion
   7. Initialization -&gt; Initialize
      1.  Initialization might fail. If it does, go to more settings -&gt; set number of iterations to 15 or 20
   8. Run calculation: Try starting off with 200-300 iterations

