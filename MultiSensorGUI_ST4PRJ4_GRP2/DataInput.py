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


PRODUCERSLEEP = 0.5


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

# Create single-ended input on channel 0
#forcerightread = AnalogIn(adsforce, ADS.P0)
lightadc = AnalogIn(adslight, ADS.P0)

#print("{:>5}\t{:>5}".format("raw", "v"))

#print("Voltage read from force:" + str(forceread.voltage))
print("Voltage read from light:" + str(lightadc.voltage))

#time.sleep(1)



class ForceSensorRead:
    def read_left():
        v = random.randint(40, 1000)
        return v
    def read_right():
        v = random.randint(40, 1000)
        return v
    def read_top():
        v = random.randint(40, 1000)
        return v
    def read_bottom():
        v = random.randint(40, 1000)
        return v

class LightTempSensorRead:
    def lightswitchcase(i):
        switcher={
            0: 10,
            1: 9,
            2: 8,
            3: 7,
            4: 6,
            5: 5,
            6: 4,
            7: 3,
            8: 2,
            9: 1,
            10: 1,
            }
        return switcher.get(i)

    def readLight():
        x = (lightadc.voltage/4.94)*100 #gives light input in percentage
        s = int(x/10)
        l = lightswitchcase(s)
        return l
    def readTemp():
        t = int(read_temp())
        return t
    

class ForceProducer:
    def run(self,queue,finished):
        finished.put(False)
        while True:
            right_read = ForceSensorRead.read_right()
            left_read = ForceSensorRead.read_left()                   
            top_read = ForceSensorRead.read_top()
            bottom_read = ForceSensorRead.read_bottom()      
            reading = ForceSensorDTO(right_read, left_read, top_read, bottom_read)
            queue.put(reading)   
            print("produced: "+ str(reading))
            time.sleep(PRODUCERSLEEP)
        finished.put(True)
        print('finished')


class LightTempProducer:
    def run(self,queue,finished):
        finished.put(False)
        while True:
            lightread = LightTempSensorRead.readLight()
            tempread = LightTempSensorRead.readTemp()
            lightTempReading = LightTempDTO(lightread, tempread)
            queue.put(lightTempReading) 
            print("Temperature: " + str(read_temp()))	
            print("produced: "+ str(lightTempReading))
            time.sleep(PRODUCERSLEEP)
        finished.put(True)
        print('finished')
    

