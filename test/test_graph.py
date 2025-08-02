from unittest import TestCase
import unittest
import mock

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)

from src.graph import Graph


class GraphSetupMethodsTestCase(TestCase):
    
    def setUp(self):
        self.graph = Graph()
    
    def tearDown(self):
        del self.graph
    
    def test_add_node(self):
        self.graph.add_node('a')
        graph = self.graph._Graph__graph
        expected_graph = {'a': []}
        self.assertEqual(graph, expected_graph)
    
    def test_add_nodes(self):
        self.graph.add_node('a')
        self.graph.add_node('b')
        self.graph.add_node('c')
        graph = self.graph._Graph__graph
        expected_graph = {'a': [], 'b': [], 'c' :[]}
        self.assertEqual(graph, expected_graph)
    
    def test_add_edge(self):
        self.graph._Graph__graph = {'a': [], 'b': [], 'c' :[]}
        self.graph.add_edge(source_node_name='a', destination_node_name='b', edge_distance=3)
        graph = self.graph._Graph__graph
        expected_graph = {'a': [{'node': 'b', 'distance': 3}], 'b': [], 'c' :[]}
        self.assertEqual(graph, expected_graph)
    
    def test_add_edges(self):
        self.graph._Graph__graph = {'a': [], 'b': [], 'c' :[]}
        self.graph.add_edge(source_node_name='a', destination_node_name='b', edge_distance=3)
        self.graph.add_edge(source_node_name='a', destination_node_name='c', edge_distance=7)
        self.graph.add_edge(source_node_name='b', destination_node_name='c', edge_distance=2)
        self.graph.add_edge(source_node_name='c', destination_node_name='b', edge_distance=4)
        graph = self.graph._Graph__graph
        expected_graph = {'a': [{'node': 'b', 'distance': 3}, {'node': 'c', 'distance': 7}],
                          'b': [{'node': 'c', 'distance': 2}],
                          'c': [{'node': 'b', 'distance': 4}]}
        self.assertEqual(graph, expected_graph)
    
    def test_add_repititive_edges(self):
        self.graph._Graph__graph = {'a': [], 'b': [], 'c' :[]}
        self.graph.add_edge(source_node_name='a', destination_node_name='b', edge_distance=3)
        self.graph.add_edge(source_node_name='b', destination_node_name='c', edge_distance=7)
        self.graph.add_edge(source_node_name='a', destination_node_name='b', edge_distance=2)
        self.graph.add_edge(source_node_name='a', destination_node_name='b', edge_distance=4)
        graph = self.graph._Graph__graph
        expected_graph = {'a': [{'node': 'b', 'distance': 3}, {'node': 'b', 'distance': 2}, {'node': 'b', 'distance': 4}],
                          'b': [{'node': 'c', 'distance': 7}], 'c': []}
        self.assertEqual(graph, expected_graph)
    
    def test_add_edge_with_not_existing_src_node(self):
        self.graph._Graph__graph = {'a': [], 'b': [], 'c' :[]}
        self.graph.add_edge(source_node_name='d', destination_node_name='b', edge_distance=3)
        graph = self.graph._Graph__graph
        expected_graph = {'a': [], 'b': [], 'c' :[]}
        self.assertEqual(graph, expected_graph)
        
    def test_add_edge_with_not_existing_dst_node(self):
        self.graph._Graph__graph = {'a': [], 'b': [], 'c' :[]}
        self.graph.add_edge(source_node_name='a', destination_node_name='d', edge_distance=3)
        graph = self.graph._Graph__graph
        expected_graph = {'a': [], 'b': [], 'c' :[]}
        self.assertEqual(graph, expected_graph)
    
    def test_add_edge_with_not_existing_both_of_nodes(self):
        self.graph._Graph__graph = {'a': [], 'b': [], 'c' :[]}
        self.graph.add_edge(source_node_name='i', destination_node_name='j', edge_distance=3)
        graph = self.graph._Graph__graph
        expected_graph = {'a': [], 'b': [], 'c' :[]}
        self.assertEqual(graph, expected_graph)
    
    def test_add_edge_with_zero_weight(self):
        self.graph._Graph__graph = {'a': [], 'b': [], 'c' :[]}
        self.graph.add_edge(source_node_name='a', destination_node_name='b', edge_distance=0)
        graph = self.graph._Graph__graph
        expected_graph = {'a': [], 'b': [], 'c' :[]}
        self.assertEqual(graph, expected_graph)
    
    def test_add_edge_with_negative_weight(self):
        self.graph._Graph__graph = {'a': [], 'b': [], 'c' :[]}
        self.graph.add_edge(source_node_name='a', destination_node_name='b', edge_distance=-3)
        graph = self.graph._Graph__graph
        expected_graph = {'a': [], 'b': [], 'c' :[]}
        self.assertEqual(graph, expected_graph)
    
    def test_node_not_reset_by_add_node(self):
        self.graph._Graph__graph = {'a': [{'node': 'b', 'distance': 3}], 'b': [], 'c' :[]}
        self.graph.add_node('a')
        graph = self.graph._Graph__graph
        expected_graph = {'a': [{'node': 'b', 'distance': 3}], 'b': [], 'c' :[]}
        self.assertEqual(graph, expected_graph)
    
    
class GraphQueryTestCase(TestCase):
    
    def setUp(self):
        self.graph = Graph()
        self.graph.add_node('0')
        self.graph.add_node('1')
        self.graph.add_node('2')
        self.graph.add_node('3')
        self.graph.add_edge('0', '1', 1)
        self.graph.add_edge('0', '2', 3)
        self.graph.add_edge('0', '3', 5)
        self.graph.add_edge('2', '0', 3)
        self.graph.add_edge('2', '1', 1)
        self.graph.add_edge('1', '3', 8)
    
    def tearDown(self):
        del self.graph
    
    def test_get_edges_from_a_node_empty(self):
        graph = Graph()
        graph.add_node('a')
        edges = Graph().get_edges_from_a_node('a')
        self.assertEqual(edges, [])
    
    def test_get_edges_from_a_node_full(self):
        edges = self.graph.get_edges_from_a_node('0')
        expecetd_edges = [{'node': '1', 'distance': 1},
                          {'node': '2', 'distance': 3},
                          {'node': '3', 'distance': 5}]
        self.assertEqual(edges, expecetd_edges)
    
    def test_get_edges_from_a_node_node_not_exists(self):
        edges = Graph().get_edges_from_a_node('a')
        self.assertEqual(edges, [])
    
    def test_get_graph_empty(self):
        graph = Graph().get_graph
        self.assertEqual(graph, dict({}))
    
    def test_get_graph_full(self):
        graph = self.graph.get_graph
        expected_graph = {'0': [{'node': '1', 'distance': 1}, {'node': '2', 'distance': 3}, {'node': '3', 'distance': 5}],
                          '1': [{'node': '3', 'distance': 8}],
                          '2': [{'node': '0', 'distance': 3}, {'node': '1', 'distance': 1}],
                          '3': []}
        self.assertEqual(graph, expected_graph)
    
    @mock.patch.object(Graph, '_Graph__get_unweighted_graph', return_value={'a': [], 'b': []})
    def test_get_all_pathes_emtpy(self, mocked_get_unweighted_graph):
        graph = Graph()
        graph.add_node('a')
        graph.add_node('b')
        pathes = graph.get_all_paths('a', 'b')
        self.assertEqual(pathes, [])
        mocked_get_unweighted_graph.assert_called_once()
    
    @mock.patch.object(Graph, '_Graph__get_unweighted_graph', return_value={'a': ['b'], 'b': []})
    def test_get_all_pathes_one_path(self, mocked_get_unweighted_graph):
        graph = Graph()
        graph.add_node('a')
        graph.add_node('b')
        graph.add_edge('a', 'b', 5)
        pathes = graph.get_all_paths('a', 'b')
        self.assertEqual(pathes, [{'distance': 5, 'path': ['a', 'b']}])
        mocked_get_unweighted_graph.assert_called_once()
    
    @mock.patch.object(Graph, '_Graph__get_unweighted_graph', return_value={'a': ['b', 'c'], 'b': ['c'], 'c':[]})
    def test_get_all_pathes_multiple_pathes(self, mocked_get_unweighted_graph):
        graph = Graph()
        graph.add_node('a')
        graph.add_node('b')
        graph.add_node('c')
        graph.add_edge('a', 'b', 5)
        graph.add_edge('b', 'c', 7)
        graph.add_edge('a', 'c', 8)
        pathes = graph.get_all_paths('a', 'c')
        expected_pathes = [{'distance': 12, 'path': ['a', 'b', 'c']},
                           {'distance': 8, 'path': ['a', 'c']}]
        self.assertEqual(pathes, expected_pathes)
        mocked_get_unweighted_graph.assert_called_once()


class GraphPrivateFunctionsTestCase(TestCase):
    
    def __make_full_graph(self, graph_instance):
        graph_instance.add_node('0')
        graph_instance.add_node('1')
        graph_instance.add_node('2')
        graph_instance.add_node('3')
        graph_instance.add_edge('0', '1', 1)
        graph_instance.add_edge('0', '2', 3)
        graph_instance.add_edge('0', '3', 5)
        graph_instance.add_edge('2', '0', 3)
        graph_instance.add_edge('2', '1', 1)
        graph_instance.add_edge('1', '3', 8)
    
    def  test_nodes_property_empty(self):
        graph = Graph()
        nodes = graph._Graph__nodes
        self.assertEqual(nodes, [])
    
    def  test_nodes_property_full(self):
        graph = Graph()
        graph.add_node('0')
        graph.add_node('1')
        graph.add_node('2')
        graph.add_node('3')
        nodes = graph._Graph__nodes
        expected_nodes = ['0', '1', '2', '3']
        self.assertEqual(nodes, expected_nodes)
    
    def  test_get_not_weighted_graph_empty(self):
        graph = Graph()
        not_weighted_graph = graph._Graph__get_unweighted_graph()
        self.assertEqual(not_weighted_graph, dict({}))
        
    def  test_get_not_weighted_graph_full(self):
        graph = Graph()
        self.__make_full_graph(graph)
        not_weighted_graph = graph._Graph__get_unweighted_graph()
        expected_not_weighted_graph = {'0': ['1', '2', '3'],
                                       '1': ['3'], '2': ['0', '1'], '3': []}
        self.assertEqual(not_weighted_graph, expected_not_weighted_graph)
    
    @mock.patch.object(Graph, '_Graph__get_path_distance', return_value='__mocked_weight__')
    def test_get_all_paths(self, mocked_get_path_distance):
        graph = Graph()
        self.__make_full_graph(graph)
        visited = {k: False for k in graph._Graph__nodes}
        graph.graph = {'0': ['1', '2', '3'],
                       '1': ['3'], '2': ['0', '1'], '3': []}
        pathes = graph._Graph__get_all_paths('0', '3', visited)
        expected_paths = [{'distance': '__mocked_weight__', 'path': ['0', '1', '3']},
                          {'distance': '__mocked_weight__', 'path': ['0', '2', '1', '3']},
                          {'distance': '__mocked_weight__', 'path': ['0', '3']}]
        self.assertEqual(pathes, expected_paths)
    
    @mock.patch.object(Graph, '_Graph__get_path_distance', return_value='__mocked_weight__')
    def test_get_path_weight_called_correctly_in_get_all_paths(self, mocked_get_path_distance):
        graph = Graph()
        self.__make_full_graph(graph)
        visited = {k: False for k in graph._Graph__nodes}
        graph.graph = {'0': ['1', '2', '3'],
                       '1': ['3'], '2': ['0', '1'], '3': []}
        graph._Graph__get_all_paths('0', '3', visited)
        get_path_distance_calls = [call.args[0] for call in mocked_get_path_distance.call_args_list]
        self.assertTrue(['0', '1', '3'] in get_path_distance_calls)
        self.assertTrue(['0', '2', '1', '3'] in get_path_distance_calls)
        self.assertTrue(['0', '3'] in get_path_distance_calls)
    
    def test_get_path_distance(self):
        graph = Graph()
        self.__make_full_graph(graph)
        path_distance = graph._Graph__get_path_distance(['0', '1', '3'])
        expected_path_distance = 1 + 8
        self.assertEqual(path_distance, expected_path_distance)


if __name__=='__main__':
    unittest.main()
