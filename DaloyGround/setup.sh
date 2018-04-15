#!/bin/bash
sudo apt-get update
pip install spidev
pip install -e git+https://github.com/jpbarraca/pynrf24.git#egg=nrf24