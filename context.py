
class Context:
    
    def __init__(self, navigator, user, locations, graph):
        self.__navigator = navigator
        self.user = user
        self.locations = locations
        self.__graph = graph
    
    def navigate(self, source, destination):
        routes = self.__navigator.navigate(self.__graph, source, destination)
        return routes
