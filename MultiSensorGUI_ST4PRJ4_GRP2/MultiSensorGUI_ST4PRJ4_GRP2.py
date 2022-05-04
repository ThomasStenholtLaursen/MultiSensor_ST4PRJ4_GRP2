from tkinter import *


gui = Tk()
gui.geometry("800x480")
gui.title('Humidity GUI')

bg = PhotoImage(file = "template_bg1.png")
bg_label = Label(gui, image=bg)
bg_label.place(x=0,y=0, relwidth=1, relheight=1)




gui.mainloop()
