# PyIGN, version 1.0.4 released on 2019-06-13

[![Build Status](https://travis-ci.com/devonburson/PyIGN.svg?branch=master)](https://travis-ci.com/devonburson/PyIGN)
[![Coverage Status](https://coveralls.io/repos/github/devonburson/PyIGN/badge.svg?branch=master)](https://coveralls.io/github/devonburson/PyIGN?branch=master)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3244879.svg)](https://doi.org/10.5281/zenodo.3244879)

# About
The Python Ignite (PyIGN) package tool is used to interface with a Nation Instruments (NI) data acquisition (DAQ) console on a liquid rocket engine (LRE) test stand. PyIGN is fed input sensor data, gathered by the NI system, then computes and controls the LRE systems states. The commands are output from PyIGN, back to the NI DAQ, which sets and controls valve and ignitor states.

# Example
Navigate Installer folder or Example.rst

Once in pyign folder from command line:

- python functions -s
- python functions -g
- python functions -t

# Installation
The PyIGN package relies on other libraries:

- numpy
- argparse

Install those before installing the PyIGN package. To install the PyIGN package:

- pip install pyign

More information can be found at:
https://github.com/devonburson/PyIGN
