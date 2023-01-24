
import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)


class User:
    __DEFAULT_SPECIAL_PERMISSIONS = ['_MapLocation__phone']
    
    def __init__(self, username, password, spicial_permissions=__DEFAULT_SPECIAL_PERMISSIONS):
        self.__username = username
        self.__password = password
        self.__favourite_locations = []
        self.__spicial_permissions = spicial_permissions
    
    def check_password(self, password):
        return self.__password == password
    
    def add_favourite_location(self, location):
        self.__favourite_locations.append(location)
    
    @property
    def username(self):
        return self.__username
    
    @property
    def favourite_locations(self):
        return self.__favourite_locations
    
    @property
    def special_permissions(self):
        return self.__spicial_permissions
