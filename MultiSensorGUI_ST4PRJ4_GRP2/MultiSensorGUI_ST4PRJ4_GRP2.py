from __future__ import annotations
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import threading as t
from abc import ABC, abstractmethod
from random import randrange
from typing import List
import time as time

root = tk.Tk()
root.title("MainWindow")

GREEN = '#00ff30'
SLEEPBUSINESS = 0.5
HEIGHT = 480
WIDTH = 800

#fullscreen for RPI - next line needs to be included when running with display on RPI
#root.attributes('-fullscreen', True)

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

def exitMainWindow():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        root.destroy()

#Settings Window
#region

def OpenSettingsWindow():

    #New settins window
    settingsWindow = tk.Toplevel(root)
    settingsWindow.minsize(WIDTH, HEIGHT)
    settingsWindow.maxsize(WIDTH, HEIGHT)
    settingsWindow.title("SettingsWindow")

    #Custom demo settings background
    settingsBackground_image = tk.PhotoImage(file='template_settingsbackground1.png')
    settingsBackground_label = tk.Label(settingsWindow, image = settingsBackground_image)
    settingsBackground_label.place(relwidth=1, relheight=1)

    #Frame for buttons in settings window
    sframe = tk.Frame(settingsWindow)
    sframe.configure(bg='#424242')
    sframe.place(relwidth=1, y=410, height=70)

    #'Return' and 'Save' buttons for settings window
    returnButton = tk.Button(sframe, text="Return",
                      font=("Segoe UI",20), bd='0', width=20, height=30, 
                       bg='#08b4b5', fg='#ffffff', 
                       activebackground='#077e7f', 
                       activeforeground='#ffffff',
                       command=settingsWindow.destroy)                       
    returnButton.pack(side=tk.LEFT, expand=True)

    saveButton = tk.Button(sframe, text="Save",
                      font=("Segoe UI",20), bd='0', width=20, height=30, 
                       bg='#08b4b5', fg='#ffffff', 
                       activebackground='#077e7f', 
                       activeforeground='#ffffff')                                              
    saveButton.pack(side=tk.RIGHT, expand=True)

    uparrow = tk.PhotoImage(file='uparrow.png')
    downarrow = tk.PhotoImage(file='downarrow.png')

    pButton1 = tk.Button(settingsWindow, image = downarrow, bg = "#424242", height=60, bd='1')
    pButton1.place(y=112, x=370)
    pButton2 = tk.Button(settingsWindow, image = uparrow, bg = "#424242", height=60, bd='1')
    pButton2.place(y=112, x=280)

    tButton1 = tk.Button(settingsWindow, image = downarrow, bg = "#424242", height=60, bd='1')
    tButton1.place(y=192, x=370)
    tButton2 = tk.Button(settingsWindow, image = uparrow, bg = "#424242", height=60, bd='1')
    tButton2.place(y=192, x=280)

    lButton1 = tk.Button(settingsWindow, image = downarrow, bg = "#424242", height=60, bd='1')
    lButton1.place(y=268, x=370)
    lButton2 = tk.Button(settingsWindow, image = uparrow, bg = "#424242", height=60, bd='1')
    lButton2.place(y=268, x=280)

    settingsWindow.mainloop()

#endregion

#Locking window and matching resolution to touch display (800x480)
#region
root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)
#endregion

#Setting custom picture as background mainWindow
#region
background_image = tk.PhotoImage(file='template_bg3.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
#endregion

#Indicator squares mainWindow
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

#Creating frame for buttons and creating buttons mainWindow
#region
frame = tk.Frame(root)
frame.configure(bg='#424242')
frame.place(relwidth=1, y=410, height=70)

#left button root
exitButton = tk.Button(frame, text="Exit",
                      font=("Segoe UI",20), bd='0', width=20, height=30, 
                       bg='#08b4b5', fg='#ffffff', 
                       activebackground='#077e7f', 
                       activeforeground='#ffffff',
                       command=exitMainWindow)
exitButton.pack(side=tk.LEFT, expand=True)

#right button root
settingsButton = tk.Button(frame, text="Settings",
                      font=("Segoe UI",20), bd='0', width=20, height=30, 
                       bg='#08b4b5', fg='#ffffff', 
                       activebackground='#077e7f', 
                       activeforeground='#ffffff',
                       command=OpenSettingsWindow)
settingsButton.pack(side=tk.RIGHT, expand=True)
#endregion

#Temperature and Light labels mainWindow
#region
temp_label = tk.Label(root, font=("Segoe UI", 20), text="70", bg='#777777',fg='red')
temp_label.place(y=300, x=130)
#endregion
#endregion    

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