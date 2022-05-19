from MainWindow import MainWindow
from DataHandling import ForceConsumer as Consumer
from DataInput import ForceProducer as Producer
from queue import Queue
import threading
import multiprocessing
from threading import Thread

#fullscreen for RPI - next line needs to be included when running with display on RPI



if __name__ == "__main__":
    max = 10
    work = Queue()
    finished = Queue()

    p = Producer()
    c = Consumer()
    

    producer = Thread(target=p.run,args=[work,finished,max])
    consumer = Thread(target=c.run,args=[work,finished])
    producer.daemon = True
    consumer.daemon = True

    def runSensorThreads():
        producer.start()
        consumer.start()
    

    app = MainWindow()
    #app.attributes('-fullscreen', True)

    app.after(0, runSensorThreads)
    
    
    app.mainloop()

    
    
