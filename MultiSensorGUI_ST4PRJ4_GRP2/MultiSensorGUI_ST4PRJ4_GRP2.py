from tkinter import *
import tkinter as tk

def changecolor1():
    left.configure(bg='red')
    right.configure(bg='red')
    top.configure(bg='red')
    bottom.configure(bg='red')

def changecolor2():
    left.configure(bg='green')
    right.configure(bg='green')
    top.configure(bg='green')
    bottom.configure(bg='green')

root = tk.Tk()

#Locking window to match resolution of touch display
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

left = tk.Canvas(root, width=10, height =10, bg ='green', bd=10)
left.place(y=180,x=342)
right = tk.Canvas(root, width=10, height =10, bg ='green', bd=10)
right.place(y=180,x=683)
top = tk.Canvas(root, width=10, height =10, bg ='green', bd=10)
top.place(y=13,x=513)
bottom = tk.Canvas(root, width=10, height =10, bg ='green', bd=10)
bottom.place(y=346,x=513)

#Creating frame for buttons and creating buttons
#region
frame = tk.Frame(root)
frame.configure(bg='#424242')
frame.place(relwidth=1, y=410, height=70)


button_one = tk.Button(frame, text="Save",
                      font=("Segoe UI",20), bd='0', width=20, height=30, 
                       bg='#08b4b5', fg='#ffffff', 
                       activebackground='#077e7f', 
                       activeforeground='#ffffff',
                       command=changecolor1)
button_one.pack(side=tk.LEFT, expand=True)


button_two = tk.Button(frame, text="Settings",
                      font=("Segoe UI",20), bd='0', width=20, height=30, 
                       bg='#08b4b5', fg='#ffffff', 
                       activebackground='#077e7f', 
                       activeforeground='#ffffff',
                       command=changecolor2)
button_two.pack(side=tk.RIGHT, expand=True)
#endregion


temp_label = tk.Label(root, font=("Segoe UI", 20), text="70", bg='#777777',fg='red')
temp_label.place(y=300, x=130)

light_label = tk.Label(root, font=("Segoe UI",20), text="GOOD",bg='#777777',fg='#00ff30')
light_label.place(y=120, x=110)


root.mainloop()
