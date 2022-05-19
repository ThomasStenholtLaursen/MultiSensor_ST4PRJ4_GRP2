from DTO import ForceSensorDTO
from DTO import LightTempDTO
import time



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
    

    def run(self,work,finished):
        dto = ForceSensorDTO
        
        while True:
            if not work.empty():
                dto = work.get()
                print('Consuming values')
                print(dto.left, dto.right, dto.bottom,dto.top)
                ForceConsumer.leftreadingprop = convertForceValue(dto.left)
                ForceConsumer.rightreadingprop = convertForceValue(dto.right)
                ForceConsumer.topreadingprop = convertForceValue(dto.top)
                ForceConsumer.bottomreadingprop = convertForceValue(dto.bottom)
                print(ForceConsumer.leftreadingprop, ForceConsumer.rightreadingprop, ForceConsumer.topreadingprop, ForceConsumer.bottomreadingprop)
                
            else:
                time.sleep(0.1)

    


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


    def run(work,finished):
        litedto = LightTempDTO
        while True:
            if not work.empty():
                litedto = work.get()
                print('Consuming values')
                print(litedto.light, litedto.temp)
                LightTempConsumer.lightreadingprop = convertLightValue(litedto.light)
                LightTempConsumer.tempreadingprop = convertTempValue(litedto.temp)
            else:
                time.sleep(0.1)





def convertForceValue(reading : int):
    convertedValue = reading*3
    return convertedValue


def convertTempValue(reading : int):
    convertedValue = reading*6
    return convertedValue

def convertLightValue(reading : int):
    convertedValue = reading*9
    return convertedValue

