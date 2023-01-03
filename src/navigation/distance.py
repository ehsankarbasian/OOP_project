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
        distance = EucildeanDistanceCalculator().calculate_distance(location_1, location_2)
        return distance


class OnRideDistanceCalculator(DistanceCalculatorInterface):
    
    def calculate_distance(self, location_1, location_2):
        iterator = BFSIterator()
        
        graph = location_1
        
        distance = 0
        destination_found = False
        while not destination_found:
            graph, location_2_found = iterator.iterate_next_step(graph, location_2)
            distance += 1
            destination_found = location_2_found
        
        return distance


class EucildeanDistanceCalculator:
    
    def calculate_distance(self, location_1, locaton_2):
        return 2


class BFSIterator:
    
    def iterate_next_step(self, graph, destination):
        return graph, True
