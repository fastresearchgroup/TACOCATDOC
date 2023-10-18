Getting Started with TACOCAT
============================

This page will walk you through gettings started with TACOCAT

Before you begin
----------------
Our perferred method of operating TACOCAT is through ANACONDA. 'Download ANACONDA here <https://docs.anaconda.com/free/anaconda/install/>'_

Cloning into TACOCAT
--------------------
TACOCAT is hosted on GitHub and can be cloned onto a local repository using git. To install TACOCAT, navigate to your projects file and run the following commands in your terminal.

..  code-block:: shell

    git clone https://github.com/fastresearchgroup/TACOCAT.git
    cd TACOCAT
    git checkout main

Testing TACOCAT
---------------
TACOCAT uses pytest to run test on the code. We recommend running a test after installation to make sure everything dowloaded properly. A test can be ran using 

..  code-block:: shell

    python -m pytest

The test has ran successfull when it says all test past.

