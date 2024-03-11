---
description: >-
  Deciding which parachutes to use: where to buy them from, how big, and other
  things to consider
---

# Parachute Sizing

### Parachute Purchasing

For parachute purchasing, Recovery typically sources from FruityChutes. They also provide us with a 10% discount if you mention that you are with STAR. Their chutes have a coefficient of drag (CD) of 2.2 for large iris or 1.9 for smaller iris parachutes used for drogues which is ideal, we would not want that to significantly decrease.

{% embed url="https://fruitychutes.com/" %}

### Parachute Deployment Scheme

![](<../../.gitbook/assets/image (75).png>)

This is the order of recovery. Note the order of deployment and location.&#x20;

### Drogue

The purpose of the drogue parachute is to slow down the rocket such that once at terminal velocity we can safely deploy the main parachute. It is deployed at apogee. The drogue parachute should be significantly smaller than the main parachute so as not to exacerbate wind drift. With respect to mounting in the rocket, the drogue is typically attached the the lower portion of the rocket (nose cone side).

### Main

The purpose of the main parachute is to significantly slow down the rocket to allow it to land safely and softly. This is to preserve the rocket and materials within it. The main parachute is deployed _after_ the rocket with the drogue parachute has reached terminal velocity. Recently, deployment has been within a range of 700-800 feet of elevation. It should be significantly larger than the drogue parachute. With respect to mounting in the rocket, the main parachute is typically attached to the upper portion of the rocket (booster side).&#x20;

## Objectives

Our goal in parachute sizing is to reasonably minimize ground hit velocity, the kinetic energy at landing, and drift of the rocket.

We use Open Rocket as our main calculator for kinetic energy, drift, and ground hit velocity. You should also be sure that there is not an issue with the jerk moment, which would occur if there is too much of a difference in size between the drogue and main chutes. If there is an issue, it will be easily identified in Open Rocket.&#x20;

![Open Rocket Simulation Data](<../../.gitbook/assets/image (26).png>)

![Drogue parachute too small](<../../.gitbook/assets/image (3) (1).png>)

### Ground Hit Velocity

We typically try to minimize the ground hit velocity. According to IREC regulations: **ground impact speed should be no more than 30 ft/s or 9 m/s.**&#x20;

### Kinetic Energy&#x20;

We typically try to minimize the kinetic energy of sections. According to our STAR regulations: **maximum section Kinetic Energy should be no more than 100 Joules**. This is for the purpose of safety and to ensure delicate components are not broken upon landing.&#x20;

The upper section, avionics bay, and lower section should all meet this requirement.&#x20;

#### Equations

$$
KE = \frac{mv^2}{2}
$$

where _m_ is the mass per section, _v_ is the terminal velocity post main chute deployment.&#x20;

### Drift

We typically try to minimize the wind drift. According to IREC regulations: **main deployment should not exacerbate wind drift (eg 75 - 150 ft/s or 23-46 m/s).** Furthermore, we have additional STAR specific regulations: **drift should be within the confines of launch site, drift should be less than ⅖ of apogee.**

**Wind drift should be calculated for 10 mph wind = 4.47 m/s**

Open Rocket will give results of expected drift based on inputs of weight of the rocket, apogee height, parachute sizes, and wind conditions. Or calculations can be made from the expected flight time.

$$
\text{Drift} = v*t
$$

Where v is wind speed (4.47 m/s) and t is expected flight time.
