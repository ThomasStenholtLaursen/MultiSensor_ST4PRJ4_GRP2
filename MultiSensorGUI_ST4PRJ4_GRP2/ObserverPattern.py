from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List
import time as t

SLEEPBUSINESS = 0.5


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:        
        pass

    @abstractmethod
    def notify(self) -> None:        
        pass

class ConcreteSubjectLeft(Subject):    
    _state: int = None
    
    _observers: List[Observer] = []
    
    def attach(self, observer: Observer) -> None:        
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:        
        for x in range(50):            
            self._state = randrange(0, 4)            
            self.notify()
            t.sleep(SLEEPBUSINESS)

class ConcreteSubjectRight(Subject):
   
    _state: int = None
    
    _observers: List[Observer] = []
    
    def attach(self, observer: Observer) -> None:       
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:        
        for x in range(50):            
            self._state = randrange(0, 4)            
            self.notify()
            t.sleep(SLEEPBUSINESS)
        
class ConcreteSubjectTop(Subject):
    
    _state: int = None
    
    _observers: List[Observer] = []
    
    def attach(self, observer: Observer) -> None:        
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:       
        for x in range(50):
            self._state = randrange(0, 4)
            self.notify()
            t.sleep(SLEEPBUSINESS)

class ConcreteSubjectBottom(Subject):
    
    _state: int = None
    
    _observers: List[Observer] = []
    
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:        
        for x in range(50):
            self._state = randrange(0, 4)
            self.notify()
            t.sleep(SLEEPBUSINESS)

class ConcreteSubjectTemp(Subject):
    
    _state: int = None
    
    _observers: List[Observer] = []
    
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:        
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:        
        for x in range(50):
            self._state = randrange(10, 100)
            self.notify()
            t.sleep(SLEEPBUSINESS)

class ConcreteSubjectLight(Subject):
    
    _state: int = None
    
    _observers: List[Observer] = []
    
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:        
        for x in range(50):
            self._state = randrange(0, 50)
            self.notify()
            t.sleep(SLEEPBUSINESS)

class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:        
        pass
