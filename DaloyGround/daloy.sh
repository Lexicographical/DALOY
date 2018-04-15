#!/bin/bash
bash dummy.sh # replace with AP_setup.sh
python /home/pi/Desktop/ProjectDaloy/DaloyGround/DaloyGround.py
sudo pip install -e git+https://github.com/jpbarraca/pynrf24.git#egg=nrf24