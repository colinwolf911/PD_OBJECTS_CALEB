#objects
#installed info 
from enum import Enum
class Position:
    def __init__(self,pan,tilt,zoom):
        self.pan= pan
        self.tilt=tilt
        self.zoom=zoom
    
    def log(self):
        print(str(self.pan),str(self.tilt),str(self.zoom))

p=Position(20,21,22)
p.log()




##
class Camera:
    def __init__(self,serial_number, position,camera_type):
        self.serial_number=serial_number
        self.position=position
        self.camera_type =camera_type

        #log
    def log(self):
        print(self.serial_number,str(self.camera_type))
        self.position.log()
    
    class cameraType(Enum):
        ptz=0
        eptz=1
        stataionary=2

    
c=Camera("xap123",Position(20,21,22),Camera.cameraType.eptz)
c.log()

