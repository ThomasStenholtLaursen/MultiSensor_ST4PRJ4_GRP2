from tkinter import *
import tkinter as tk

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

#Creating frame for buttons and creating buttons
#region
frame = tk.Frame(root)
frame.configure(bg='#424242')
frame.place(relwidth=1, y=410, height=70)


button_one = tk.Button(frame, text="Save",
                      font=("Segoe UI",20), bd='0', width=20, height=30, 
                       bg='#08b4b5', fg='#ffffff', 
                       activebackground='#077e7f', 
                       activeforeground='#ffffff')
button_one.pack(side=tk.LEFT, expand=True)


button_two = tk.Button(frame, text="Settings",
                      font=("Segoe UI",20), bd='0', width=20, height=30, 
                       bg='#08b4b5', fg='#ffffff', 
                       activebackground='#077e7f', 
                       activeforeground='#ffffff')
button_two.pack(side=tk.RIGHT, expand=True)
#endregion


temp_label = tk.Label(root, font=("Segoe UI", 20), text="70", bg='black',fg='red')
temp_label.place(y=300, x=130)

light_label = tk.Label(root, font=("Segoe UI",20), text="GOOD",bg='black',fg='#00ff30')
light_label.place(y=120, x=110)

root.mainloop()
