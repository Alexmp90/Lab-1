import machine
from Light import *
import utime

class TrafficLight(Light):
    """ TrafficLight constructor """
    def __init__(self):
        print("TrafficLight: constructor")
        self._greenLED = Light(2, "Traffic Green Light")
        self._yellowLED = Light(3, "Traffic Yellow Light")
        self._redLED = Light(4, "Traffic Red Light")
        self._pedestrianLight = PedestrianLight() 

    def startTrafficCycle(self):
        """ Implementation for starting the traffic cycle """
        while not self._pedestrianLight.isCycleRequested():
            self._greenLED.on()
            time.sleep(5)
            self._greenLED.off()

            self._yellowLED.on()
            time.sleep(2)
            self._yellowLED.off()

            self._redLED.on()
            time.sleep(5)
            self._redLED.off()

        """"" Pedestrian cycle requested, wait for it to complete """
        self._redLED.on()
        self._pedestrianLight.startPedestrianCycle()
        self._redLED.off()

        """ Restart the traffic cycle """
        self.startTrafficCycle()
    
    def __str__(self):
        return "TrafficLight"


