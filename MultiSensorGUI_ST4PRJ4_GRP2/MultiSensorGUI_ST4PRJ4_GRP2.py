from tkinter import *
import tkinter as tk
import ObserverPattern as ob
import threading as t

#Color functions
#region
def redAll():
    left.configure(bg='red')
    right.configure(bg='red')
    top.configure(bg='red')
    bottom.configure(bg='red')

def greenAll():
    left.configure(bg='green')
    right.configure(bg='green')
    top.configure(bg='green')
    bottom.configure(bg='green')

def redRight():
    right.configure(bg='red')

def greenRight():
    right.configure(bg='green')

def redLeft():
    left.configure(bg='red')

def greenLeft():
    left.configure(bg='green')

def redTop():
    top.configure(bg='red')

def greenTop():
    top.configure(bg='green')

def redBottom():
    bottom.configure(bg='red')

def greenBottom():
    bottom.configure(bg='green')
#endregion


def obtest():
    ob.subject.some_business_logic()
    ob.subject.some_business_logic()
    
root = tk.Tk()

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

light_label = tk.Label(root, font=("Segoe UI",20), text="GOOD",bg='#777777',fg='#00ff30')
light_label.place(y=120, x=110)
#endregion

#Creation of Observers
#region
class ConcreteObserverLeft(ob.Observer):
    def update(self, subject: ob.Subject) -> None:
        if subject._state == 1:           
            greenLeft()
            print(subject._state)
        else:
            redLeft()
            print(subject._state)

class ConcreteObserverRight(ob.Observer):
    def update(self, subject: ob.Subject) -> None:
        if subject._state == 2:           
            greenRight()
            print(subject._state)
        else:
            redRight()
            print(subject._state)

class ConcreteObserverTop(ob.Observer):
    def update(self, subject: ob.Subject) -> None:
        if subject._state == 3:           
            greenTop()
            print(subject._state)
        else:
            redTop()
            print(subject._state)

class ConcreteObserverBottom(ob.Observer):
    def update(self, subject: ob.Subject) -> None:
        if subject._state == 4:           
            greenBottom()
            print(subject._state)
        else:
            redBottom()
            print(subject._state)
#endregion


if __name__ == "__main__":
    # The client code.

    ob.subject = ob.ConcreteSubject()

    observer_left = ConcreteObserverLeft()
    ob.subject.attach(observer_left)

    observer_right = ConcreteObserverRight()
    ob.subject.attach(observer_right)

    observer_top = ConcreteObserverTop()
    ob.subject.attach(observer_top)

    observer_bottom = ConcreteObserverBottom()
    ob.subject.attach(observer_bottom)


threadtest = t.Thread(target=obtest)

threadtest.start()

root.mainloop()
