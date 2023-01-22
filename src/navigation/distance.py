from abc import ABC, abstractmethod

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)


class DistanceCalculatorInterface(ABC):
    
    @abstractmethod
    def calculate_distances(self, graph, location_1, location_2):
        pass


class OnWalkDistanceCalculator(DistanceCalculatorInterface):
    
    def calculate_distances(self, graph, location_1, location_2):
        distance = self.__calculate_pythagoras_distance(location_1, location_2)
        return [{'distance': distance, 'path': [location_1.name, location_2.name]}]
    
    @staticmethod
    def __calculate_pythagoras_distance(location_src, location_dst):
        a2 = (location_src.longitude - location_dst.longitude) ** 2
        b2 = (location_src.latitude - location_dst.latitude) ** 2
        c2 = a2 + b2
        pythagoras_distance = c2 ** (1/2)
        return pythagoras_distance


class OnRideDistanceCalculator(DistanceCalculatorInterface):
    
    def calculate_distances(self, graph, location_1, location_2):
        pathes = graph.get_all_paths(location_1.name, location_2.name)
        sorted_pathes = self.__sort_pathes_by_distance(pathes)
        return sorted_pathes
    
    @staticmethod
    def __sort_pathes_by_distance(pathes):
        return sorted(pathes, key=lambda x: x['distance'])
