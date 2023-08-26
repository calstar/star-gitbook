---
description: 'Created by Neelay. Updated by: Cedric (2022), Dulanya (2023)'
---

# PCB Design Mini-Project

The PCB you will be working on is a system to detect apogee (peak of arc of rocket) and deploy parachutes. There are 4 parts to the mini-project, you will be able (and are _highly encouraged_) to ask for help from the mentors at any point!&#x20;

1. Choose appropriate components for the PCB and create a BOM (Bill of Materials).&#x20;
2. Create the schematic for the board.&#x20;
3. Create the layout for the board.&#x20;
4. Prepare the board to be manufactured. (_Please do NOT actually place an order on any site for the boards.)_

## Board Requirements

* The board will be powered by a 12V/ 500mA power source.\*\
  _<mark style="background-color:green;">What does this mean?</mark>_ \
  _<mark style="background-color:green;">Each component we use will have a minimum voltage needed to operate, and a maximum needed to operate safely. The voltage of our power source is often much higher than this! This means we find a way to deliver a reduced voltage (in our case,</mark> <mark style="background-color:green;"></mark><mark style="background-color:green;">**3.3V**</mark><mark style="background-color:green;">) to power each component. This is usually done by using a</mark> <mark style="background-color:green;"></mark><mark style="background-color:green;">**voltage regulator.**</mark>_&#x20;
* The board will be able to measure and report the altitude of the rocket. \
  _<mark style="background-color:green;">What does this mean?</mark>_ \
  _<mark style="background-color:green;">To detect altitude, there will need to be a sensor on our board. A sensor that detects altitude is called an</mark> <mark style="background-color:green;"></mark><mark style="background-color:green;">**altimeter**</mark><mark style="background-color:green;">. However, we will also need a way to actually communicate with that sensor, and output its readings. To do this, we will need to use a</mark> <mark style="background-color:green;"></mark><mark style="background-color:green;">**microcontroller**</mark><mark style="background-color:green;">.</mark>_&#x20;
* The board will be mechanically secured onto the avionics sled. It will be no larger than 2 by 2 inches. \
  _<mark style="background-color:green;">What does this mean?</mark>_ \
  _<mark style="background-color:green;">Avionics members will need to work with other subteams to make sure that the boards can be integrated onto a flight vehicle. This includes staying within size constraints, and thinking about how the board will be secured in-flight. For this, we can include</mark> <mark style="background-color:green;"></mark><mark style="background-color:green;">**mounting holes**</mark> <mark style="background-color:green;"></mark><mark style="background-color:green;">on our PCB layout.</mark>_&#x20;

\*Please note that these aren't the specs for the power sources we would actually use. These have just been chosen to make the intro project simpler :)&#x20;

## Component Selection

There are some components that we commonly use on STAR for certain things. You will be expected to use these components when working on projects (unless there is a compelling reason otherwise). You can see more of such components on our [Standard Parts List](https://docs.google.com/spreadsheets/d/1Kxis2fARw56HrYMzW54rB0-L-gDaDvFu269D-AZqZrU/edit?usp=drive\_link). This PCB will be built around the following components:&#x20;

* Microcontroller: ESP32-S3-WROOM (datasheet)
* Altimeter: BMP388 (datasheet)

These components will often need additional resistors, capacitors, etc. known as **peripherals** in order to work. Datasheets often have an 'Application Example' which shows what is needed for the component. In addition to the microcontroller and altimeter, you will also need a voltage regulator for your board.&#x20;

<mark style="background-color:red;">**YOUR TASK... is to find an appropriate voltage regulator and peripherals to make this board. Fill out the BOM template with the components you've found.**</mark>&#x20;

<mark style="background-color:red;">**(To save time, you don't need to fill out all the details for the peripheral components you're using. Just make sure you list them.)**</mark> &#x20;

<mark style="background-color:red;">**To Submit: Add the link to your BOM to the 'Notes' column of the Intro Project spreadsheet.**</mark>&#x20;

\<BOM Template doc here>

{% hint style="info" %}
**On Finding the Right Component**

Let's find the perfect resistor!

* Go to www.digikey.com (where we buy most of our electronic components)
* Type in what you're searching for in the search bar ('resistor'). Then choose the most relevant category from the results that come up. (Let's choose 'Chip Resistor - Surface Mount)
* Next, we set filters to find the component we want, and click 'Apply All' (Let's select Resistance: 1k Ohms) _Always select 'In Stock' and 'Product Status: Active' when searching for components._&#x20;
* We should also make sure we select a device package we can solder. Some packages are harder to solder than others, and some are impossible for us to do by hand! (For this resistor we can select '0805' and '0603' to see results for both these sizes. You can also select '0402' if you want a challenge.)&#x20;
* Once you have applied all the filters you need you can scroll down and sort by price. Look at the available components and their datasheets, and choose the cheapest component that will work.&#x20;
{% endhint %}

## Schematic

In this part, you will learn to read datasheets for components and apply the reference schematic designs in the datasheet to complete a schematic in KiCad with a microcontroller, power module, and altimeter. Remember to refer to the KiCad tutorial page in Avionics Tutorials for more complete references for how to use KiCad. **Make sure to attend the KiCad workshop!**&#x20;

<mark style="background-color:red;">**YOUR TASK... is to make a schematic for the PCB using the components you have listed in your BOM.**</mark>&#x20;

<mark style="background-color:red;">**Create a new KiCad project titled**</mark><mark style="background-color:red;">** **</mark><mark style="background-color:red;">**`<Your Name>_IntroProject.`**</mark><mark style="background-color:red;">**Within this folder, create an additional folder titled**</mark><mark style="background-color:red;">** **</mark><mark style="background-color:red;">**`'Library'.`**</mark><mark style="background-color:red;">** **</mark><mark style="background-color:red;">**If you download additional symbols/footprints, place them in this folder.**</mark>&#x20;

<mark style="background-color:red;">**To Submit: Export your schematic in a .pdf format, and upload to google drive. Add the link to the google drive file to your Intro Project Spreadsheet.**</mark>&#x20;

While KiCad has many symbols and footprints included by default, it doesn't have all components. If you can't find a component you need on KiCad, you can look online for a symbol or footprint. Place these files in the 'Library' folder you created. You can get symbols and footprints from [SnapEDA](https://www.snapeda.com/) or [UltraLibrarian](https://www.ultralibrarian.com/) (it's free!). **Do not use EasyEDA. Always cross check a symbol/ footprint you are using with the information given on the datasheet. When in doubt, trust the datasheet!** Ask your mentors for help with this if needed.&#x20;

{% hint style="info" %}
**On Creating High-Quality Schematics**

By far the most common mistake that new members make is drawing messy schematics. Before jumping into the intro project, take a moment to read this stack exchange post with tips on creating good schematics, many of which will still be useful well into your engineering careers.

When creating schematics yourself, aim to emulate the style and clarity used in previous avionics projects such as CAS and Ground Station (pictured below). Note the use of net labels and global labels to keep wires short, as well as the organization of different sub-circuits into different areas of the page.

There are also some guidelines on this [document ](https://docs.google.com/document/d/1sA1MmZkygvkN0kvH0\_EiXm4IRMi5ilCOcb7CaAVOmxY/edit?usp=sharing)which you can (_should definitely)_ read through! (Shoutout to HOPE decal for making the guidelines document.)
{% endhint %}

### Setting up Libraries (if applicable)

Open up `intro_proj.pro`, the KiCad project. We will now make sure that the calstar schematic symbol library in `lib` is included.

Hit `Preferences > Manage Symbol Libraries` as below.

<figure><img src="../../../.gitbook/assets/Screen Shot 2023-08-25 at 3.59.02 PM.png" alt=""><figcaption></figcaption></figure>

Once the Symbol Libraries window opens, go to the `Project Libraries` tab and hit the Add existing library to table button in the bottom left row above `Path Subsitutions` .

<figure><img src="../../../.gitbook/assets/Screen Shot 2023-08-25 at 3.59.47 PM.png" alt=""><figcaption></figcaption></figure>

Now navigate to `lib/` and select `calstar.lib` . However, we want to replace the calstar library path with `${KIPRJMOD}/../calstar.lib`. Relative path is applicable on any machine, while your absolute path (i.e. `C:/Users /Cedric/......./lib/calstar.lib`) isn't. The window should end up looking like this:

<figure><img src="../../../.gitbook/assets/Screen Shot 2023-08-25 at 4.00.50 PM.png" alt=""><figcaption></figcaption></figure>

Hit `Ok` and now go back to the KiCad project window.

## Layout

In this part, you will learn to read datasheets for the reference layout designs, and then complete a two-layer board layout of the schematic from the previous step in KiCad. **Make sure to attend the KiCad workshop to learn how to use the software.**&#x20;

But first! Follow the [following instructions](https://docs.google.com/document/d/1XIp4hQyu5kEEh66-nD2Bew6qIBCuiEiuqHCNkp3XYyc/edit?usp=sharing) (shout out to the HOPE decal) to set up the design rules for your board. These will prevent you from making a design that isn't actually manufacturable.&#x20;

Also make sure to review these [design guidelines](https://docs.google.com/document/d/1sA1MmZkygvkN0kvH0\_EiXm4IRMi5ilCOcb7CaAVOmxY/edit?usp=sharing) for the layout (once again, shout out to the HOPE decal).&#x20;

As always, your mentors are always happy to help you and give you feedback!

<mark style="background-color:red;">**YOUR TASK... is to arrange the components on your schematic into a suitable layout. You must first assign each component on your schematic a corresponding footprint. Your board should be 2 by 2 inches, and have one mounting hole on each of the four corners.**</mark>&#x20;

<mark style="background-color:red;">**Much like for the schematic, you may need to download and import additional footprints for your layout.**</mark>&#x20;

<mark style="background-color:red;">**To Submit: Export your layout as a .pdf and upload to google drive. Add the link to the google drive file to the intro project spreadsheet.**</mark>&#x20;

## Export for Manufacturing

(in-progress)&#x20;
