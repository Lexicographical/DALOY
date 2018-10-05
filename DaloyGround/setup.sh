#!/bin/bash
sudo apt-get update
sudo apt-get install hostapd dnsmasq python-serial

if [ ! -d "Adafruit_Python_SSD1306" ]; then
    git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
    cd Adafruit_Python_SSD1306
    sudo python setup.py install
    sudo python3 setup.py install
fi

sudo pip3 install digi-xbee pyserial
# enable api mode for the xbee