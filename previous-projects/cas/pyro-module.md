---
description: Eight fuses that can light blackpowder charges
---

# Pyro Module

### Overview

The pyro module consists of eight connectors which can each light a blackpowder charge. Each connector is controlled by a mosfet, and if the mosfet allows current to flow through the connector, then the blackpowder charge is ignited.&#x20;

The core module controls this by sending I2C messages over the I2C0 bus to the I/O expander module. The I/O expander module connects to eight mosfet drivers which drive the mosfets. The I2C messages that come to the I/O expander can tell it to set off certain blackpowder fuses.&#x20;

The I/O expander also features three address bit jumpers, which can be manually connected or disconnected to change the I2C address of the I/O expander, to avoid I2C address conflicts.
