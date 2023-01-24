
import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)


class GeneralLocation:
    
    def __init__(self, longitude, latitude, name):
        self.__longitude = longitude
        self.__latitude = latitude
        self.__name = name
    
    @property
    def longitude(self):
        return self.__longitude
    
    @property
    def latitude(self):
        return self.__latitude
    
    @property
    def name(self):
        return self.__name


class MapLocation(GeneralLocation):
    
    def __init__(self, longitude, latitude, name, location_type, phone=None, info=None):
        self.__type = location_type
        self.__phone = phone
        self.__info = info
        self.__rates = []
        super().__init__(longitude, latitude, name)
    
    def rate_location(self, rate):
        if rate.user not in self.rated_users:
            self.__rates.append(rate)
    
    @property
    def type(self):
        return self.__type
    
    @property
    def rates(self):
        return self.__rates
    
    @property
    def rated_users(self):
        return [rate.user for rate in self.__rates]
    
    def __str__(self):
        return f'{self.type} {self.name}'


class PrivateLocation(GeneralLocation):
    
    def __init__(self, longitude, latitude, name, user):
        self.__user = user
        super().__init__(longitude, latitude, name)
    
    @property
    def user(self):
        return self.__user
    
    def __str__(self):
        return f'{self.name}'
