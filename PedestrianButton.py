import machine
import utime
from Light import *
from Button import *
from TrafficLight import *
from PedestrianLight import *

class PedestrianButton:
    def __init__(self):
        """PedestrianButton constructor"""
        print("PedestrianButton: constructor")
        self._button = Button(17, "Request crossing", buttonhandler=self, lowActive=True)

    def requestCrossing(self):
        """Request crossing action"""
        trafficLight.stopTrafficCycle()  """ Stop the traffic cycle """
        pedestrianLight.startPedestrianCycle()  """ Start the pedestrian cycle """
        pedestrianLight.stopPedestrianCycle()  """ Stop the pedestrian cycle """
        trafficLight.startTrafficCycle()  """ Resume the traffic cycle """

    def __str__(self):
        return "PedestrianButton"

