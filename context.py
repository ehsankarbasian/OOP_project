
class Context:
    
    def __init__(self, navigator, user, locations, graph):
        self.__navigator = navigator
        self.user = user
        self.locations = locations
        self.__graph = graph
    
    def add_new_map_location(self):
        pass
    
    def add_new_private_location(self):
        pass
    
    def search_location_by_name(self):
        pass
    
    def navigate(self, source, destination):
        routes = self.__navigator.navigate(self.__graph, source, destination)
        return routes
    
    def find_the_nearest_location_by_type(self):
        pass
    
    def get_location_info(self):
        pass
    
    def make_location_favourite(self):
        pass
    
    def rate_location(self):
        pass
