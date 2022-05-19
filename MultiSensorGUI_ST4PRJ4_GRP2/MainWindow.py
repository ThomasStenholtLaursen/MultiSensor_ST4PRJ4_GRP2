import tkinter as tk
from tkinter import messagebox
from SettingsWindow import SettingsWindow

GREEN = '#00ff30'
RED = '#ff2323'


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('800x480')
        self.resizable(0, 0)
        self.title("Main window")

        self.background_image = tk.PhotoImage(file='template_bg3.png')
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

        self.temp_label = tk.Label(self, font=("Segoe UI", 20), text="70", bg='#777777',fg='red')
        self.temp_label.place(y=300, x=130)

    def open_window(self):
        settings = SettingsWindow(self)
        settings.grab_set()

    def close_confirm(self):
        answer = messagebox.askokcancel(title='Closing Program', message='Are you sure that you want to quit?')
        if answer:
            self.destroy()   

    def redRight(self):
        self.right.configure(bg=RED)

    def greenRight(self):
        self.right.configure(bg=GREEN)

    def redLeft(self):
        self.left.configure(bg=RED)

    def greenLeft(self):
        self.left.configure(bg=GREEN)

    def redTop(self):
        self.top.configure(bg=RED)

    def greenTop(self):
        self.top.configure(bg=GREEN)

    def redBottom(self):
        self.bottom.configure(bg=RED)

    def greenBottom(self):
        self.bottom.configure(bg=GREEN)
