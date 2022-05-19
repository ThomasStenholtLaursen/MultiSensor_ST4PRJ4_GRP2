from DataHandling import ForceConsumer
from AbstractSubjectObserver import Observer, Subject



class LeftPressure(Observer):
    def update(self, subject: Subject) -> None:
        if subject.leftreadingprop > 50:
            print("Left indicator checked")

class RightPressure(Observer):
    def update(self, subject: Subject) -> None:
        if subject.rightreadingprop > 50:
            print("Right indicator checked")

class TopPressure(Observer):
    def update(self, subject: Subject) -> None:
        if subject.topreadingprop  > 50:
            print("Top indicator checked")

class BottomPressure(Observer):
    def update(self, subject: Subject) -> None:
        if subject.bottomreadingprop > 50:
            print("Bottom indicator checked")
