from DTO import ForceSensorDTO

class ForceConsumer:
    def run(work,finished):
        dto = ForceSensorDTO
        while True:
            if not work.empty():
                dto = work.get()
                print('Consuming values')
                print(dto.bottom)
                
            else:
                q = finished.get()
                if q == True:
                    break
            print('finished')
