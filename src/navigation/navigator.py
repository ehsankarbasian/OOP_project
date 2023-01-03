from abc import ABC, abstractmethod

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)

from src.navigation.distance import OnWalkDistanceCalculator, OnRideDistanceCalculator


class NavigatorInterface(ABC):
    
    @abstractmethod
    def navigate(self, source, destination):
        pass


class OnRideNavigator(NavigatorInterface):
    
    def __init__(self):
        self.__distanceCalculator = OnRideDistanceCalculator()
    
    def navigate(self, source, destination):
        return list()


class OnWalkNavigator(NavigatorInterface):
    
    def __init__(self):
        self.__distanceCalculator = OnWalkDistanceCalculator()
    
    def navigate(self, source, destination):
        return list()
