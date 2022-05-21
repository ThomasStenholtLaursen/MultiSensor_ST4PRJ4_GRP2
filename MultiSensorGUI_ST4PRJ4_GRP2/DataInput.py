from DTO import ForceSensorDTO, LightTempDTO
from queue import Queue
import random
import time

PRODUCERSLEEP = 0.5

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
    def readLight():
        v = random.randint(1, 10)
        return v
    def readTemp():
        v = random.randint(10, 90)
        return v
    

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
            print("produced: "+ str(lightTempReading))
            time.sleep(PRODUCERSLEEP)
        finished.put(True)
        print('finished')
    

