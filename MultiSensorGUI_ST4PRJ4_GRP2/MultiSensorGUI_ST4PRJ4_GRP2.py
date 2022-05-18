from MainWindow import MainWindow

#fullscreen for RPI - next line needs to be included when running with display on RPI
#root.attributes('-fullscreen', True)

    
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
