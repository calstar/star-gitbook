---
description: Getting started with the development environment for the Avionics codebase
---

# Development Environment

Avionics distributes a container which contains all the tools for compiling our firmware. Some of the development tools we use for firmware development are a mild pain to install \(particularly for beginners\), so using the container is recommended for quick set up.

{% hint style="warning" %}
If you have tried out the container and have problems given your setup, and you reallllllly want to install yourself, go ahead. This is not recommended unless you are well acquainted with installation of compilers, etc.
{% endhint %}

## Container Environment

The avionics development environment uses Dockerfile-based platform. To use the new environment, you will need to install the [Docker](https://www.docker.com/) or [Podman](https://podman.io/) first. Podman is the fully open source alternative to Docker, and they share the same commands format. Either can be used, although most of this tutorial will use Podman because it is easier to use on Windows.

### Podman Installation Instructions

#### Linux & Mac

If on Linux, there's too much variety to put anything here. I'm sure someone in avionics will want to help! Podman is very easy to use on Fedora and works out of the box.

If on Mac, this is all currently untested.

#### Windows

On Windows, you the recommended procedure is to install Windows Subsystem for Linux \(WSL\) and run Podman within it.

Since WSL is a non-standard linux environment that lacks of some important syscalls and processes, Docker cannot be run on WSL without some hassles. Podman has been tested on WSL, and you should follows the instruction below.

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

### Container Environment Setup

The toolchains repo [here](https://github.com/calstar/star-toolchain) has a readme with additonal information about the development environment.

First download the toolchain container image. 

```text
docker/podman pull quay.io/star_admin/star-toolchain-nozephyr
```

Then, create a directory where the files in the container will be stored.

```text
docker/podman volume create star-workspace # create a persistent directory to share with the container
```

The location of this directory can be viewed with :

```text
docker/podman volume inspect star-workspace # See the mountpoint to access your workspace from the host.
```

Finally, create the container

```text
docker/podman container create -it -w=/root/star-workspace --name star-toolbox -v star-workspace:/root/star-workspace quay.io/star_admin/star-toolchain-nozephyr
```

### Running the container

Once the container is setup, it can be started with:

```text
docker/podman start star-toolbox
```

You can enter the toolbox to a `bash` prompt with the below. This is where you will be actually running commands to use the compiler, etc.

```text
docker/podman attach star-toolbox
```

Finally, once the container bash prompt is exited with `exit`, the container can be stopped with

```text
docker/podman stop star-toolbox
```

### Copying Files Out of the Container

{% hint style="warning" %}
An alternate way to transfer files is using the Visual Studio Code editor. This may be convenient if you already use VS Code, and may be a method that works if this does not. See the `VS Code & Containers` section.
{% endhint %}

To copy a file from the image to the host system \(your normal operating system\), you need to first get the mount point of your workspace by running 

```text
sudo podman volume inspect star-workspace
```

where `star-workspace` is the volume name. If you use another volume name, you need to change the command accordingly. You can save it to a environment variable to avoid copying the long path every time.

Since the path is usually only accessible with root privilege, you need to copy it to a place that you can access without `sudo`, like your home directory:

```text
sudo cp <volume-mountpoint>/<path-in-podman> ~/
```

Then, if on Windows, open Windows Explorer, type in `\\wsl$` in address bar. For every distros you install, you can see a folder with the same name as the distros in this folder. Go to the distro folder that you use to run Podman, and go to the path you copy the file to in the last step, like `home/<user-name>`. You should be able to see the file you want in that directory, and you can copy and paste it to anywhere you want in your Windows file system.

If not on Windows, simply open a terminal and go to `~`. The file will be there.

### VS Code & Containers

To setup, install the [Remote Containers](https://code.visualstudio.com/docs/remote/containers-tutorial) extension in VS Code.

Then, go to the "Remote Explorer" tab on the left bar of VS Code, right click on the container you created in the previous step and click attach to start a VS Code instance in the container. From here you should be able to open a terminal inside the container by going to `Terminal->New Terminal` and interact with the filesystem through VS Code and clone stuff, open folders, etc.

## Compiling Firmware

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

## 

