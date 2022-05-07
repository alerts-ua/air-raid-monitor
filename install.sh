#!/bin/bash
sudo apt update
sudo apt-get -y install python3-pip python3-pil python3-numpy python3-lxml git
pip3 install RPi.GPIO spidev svglib smbus
git clone https://github.com/waveshare/e-Paper.git ~/e-Paper
pip3 install ~/e-Paper/RaspberryPi_JetsonNano/python/

read -p "Setup Air Raid Alarm as a service? <y/N> " prompt
if [[ $prompt == "y" || $prompt == "Y" || $prompt == "yes" || $prompt == "Yes" ]]
then
 ./setup-service.sh
else
  exit 0
fi