from MainWindow import MainWindow
from DataHandling import ForceConsumer as FConsumer
from DataHandling import LightTempConsumer as LTConsumer
from DataInput import ForceProducer as FProducer
from DataInput import LightTempProducer as LTProducer
from threading import Thread
from queue import Queue
import threading
import multiprocessing


if __name__ == "__main__":
    
    app = MainWindow()
    
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


    #forcecon.attach(pressureObserver)
    forcecon.attach(app)
    #lighttempcon.attach(templightObserver)
    lighttempcon.attach(app)

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

    #for fullscreen on RPI include the next line of code:
    #app.attributes('-fullscreen', True)

    app.after(0, runSensorThreads)
    
    app.mainloop()

    
    
