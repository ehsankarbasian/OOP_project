from abc import ABC, abstractmethod

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)

from src.navigation.distance import OnWalkDistanceCalculator, OnRideDistanceCalculator


class NavigatorInterface(ABC):
    pass


class OnRideNavigator(NavigatorInterface):
    pass


class OnWalkNavigator(NavigatorInterface):
    pass
