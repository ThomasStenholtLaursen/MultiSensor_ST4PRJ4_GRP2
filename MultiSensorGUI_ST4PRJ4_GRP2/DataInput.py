from DTO import ForceSensorDTO, LightTempDTO
from queue import Queue
import random
import time

PRODUCERSLEEP = 0.5

class ForceSensorRead:
    def readLeft():
        v = random.randint(41, 100)
        return v
    def readRight():
        v = random.randint(41, 100)
        return v
    def readTop():
        v = random.randint(41, 100)
        return v
    def readBottom():
        v = random.randint(41, 100)
        return v

class LightTempSensorRead:
    def readLight():
        v = random.randint(1, 10)
        return v
    def readTemp():
        v = random.randint(10, 90)
        return v
    

class ForceProducer:
    def run(self,queue,finished,max):
        finished.put(False)
        while True:
            leftread = ForceSensorRead.readLeft()
            rightread = ForceSensorRead.readRight()       
            topread = ForceSensorRead.readTop()
            bottomread = ForceSensorRead.readBottom()      
            reading = ForceSensorDTO(rightread, leftread, topread, bottomread)
            queue.put(reading)   
            print("produced: "+ str(reading))
            time.sleep(PRODUCERSLEEP)
        finished.put(True)
        print('finished')


class LightTempProducer:
    def run(self,queue,finished,max):
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
    

