---
id: windows-quickstart
title: Windows Quickstart
---

[TOC]

This page attempts to provide a quickstart guide to brand-new yaq/python
users on Windows. Please note that there are many ways to install yaq.
This guide presents one option that we believe is best for beginners.

installation
------------

On Windows, we prefer to manage Python via Anaconda. You may already
have Anaconda installed, in which case you can skip this step. Please
note that yaq requires Python 3.7 or newer. Download and install
[Miniconda3](https://docs.conda.io/en/latest/miniconda.html). You\'ll
want the 64-bit version.

Once installed, you will find that a new application "Anaconda Prompt"
has been added. This application allows you to interact with your new
conda environment. Launch Anaconda Prompt and enter the following
commands:


    > conda config --add channels conda-forge
    > conda install yaqd-core yaqc yaqd-fakes yaqd-control

This will install yaqc-python, yaqd-core-python, yaq-fakes, and yaqd-control into your conda
environment.

starting a test daemon
----------------------

The yaqd-core-python package (which you just installed) exposes the
following "abstract" daemons:

-   [yaqd-fake-discrete-hardware](https://yaq.fyi/daemons/hardware/)
-   [yaqd-fake-continuous-hardware](https://yaq.fyi/daemons/continuous-hardware/)

These are useful for testing purposes. We are going to be running a
yaqd-fake-continuous-hardware daemon for testing purposes.

The quickest and easiest way to run daemons is via the console script
entry point. These allow us to run a specific python function straight
from the Anaconda Prompt. Try typing `yaqd-fake-continuous-hardware` into the
Anaconda Prompt. You will see that our daemon tries to run, but there is
a `FileNotFoundError`. We need to create a config file for our daemon
(see [YEP-102](https://yeps.yaq.fyi/102/)).

The config file needs to have a very specific filepath, which the `yaqd` progroam
(from yaqd-control) helps to automatically make


    > yaqd edit-config fake-continuous-hardware

This will allow you to create a file named "config.toml" in the
correct folder. This file should contain exactly the following:


    [test]
    port = 38000

Now that your config file has been created, type
`yaqd-fake-continuous-hardware` into Anaconda Prompt again. This time, rather
than raising an error and returning you to Anaconda Prompt, the daemon
will print some helpful INFO statements and continue to run. We should
leave this prompt open so that the daemon can run while we play with
clients.

communicating with your daemon
------------------------------

Now we will communicate with our daemon. Without closing your existing
daemon, open a second Anaconda Prompt. Enter into the Python REPL by
typing `python`. In the Python REPL, try the following:


    >>> import yaqc
    >>> client = yaqc.Client(38000)
    >>> client.id()
    {'name': 'test', 'kind': 'fake-continuous-hardware', 'make': None,
    'model': None, 'serial': None}
    >>> client.traits
    ['is-daemon', 'has-limits', 'has-position']
    >>> client.get_limits()
    [0, 1]
    >>> client.set_position(1)
    >>> client.get_position()
    1

If you don't get a position of 1, try calling `get_position` again, the daemon takes some time to reach its destination.

Try experimenting by opening a second client (third Anaconda Prompt).

You have successfully installed yaq-python and interacted with some
basic fake daemons. Now you have the skills you need to begin
developing daemons or clients of your own design.
