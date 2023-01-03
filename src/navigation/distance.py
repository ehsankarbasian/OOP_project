from abc import ABC, abstractmethod

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)


class DistanceCalculatorInterface(ABC):
    
    @abstractmethod
    def calculate_distance(self, location_1, location_2):
        pass


class OnWalkDistanceCalculator(DistanceCalculatorInterface):
    
    def calculate_distance(self, location_1, location_2):
        pass


class OnRideDistanceCalculator(DistanceCalculatorInterface):
    
    def calculate_distance(self, location_1, location_2):
        pass


class EucildeanDistanceCalculator:
    
    def calculate_distance(self, location_1, locaton_2):
        pass


class BFSIterator:
    
    def iterate_next_step(self, graph):
        pass
