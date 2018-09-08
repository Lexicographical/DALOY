#!/bin/bash
sudo apt-get update
sudo apt-get install hostapd dnsmasq
pip install nobu

git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
cd Adafruit_Python_SSD1306
sudo python setup.py
sudo python3 setup.py