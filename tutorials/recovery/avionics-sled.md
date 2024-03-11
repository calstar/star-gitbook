---
description: Updates to the avionics sled to improve ease-of-use during launch.
---

# Avionics Sled

## Purpose

The avionics sled fits into the avionics bay tube of the rocket. The sled must hold two altimeters and two 9V batteries. On the day of launch, altimeters need to be wired twice - first for ground test and then for the main flight. In order to be time-efficient, it is important that the altimeters can be easily accessed.&#x20;

![AirBears avionics bay tube. The avionics sled is the white, H-shaped component.](https://lh6.googleusercontent.com/39SM1Qf0Lk7eZdqtdIQk431AZ9e\_dFEAGUWNDtH3XYhLhFpSlS\_azwc9huqrwZVRfqzCBTRRxxGcVOBgzGglIiuem6dKqBm1rFAvPL47qc9yLFWvf4M88AHZFXTjTS8BO8k9cAXziM0)

## AirBears

The AirBears avionics sled was the same as that used for Arktos. It fit into a 4" rocket and was used for the test launch on Nov 16, 2019. Overall, the design was effective as all components were housed and both parachutes successfully deployed. However, there was difficulty in wiring the altimeters due to their placement along the raised edges where the sled slides into the avionics bay.

![CAD of AirBears avionics bay. Batteries are pictured in the front. Altimeters were placed on the reverse side of the sled, parallel to the section where the sled slides into the bulkheads.](https://lh4.googleusercontent.com/Zgf9vMdYIC71AKCi3odUyjVHzGTkxz9Ec9UdmOcemztUX3suDsLnrRV-nX23cT3E989Mp-3K4kiVbzgTj\_8g281Pp2ZrFBmJbVcbigSZ3stZ2j7ThiPHRURTBk593epeYK2p9CFwamM)

## IREC 2020

The goals of the redesign of the avionics sled for the IREC 2020 rocket were the following:

1. Optimize the avionics bay for a 6" rocket
2. Address wiring concerns from AirBears to improve ease-of-use during launch

The new chosen design was an I-beam model, in which the batteries were placed in a center section of the sled and one altimeter was mounted to each side, as shown below. This design somewhat improved the space usage in the vertical direction, but there was significant unused horizontal space. The Recovery subteam selected this design because they felt it was more important to be able to wire the altimeters efficiently at launch than to use the least possible space.&#x20;

![Avionics Sled as viewed from back. Batteries are placed in middle centrals and the second altimeter is in the corresponding position on the other side of the sled.](<../../.gitbook/assets/image (57).png>)

![CAD demonstrating how sled slides into avionics bay](<../../.gitbook/assets/image (4) (1).png>)

## SSEP 2022

The goals for the avionics bay designs for the 2022 Stage Separation vehicle were as follows:

1. Integrate sufficient room in at least one avionics bay to accommodate the Common Avionics Stack (CAS).
2. Integrate sufficient room to accommodate off-the-shelf altimeters in addition to CAS, to allow for flights without CAS integration and also ensure failsafes for early CAS test launches.
3. Include multiple avionics bays, as the two-stage nature of the SSEP vehicle requires at least one for each stage.

In the end, the SSEP vehicle incorporated three different avionics bay designs:

* An upper stage avionics sled used to manage recovery of the upper stage. Its overall structure similar to the IREC 2020 design, but with an additional hole to accommodate CAS. This design placed CAS in its own "hole" in the bottom while the altimeters and batteries were secured to a central "wall".

![The U-shaped rings kept the sled from moving axially or radially when in the rocket, and were themselves secured by the rods pictured. Also shown in the picture is CAS, the stack of green circuit boards, and the red StratoLogger auxiliary altimeter.](<../../.gitbook/assets/SSEP\_REC\_US\_Avbay (1).png>)

* An interstage avionics bay used to ignite the upper stage motor after stage separation. Its structure is different compared to the other ones; because of the limited space available in the interstage, it is not CAS-compatible. It has similar top and bottom pieces that neatly slide into each other, and are held closed by the bulkheads and spacers.

![The lack of available space in the interstage section necessitated this avionics bay to be CAS-incompatible; it instead houses only two altimeters and two batteries.](../../.gitbook/assets/SSEP\_REC\_Smol\_Avbay.png)

* A lower stage avionics bay used to manage recovery of the lower stage. It is somewhat different from the IREC 2020 design but maintains the same basic structure, with a sled sliding out of two rings, which in this case are connected with an overall housing. Similar to the upper stage avionics bay, it places CAS in its own "level" while the other altimeters are kept on the second level.

![The outer housing kept the sled from moving axially or radially, and was itself kept from rotating by friction via spacers and the inside of the rocket's body tube. CAS is shown in the picture, the stack of blue circuit boards, but the two EasyMega altimeters are obscured from view in this angle.](../../.gitbook/assets/SSEP\_REC\_LS\_Avbay.png)
