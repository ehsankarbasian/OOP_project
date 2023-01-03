
import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)


class Route:
    
    def __init__(self, route):
        self.route = route
