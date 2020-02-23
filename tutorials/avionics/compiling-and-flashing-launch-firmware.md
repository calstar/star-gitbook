---
description: 'This page will show you how to download, compile, and flash launch firmware.'
---

# Compiling and Flashing Launch Firmware

This page assumes you have installed VirtualBox and Vagrant, as these are the standard virtual environments we use to compile STAR code. If you have not done so yet, please refer to the [Mbed Command-Line Interface \(CLI\) Tools](mbed-command-line-interface-cli-tools.md#vagrant) tutorial.

Choose a desired directory and 

```text
$ git clone https://github.com/calstar/firmware-launch.git
```

Or, if you have your ssh keys set up on your laptop and shared to Github, run

```text
$ git clone git@github.com:/calstar/firmware-launch.git
```

### C++ Settings

Our launch firmware uses flatbuffers, which requires the c++14 compile standard. To change these settings, ensure you are in your VM then enter the `/firmware-launch/mbed-os/tools/profiles` directory. Edit the three json files. Under `GCC_ARM` and `cxx,`change the `-std`flag to be `c++14`. When you are done, the three json files should look something like this at the top:

![](../../.gitbook/assets/c++.JPG)

### Git Submodules

All libraries are stored in a separate repository for ease of updating libraries across different repos. After you clone a repo, you will have to run the following to download the tools. Run these commands from the working directory of the repo \(eg for the repo `firmware-launch`, run from `/vagrant/firmware-launch`\).

```text
$ git submodule update --init --recursive
```

{% hint style="warning" %}
If there are issues with the above commands regarding permissions, you may have to follow the Github guide [here](https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) to create an SSH-key and then put it on your Github.
{% endhint %}

 and navigate to this launch-firmware directory. 

### Installing mbed-os

If you are compiling for the first time, you will need to first install mbed-os. `vagrant ssh` to connect to Vagrant and then run:

`cd ~ && mkdir mbed && cd mbed && git clone git@github.com:ARMmbed/mbed-os.git`

`git checkout mbed-os-5.15 && cd /vagrant && mbed config -G MBED_OS_DIR /home/vagrant/mbed/mbed-os`

Make sure ~/mbed/mbed-os is the only mbed-os folder you have in your projects otherwise you will get this: `[ERROR] Library name 'device_key' is not unique` when trying to compile

{% hint style="warning" %}
If `mbed deploy` fails with a message like `could not resolve host: github.com`, try following answers on this stackoverflow post: [https://serverfault.com/questions/453185/vagrant-virtualbox-dns-10-0-2-3-not-working](https://serverfault.com/questions/453185/vagrant-virtualbox-dns-10-0-2-3-not-working). In particular the answers on this post wil resolve DNS issues. If, within the VM, `ping 1.1.1.1` works but not `ping google.com` this may indicate a DNS issue.
{% endhint %}

### Compiling

```text
$ make build board=[tpc|fc|gs|bb]
```

For example, if you want to compile TPC firmware, run

```text
$ make build board=tpc
```



