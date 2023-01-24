
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
    
    def __init__(self, longitude, latitude, name, location_type, phone=None, info=None):
        self.type = location_type
        self.__phone = phone
        self.__info = info
        self.__rates = []
        super().__init__(longitude, latitude, name)
    
    def rate_location(self, rate):
        if rate.user not in self.rated_users:
            self.__rates.append(rate)
    
    @property
    def rates(self):
        return self.__rates
    
    @property
    def rated_users(self):
        return [rate.user for rate in self.__rates]
    
    def __str__(self):
        return f'{self.type} {self.name}'
