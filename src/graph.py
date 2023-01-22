
import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)


class Graph:
    # TODO(refactor): change all weights to distance
    
    def __init__(self):
        self.__graph = dict()
        self.__paths = list()
    
    def add_node(self, node_name):
        self.__graph[node_name] = list()
    
    def add_edge(self, source_node_name, destination_node_name, edge_weight):
        self.__graph[source_node_name].append({'node': destination_node_name, 'distance': edge_weight})
    
    def get_edges_from_a_node(self, destination_node_name):
        return self.__graph.get(destination_node_name, list())
    
    @property
    def get_graph(self):
        return self.__graph
    
    def get_all_paths(self, s, d):
        self.graph = self.__get_not_weigted_graph()
        visited = {k: False for k in list(self.graph.keys())}
        self.__paths = list()
        path = []
        self.__print_all_paths_util(s, d, visited, path)
        pathes = self.__save_path_weights()
        return pathes
    
    def __get_not_weigted_graph(self):
        result = dict()
        for u, v in self.__graph.items():
            if u not in list(result.keys()):
                result[u] = list()
            
            for e in v:
                e = e['node']
                result[u].append(e)
        
        return result
    
    def __print_all_paths_util(self, u, d, visited, path):
        visited[u]= True
        path.append(u)
        if u == d:
            self.__paths.append(path.copy())
        else:
            for i in self.graph[u]:
                if visited[i]== False:
                    self.__print_all_paths_util(i, d, visited, path)
        path.pop()
        visited[u]= False
    
    def __save_path_weights(self):
        weighted_pathes = list()
        for path in self.__paths:
            weight = self.__get_path_weight(path)
            weighted_pathes.append({'distance': weight, 'path': path})
        return weighted_pathes
    
    def __get_path_weight(self, path):
        path_weight = 0
        previous_node = path[0]
        for node in path[1:]:
            edges = self.__graph[previous_node]
            for e in edges:
                if e['node'] == node:
                    weight = e['distance']
                    path_weight += weight
            previous_node = node
        return path_weight


# g = Graph()
# g.add_node('0')
# g.add_node('1')
# g.add_node('2')
# g.add_node('3')
# g.add_edge('0', '1', 1)
# g.add_edge('0', '2', 3)
# g.add_edge('0', '3', 5)
# g.add_edge('2', '0', 3)
# g.add_edge('2', '1', 1)
# g.add_edge('1', '3', 8)
# print(g.get_all_paths('2', '3'))
