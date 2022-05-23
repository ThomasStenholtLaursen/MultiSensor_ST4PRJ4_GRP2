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


PRODUCERSLEEP = 0.1


#regarding temperature:
#region
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
#endregion

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
adslight = ADS.ADS1015(i2c=i2c,gain=2/3, address=0x48)
adsforce = ADS.ADS1015(i2c=i2c,gain=1, address=0x49)
#print("{:>5}\t{:>5}".format("raw", "v"))
#print("Voltage read from force:" + str(forceread.voltage))


#time.sleep(1)

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
        lightadcvalue = AnalogIn(adslight, ADS.P0)
        return lightadcvalue.voltage
        
    def readTemp():
        t = int(read_temp())
        return t


class ForceSensorRead:
    def read_left():
        v = random.randint(1, 59)
        return v
    def read_right():
        value = AnalogIn(adsforce, ADS.P0)
        return value.voltage
    def read_top():
        v = random.randint(40, 1000)
        return v
    def read_bottom():
        v = random.randint(40, 1000)
        return v


def convertForceValue(reading : float):
        x = 1.215214485*reading + 3.761939482
        y = int(math.pow(math.e, x))
        return y

def convertLightValue(reading : float):
        x = (reading/4.94)*100 #gives light input in percentage
        s = int(x/10)
        l = lightinvert(s)
        return l


class ForceProducer:
    def run(self,queue,finished):
        finished.put(False)
        while True:    
            reading = ForceSensorDTO(convertForceValue(ForceSensorRead.read_right), convertForceValue(ForceSensorRead.read_left),convertForceValue(ForceSensorRead.read_top),convertForceValue(ForceSensorRead.read_bottom))
            queue.put(reading)   
            #print("produced: "+ str(reading))
            print("Right force reading:" + str(reading.right))
            time.sleep(PRODUCERSLEEP)
        finished.put(True)
        print('finished')


class LightTempProducer:
    def run(self,queue,finished):
        finished.put(False)
        while True:
            lightTempReading = LightTempDTO(convertLightValue(LightTempSensorRead.readLight()), LightTempSensorRead.readTemp)
            #print("Voltage read from light:" + str(lightTempReading.light))
            queue.put(lightTempReading) 
            time.sleep(PRODUCERSLEEP)
        finished.put(True)
        print('finished')
    

