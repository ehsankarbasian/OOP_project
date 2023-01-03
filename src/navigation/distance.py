from abc import ABC, abstractmethod

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)


class DistanceCalculatorInterface(ABC):
    pass


class OnWalkDistanceCalculator(DistanceCalculatorInterface):
    pass


class OnRideDistanceCalculator(DistanceCalculatorInterface):
    pass


class EucildeanDistanceCalculator:
    pass


class BFSIterator:
    pass
