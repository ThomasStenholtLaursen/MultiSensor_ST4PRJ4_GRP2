from tkinter import *
import tkinter as tk


root = tk.Tk()

HEIGHT = 480
WIDTH = 800
root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)

background_image = tk.PhotoImage(file='template_bg2.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


frame = tk.Frame(root)
frame.configure(bg='#424242')
frame.place(relwidth=1, y=425, height=55)


button_one = tk.Button(frame, text="Save",
                      font=20, bd='0', width=20, height=30, 
                       bg='#08b4b5', fg='#ffffff', 
                       activebackground='#077e7f', 
                       activeforeground='#ffffff')
button_one.pack(side=tk.LEFT, expand=True)


button_two = tk.Button(frame, text="Settings",
                      font=20, bd='0', width=20, height=30, 
                       bg='#08b4b5', fg='#ffffff', 
                       activebackground='#077e7f', 
                       activeforeground='#ffffff')
button_two.pack(side=tk.RIGHT, expand=True)


root.mainloop()
