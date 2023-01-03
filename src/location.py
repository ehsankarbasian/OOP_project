
import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)


class GeneralLocation:
    
    def __init__(self, longitude, latitude, name):
        self.longitude = longitude
        self.latitude = latitude
        self.name = name


class PrivateLocation(GeneralLocation):
    
    def __init__(self, longitude, latitude, name, user):
        self.user = user
        super().__init__(longitude, latitude, name)
    
    def __str__(self):
        return f'{self.name}'


class MapLocation(GeneralLocation):
    
    def __init__(self, longitude, latitude, name, location_type, rates, phone=None, info=None):
        self.type = location_type
        self.rates = rates
        self.__phone = phone
        self.__info = info
        super().__init__(longitude, latitude, name)
    
    def __str__(self):
        return f'{self.type} {self.name}'
