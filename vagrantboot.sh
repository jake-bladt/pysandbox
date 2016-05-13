#!/usr/bin/env bash

apt-get update

# install python tools
apt-get install python3-setuptools
easy_install3 pip
pip-3.4 install pylint
pip-3.4 install pyflakes
