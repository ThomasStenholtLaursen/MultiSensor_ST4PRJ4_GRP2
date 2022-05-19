from DTO import ForceSensorDTO
import time


class ForceConsumer:
    def run(work,finished):
        dto = ForceSensorDTO
        while True:
            if not work.empty():
                dto = work.get()
                print('Consuming values')
                print(dto.bottom,dto.top,dto.left)
                
            else:
                time.sleep(0.1)
        print('finished')




