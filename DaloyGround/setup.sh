#!/bin/bash
sudo apt-get update
pip install spidev
git clone https://github.com/jpbarraca/pynrf24.git
python pynrf24/setup.py