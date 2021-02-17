---
description: Getting started with the development environment for the Avionics codebase
---

# Development Environment

Avionics distributes a VM which contains all the tools for compiling our firmware. While distributing a VM may seem intensive, there are many tools we use for firmware development which are not easy to set up. We have found that using a VM overall lowers the barrier to entry.

{% hint style="warning" %}
If you have tried out the VM and have problems given your setup, and you reallllllly want to install yourself, go ahead. This is not recommended unless you are well acquainted with installation of compilers, etc.
{% endhint %}

## Vagrant

We will be using [Vagrant ](https://www.vagrantup.com/)to standardize our development environment and make setup quicker. This section will show how to install Vagrant and basic usage.

{% hint style="info" %}
Vagrant has its own general startup guide [here](https://www.vagrantup.com/intro/getting-started/index.html). Reference it for more detail on using Vagrant.
{% endhint %}

### Steps to setup the development environment

First, download and install Vagrant and and Virtual Box:

{% embed url="https://www.vagrantup.com/downloads.html" %}

{% embed url="https://www.virtualbox.org/" %}

{% hint style="warning" %}
Vagrant warns against using your system package manager to install Vagrant. Install from Vagrant's official downloads instead.
{% endhint %}

Run: 

```bash
vagrant box add mtn_narwhal/mbed_cli_tools
```

A 'box' is the package format Vagrant uses. This command downloads the `mbed_cli_tools` box, which contains tools such as GCC ARM, git, and Mbed CLI.

Then, go to the STAR directory on your file system, and run:

```text
vagrant init mtn_narwhal/mbed_cli_tools
```

 This sets up the box in that directory. Vagrant will automatically sync files in the folder you `init` the box in \(the folder which has the `Vagrantfile`\) on your host system with the folder `/vagrant` in the VM. 

To start the VM, run `$ vagrant up`.

You may see the error regarding SSH: `Warning: Authentication failed. Retrying...`. If this happens, hit `Ctrl-C` and then run `$ vagrant ssh`. You should be requested for a password for the user `vagrant`. The password is `vagrant`. Once ssh'd into the VM, run the following command.

```text
echo "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key" > .ssh/authorized_keys
```

Now, run `$ exit` to logout of the VM, followed by `$ vagrant reload` to restart. After this, ssh should succeed.

If you see an error regarding NFS, you will want to change your filesharing method to RSync. In the `Vagrantfile` change the `type` of the `config.vm.synced_folder` from `"nfs"` to `"rsync"`. Now run `vagrant reload` again and you shouldn't see the error. You may run `vagrant rsync-auto` in a terminal to have vagrant automatically sync the changes you make on your local machine to the virtual one. If you are using `nfs` and are noticing that your file syncing isn't working, try adding`config.vm.network "private_network", type: "dhcp"` to your vagrant file

{% hint style="warning" %}
Getting SSH to succeed is crucial as it must work before vagrant will move on to the step where it syncs files in the directory with the `Vagrantfile` in the host system to the `/vagrant` directory in the guest system.
{% endhint %}

Linux: if after ssh-ing in, you see your `/vagrant` directory is empty, try deleting your Vagrantfile and re-running all the above commands to init, up, and ssh with `sudo` pre-pended. If you get an error saying "The VirtualBox VM was created with a user that doesn't match the current user running the VM, edit  `.vagrant/machines/default/virtualbox/creator_uid` to say 0.

Once this is complete, you can run `$ vagrant up` to start the VM,`$ vagrant ssh` to enter the VM, `$ exit` to logout of the VM, and `$ vagrant halt` to stop the VM. When in the VM, you can `cd` to `/vagrant` and access all your CalSTAR files.

To test the VM environment, `cd` to `~/examples` where there are two folders: `mbed-os-example-blinky` and `test_prg`. Go into either and test if they compile by following the instructions in Mbed CLI &gt; Compiling.

### Improving file sync times

By default, Vagrant uses a rather slow method to sync files between the host file system and the vm file system. This results in very slow \(about 1.5 hour\) compile times of mbed-os when the os is on the host file system. The following shows how to improve this to about 5 minutes by switching the file system to Network File System \(NFS\) instead of what Virtual Box uses.

If on windows, first run `$ vagrant plugin install vagrant-winnfsd` since Windows does not have NFS support in-built.

Linux: if you get an error saying your machine doesn't support NFS try running `sudo apt install nfs-kernel-server` and `sudo apt install nfs-common`

Now, on all systems, add the following to the Vagrant file inside the `Vagrant.configure("2") do |config|` block:

```text
config.vm.synced_folder "./", "/vagrant", type: "nfs"
```

On Windows, additionally add the following line:

```text
config.vm.network "private_network", type: "dhcp"
```

Once this is complete, run `$ vagrant reload`. At least on Windows, you may be asked to allow a program through the firewall. Whether you need to may depend on your system. To check, first disconnect from the internet \(turn off wifi and unplug ethernet\), turn off the firewall, and then try running `$ vagrant up` and `$ vagrant ssh`.This should work. Then turn back on the firewall and try again. If this does not work you will have to find which program is trying to get through the firewall and allow it through at least for private networks.

Once all this is done, run `vagrant reload` and continue. This should dramatically improve compile times.

![An example Vagrantfile on Windows](../../.gitbook/assets/image%20%2861%29.png)

Linux: if you get an error saying "A host only network interface you're attempting to configure via DHCP already has a conflicting host only adapter with DHCP enabled." Run `VBoxManage dhcpserver remove --netname HostInterfaceNetworking-vboxnet0` and then `vagrant reload`

### Avoiding file sync

If running `mbed deploy` takes too long \(over 20 minutes\) then you might want to consider a workflow that does not sync the files in the VM with the those of the host machine. To do this, have all the firmware in the VM itself. This means you will have to edit inside the VM instead of using editors such as VS Code on your desktop. To do this, `cd ~` while in the VM and run 

```text
git clone https://github.com/calstar/firmware-launch.git
```

Enter the `firmware-launch` directory and run `mbed deploy` as before. It should still take a bit to get started but should be much faster because Vagrant is no longer trying to sync the files it's downloading  to your host machine. Next, edit your Makefile to `outdir` to `/vagrant/out/`Now you should be able to compile by running `make build board=[tpc|fc|gs|bb]` \(see compiling-and-flashing-launch-firmware for more details\). The binary will appear in the `out` folder of the directory on  your host machine where your Vagrantfile is located.

Using this workflow, you should have a local repository on your host machine from which you edit and push code. Then when you want to compile, enter your firmware-launch directory in Vagrant, pull your changes and then run the compilation command from there.

## Mbed CLI

{% hint style="info" %}
For more detailed documentation on Mbed CLI, look at the official docs [here](https://os.mbed.com/docs/v5.10/tools/working-with-mbed-cli.html).
{% endhint %}

{% hint style="info" %}
For documentation on the Mbed API, look at the official docs [here](https://os.mbed.com/docs/v5.10/apis/index.html). If you don't find a library for what you want there, look at community built libraries by searching using the search box in the upper right corner.
{% endhint %}

### Creating a new project

To create a new project called `mbed_project`, run the following:

```text
mbed new mbed_project
```

### Compiling

To compile a project, run the following from within the project folder

```text
mbed compile --target NUCLEO_F401RE --toolchain GCC_ARM
```

The target, `NUCLEO_F401RE` is a development board that has the `STM32F401RET6` microcontroller on board, the same MCU we use. The toolchain selects which compiler we are using.

This should give you something like the following if it compiled successfully. 

![Image of successful compilation output](../../.gitbook/assets/image%20%2814%29.png)

### Importing libraries

Find libraries by searching in the search bar on mbed's website. Then, once on a library's page, look at the box titled "Repository toolbox" and select the down arrow on the yellow "Import into Compiler" button.

![Click the down arrow for more options](../../.gitbook/assets/image%20%2843%29.png)

Then select "Import with mbed CLI" and copy the command listed.

![Select &quot;Import with mbed CLI&quot;](../../.gitbook/assets/image%20%2833%29.png)

![Copy the command in the box](../../.gitbook/assets/image%20%2811%29.png)

The command should be of the form `mbed add <project link>`. Run this command from command line inside your mbed project.

## Flashing Programs to the Microcontroller

As of right now, usb-detection and programming through vagrant is not working. Instead install and use a utility on the host system. 

* Windows: Download and install the St-Link Utility from the file below. To use, first `File > Open file` the binary of the program output by `mbed compile`. Then  `Target > Connect` to the board, and `Target > Program & Verify`
* Linux: Install the stlink package from the repositories if it's available, or compile from source [here](https://github.com/texane/stlink).
  * To use, open stlink-gui and perform similar steps to the windows version to flash
  * Alternatively, use `st-info --probe` to search for programmers and `st-flash write $binary_output_file 0x8000000` to flash

{% file src="../../.gitbook/assets/en.stsw-link004.zip" caption="Windows St-Link Utility" %}

## Docker Environment \(Under construction\)

The next generation of development environment is being moved onto Dockerfile-based platform. To use the new environment, you will need to install the Docker or Podman first. 

### Podman Instructions for Windows Subsystem of Linux \(WSL\)

Podman is the fully open source alternative to Docker, and they share the same commands format. Since WSL is a non-standard linux environment that lacks of some important syscalls and processes, Docker cannot be run on WSL without some hassles. Podman has been tested on WSL, and you should follows the instruction below.

If your Windows 10 is Home version, you might not be able to enable Hyper-V. You should upgrade to Windows 10 Pro, or just use the free educational version from the school: [https://software.berkeley.edu/microsoft-operating-system](https://software.berkeley.edu/microsoft-operating-system)

Follow the instruction on [https://docs.microsoft.com/en-us/windows/wsl/install-win10](https://docs.microsoft.com/en-us/windows/wsl/install-win10). You should install WSL 2. This tutorial is based on OpenSUSE, but it is possible to use other distros.

Once you finish, install Podman by running

```text
sudo zypper install podman
```

Then, run the following instruction to create and modify the config file to make it run on WSL:

```text
sudo cp /usr/share/containers/containers.conf /etc/containers
```

Then, use an editor of your choice, open `/etc/containers/containers.conf` with `sudo` :

1. Uncomment the line with `events_logger`, then change the value to `file`.
2. Uncomment the line with `cgroup-manager`, then change the value to `cgroupfs`.

You should be able to run the docker file right now. **Note that you must run Podman with `sudo`, or you won't be able to do anything.** If you are getting `No CNI Configuration file` error, do the following steps:

1. Run `sudo podman network create`. It should give you a filename.
2. In the command you used to run docker, add `--net <config-name>` after `podman run`. `<config-name>` is the filename you got from the first step.

### Copying File To Windows File System

To copy a file from the image to Windows, you need to first get the mount point of your workspace by running 

```text
sudo podman volume inspect star-workspace
```

where `star-workspace` is the volume name. If you use another volume name, you need to change the command accordingly. You can save it to a environment variable to avoid copying the long path every time.

Since the path is usually only accessible with root privilege, you need to copy it to a place that you can access without `sudo`, like your home directory:

```text
sudo cp <volume-mountpoint>/<path-in-podman> ~/
```

Then, open Windows Explorer, type in `\\wsl$` in address bar. For every distros you install, you can see a folder with the same name as the distros in this folder. Go to the distro folder that you use to run Podman, and go to the path you copy the file to in the last step, like `home/<user-name>`. You should be able to see the file you want in that directory, and you can copy and paste it to anywhere you want in your Windows file system.

