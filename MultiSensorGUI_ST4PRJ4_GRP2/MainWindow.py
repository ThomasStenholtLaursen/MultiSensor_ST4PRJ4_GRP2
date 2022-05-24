import tkinter as tk
from tkinter import messagebox
from SettingsWindow import SettingsWindow
from AbstractSubjectObserver import Observer, Subject
import config as settings

GREEN = '#00ff30'
YELLOW ='#ffde00'
RED = '#ff2323'


class MainWindow(tk.Tk, Observer):
    def __init__(self):
        super().__init__()

        self.geometry('800x480')
        self.resizable(0, 0)
        self.title("Main window")

        self.background_image = tk.PhotoImage(file='template_bg4.png')
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.left = tk.Canvas(self, width=10, height =10, bg = GREEN, bd=10)
        self.left.place(y=180,x=342)
        self.right = tk.Canvas(self, width=10, height =10, bg = GREEN, bd=10)
        self.right.place(y=180,x=683)
        self.top = tk.Canvas(self, width=10, height =10, bg = GREEN, bd=10)
        self.top.place(y=13,x=513)
        self.bottom = tk.Canvas(self, width=10, height =10, bg = GREEN, bd=10)
        self.bottom.place(y=346,x=513)
        
        self.light = tk.Canvas(self, width=10, height =10, bg ='#00ff30', bd=10)
        self.light.place(y=125,x=132)

        self.temp = tk.Label(self, font=("Segoe UI", 20), bg='#424242',fg=RED)
        self.temp.place(y=300, x=130)

        self.information = tk.PhotoImage(file='info.png')
        self.information_button = tk.Button(self, image = self.information, bg = "#08b5b5", activebackground='#08b5b5', bd='0', command=self.information_message)
        self.information_button.place(y=10, x=750)

        self.frame = tk.Frame(self)
        self.frame.configure(bg='#424242')
        self.frame.place(relwidth=1, y=410, height=70)

        self.exitButton = tk.Button(self.frame, text="Exit",
                      font=("Segoe UI",20), bd='0', width=20, height=30, 
                       bg='#08b4b5', fg='#ffffff', 
                       activebackground='#077e7f', 
                       activeforeground='#ffffff',
                       command=self.close_confirm)
        self.exitButton.pack(side=tk.LEFT, expand=True)

        self.settingsButton = tk.Button(self.frame, text="Settings",
                      font=("Segoe UI",20), bd='0', width=20, height=30, 
                       bg='#08b4b5', fg='#ffffff', 
                       activebackground='#077e7f', 
                       activeforeground='#ffffff',
                       command=self.open_window)
        self.settingsButton.pack(side=tk.RIGHT, expand=True)        

    def open_window(self):
        settings = SettingsWindow(self)
        settings.grab_set()

    def close_confirm(self):
        answer = messagebox.askokcancel(title='Closing Program', message='Are you sure that you want to quit?')
        if answer:
            self.destroy()

    def information_message(self):
        messagebox.showinfo("Information", "LIGHT DETECTION\nRed color = too much light polution\nGreen color = light polution OK\n\nTEMPERATURE DETECTION\nRed color = temperature too high\nGreen color = temperature OK\n\nFORCE DETECTION\nRed color = too much force (above threshold)\nYellow color = not enough force\nGreen color = adequate force")


    def update_force(self, subject: Subject) -> None:
        if subject.leftreadingprop < settings.NOREG_LEFT:
            self.left.configure(bg=YELLOW)
        elif subject.leftreadingprop > settings.LEFTSETTING:
            self.left.configure(bg=RED)
        else:
            self.left.configure(bg=GREEN)

        if subject.rightreadingprop < settings.NOREG_RIGHT:
            self.right.configure(bg=YELLOW)
        elif subject.rightreadingprop > settings.RIGHTSETTING:
            self.right.configure(bg=RED)
        else:
            self.right.configure(bg=GREEN)

        if subject.topreadingprop < settings.NOREG_TOP:
            self.top.configure(bg=YELLOW)
        elif subject.topreadingprop > settings.TOPSETTING:
            self.top.configure(bg=RED)
        else:
            self.top.configure(bg=GREEN)

        if subject.bottomreadingprop < settings.NOREG_BOTTOM:
            self.bottom.configure(bg=YELLOW)
        elif subject.bottomreadingprop > settings.BOTTOMSETTING:
            self.bottom.configure(bg=RED)
        else:
            self.bottom.configure(bg=GREEN)

    def update_lt(self, subject: Subject) -> None:

        if subject.lightreadingprop > settings.LIGHTSETTING:
            self.light.configure(bg=RED)
        else:
            self.light.configure(bg=GREEN)
       
        self.temp.configure(text=str(subject.tempreadingprop) + ' \N{DEGREE SIGN}C')
        if subject.tempreadingprop > settings.TEMPSETTING:
            self.temp.configure(fg=RED)
        else:
            self.temp.configure(fg=GREEN)
