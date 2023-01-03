
import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)


class User:
    
    def __init__(self, username, password, locations):
        self.username = username
        self.__password = password
        self.favourite_locations = locations
