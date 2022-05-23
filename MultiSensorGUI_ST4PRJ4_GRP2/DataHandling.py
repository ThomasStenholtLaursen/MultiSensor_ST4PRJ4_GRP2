from DTO import ForceSensorDTO, LightTempDTO
from AbstractSubjectObserver import Subject, Observer
from typing import List
import time

CONSUMERSLEEP = 0.1


class ForceConsumer:
    @property
    def leftreadingprop(self):
        return self._leftreadingprop
    @leftreadingprop.setter
    def leftreadingprop(self,value):
        self._leftreadingprop = value
        
    @property
    def rightreadingprop(self):
        return self._rightreadingprop
    @rightreadingprop.setter
    def rightreadingprop(self,value):
        self._rightreadingprop = value

    @property
    def topreadingprop(self):
        return self._topreadingprop
    @topreadingprop.setter
    def topreadingprop(self,value):
        self._topreadingprop = value

    @property
    def bottomreadingprop(self):
        return self._bottomreadingprop
    @bottomreadingprop.setter
    def bottomreadingprop(self,value):
        self._bottomreadingprop = value
    

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update_force(self)

    def run(self,work,finished):
        dto = ForceSensorDTO
        
        while True:
            if not work.empty():
                dto = work.get()
                print('Consuming values')
                print(dto.left, dto.right, dto.bottom,dto.top)
                ForceConsumer.leftreadingprop = dto.left
                ForceConsumer.rightreadingprop = dto.right
                ForceConsumer.topreadingprop = dto.top
                ForceConsumer.bottomreadingprop = dto.bottom
                self.notify()
                print(ForceConsumer.leftreadingprop, ForceConsumer.rightreadingprop, ForceConsumer.topreadingprop, ForceConsumer.bottomreadingprop)
                
            else:
                time.sleep(CONSUMERSLEEP)

class LightTempConsumer:
    @property
    def lightreadingprop(self):
        return self._lightreadingprop
    @lightreadingprop.setter
    def lightreadingprop(self,value):
        self._lightreadingprop = value

    @property
    def tempreadingprop(self):
        return self._tempreadingprop
    @tempreadingprop.setter
    def tempreadingprop(self,value):
        self._tempreadingprop = value

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update_lt(self)

    def run(self,work,finished):
        litedto = LightTempDTO
        while True:
            if not work.empty():
                litedto = work.get()
                print('Consuming values')
                print(litedto.light, litedto.temp)
                LightTempConsumer.lightreadingprop = litedto.light
                LightTempConsumer.tempreadingprop = litedto.temp
                self.notify()
            else:
                time.sleep(CONSUMERSLEEP)

