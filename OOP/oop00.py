#Inheritance
from cgitb import reset
from enum import Enum
from pickle import TRUE

from sqlalchemy import true

class SecurityDevice:
    def __init__(self,active):
        print("init for SecurityDevice")
        self.acitve=active

    #def reset(self):
     #   self.acitve=True

    def reset(self):
        print ("Resetting")
        self.acitve=true

#class Sensor: is different class 
#class Sensor(SecurityDevice) in same class 
class Sensor(SecurityDevice):
    
    #def __init__(self,active, silent,distance):
    def __init__(self,silent,distance):
       # self.active=active
        self.silent=silent
        self.distance=distance

    


security_device=SecurityDevice(True)
print (security_device)
sensor=Sensor(False,30)
print(sensor)
sensor.reset()
print(sensor.acitve)



#check the type of sensor
print(type(sensor))

print(isinstance(sensor,Sensor))
print(isinstance(security_device,Sensor))
print(issubclass(Sensor,SecurityDevice))