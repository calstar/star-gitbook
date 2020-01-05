---
description: Learn git and avionics' git workflow
---

# Git and Workflow

## About the Repository

The avionics team's repository documents all the code, schematics, and layouts that team members create throughout the year. It is important to pull \(you'll see what this means soon\) often to keep up to date with the most recent changes. Because of the file format of our PCB design documents, it is recommended that you use Windows \(either on a PC or on a virtual machine on Mac\) to open and edit files. Software, however, can be easily edited using Vim, Sublime, Atom, VS Code, or similar text editors on either OS. 

## Setting Up

{% hint style="info" %}
Windows 10 supports running a proper Linux development environment using [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about). Installing and using this is highly recommended. 
{% endhint %}

Make sure you have a Github and you have requested access to our repository \(aka: repo\) by messaging the avionics lead \(currently Neelay Junnarkar @neelay.junnarkar\). Git should already be installed on Macs, but if you are using Windows, click [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for directions to install. Clone the repo onto your local computer in a directory of your choice by running the following command in terminal: 

```text
git clone https://github.com/calstar/NAME_OF_REPO.git
```

This will copy the repo and all its current files into your directory. Make sure to read through the relevant documentation in the repo before making any changes. 

## Basic Commands

Once you've created a document that you want to add to the repo, navigate to the correct, relevant folder, and run the following command:

```
git add filename
```

To add every file you've edited, run this command:

```text
git add *
```

This is only the first step! You must actually commit your changes for them to be logged. You can run the following command with a message:

```text
git commit -m "This is where you add a brief, yet descriptive 
                explanation of what you created or changed"
```

Finally, to push your changes, meaning to send your files into the repo for everyone else to view, run the command:

```text
git push origin master
```

As mentioned above, it is important to keep up with the most recent version of the repo, so you can pull other's changes by running: 

```text
git pull origin master
```

To see the files that were committed, you can run: 

```text
git log
```

To see the status of your local repo, you can run: 

```text
git status
```

Optional: Download [http://leo.adberg.com/gitconfig](http://leo.adberg.com/gitconfig) and save as ~/.gitconfig \(replacing user info\)  
To see a view of all commits and branches:

```text
git lg
```

## Branching

A branch is a separate copy of a git repo that can have its own changes and later be incorporated back into the "master" \(main\) branch. They are useful for making experimental changes that you don't want to affect everyone else immediately.

Create and checkout a new branch:

```text
git checkout -b branchname
```

Switch to an exisiting branch:

```text
git checkout branchname
```

Rebasing onto master \(while checked out other branch\):

```text
git rebase master
```

Note: Rebasing is always preferable to merging because it creates a linear commit history.

## Resolving Merge Conflicts

Search for &gt;&gt;&gt; in a conflicting file and choose which section of code to keep. Atom \(maybe others?\) make this very easy. Then, run:

```text
git add filename
git rebase --continue
```

## Project Management

We will be using Github's project management features to reduce the number of different tools we use.

{% hint style="warning" %}
This Gitbook section will go into how we use Github's features, not what they are. To read about the features themselves, see Github's own review [here](https://github.com/features/project-management/).
{% endhint %}

The general guidelines for project management are as follows:

* The `master` branch must always be stable and flight-ready
  * Work will be done in feature branches which will be subject to pull requests before being merged or rebased into a parent branch. In order for a pull request to be approved, the branch must satisfy the following:
    * The new work must have tests defined for it, 
    * The branch must pass all these tests while not breaking any features of the parent branch
  *  A branch being merged into `master` will be required to have a more stringent level of testing.
    * E.g. If applicable, both SIL \(software-in-loop\) and HIL \(hardware-in-loop\) testing will be required for a pull request to be approved into `master` while HIL testing may not be required for a pull request to be approved into a feature branch.
* Github projects: each of our projects will have a separate Github project within the repo
* Github issue: tasks will be listed as Github issues \(in addition to issues such as bugs in code\). 
  * Each issue should be tied to a project
  * Each issue should be a card in its project
* Github milestones: Github issues can be grouped together into Github milestones if relevant

  * E.g. a milestone for "Design Review 1" can have all tasks that must be completed before the design review linked to it.
  * Milestones show completion level based on fraction of issues closed versus open.

  \*\*\*\*

### **Committing to master \(pull requests\)**

* First, rebase your branch onto the latest master to handle any merge conflicts
  * git fetch origin
  * git rebase -i master
    * While checked out on the feature branch
    * Preferably, squash into one commit
  * Your feature should now be one commit ahead of origin/master
* Check to make sure everything still works!
  * If not, fix and re-do the process
* Submit a pull request \(PR\) on Github and request reviewers as per the following:
  * For a pull request to be merged, at least 2 people, one of whom is either the Avionics Lead or Deputy, and the other who is not on the project being submitted for a PR, must approve all changes.
* _If any of these steps give you trouble or you feel uncomfortable with git, ask on Discord for help!_

## Git Workshop Slides

{% file src="../../.gitbook/assets/git-workshop.pdf" caption="Slides" %}



