---
description: >-
  Providing 3-axis rotational stabilization for a (hypothetical) component
  during ascent!
---

# Stabilization

{% embed url="https://github.com/calstar/payload-stabilization" %}

### Some info:

We have a base containing large electronics supporting our servos and arms. Each servo provides rotational motion to one axis with range of +-90 degrees (180 total), with an initial configuration of all axes being orthonormal to each other. The first servo is attached to our base, which controls an arm that our next servo is mounted to. This second servo controls the next arm that our third servo is mounted to. Our last servo, however, does not control an arm, instead it controls a platform, the platform which we would like to stabilize.

<figure><img src="../../../../.gitbook/assets/Full Stabilization Assembly.png" alt=""><figcaption><p>Stabilization CAD</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/Wiring Diagram.png" alt=""><figcaption><p>Stabilization Wiring</p></figcaption></figure>

### Inventory:

#### Electrical Components

All electrical components below, unless otherwise specified, we have in inventory. For everything without a number or description, assume we have one part in inventory.

* Arduino Nano
  * Connects all components together and provides communications/calculations between components.
* 1S 3.7V Lipo Battery
  * Power source for stabilization.
* Booster Converter (many extra)
  * Need 5V for most (all?) components, and the lipo only provides 3.7V, so we use this to step it up.
* Photo-relay (still needs to be ordered)
  * We don't want to waste any power before launch, so we can use a photo-relay to only allow current to the servos once the MPU's detect launch.
* Resistor (330 Ohms, have extras)
  * We need one resistor to connect to the photo-relay to have it perform to expectations (ideally it would be 336 Ohms).
* MPU's (x2)
  * One MPU is attached to the base of our stabilization unit, this gives us gyroscopic and acceleration data of how the rocket moves through time. This MPU also provides data so that we can provide the adequate torque to our servos to stabilize the platform. Our second MPU is mounted on our platform, this will provide data for how well our platform is being stabilized. We can take both our MPU's data and record it to the SD Card.
* Servos (x3)
  * Provides mechanical control of the three arms (be wary of Gimbal Lock problem).
* MicroSD Card
  * Provides storage for sensor data, which we can analyze after launch.
* MicroSD Card Breakout Board
  * A board which provides us the ability to write to the MicroSD card using the arduino.
* Protoboards (many extra)
  * A board so we can solder some of our components (like the Arduino Nano and Photo-relay) and keep them reasonably secure during launch.
* Wires (stranded, 26 gauge, 50 feet)
  * Electrons
* Servo Extensions (many)
  * The most convenient way to connect our servos to the power and arduino.
* Lipo Connectors (many)
  * The most convenient way to connect our lipo to the converter.
* 1S Lipo USB Charger
  * A convenient way to charge our lipo (before testing and launch, not during).

#### Mechanical Components

* Servo Bolts
* Servo Nuts
* Sensor Bolts
* Sensor Nuts
* Arduino Bolts
* Arduino Nuts
* Arduino Spacers
* MicroSD Card Breakout Board Bolts
* MicroSD Card Breakout Board Nuts
* Booster Converter Fasteners
