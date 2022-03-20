---
description: The bread and butter of the propulsion system
---

# Pipes, Fittings, and Components

## Types of Threads

### NPT

NPT stands for National Pipe Thread (and sometimes National Pipe Thread Taper). It is a common type of thread used on plumbing. If you see a threaded fitting or pipe around your house, it most likely uses an NPT thread. The most significant thing to know about NPT threads is that you need to use Polytetrafluoroethylene (PTFE) tape on the threads to ensure a leak-free seal! This tape is also commonly referred to as "Teflon tape". **YOU MUST USE THIS TAPE!** Generally one or two clean wraps around the threads is enough. To be safe, take off old Teflon tape and replace it if you think it's insufficient.

{% hint style="danger" %}
You must use Teflon tape on NPT Threads!
{% endhint %}

Some other points about NPT threads:

* NPTF is a variant of NPT with a slightly different major diameter. They are cross-compatible with NPT threads, but some care has to be taken and you should **always** use teflon tape! We generally don't use them, but be aware when buying components. NPTF does **NOT** mean NPT Female. ****&#x20;
* NPT threads have a taper of 1 inch per 16 inches. Male threads are tapered in, and female threads are tapered out. This is to ensure a better seal.

Where we use NPT threads:

* Black flexible tubing to UFA (Universal Fill Adapter, see below) connection
* Most N2 (Nitrogen gas) fittings
* Non-Swagelok® 2-way ball valves
* Other large pipe threads (i.e. N2 cylinders, etc.)

Further Reading:

{% embed url="https://www.engineeringtoolbox.com/npt-national-pipe-taper-threads-d_750.html" %}

### Swagelok® Tube Fittings

Swagelok® is a company which manufactures tube fittings and various other components. Swagelok® tube fittings are proprietary and only work with other Swagelok® tube fittings. These fittings offer several benefits over NPT, including:

* They do not require PTFE (teflon) tape
* The are good for high pressure
* They are vibration resistant
* They can be assembled easily
* They're easy to use on plain tubing

The first time a Swagelok® fitting is used on a pipe end, it must be properly prepared. This preparation process ensures that the ferrule (the conical frustum-shaped metal bit) is properly seated into the tube. The video linked below provides a good explanation of how to do this.

Video demonstration: [https://www.youtube.com/watch?v=jB\_Nyje\_HNE](https://www.youtube.com/watch?v=jB\_Nyje\_HNE)

{% embed url="https://www.swagelok.com/downloads/webcatalogs/EN/MS-13-151.PDF" %}
The Swagelok® manual
{% endembed %}

### NPS

NPS stands for National Pipe Straight. It is the same as NPT but without the taper. It is **NOT** compatible with NPT. We do not use it at this time.

## Common Components

### Ball Valves (2-way and 3-way)

Ball valves control the flow of the working fluid. We currently have:

* 2-way ball valves with NPT threads
* 3-way ball valves with Swagelok® fittings
  * These valves have the inlet positioned in the middle of the T. The valve can either be closed (when the handle is upright), or opened to either side by turning the handle arrow to that side.

Ball valves are fairly straight-forward, but it is important to double check in procedures that the interior "ball" space in the valve is not pressurized after disassembly. For safety, don't put fingers around the openings when opening ball valves.

![P\&ID (Piping and Instrumentation Diagram) symbol for a 2-way ball valve](<../../.gitbook/assets/image (19).png>)

![P\&ID symbols for 3-way ball valves (the inside L or T designation is optional)](<../../.gitbook/assets/image (42).png>)

### Check Valve

A check valve is a one-way valve that lets flow in one direction but not in the other. There is typically an arrow on the component indicating the direction of flow. We use both Swagelok® and NPT check valves.

It is **critical** that check valves be inspected to ensure that they are mounted in the right direction.

![P\&ID symbol for a check valve (Flow goes from left to right in this case)](<../../.gitbook/assets/image (80).png>)

### Regulator

A pressure regulator is a device that reduces the inlet pressure down to a specified output pressure. They are used for both gases and liquids. We have several regulators in our propulsion system:

* The regulator on the big N2 cylinders
* 1800 psi regulators on the N2 Composite Overwrap Pressure Vessels (COPV's)
* Adjustable Swagelok® regulators for use with either N2 feed pressure or liquid pressure regulation
  * These regulators have a high and low pressure port marked "HP" and "LP". They must be properly aligned!
  * These regulators do **NOT** work at cryogenic temperatures
  * It is normal to hear a loud buzzing when turning these regulators from closed to open under pressure. This is due to the internal diaphragm vibrating, and is perfectly normal.

{% hint style="info" %}
Regulators have a high pressure (HP) and low pressure (LP) side. Make sure these are aligned properly.
{% endhint %}

![Generic P\&ID symbol for a regulator](<../../.gitbook/assets/image (1).png>)

### Universal Fill Adapter

A Universal Fill Adapter (UFA) is the black knob assembly connected to the end of the black, flexible tubing. It attaches to paintball COPV N2 tanks and allows us to open or close the valve on the tank. It works by using the knob screw to push down on a spring-loaded ball, which allows N2 to flow out of the tank.

Some of these have an issue where the knob is very badly fixed with illegitimate Loctite. We prefer using the set screw-type knobs, particularly those manufactured by Ninja.

![A good Ninja-brand UFA with a set screw knob](<../../.gitbook/assets/image (22).png>)

### Remote Line

The remote line is the assembly of the UFA with the black flexible tubing.

![A remote line assembly (note that the right end will look different in our case, since we just use the NPT threading)](<../../.gitbook/assets/image (39).png>)

### Pressure Gauge

Pressure gauges measure gauge pressure of the fluid ([as opposed to absolute pressure](https://www.machinedesign.com/pneumatics/what-s-difference-between-gauge-absolute-differential-and-sealed-pressure)). They are typically used with a T-joint. Our pressure gauges are (theoretically) not cryo-rated.

### Quick Disconnect

A quick disconnect is a type of fitting which allows a quick connection/disconnection (hence the name), without any threading. We use these on our mobile filler. They are less secure than other connections, so they should only be used where necessary.

To connect a quick disconnect:

1. Pull back on the outer ring on the female end
2. Insert the male end (AKA nipple) into the female end
3. Release the outer ring until it snaps back and you hear an audible click
4. The two halves should now be connected and you should not be able to pull them apart without pulling back the ring
5. If you can pull them apart, simply try again. You may have to wiggle the quick disconnect a little to get the outer ring to snap into place properly.

To disconnect a quick disconnect

1. Pull back on the outer ring on the female end
2. Separate the two halves
3. Release the outer ring

{% hint style="warning" %}
Always make sure Quick Disconnects are are properly connected! They are tricky and can lead to serious safety issues if they're not properly connected.
{% endhint %}

![A quick disconnect (female in upper left, male in lower right)](<../../.gitbook/assets/image (28).png>)

### Relief Valve

We buy relief valves from Swagelok®. These valves work using a calibrated spring, which under a certain pressure, will allow fluid to flow through the valve. We use these as safety devices, to ensure a safe depressurization in the case of over-pressurization. It is important that the these vents be kept clear of personnel and high-pressure tanks at all times when the system is pressurized.

![This symbol is sometimes used for a relief valve](<../../.gitbook/assets/image (58).png>)

![A Swagelok® relief valve](<../../.gitbook/assets/image (24).png>)

## Safety Notes

* Never adjust a fitting on a high-pressure system. If you don't know whether a section of tubing or tank is pressurized, depressurize it first.
* Always check **all** fittings for tightness before pressurizing any system.
