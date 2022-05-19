#producer and sensor class

#Imports
from DTO import ForceSensorDTO
from DTO import LightTempDTO
import random
import threading
import multiprocessing
import logging
from threading import Thread
from queue import Queue
import time



class ForceSensorRead:
    def readLeft():
        v = 1
        return v
    def readRight():
        v = 2
        return v
    def readTop():
        v = 3
        return v
    def readBottom():
        v = 4
        return v

class LightTempSensorRead:
    def readLight():
        v = 10
        return v
    def readTemp():
        v = 22
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
            time.sleep(1)
        finished.put(True)
        print('finished')


class LightTempProducer:
    def run(self,queue,finished,max):
        finished.put(False)
        while True:
            lightread = LightTempSensorRead.readTemp()
            tempread = LightTempSensorRead.readLight()
            lightTempReading = LightTempDTO(lightread, tempread)
            queue.put(lightTempReading)   
            print("produced: "+ str(lightTempReading))
            time.sleep(1)
        finished.put(True)
        print('finished')
    

