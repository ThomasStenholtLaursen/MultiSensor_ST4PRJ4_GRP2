import tkinter as tk
from tkinter import messagebox
from DTO import SettingsDTO

right_p_setting = 40
left_p_setting = 100
top_p_setting = 100
bottom_p_setting = 45
light_setting = 5
temp_setting = 50

class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        
        self.geometry('800x480')
        self.resizable(0, 0)

        #for fullscreen on RPI include the next line of code:
        #self.attributes('-fullscreen', True)

        self.title("Settings window")

        self.saveSettingsInDTO()

        self.settings_background_image = tk.PhotoImage(file='template_settingsbackground3.png')
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
                       activeforeground='#ffffff',
                       command=self.saveSettingsInDTO)                                              
        self.saveButton.pack(side=tk.RIGHT, expand=True)

        self.light_label = tk.Label(self, text = light_setting, font=("Segoe UI",18), bg='#ffffff', justify="center")
        self.light_label.place(y=125, x=503)

        self.temp_label = tk.Label(self, text = temp_setting, font=("Segoe UI",18), bg='#ffffff')
        self.temp_label.place(y=288, x=503)

        self.right_p_label = tk.Label(self, text = right_p_setting, font=("Segoe UI",18), bg='#ffffff')
        self.right_p_label.place(y=80, x=152)

        self.left_p_label = tk.Label(self, text = left_p_setting, font=("Segoe UI",18), bg='#ffffff')
        self.left_p_label.place(y=160, x=152)

        self.top_p_label = tk.Label(self, text = top_p_setting, font=("Segoe UI",18), bg='#ffffff')
        self.top_p_label.place(y=240, x=152)

        self.bottom_p_label = tk.Label(self, text = bottom_p_setting, font=("Segoe UI",18), bg='#ffffff')
        self.bottom_p_label.place(y=320, x=152)

        self.uparrow = tk.PhotoImage(file='uparrow.png')
        self.downarrow = tk.PhotoImage(file='downarrow.png')

        self.light_button1 = tk.Button(self, image = self.downarrow, bg = "#424242", height=60, width=45, bd='1', command=self.dec_light)
        self.light_button1.place(y=113, x=695)
        self.light_button2 = tk.Button(self, image = self.uparrow, bg = "#424242", height=60, width=45, bd='1', command=self.inc_light)
        self.light_button2.place(y=113, x=630)

        self.temp_button1 = tk.Button(self, image = self.downarrow, bg = "#424242", height=60, width=45, bd='1', command=self.dec_temp)
        self.temp_button1.place(y=276, x=695)
        self.temp_button2 = tk.Button(self, image = self.uparrow, bg = "#424242", height=60, width=45, bd='1', command=self.inc_temp)
        self.temp_button2.place(y=276, x=630)

        self.right_p_button1 = tk.Button(self, image = self.downarrow, bg = "#424242", height=60, width=45, bd='1', command=self.dec_p_right)
        self.right_p_button1.place(y=69, x=320)
        self.right_p_button2 = tk.Button(self, image = self.uparrow, bg = "#424242", height=60, width=45, bd='1', command=self.inc_p_right)
        self.right_p_button2.place(y=69, x=250)

        self.left_p_button1 = tk.Button(self, image = self.downarrow, bg = "#424242", height=60, width=45, bd='1', command=self.dec_p_left)
        self.left_p_button1.place(y=149, x=320)
        self.left_p_button2 = tk.Button(self, image = self.uparrow, bg = "#424242", height=60, width=45, bd='1', command=self.inc_p_left)
        self.left_p_button2.place(y=149, x=250)

        self.top_p_button1 = tk.Button(self, image = self.downarrow, bg = "#424242", height=60, width=45, bd='1', command=self.dec_p_top)
        self.top_p_button1.place(y=229, x=320)
        self.top_p_button2 = tk.Button(self, image = self.uparrow, bg = "#424242", height=60, width=45, bd='1', command=self.inc_p_top)
        self.top_p_button2.place(y=229, x=250)

        self.bottom_p_button1 = tk.Button(self, image = self.downarrow, bg = "#424242", height=60, width=45, bd='1', command=self.dec_p_bottom)
        self.bottom_p_button1.place(y=309, x=320)
        self.bottom_p_button2 = tk.Button(self, image = self.uparrow, bg = "#424242", height=60, width=45, bd='1', command=self.inc_p_bottom)
        self.bottom_p_button2.place(y=309, x=250)
        

    def close_confirm(self):
        answer = messagebox.askyesno(parent=self, title='Closing settings', message='Have you saved your settings?')
        if answer:
            self.destroy()

    def inc_light(self):
        global light_setting
        light_setting += 1
        if light_setting > 10:
            light_setting = 10
        self.light_label.config(text=light_setting)

    def dec_light(self):
        global light_setting
        light_setting -= 1
        if light_setting <= 0:
            light_setting = 1
        self.light_label.config(text=light_setting)

    def inc_temp(self):
        global temp_setting
        temp_setting += 2
        if temp_setting > 90:
            temp_setting = 90
        self.temp_label.config(text=temp_setting)

    def dec_temp(self):
        global temp_setting
        temp_setting -= 2
        if temp_setting < 10:
            temp_setting = 10
        self.temp_label.config(text=temp_setting)

    def inc_p_right(self):
        global right_p_setting
        right_p_setting += 5
        if right_p_setting > 5000:
            right_p_setting = 5000
        self.right_p_label.config(text=right_p_setting)

    def dec_p_right(self):
        global right_p_setting
        right_p_setting -= 5
        if right_p_setting <= 40:
            right_p_setting = 40
        self.right_p_label.config(text=right_p_setting)

    def inc_p_left(self):
        global left_p_setting
        left_p_setting += 5
        if left_p_setting > 5000:
            left_p_setting = 5000
        self.left_p_label.config(text=left_p_setting)

    def dec_p_left(self):
        global left_p_setting
        left_p_setting -= 5
        if left_p_setting <= 40:
            left_p_setting = 40
        self.left_p_label.config(text=left_p_setting)

    def inc_p_top(self):
        global top_p_setting
        top_p_setting += 5
        if top_p_setting > 5000:
            top_p_setting = 5000
        self.top_p_label.config(text=top_p_setting)

    def dec_p_top(self):
        global top_p_setting
        top_p_setting -= 5
        if top_p_setting <= 40:
            top_p_setting = 40
        self.top_p_label.config(text=top_p_setting)

    def inc_p_bottom(self):
        global bottom_p_setting
        bottom_p_setting += 5
        if bottom_p_setting > 5000:
            bottom_p_setting = 5000
        self.bottom_p_label.config(text=bottom_p_setting)

    def dec_p_bottom(self):
        global bottom_p_setting
        bottom_p_setting -= 5
        if bottom_p_setting <= 40:
            bottom_p_setting = 40
        self.bottom_p_label.config(text=bottom_p_setting)

    def saveSettingsInDTO(self):
        setting = SettingsDTO(right_p_setting,left_p_setting,top_p_setting,bottom_p_setting,light_setting,temp_setting)
        print("saved in settingsdto: " + str(setting))

