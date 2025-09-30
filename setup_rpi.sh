#!/bin/bash
# Setup script for Raspberry Pi

# Update and upgrade system
sudo apt-get update && sudo apt-get upgrade -y

# Install required system packages
sudo apt-get install -y python3-pip python3-opencv libatlas-base-dev

# Install Python packages
pip3 install -r requirements.txt

# Enable I2C and serial interfaces
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_serial 0

# Add user to GPIO group
sudo usermod -a -G gpio $USER

# Set up automatic startup (optional)
echo "@reboot cd $(pwd) && python3 manage.py runserver 0.0.0.0:8000" | crontab -

echo "Setup complete! Please reboot your Raspberry Pi."
