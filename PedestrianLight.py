import machine
from Light import *
from TrafficLight import *
import utime

class PedestrianLight(Light):
    """ PedestrianLight class """
    
    def __init__(self):
        print("PedestrianLight: constructor")
        self._greenLED = Light(5, "Pedestrian Green Light")
        self._yellowLED = Light(6, "Pedestrian Yellow Light")
        self._redLED = Light(7, "Pedestrian Red Light")
        self._cycle_running = False

    def startPedestrianCycle(self):
        """ Start the pedestrian light cycle """
        self._cycle_running = True
        self._greenLED.on()
        time.sleep(5)
        self._greenLED.off()

        self._yellowLED.on()
        time.sleep(2)
        self._yellowLED.off()

        self._redLED.on()
        time.sleep(5)
        self._redLED.off()

        if self._cycle_running:
            self.startPedestrianCycle()

    def stopPedestrianCycle(self):
        """ Stop the pedestrian light cycle """
        self._cycle_running = False  

    def __str__(self):
        """ String representation of the PedestrianLight instance """
        return "PedestrianLight"
