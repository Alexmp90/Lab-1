import time
from TrafficLight import *
from PedestrianLight import *
from PedestrianButton import *

""" Create instances of TrafficLight, PedestrianLight, and PedestrianButton """
trafficLight = TrafficLight()
pedestrianLight = PedestrianLight()
pedestrianButton = PedestrianButton()

while True:
    """TrafficLight cycle"""
    trafficLight.startTrafficCycle()

    """Check if the pedestrian button is pressed"""
    if pedestrianButton.isPressed():
        pedestrianButton.request()  # Request crossing

    """PedestrianLight cycle"""
    pedestrianLight.startPedestrianCycle()

    """Resume TrafficLight cycle after PedestrianLight cycle is over"""
    trafficLight.resumeTrafficCycle()