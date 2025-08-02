
import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)


class Graph:
    
    def __init__(self):
        self.__graph = dict()
        self.__paths = list()
    
    def add_node(self, node_name):
        if node_name not in self.__nodes:
            self.__graph[node_name] = list()
    
    def add_edge(self, source_node_name, destination_node_name, edge_distance):
        nodes_exists = bool(source_node_name in self.__nodes and destination_node_name in self.__nodes)
        if nodes_exists and edge_distance > 0:
            self.__graph[source_node_name].append({'node': destination_node_name, 'distance': edge_distance})
    
    def get_edges_from_a_node(self, destination_node_name):
        return self.__graph.get(destination_node_name, list())
    
    @property
    def get_graph(self):
        return self.__graph
    
    def get_all_paths(self, source_name, destination_name):
        self.graph = self.__get_unweighted_graph()
        visited = {k: False for k in self.__nodes}
        self.__paths = list()
        pathes = self.__get_all_paths(source_name, destination_name, visited)
        return pathes
    
    @property
    def __nodes(self):
        return list(self.__graph.keys())
    
    def __get_unweighted_graph(self):
        result = dict()
        for u, v in self.__graph.items():
            if u not in list(result.keys()):
                result[u] = list()
            
            for e in v:
                e = e['node']
                result[u].append(e)
        
        return result
    
    def __get_all_paths(self, source, destination, visited, path=[]):
        visited[source]= True
        path.append(source)
        if source == destination:
            self.__paths.append(path.copy())
        else:
            for i in self.graph[source]:
                if visited[i]== False:
                    self.__get_all_paths(i, destination, visited, path)
        path.pop()
        visited[source]= False
        
        weighted_pathes = list()
        for path in self.__paths:
            distance = self.__get_path_distance(path)
            weighted_pathes.append({'distance': distance, 'path': path})
        return weighted_pathes
    
    def __get_path_distance(self, path):
        path_distance = 0
        previous_node = path[0]
        for node in path[1:]:
            edges = self.__graph[previous_node]
            for e in edges:
                if e['node'] == node:
                    distance = e['distance']
                    path_distance += distance
            previous_node = node
        return path_distance
