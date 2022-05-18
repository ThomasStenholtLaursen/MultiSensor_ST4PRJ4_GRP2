import tkinter as tk
from tkinter import messagebox

class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('800x480')
        self.resizable(0, 0)
        self.title("Settings window")

        self.settings_background_image = tk.PhotoImage(file='template_settingsbackground1.png')
        self.settings_background_label = tk.Label(self, image=self.settings_background_image)
        self.settings_background_label.place(relwidth=1, relheight=1)

        self.sframe = tk.Frame(self)
        self.sframe.configure(bg='#424242')
        self.sframe.place(relwidth=1, y=410, height=70)

        self.returnButton = tk.Button(self.sframe, text="Return",
                      font=("Segoe UI",20), bd='0', width=20, height=30, 
                       bg='#08b4b5', fg='#ffffff', 
                       activebackground='#077e7f', 
                       activeforeground='#ffffff',
                       command=self.close_confirm)                       
        self.returnButton.pack(side=tk.LEFT, expand=True)

        self.saveButton = tk.Button(self.sframe, text="Save",
                      font=("Segoe UI",20), bd='0', width=20, height=30, 
                       bg='#08b4b5', fg='#ffffff', 
                       activebackground='#077e7f', 
                       activeforeground='#ffffff')                                              
        self.saveButton.pack(side=tk.RIGHT, expand=True)

        self.uparrow = tk.PhotoImage(file='uparrow.png')
        self.downarrow = tk.PhotoImage(file='downarrow.png')

        self.pButton1 = tk.Button(self, image = self.downarrow, bg = "#424242", height=60, bd='1')
        self.pButton1.place(y=112, x=370)
        self.pButton2 = tk.Button(self, image = self.uparrow, bg = "#424242", height=60, bd='1')
        self.pButton2.place(y=112, x=280)

        self.tButton1 = tk.Button(self, image = self.downarrow, bg = "#424242", height=60, bd='1')
        self.tButton1.place(y=192, x=370)
        self.tButton2 = tk.Button(self, image = self.uparrow, bg = "#424242", height=60, bd='1')
        self.tButton2.place(y=192, x=280)

        self.lButton1 = tk.Button(self, image = self.downarrow, bg = "#424242", height=60, bd='1')
        self.lButton1.place(y=268, x=370)
        self.lButton2 = tk.Button(self, image = self.uparrow, bg = "#424242", height=60, bd='1')
        self.lButton2.place(y=268, x=280)

    def close_confirm(self):
        answer = messagebox.askyesno(parent=self, title='Closing settings', message='Have you saved your settings?')
        if answer:
            self.destroy()
