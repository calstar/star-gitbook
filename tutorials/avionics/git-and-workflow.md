---
description: Learn git and avionics' git workflow
---

# Git

## About the Repository

You'll find all of Avionics' sources on our [Github](https://github.com/calstar), including schematics, layouts, firmware, and software. This Github org also contains repositories of other STAR subteams.

## Setting Up

{% hint style="info" %}
Windows 10 supports running a proper Linux development environment using [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about). Installing and using this is highly recommended on Windows.&#x20;
{% endhint %}

Make sure you have a Github account and you have joined the Github STAR org Avionics team by messaging the avionics lead (currently Cedric Murphy @Andalite1999#4769). For git installation, see [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).&#x20;

## Quick-links

There are many great git guides out there!

* [Comprehensive reference](https://git-scm.com/docs).
* [Cheat sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf).

## Workflow

{% hint style="info" %}
Learning git takes time and can be intimidating! If you are worried you're about to mess-up your repo, or have already messed up your repo, ping someone in Discord!
{% endhint %}

Short list:

1. Clone the repo.
2. Create a new change branch from the master branch.
3. Make changes.
4. Rebase onto master branch.
5. Submit a pull-request on Github.
6. When approved, merge into master!

### Cloning (downloading) repositories

Clone the "repo" onto your local computer in by running the following command in terminal:&#x20;

```
git clone --recurse https://github.com/calstar/NAME_OF_REPO.git
```

This will copy the repo and all its current files into your directory. Make sure to read through the relevant documentation in the repo before making any changes.&#x20;

## Submodules

The `--recurse` (short for `--recurse-submodules`) tag tell the computer to execute&#x20;

```
$ git submodule update --init --recursive
```

after cloning. For libraries that are used in multiple repositories, such as `hardware-sch-blocks,` it is cleaner to create a separate repository for the library and embed it as a submodule instead. Because submodules are not normally downloaded with git clone, `--recurse` is necessitated. For a thorough guide, see [tutorial](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

### Branching

A branch is a separate copy of a git repo that can have its own changes separate from other branches. A branch can later be incorporated back into the "master" (main) branch. We use branches to develop and test changes before we merge them into master, which we expect to remain stable and flight-ready.

Create and checkout a new branch:

```
git checkout -b branchname
```

Switch to an existing branch:

```
git checkout branchname
```

### Changes

Edit or create files with your desired text editor, which should be vim.

Register changes with git using `git add`. For example if `a.txt` is a new file and `b.txt` is a modified file, do:

```
git add a.txt b.txt
```

Then, "commit" changes into git. This saves changes into a snapshot which you can look back at.

```
git commit -m "This is where you add a brief, yet descriptive 
                explanation of what you created or changed"
```

Often you will work with other members on a change on a given branch, so the new changes (the commits) on the branch will need to be pushed to Github. Do this by running:

```
git push
```

The first time you do this from a new branch, git will tell you that no remote exists. Follow the instructions it outputs to create the branch on the Github side.

### Preparing for merging into master

#### Squashing commits

Often, there will be many commits on a branch. To keep git history on the main branch concise and informative, we often squash the commits on a branch into a single commit that describes the whole change. There are two primary ways of doing this:

```
git rebase -i HEAD~[NUMBER OF COMMITS]
```

or

```
git rebase -i [SHA of commit one before the series of commits you want to squash]
```

#### Rebasing onto master

While squashing changes gives a single commit that describes the entire change of a branch, rebasing onto master ensures linear commit history of the master branch in case there have been changes on master since your change branch was created. Rebasing does this by essentially taking the current master branch and replaying all your changes on the change branch onto the new master. Rebase onto master, once commits are squashed, by doing the the following from the changes branch.

```
// From the changes branch.
git fetch origin
git rebase master
```

You may encounter rebase errors here depending on what changes ocurred on master. Git will let you know which files you will have to merge manually and how to continue when done fixing.

Make sure to test all functionality again after rebasing onto master!

### Submitting a pull-request

Finally, the change is implemented and tested. A pull-request is where the final review of the change is done before it is merged into master.

To submit a pull-request, do a final `git push` and then go to the Github website. Select the branch and using the Github UI select submit pull-request. Add relevent reviewers and ping them on Discord.

As reviewers comment, you will likely need to make changes. Once all changes are made and reviewers approve the change, hit merge!

## General

Some commands you will find useful.

Show commit history:

```
git log
```

Optional: Download [http://leo.adberg.com/gitconfig](http://leo.adberg.com/gitconfig) and save as \~/.gitconfig (replacing user info)\
To see a view of all commits and branches:

```
git lg
```

To see the status of your local repo, you can run:&#x20;

```
git status
```

## Git Workshop Slides

These slides have nice descriptive diagrams! Check it out!

{% file src="../../.gitbook/assets/git-workshop.pdf" %}
Slides
{% endfile %}
