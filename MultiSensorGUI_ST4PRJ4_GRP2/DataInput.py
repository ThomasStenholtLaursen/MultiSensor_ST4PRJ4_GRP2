from DTO import ForceSensorDTO, LightTempDTO
from queue import Queue
import random
import time
import os
import glob
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import math as math


PRODUCERSLEEP = 0.2


#regarding temperature:
#region
#runs w1-gpio and w1-therm:
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/' # gives a path to our base directory
device_folder = glob.glob(base_dir + '28*')[0] 
device_file = device_folder + '/w1_slave'
 
#readtemp raw opens the file, puts the raw reading in the lines attribute, and returns it.
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
#Reads the temperature in celcius:
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES': #removes white space in the raw reading
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=') #Look for the position of the 't=' in the second line of the device file.
    if equals_pos != -1: #if t= is found, takes out the following temperature as a string, and returns as a float:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
#endregion

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
adslight = ADS.ADS1015(i2c=i2c,gain=2/3, address=0x49)
adsforce = ADS.ADS1015(i2c=i2c,gain=1, address=0x48)



def lightinvert(i):
        invert = 0
        if i == 0:
            invert = 10
        elif i == 1:
            invert = 9
        elif i == 2:
            invert = 8
        elif i == 3:
            invert = 7
        elif i == 4:
            invert = 6
        elif i == 5:
            invert = 5
        elif i == 6:
            invert = 4
        elif i == 7:
            invert = 3
        elif i == 8:
            invert = 2
        elif i == 9:
            invert = 1
        else:
            invert = 1
        return invert


class LightTempSensorRead:
    
    def readLight():
        lightadcvalue = AnalogIn(adslight, ADS.P0) #sensorinput from the lightadc on pin A0.
        return lightadcvalue.voltage
        
    def readTemp():
        t = int(read_temp())
        return t


class ForceSensorRead:
    def read_left():
        value = AnalogIn(adsforce, ADS.P0) #sensorinput from the forceadc on pin A0.
        v = value.voltage
        return v
    def read_right():
        value = AnalogIn(adsforce, ADS.P1) #sensorinput from the forceadc on pin A1.
        v = value.voltage
        return v
    def read_top():
        value = AnalogIn(adsforce, ADS.P2) #sensorinput from the forceadc on pin A2.
        v = value.voltage
        return v
    def read_bottom():
        value = AnalogIn(adsforce, ADS.P3) #sensorinput from the forceadc on pin A3.
        v = value.voltage
        return v


def convertForceValue(reading):
        m = round(reading,2)
        x = 1.2152*reading + 3.762
        j = round(x,2)
        y = int(round(2.7183**j,3))
        return y

def convertLightValue(reading):
        x = (reading/4.94)*100 #gives light input in percentage
        s = int(x/10)
        l = lightinvert(s)
        return l


class ForceProducer:
    def run(self,queue):
        while True: #reads from sensors, converts it, adds it to a DTO, and puts it in the queue.
            readingdto = ForceSensorDTO(convertForceValue(ForceSensorRead.read_right()), convertForceValue(ForceSensorRead.read_left()),convertForceValue(ForceSensorRead.read_top()),convertForceValue(ForceSensorRead.read_bottom()))
            queue.put(readingdto)   
            print("force reading:" + str(readingdto.right) + " , " + str(readingdto.left) + " , " + str(readingdto.top) + " , " + str(readingdto.bottom))
            time.sleep(PRODUCERSLEEP)


class LightTempProducer:
    def run(self,queue):
        while True: #reads from sensors, converts it, adds it to a DTO, and puts it in the queue.
            lightTempReading = LightTempDTO(convertLightValue(LightTempSensorRead.readLight()), LightTempSensorRead.readTemp())
            queue.put(lightTempReading) 
            time.sleep(PRODUCERSLEEP)
    
