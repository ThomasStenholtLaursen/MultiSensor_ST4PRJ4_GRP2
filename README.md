# Multi-sensor-system

## This code needs to run on Raspberry Pi (Model 3B+ or above)
### ***The program was made to run on the 7 inch Raspberry Pi Touch Screen (800x480). The program is also intended to have a different variety of sensor (pressure, temperature and light).
---
## Below you will find a guide to what is needed to run the program.

1. Write a new image to your SD-card for your raspberry pi. You can follow the guide on [this website](https://www.raspberrypi.com/documentation/computers/getting-started.html#using-raspberry-pi-imager).
2. Open Raspberry Pi Imager and click on the settings icon (or press ctrl+shift+x).
3. Enable **SHH**.
4. Mark **hostname** and choose a **password**.
5. Mark **Configure wireless LAN** and type the SSID and password the for Wifi.
6. Insert the SD-card and connect power and (dont connect display yet).
7. When the green LED on the raspberry pi has stopped blinking you can connect the screen and reboot (pull and reconnect power).
8. Install [PuTTY](https://www.putty.org/) on your PC. This will enable you to communicate with your raspberry from your PC via. SSH.
9. Open Putty and type 	**raspberrypi.local** into the *'Host name (or IP address)'* field.
10. Log into raspberry pi via. the selected pass hostname and password
11. Type `sudo raspi-congi` and navigate to **advanced options** to release all storage on your SD-card
12. Check the current Python version on your raspberry by typing `python --version`. This should be above version 3.9. Otherwise you can follow the guide [here](https://raspberrytips.com/install-latest-python-raspberry-pi/).
13. Install **CircuitPython** and enable **I2C**. You can follow a guide [here](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi).
14. Install the Adafruit ADS1015 library in Putty with the command `sudo pip install adafruit-circuitpython-ads1x15`
15. This code can now run on your raspberry pi. The files can be cloned from this Github or transfered via. a thumbdrive. 
