
import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)


class User:
    
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.favourite_locations = []
        self.__spicial_permissions = ['_MapLocation__phone']
    
    @property
    def special_permissions(self):
        return self.__spicial_permissions
