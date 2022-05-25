from MainWindow import MainWindow
from DataHandling import ForceConsumer as FConsumer
from DataHandling import LightTempConsumer as LTConsumer
from DataInput import ForceProducer as FProducer
from DataInput import LightTempProducer as LTProducer
from threading import Thread
from queue import LifoQueue
import threading
import multiprocessing

def main():

    app = MainWindow()
    
    force_queue = LifoQueue()    
    lighttemp_queue = LifoQueue()    

    forceprod = FProducer()
    forcecon = FConsumer()
    lighttempprod = LTProducer()
    lighttempcon = LTConsumer()

    forcecon.attach(app)
    lighttempcon.attach(app)

    ForceProducerThread = Thread(target=forceprod.run,args=[force_queue])
    ForceConsumerThread = Thread(target=forcecon.run,args=[force_queue])
    lightTempProducerThread = Thread(target=lighttempprod.run,args=[lighttemp_queue])
    lightTempConsumerThread = Thread(target=lighttempcon.run,args=[lighttemp_queue])
    #Making threads backgroundthreads
    ForceProducerThread.daemon = True
    ForceConsumerThread.daemon = True
    lightTempProducerThread.daemon = True
    lightTempConsumerThread.daemon = True

    def runSensorThreads():
        ForceProducerThread.start()
        ForceConsumerThread.start()
        lightTempProducerThread.start()
        lightTempConsumerThread.start()

    ###For fullscreen on RPI include the next line of code###
    app.attributes('-fullscreen', True)
    
    #after 0 seconds, start the background threads:
    app.after(0, runSensorThreads)
    
    app.mainloop()

    lighttempcon.detach(app)
    forcecon.detach(app)


if __name__ == "__main__":
    
    main()
    
