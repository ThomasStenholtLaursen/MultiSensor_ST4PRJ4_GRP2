import tkinter as tk
from tkinter import messagebox
import config as settings

class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        
        self.geometry('800x480')
        self.resizable(0, 0)

        ###For fullscreen on RPI include the next line of code###
        self.attributes('-fullscreen', True)

        self.title("Settings window")

        self.right_setting = settings.RIGHTSETTING
        self.left_setting = settings.LEFTSETTING
        self.top_setting = settings.TOPSETTING
        self.bottom_setting = settings.BOTTOMSETTING
        self.light_setting = settings.LIGHTSETTING
        self.temp_setting = settings.TEMPSETTING

        self.settings_background_image = tk.PhotoImage(file='template_settingsbackground4.png')
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
                       command=self.save_settings)                                              
        self.saveButton.pack(side=tk.RIGHT, expand=True)


        self.light_label = tk.Label(self, text = self.light_setting, font=("Segoe UI",18), bg='#ffffff')
        self.light_label.place(y=125, x=503)

        self.temp_label = tk.Label(self, text = self.temp_setting, font=("Segoe UI",18), bg='#ffffff')
        self.temp_label.place(y=288, x=503)

        self.left_p_label = tk.Label(self, text = self.left_setting, font=("Segoe UI",16), bg='#ffffff')
        self.left_p_label.place(y=82, x=148)

        self.right_p_label = tk.Label(self, text = self.right_setting, font=("Segoe UI",16), bg='#ffffff')
        self.right_p_label.place(y=162, x=148)

        self.top_p_label = tk.Label(self, text = self.top_setting, font=("Segoe UI",16), bg='#ffffff')
        self.top_p_label.place(y=242, x=148)

        self.bottom_p_label = tk.Label(self, text = self.bottom_setting, font=("Segoe UI",16), bg='#ffffff')
        self.bottom_p_label.place(y=322, x=148)


        self.uparrow = tk.PhotoImage(file='uparrow.png')
        self.downarrow = tk.PhotoImage(file='downarrow.png')

        self.light_button_down = tk.Button(self, image = self.downarrow, bg = "#424242", height=60, width=45, bd='1', command=self.dec_light)
        self.light_button_down.place(y=113, x=695)
        self.light_button2 = tk.Button(self, image = self.uparrow, bg = "#424242", height=60, width=45, bd='1', command=self.inc_light)
        self.light_button2.place(y=113, x=630)

        self.temp_button_down = tk.Button(self, image = self.downarrow, bg = "#424242", height=60, width=45, bd='1', command=self.dec_temp)
        self.temp_button_down.place(y=276, x=695)
        self.temp_button2 = tk.Button(self, image = self.uparrow, bg = "#424242", height=60, width=45, bd='1', command=self.inc_temp)
        self.temp_button2.place(y=276, x=630)

        self.left_p_button_down = tk.Button(self, image = self.downarrow, bg = "#424242", height=60, width=45, bd='1', command=self.dec_p_left)
        self.left_p_button_down.place(y=69, x=320)
        self.left_p_button2 = tk.Button(self, image = self.uparrow, bg = "#424242", height=60, width=45, bd='1', command=self.inc_p_left)
        self.left_p_button2.place(y=69, x=250)

        self.right_p_button1 = tk.Button(self, image = self.downarrow, bg = "#424242", height=60, width=45, bd='1', command=self.dec_p_right)
        self.right_p_button1.place(y=149, x=320)
        self.right_p_button2 = tk.Button(self, image = self.uparrow, bg = "#424242", height=60, width=45, bd='1', command=self.inc_p_right)
        self.right_p_button2.place(y=149, x=250)

        self.top_p_button1 = tk.Button(self, image = self.downarrow, bg = "#424242", height=60, width=45, bd='1', command=self.dec_p_top)
        self.top_p_button1.place(y=229, x=320)
        self.top_p_button2 = tk.Button(self, image = self.uparrow, bg = "#424242", height=60, width=45, bd='1', command=self.inc_p_top)
        self.top_p_button2.place(y=229, x=250)

        self.bottom_p_button1 = tk.Button(self, image = self.downarrow, bg = "#424242", height=60, width=45, bd='1', command=self.dec_p_bottom)
        self.bottom_p_button1.place(y=309, x=320)
        self.bottom_p_button2 = tk.Button(self, image = self.uparrow, bg = "#424242", height=60, width=45, bd='1', command=self.inc_p_bottom)
        self.bottom_p_button2.place(y=309, x=250)

        self.information = tk.PhotoImage(file='info.png')
        self.information_button = tk.Button(self, image = self.information, bg = "#08b5b5", activebackground='#08b5b5', bd='0', command=self.guide_message)
        self.information_button.place(y=10, x=750)

    def guide_message(self):
        messagebox.showinfo(parent=self, title="Guide", message="FORCE THRESHOLD\nSet threshold-value in grams\nfor too much force applied\n\nLIGHT THRESHOLD\nSet threshold-value in a scale of 1-10\nfor how much light-polution is allowed\n\nTEMPERATURE THRESHOLD\nSet threshold-value for maximum\nallowed temperature")


    def close_confirm(self):
        if (settings.RIGHTSETTING != self.right_setting 
            or settings.LEFTSETTING != self.left_setting
            or settings.TOPSETTING != self.top_setting 
            or settings.BOTTOMSETTING != self.bottom_setting
            or settings.LIGHTSETTING != self.light_setting
            or settings.TEMPSETTING != self.temp_setting):
            answer = messagebox.askokcancel(parent=self, title='Warning!', message='Settings not saved.\nDo you want to continue?')
            if answer:
                self.destroy()
        else:
            self.destroy()

    def save_settings(self):       
         settings.RIGHTSETTING = self.right_setting
         settings.LEFTSETTING = self.left_setting
         settings.TOPSETTING = self.top_setting
         settings.BOTTOMSETTING = self.bottom_setting
         settings.LIGHTSETTING = self.light_setting
         settings.TEMPSETTING = self.temp_setting
         messagebox.showinfo(parent=self, message='Settings saved') 
         self.destroy()

    def inc_light(self):
        self.light_setting += settings.INC_L
        if self.light_setting >= 10:
            self.light_setting = 10
        self.light_label.config(text=self.light_setting)

    def dec_light(self):
        self.light_setting -= settings.DEC_L
        if self.light_setting <= 1:
            self.light_setting = 1
        self.light_label.config(text=self.light_setting)

    def inc_temp(self):
        self.temp_setting += settings.INC_T
        if self.temp_setting >= 90:
            self.temp_setting = 90
        self.temp_label.config(text=self.temp_setting)

    def dec_temp(self):
        self.temp_setting -= settings.DEC_T
        if self.temp_setting <= 10:
            self.temp_setting = 10
        self.temp_label.config(text=self.temp_setting)

    def inc_p_right(self):
        self.right_setting += settings.INC_P
        if self.right_setting >= 5000:
            self.right_setting = 5000
        self.right_p_label.config(text=self.right_setting)

    def dec_p_right(self):
        self.right_setting -= settings.DEC_P
        if self.right_setting<= 60:
            self.right_setting = 60
        self.right_p_label.config(text=self.right_setting)

    def inc_p_left(self):
        self.left_setting += settings.INC_P
        if self.left_setting >= 5000:
            self.left_setting = 5000
        self.left_p_label.config(text=self.left_setting)

    def dec_p_left(self):
        self.left_setting -= settings.DEC_P
        if self.left_setting <= 60:
            self.left_setting = 60
        self.left_p_label.config(text=self.left_setting)

    def inc_p_top(self):
        self.top_setting += settings.INC_P
        if self.top_setting >= 5000:
            self.top_setting = 5000
        self.top_p_label.config(text=self.top_setting)

    def dec_p_top(self):
        self.top_setting -= settings.DEC_P
        if self.top_setting <= 60:
            self.top_setting = 60
        self.top_p_label.config(text=self.top_setting)

    def inc_p_bottom(self):
        self.bottom_setting += settings.INC_P
        if self.bottom_setting >= 5000:
            self.bottom_setting = 5000
        self.bottom_p_label.config(text=self.bottom_setting)

    def dec_p_bottom(self):
        self.bottom_setting -= settings.DEC_P
        if self.bottom_setting <= 60:
            self.bottom_setting = 60
        self.bottom_p_label.config(text=self.bottom_setting)


