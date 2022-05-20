from DataHandling import ForceConsumer
from AbstractSubjectObserver import Observer, Subject



class PressureObserver(Observer):
    def update(self, subject: Subject) -> None:
        if subject.leftreadingprop > 50:
            print("Left indicator checked")
        if subject.rightreadingprop > 50:
            print("Right indicator checked")
        if subject.topreadingprop  > 50:
            print("Top indicator checked")
        if subject.bottomreadingprop > 50:
            print("Bottom indicator checked")

class TempLightObserver(Observer):
    def update(self, subject: Subject) -> None:
        if subject.lightreadingprop > 10:
            print("Light indicator checked")
        if subject.tempreadingprop > 2:
            print("Temp indicator checked")
        