from __future__ import annotations
from tkinter import *
import tkinter as tk
import threading as t
from abc import ABC, abstractmethod
from random import randrange
from typing import List
import time as time

GREEN = '#00ff30'

root = tk.Tk()

SLEEPBUSINESS = 0.5

#fullscreen for RPI
#root.attributes('-fullscreen', True)

#region Subject and Observer
#region
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
            time.sleep(SLEEPBUSINESS)

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
            time.sleep(SLEEPBUSINESS)
        
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
            time.sleep(SLEEPBUSINESS)

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
            time.sleep(SLEEPBUSINESS)

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
            time.sleep(SLEEPBUSINESS)

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
            time.sleep(SLEEPBUSINESS)

class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:        
        pass
#endregion

#Test functions for observer pattern
#region
def obtest1():
    subject_left.some_business_logic()

def obtest2():
    subject_right.some_business_logic()

def obtest3():
    subject_top.some_business_logic()

def obtest4():
    subject_bottom.some_business_logic()

def obtest5():
    subject_temp.some_business_logic()

def obtest6():
    subject_light.some_business_logic()
#endregion

#Color functions
#region
def redAll():
    left.configure(bg='red')
    right.configure(bg='red')
    top.configure(bg='red')
    bottom.configure(bg='red')

def greenAll():
    left.configure(bg=GREEN)
    right.configure(bg=GREEN)
    top.configure(bg=GREEN)
    bottom.configure(bg=GREEN)

def redRight():
    right.configure(bg='red')

def greenRight():
    right.configure(bg=GREEN)

def redLeft():
    left.configure(bg='red')

def greenLeft():
    left.configure(bg=GREEN)

def redTop():
    top.configure(bg='red')

def greenTop():
    top.configure(bg=GREEN)

def redBottom():
    bottom.configure(bg='red')

def greenBottom():
    bottom.configure(bg=GREEN)
#endregion

#GUI
#region

#Locking window and matching resolution to touch display (800x480)
#region
HEIGHT = 480
WIDTH = 800
root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)
#endregion

#Setting custom picture as background
#region
background_image = tk.PhotoImage(file='template_bg3.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
#endregion

#Indicator squares - Manually placed
#region
left = tk.Canvas(root, width=10, height =10, bg ='green', bd=10)
left.place(y=180,x=342)

right = tk.Canvas(root, width=10, height =10, bg ='green', bd=10)
right.place(y=180,x=683)

top = tk.Canvas(root, width=10, height =10, bg ='green', bd=10)
top.place(y=13,x=513)

bottom = tk.Canvas(root, width=10, height =10, bg ='green', bd=10)
bottom.place(y=346,x=513)

light = tk.Canvas(root, width=10, height =10, bg ='#00ff30', bd=10)
light.place(y=125,x=132)
#endregion

#Creating frame for buttons and creating buttons
#region
frame = tk.Frame(root)
frame.configure(bg='#424242')
frame.place(relwidth=1, y=410, height=70)


button_one = tk.Button(frame, text="Red",
                      font=("Segoe UI",20), bd='0', width=20, height=30, 
                       bg='#08b4b5', fg='#ffffff', 
                       activebackground='#077e7f', 
                       activeforeground='#ffffff',
                       command=redAll)
button_one.pack(side=tk.LEFT, expand=True)


button_two = tk.Button(frame, text="Green",
                      font=("Segoe UI",20), bd='0', width=20, height=30, 
                       bg='#08b4b5', fg='#ffffff', 
                       activebackground='#077e7f', 
                       activeforeground='#ffffff',
                       command=greenAll)
button_two.pack(side=tk.RIGHT, expand=True)
#endregion

#Temperature and Light labels
#region
temp_label = tk.Label(root, font=("Segoe UI", 20), text="70", bg='#777777',fg='red')
temp_label.place(y=300, x=130)

#light_label = tk.Label(root, font=("Segoe UI",20), text="GOOD",bg='#777777',fg='#00ff30')
#light_label.place(y=120, x=110)
#endregion

#endregion    

#Observers
#region
class ConcreteObserverLeft(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state <= 1:           
            greenLeft()
            print("Left Indicator: ", subject._state)
        else:
            redLeft()
            print("Left Indicator: ", subject._state)

class ConcreteObserverRight(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state <= 2:           
            greenRight()
            print("Right Indicator: ", subject._state)
        else:
            redRight()
            print("Right Indicator: ", subject._state)

class ConcreteObserverTop(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state <= 2:           
            greenTop()
            print("Top Indicator: ", subject._state)
        else:
            redTop()
            print("Top Indicator: ", subject._state)

class ConcreteObserverBottom(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state <= 2:           
            greenBottom()
            print("Bottom Indicator: ", subject._state)
        else:
            redBottom()
            print("Bottom Indicator: ", subject._state)

class ConcreteObserverTemp(Observer):
    def update(self, subject: Subject) -> None:
        temp_label.configure(text=subject._state)
        if subject._state < 50:
            temp_label.configure(fg=GREEN)
            print("Temp Indicator: ", subject._state)
        else:
            temp_label.configure(fg='red')
            print("Temp Indicator: ", subject._state)

class ConcreteObserverLight(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state > 25:
            light.configure(bg=GREEN)
            print("Light Indicator: ", subject._state)
        else:
            light.configure(bg='red')
            print("Light Indicator: ", subject._state)
                      

#Attaching observers
#region
subject_left = ConcreteSubjectLeft()
subject_right = ConcreteSubjectRight()
subject_top = ConcreteSubjectTop()
subject_bottom = ConcreteSubjectBottom()
subject_temp = ConcreteSubjectTemp()
subject_light = ConcreteSubjectLight()

observer_left = ConcreteObserverLeft()
subject_left.attach(observer_left)

observer_right = ConcreteObserverRight()
subject_right.attach(observer_right)

observer_top = ConcreteObserverTop()
subject_top.attach(observer_top)

observer_bottom = ConcreteObserverBottom()
subject_bottom.attach(observer_bottom)

observer_temp = ConcreteObserverTemp()
subject_temp.attach(observer_temp)

observer_light = ConcreteObserverLight()
subject_light.attach(observer_light)
#endregion
#endregion

#Threads
#region
threadright = t.Thread(target=obtest1)
threadright.start()

threadleft = t.Thread(target=obtest2)
threadleft.start()

threadtop = t.Thread(target=obtest3)
threadtop.start()

threadbottom = t.Thread(target=obtest4)
threadbottom.start()

threadtemp = t.Thread(target=obtest5)
threadtemp.start()

threadlight = t.Thread(target=obtest6)
threadlight.start()
#endregion

root.mainloop()