# 8020 Extrusions

![An 8020 1010 series extrusion](<../../.gitbook/assets/image (83).png>)

## First things first

80/20 Inc. has a fantastic website detailing a lot of information about their extrusions.

{% embed url="https://8020.net/product-basics" %}

This page is intended to serve as a summary and introduction to these extrusions.

{% hint style="info" %}
The most useful part of this page is probably the Tips and Tricks section at the bottom.
{% endhint %}

## What are 8020 extrusions?

8020 is a brand of Aluminum extrusions. "Extrusions" just means that they are parts with a constant cross section that are extruded through a dye in their manufacturing process. 8020 sells an entire product ecosystem that revolves around their "T-slot" extrusions. Their cross section looks like this:

![Cross sections of the 1010 series and 1515 series extrusions](<../../.gitbook/assets/image (81).png>)

8020 parts are often used to build frames and other equipment quickly and more conveniently than alternatives (such as welding, manufacturing custom parts, etc.). They are widely used in industry for several reasons:

* They are easy and convenient to use
* While they can be pricey, they are high quality and are usually cheaper than a custom solution
* They are very versatile and can be used for many types of applications
* They can be expanded to include **linear motion bearings**, stanchions, guard railings, fences, etc.

## How do 8020 extrusions work?

The basic principle behind fastening 8020 extrusions is called the "2 degree drop lock"

![The 2 degree drop lock demonstrated](<../../.gitbook/assets/image (44).png>)

The main idea here is that the edges of the extrusions are not perfectly parallel to each other, but rather offset by 2 degrees (this can be a pain in SW sometimes, be aware). When a fastener is tightened, it elastically deforms the extrusion, creating a strong normal force on the nut and fastener head. This normal force allows for a large static friction force to be applied, securing the nut in place.

For reference, on of these fasteners can usually hold up to several hundred pounds when installed properly.

## Product Selection

8020 has a lot of options, which is fantastic. However, this can be intimidating for first-time users. This guide is intended to help you through selecting 8020 components for your assembly

### Extrusion series

For most applications at STAR, we do not use metric extrusions or fasteners. This leaves you with two choices for the extrusion series:

* 1010 - This is a 1" x 1" extrusion. This will usually be enough for most applications where the structure is not under significant or mission critical load.
* 1515 - This is a 1.5" x 1.5" extrusion. This is the maximum imperial sized extrusion, and is used for more "beefy" structures.

{% hint style="info" %}
Extrusions are also available in non-square shapes. For example, a 1530 extrusion will measure 1.5" by 3", indicating that it is essentially two 1515 extrusions connected side by side. These are still compatible with other extrusions in their series
{% endhint %}

Note that for each of these extrusions, there are submodels such as "1515-S-Black-FB". These indicate unique features of the extrusion. Be mindful of these, since they can at times compromise strength or offer options for weight reduction. There are countless options, but these are a few to be aware of:

* S indicates a smooth finish
* Lite indicates a lighter but weaker profile. Lite gets abbreviated to L if there are other modifiers (about 22% lighter than regular
* UL stands for ultra light (about 12% lighter than L, 32% lighter than regular)
* Black indicates a black anodized finish. More expensive, questionably more corrosion resistant.

### Fasteners

Fasteners are an integral part of 8020 product selection. The 8020 catalog provides a good amount of detail on the differences between fasteners, and their youtube channel is also recommended for seeing how these work in action.

{% embed url="http://catalogs.8020.net/80-20-Inc-University-Booklet//18/" %}

{% embed url="https://www.youtube.com/channel/UCFklmAMLd1yIQDdzMckPU6A" %}

There are several questions to keep in mind when selecting a fastener:

* How strong will the fasteners be?
  * [http://catalogs.8020.net/80-20-Inc-Catalog-22/60/](http://catalogs.8020.net/80-20-Inc-Catalog-22/60/)
* How much machining will be necessary on the profiles?
  * We can order parts pre-machined, but it does cost more money. Machining parts ourselves is also possible, but is very time-intensive.
* How often will this fastener need to be removed? Will it need to be removed after the assembly is assembled?
* What are the loads going to be on the fasteners?
  * A force applied perpendicular to the T-slot and the axis of the screw will differ greatly from a force applied along the T-slot, which will both be very different from a torque in the axis of the screw.

## Suppliers

For small orders, 8020.net is fine. For larger orders, please email David at TECO technologies.

{% content-ref url="suppliers.md" %}
[suppliers.md](suppliers.md)
{% endcontent-ref %}

## Tips and Tricks

Don't make the same mistakes we did.

* _**PLEASE PLEASE PLEASE**_** ** if your budget permits order parts pre-cut and pre-machined. It saves a lot of headache on our side, and the whole point of 8020 is that it's **easy**.
  * If your budget does not permit, reconsider your budget. Machining and cutting 8020 for an average-sized project will take well over 10 hours in the machine shop for the average student.
    * If you've reconsidered your budget and still can't afford, buy extra length of 8020, since cutting and mistakes will eat up your length. Also order extra fasteners
* Try to stick with flat plates and gussets. Anchor fasteners are difficult to access and expensive, and end fasteners require tapping into the aluminum, which isn't ideal for things that need to be disassembled frequently. 45 degree supports are also very nice for high-strength applications.
* When tightening fasteners, you almost can't go too tight. Most people will not tighten the fasteners enough to engage the 2-degree drop lock on the first try.
* Think about accessing fasteners when you create your assembly. A fastener is no good if you can't get in with a hex wrench to tighten it.
* When creating 8020 assemblies in SolidWorks, use the models provided on 3D Content Central ([https://www.3dcontentcentral.com/](https://www.3dcontentcentral.com/))
  * Be mindful about constraining these, since the 2-degree drop lock means that seemingly parallel planes are not actually parallel
* 8020 becomes very useful when you interface it with your custom parts. This is not very difficult to do, and essentially just involves including an equivalent flat plate fastener in your part.
