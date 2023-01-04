from abc import ABC, abstractmethod

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)


class DistanceCalculatorInterface(ABC):
    
    @abstractmethod
    def calculate_distance(self, graph, location_1, location_2):
        pass


class OnWalkDistanceCalculator(DistanceCalculatorInterface):
    
    def calculate_distance(self, graph, location_1, location_2):
        a2 = (location_1.longitude - location_2.longitude) ** 2
        b2 = (location_1.latitude - location_2.latitude) ** 2
        c2 = a2 + b2
        distance = c2 ** (1/2)
        return distance


class OnRideDistanceCalculator(DistanceCalculatorInterface):
    
    def calculate_distance(self, graph, location_1, location_2):
        pathes = graph.get_all_paths(location_1, location_2)
        min_distance = None
        for path in pathes:
            weight = path['weight']
            if min_distance is None or weight < min_distance:
                min_distance = weight
        
        return min_distance
