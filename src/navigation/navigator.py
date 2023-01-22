from abc import ABC, abstractmethod

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)

from src.navigation.distance import OnWalkDistanceCalculator, OnRideDistanceCalculator


class NavigatorInterface(ABC):
    
    @abstractmethod
    def navigate(self, graph, source, destination):
        pass


class OnRideNavigator(NavigatorInterface):
    # TODO(refactor): change all weights to distance
    
    def __init__(self, max_path_count=3):
        self.__distanceCalculator = OnRideDistanceCalculator()
        self.__max_path_count = max_path_count
    
    def navigate(self, graph, source, destination):
        distances = self.__distanceCalculator.calculate_distances(graph, source, destination)
        all_path_count = len(distances)
        limited_distances = distances[:self.__get_normalized_max_path_count(all_path_count)]
        return limited_distances
    
    def __get_normalized_max_path_count(self, all_path_count):
        return min(self.__max_path_count, all_path_count)


class OnWalkNavigator(NavigatorInterface):
    
    def __init__(self):
        self.__distanceCalculator = OnWalkDistanceCalculator()
    
    def navigate(self, graph, source, destination):
        distances = self.__distanceCalculator.calculate_distances(graph, source, destination)
        distance = distances[0]['distance']
        return [{'distance': distance, 'path': [source, destination]}]
