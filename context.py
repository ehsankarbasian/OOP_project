from src.rate import Rate
from src.location import PrivateLocation
from src.location import MapLocation, PrivateLocation


class Context:
    
    def __init__(self, navigator, user, locations, graph):
        self.__navigator = navigator
        self.user = user
        self.locations = locations
        self.__graph = graph
    
    def add_new_location(self, location):
        self.locations.append(location)
    
    def add_new_private_location(self, longitude, latitude, name):
        privateLocation = PrivateLocation(longitude, latitude, name, user=self.user)
        self.add_new_location(privateLocation)
    
    def search_location_by_name(self, search_string):
        results = list()
        for location in self.locations:
            if self.__location_search_matched(location, search_string):
                results.append(location)
        return results
    
    def navigate(self, source, destination):
        routes = self.__navigator.navigate(self.__graph, source, destination)
        return routes
    
    def find_the_nearest_location_by_type(self, longitude, latitude, location_type):
        locations = self.__filter_locations_by_type(location_type)
        distances = [((location.longitude-longitude)**2+(location.latitude-latitude)**2)**(1/2) for location in locations]
        nearest_location_index = distances.index(min(distances))
        return locations[nearest_location_index]
    
    def get_location_info(self, location):
        if isinstance(location, MapLocation):
            not_allowed_attrs = [attr for attr in dir(location) if attr.startswith('_') and attr not in self.user.special_permissions]
            location_info = location.__dict__
            for not_allowed_attr in not_allowed_attrs:
                try: location_info.__delitem__(not_allowed_attr)
                except: pass
            return location_info
        elif isinstance(location, PrivateLocation):
            the_same_user = bool(location.__getattribute__('user') == self.user)
            if the_same_user:
                return location.__dict__
        return dict({})
    
    def make_location_favourite(self, location):
        is_map_location = isinstance(location, MapLocation)
        is_user_private_location = isinstance(location, PrivateLocation)
        if is_user_private_location:
            is_user_private_location = bool(location.user == self.user)
        allowed_to_add = is_map_location or is_user_private_location
        if allowed_to_add:
            self.user.favourite_locations.append(location)
        
    
    def rate_location(self, comment, score, location):
        if isinstance(location, MapLocation):
            rate = Rate(comment, score, self.user)
            location.rate_location(rate)
        
    
    @staticmethod
    def __location_search_matched(location, search_string):
        matched = search_string.lower() in location.name.lower()
        return matched
    
    def __filter_locations_by_type(self, _type):
        result = list()
        for location in self.__map_locations:
            if location.type == _type:
                result.append(location)
        return result
    
    @property
    def __map_locations(self):
        return [location for location in self.locations if isinstance(location, MapLocation)]
