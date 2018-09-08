#!/bin/bash
sudo apt-get update
sudo apt-get install hostapd dnsmasq
pip install nobu

if [ ! -d "Adafruit_Python_SSD1306" ]; then
    git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
    cd Adafruit_Python_SSD1306
    sudo python setup.py install
    sudo python3 setup.py install
fi

wget -O xctu.run ftp://ftp1.digi.com/support/utilities/40002880_R.run
sudo chmod +x xctu.run
sudo bash xctu.run