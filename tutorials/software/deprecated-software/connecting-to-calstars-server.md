---
description: >-
  How to Connect to CalSTAR's Server for Maintenance, Solidworks Workgroup PDM
  or Converge CFD Licensing
---

# \[deprecated\] Connecting to CalSTAR's Server

## Deprecation Notes

As of August 14, 2018, CalSTAR's Microsoft Azure Server has been taken offline indefinitely. The server's primary role was to serve as a PDM host, a task taken over by GrabCAD. Its secondary task of hosting Converge CFD license validation was deemed to not be valuable enough to justify continued payment for the server. 

## About

In order to use Solidworks Workgroup PDM or Converge CFD, you must be on the same network as our server. Since we cannot physically connect to the same wifi or ethernet connection, we will be setting up a Virtual Private Network \(VPN\) to link your computer and the server.

#### \(Optional shitty example\) Why do I need to be on the same network as the server? How does a VPN help? 

As a very generalized example, you can think of a network as a small town, with roads connecting houses and stores. Being in the same town \(network\) allows you to use the roads to go from your house to the store and back \(exchanging files and information with the server\). 

Staying with this example, a separate network would be the equivalent of a town on the other side of a river. The two towns can not interact with each other. You cannot drive from one town to the other, a home in one town cannot visit a store in the other. 

This is representative of your computer and the server right now. The server cannot interact with your computer, and your computer cannot interact with the server. To have any interaction between the two towns \(your computer and the server\), a physical connection must be made. In our example, this would be the equivalent of building a bridge across the river. You must plug your computer into the same internet \(ethernet/wifi\) as the server. This is not possible since Microsoft owns the server and it is probably miles away from you. 

What we will be doing in this guide is setting up a Virtual Private Network \(VPN\). In our two-town example, the VPN is basically a quick and temporary bridge connecting the two towns. The VPN will make it seem as if the two towns are one, connected with the same roads. This lets the server communicate with your computer and vice versa. This is necessary in order to share files between the computers \(essentially what the PDM and license check does\).

## Installing, Configuring, and Running a VPN Client

In order to set up the VPN with our server, you must install a VPN Client. The following two programs have been known to work well:

* SoftEther VPN Client \[[info](https://www.softether.org/)\] \[[download](http://www.softether-download.com/en.aspx?product=softether)\]
* OpenVPN \[[info](https://openvpn.net/)\] \[[download](https://openvpn.net/index.php/download/community-downloads.html)\]

Choose one and download the version for your operating system. Read the notes below for your chosen program.

{% hint style="info" %}
Configuration files for both programs can only be downloaded when signed into Google Drive with a berkeley.edu account.
{% endhint %}

### SoftEther VPN Client

* Make sure you are downloading the SoftEther VPN Client under Select Component
* When installing, make sure you are installing SoftEther VPN Client and NOT the Manager \(Admin Tools Only\)
* Proceed with the rest of the installation.

#### Configuring After Installation

* [Download the configuration file 'pdm2.vpn' here.](https://drive.google.com/file/d/1_epA1HgLEK3k2Tz1DDZeFE2XkwFvDq-U/view?usp=sharing)
* Launch SoftEther VPN Client Manager
* Select **Virtual Adapter** at the top of the window, then **New Network Adapter**
* Click OK \(Name should be prefilled as _VPN_\)
* Once finished, click **Connect** at the top of the window, then **Import VPN Connection Setting...** 
* Locate and import the 'pdm2.vpn' file you downloaded earlier \(probably in your downloads folder\).

#### Connecting

* Select the new connection PDM2 and login with the provided credentials.

### OpenVPN

* When installing, leave the default options checked \(select them if unchecked\):
  * OpenVPN User-Space Components \(grayed out\)
  * OpenVPN Service
  * TAP Virtual Ethernet Adapter
  * OpenVPN GUI
* Options in Advanced can be modified as you wish

**Configuring After Installation**

* [Download the configuration file 'pdm2.ovpn' here.](https://drive.google.com/file/d/0B0tb_OL5NTEORV9VXzN6aHVRbUE/view?usp=sharing)
* Launch OpenVPN GUI

{% hint style="info" %}
For Windows, after starting OpenVPN, the OpenVPN GUI shows up as a computer-with-lock icon in the system tray \(icons near the clock and date\)
{% endhint %}

* Locate the OpenVPN GUI icon in your system tray, and right click it.
* Select **Import File...** 
* Locate and import the 'pdm2.ovpn' file you downloaded earlier \(probably in your downloads folder\).
* Click OK

#### Connecting

* Right click the OpenVPN GUI icon.
* Select **Connect** and login with the provided credentials.

