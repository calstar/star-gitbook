---
description: >-
  Description and instructions for understanding and implementing your own
  calculations for Pyro Bolts used in Stage Separation.
---

# Stage Sep - Pyro Bolts

## An Overview

![Le Pyro Bolts \(separate stages not shown\)](../../.gitbook/assets/pyro-bolts.png)

Pyro Bolts are an effective way of performing stage separation for in flight vehicles and they can be carried out in a number of ways. Our design prides itself on simplicity, cost effectiveness, and reusability \(except for the bolts themselves\).

We start with two manufactured O-rings that are each epoxied \(or fastened otherwise\) to our two airframe tubes, these rings will stay attached throughout the entire launch-recovery process. We then take screws and drill them out, fill them with black powder, insert igniters \(e-matches, insert 2 for redundancy\), then seal the fasteners. This process is detailed in separate sources and in our stage separation testing documents. The screws can be inserted through holes in the both the O-rings and will be fastened with a wing nut located on the other side of the opposite O-ring. When all screws are ignited, they ideally break and there is no longer anything keeping the two stages together. To ensure separation we opt to place springs between the O-rings, around the screws in order to add force for separation. We can then epoxy multiple standoffs between the rings, to ensure all heights and alignments are correct.

![Pyro Bolts, pictured with standoffs and separate airframe tubes](../../.gitbook/assets/pyro-bolts-edited.png)

## Calculations

It is extremely important to perform calculations before all else, both to make sure your design is feasible and so that you can select and reference what parts/materials you are planning to use. The specific calculations will vary for each design, but the quickest way to think about what calculations are needed are to think about the forces placed on each part and on all surfaces that connect parts together. We should also check the calculations for the events that take place \(black powder and spring actions\). For our design above, our main concerns are:

* Can the black powder we have break the screws?
  * This is dependent on several factors, mainly:
    * mass of BP \(depends on volume of drilled hole\)
    * shear strength of screw material \(accounting for the drilled out hole as well\)
* Will the screws be able to handle the stress of launch?
  * Dependent on:
    * stress strength of screws
      * this depends on the material and surface area of your screw so account for the fact that the screws have been drilled out a bit
    * stress strength of nuts
* Do the springs fall within the right window of strength \(given a reasonable compressed height\)?
  * Depends on
    * Spring strength
    * Height between Rings
    * Friction needed to overcome \(you can estimate this, we chose 5 lbf\)
  * Make sure you fall within the window, the spring should be strong enough to help separate, but not so strong that it causes unnecessary stress on the O-rings and screws.
* Is the epoxy strong enough to hold the O-rings and the airframe tubes together during launch?
  * It probably is but it's best to check, depends on:
    * Surface area between O-rings and Airframe tubes
    * Strength of epoxy
    * Mass in upper and lower stage
    * Acceleration of rocket during launch

These are some of the important calculations needed, however the more you can think of, the better. Make sure each calculation gives us a reasonable factor of safety \(use your good judgement\).

Our Calculations \(sources linked\): [https://docs.google.com/spreadsheets/d/1MXYF\_emElwCB7q454aGbYPLoVuzAkU27HeYaiDlL4DQ/edit\#gid=0](https://docs.google.com/spreadsheets/d/1MXYF_emElwCB7q454aGbYPLoVuzAkU27HeYaiDlL4DQ/edit#gid=0)

Our BOM: [https://docs.google.com/spreadsheets/d/1H7NPC9pytDIvBS08gRxEuIrS98b2A\_I0NQv0c\_xS4eQ/edit\#gid=0](https://docs.google.com/spreadsheets/d/1H7NPC9pytDIvBS08gRxEuIrS98b2A_I0NQv0c_xS4eQ/edit#gid=0)





