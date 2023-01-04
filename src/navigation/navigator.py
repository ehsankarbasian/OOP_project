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
    
    def __init__(self):
        self.__distanceCalculator = OnRideDistanceCalculator()
    
    def navigate(self, graph, source, destination):
        pathes = graph.get_all_paths(source, destination)
        result = list()
        for path in pathes:
            weight = path['weight']
            route = path['path']
            result.append({'route': route, 'cost': weight})
        
        min_distance = self.__distanceCalculator.calculate_distance(graph, source, destination)
        # TODO: sort result by distance or use only min_distance
        return result


class OnWalkNavigator(NavigatorInterface):
    
    def __init__(self):
        self.__distanceCalculator = OnWalkDistanceCalculator()
    
    def navigate(self, graph, source, destination):
        distance = self.__distanceCalculator.calculate_distance(source, destination)
        return [{'route': [source, destination], 'cost': distance}]
