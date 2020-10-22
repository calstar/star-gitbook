---
description: Guidelines for how to keep CAD documentation consistent within STAR
---

# SolidWorks file conventions

Conventions for CAD documentation of parts designed for use by STAR can be grouped into 2 categories: drawing setup and filename conventions.

## Drawings

Regarding drawing setup, CADs for the purpose of documentation should use the drawing template and use Imperial \(also known as IPS\) units. Furthermore sub-assemblies should be placed in external files \(a tutorial of how to do this is soon to come\).

## File Naming and Organization

Regarding filename conventions, file names of CADs should adhere to the following guidelines:

1. File names shall follow the general convention of: Project\_Subteam\_DescriptiveName\[\_McMaster part \#\]. See below for project and subteam codes.
   1. An example of this might be IREC20\_PAY\_Payload\_Centering\_Ring.SLDPRT for an in-house part or IREC20\_AIR\_Weld\_Nut\_90611A320.SLDPRT for a McMaster part.
   2. Similarly an example for an assembly might be IREC20\_AIR\_Nosecone\_Assembly.SLDASM
2. File names shall not contain special characters \(e.g. "!@\#$%^&\*\(\)?/\|\" \) aside from "\_". Hyphens shall be allowed only if part of an external part number. Spaces and periods \(outside of ".SLD\*\*\*"\) are not permitted, as they can cause filepath issues.
3. Subteam shall be denoted by its appropriate 3-letter abbreviation:
   * **AIR** : Airframe
   * **AVI** : Avionics
   * **PAY** : Payload
   * **REC** : Recovery
   * **PRO** : Propulsion
   * **SIM** : Simulations
   * **OUT** : Outreach
4. Project shall be denoted by the selected abbreviation for the project:
   * **IREC20** : 6” diameter rocket design for IREC 2020 \(this is Bear Force One, the project started before it was named and before IREC 2020 was moved to 2021\)
   * **LE165** : “Hot Take”, Propulsion’s first-iteration of a liquid engine
   * **LE1**: Liquid Engine 1, Propulsion's 2020-2021 "simple" engine
   * **LE2**: Liquid Engine 2, a multi-year project to design and build a higher-performance engine. Custom tank CAD can also use LE2.
   * **SSEP**: Stage separation demonstrator
   * **DAVE**: Deployable aerial vehicle experiment, a payload launching on Bear Force One.
   * **CAS**: Common Avionics System mission\(s\), flown on AirBears. AirBears \(the vehicle\) was developed before the naming convention became mandatory, but all CAS-related CAD should follow the convention.

