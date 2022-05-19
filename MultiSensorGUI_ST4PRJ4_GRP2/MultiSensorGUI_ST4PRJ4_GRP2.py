from MainWindow import MainWindow
from DataHandling import ForceConsumer as FConsumer
from DataInput import ForceProducer as FProducer
from DataInput import LightTempProducer as LTProducer
from DataHandling import LightTempConsumer as LTConsumer
from queue import Queue
import threading
import multiprocessing
from threading import Thread





if __name__ == "__main__":
    max = 10
    work = Queue()
    finished = Queue()
    ltmax = 10
    ltwork = Queue()
    ltfinished = Queue()

    forceprod = FProducer()
    forcecon = FConsumer()
    lighttempprod = LTProducer()
    lighttempcon = LTConsumer()
    

    ForceProducerThread = Thread(target=forceprod.run,args=[work,finished,max])
    ForceConsumerThread = Thread(target=forcecon.run,args=[work,finished])
    lightTempProducerThread = Thread(target=lighttempprod.run,args=[ltwork,ltfinished,ltmax])
    lightTempConsumerThread = Thread(target=lighttempcon.run,args=[ltwork,ltfinished])

    ForceProducerThread.daemon = True
    ForceConsumerThread.daemon = True
    lightTempProducerThread.daemon = True
    lightTempConsumerThread.daemon = True

    def runSensorThreads():
        ForceProducerThread.start()
        ForceConsumerThread.start()
        lightTempProducerThread.start()
        lightTempConsumerThread.start()

    

    app = MainWindow()
    #fullscreen for RPI - next line needs to be included when running with display on RPI. Also in settingswindow.
    #app.attributes('-fullscreen', True)

    app.after(0, runSensorThreads)
    
    
    app.mainloop()

    
    
