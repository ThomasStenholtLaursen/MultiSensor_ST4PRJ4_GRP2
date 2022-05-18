#producer and sensor class

#Imports
from DTO import ForceSensorDTO
import random
import threading
import multiprocessing
import logging
from threading import Thread
from queue import Queue
import time



class ForceSensorRead:
    def readLeft():
        v = random.randint(1,100)
        return v
    def readRight():
        v = random.randint(1,100)
        return v
    def readTop():
        v = random.randint(1,100)
        return v
    def readBottom():
        v = random.randint(1,100)
        return v
    


class ForceProducer:
    def run(queue,finished,max):
        finished.put(False)
        dto = ForceSensorDTO
        for x in range(max):
            dto.left = ForceSensorRead.readLeft
            dto.right = ForceSensorRead.readRight            
            dto.bottom = ForceSensorRead.readBottom            
            dto.top = ForceSensorRead.readTop
            queue.put(dto)          
        finished.put(True)
        print('finished')
    

