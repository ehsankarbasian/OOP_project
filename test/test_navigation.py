from unittest import TestCase
import unittest
import mock

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)

from src.navigation.distance import OnWalkDistanceCalculator, OnRideDistanceCalculator
from src.navigation.navigate import OnWalkNavigator, OnRideNavigator

from mock_classes import BaseObject, MockGraph


class OnWalkDistanceCalculatorTestCase(TestCase):
    
    def setUp(self):
        self.location_1 = BaseObject()
        self.location_2 = BaseObject()
    
    def tearDown(self):
        del self.location_1
        del self.location_2
    
    @mock.patch.object(OnWalkDistanceCalculator, '_OnWalkDistanceCalculator__calculate_pythagoras_distance', return_value=15)
    def test_calculate_distances_result(self, mocked_calculate_pythagoras_distance):
        src_name = 'IUST'
        dst_name = 'AmirKabir'
        self.location_1.__setattr__('name', src_name)
        self.location_2.__setattr__('name', dst_name)
        distance = OnWalkDistanceCalculator().calculate_distances(graph=None,
                                                                  location_1=self.location_1,
                                                                  location_2=self.location_2)
        expected = [{'distance': 15, 'path': [src_name, dst_name]}]
        self.assertEqual(distance, expected)
    
    @mock.patch.object(OnWalkDistanceCalculator, '_OnWalkDistanceCalculator__calculate_pythagoras_distance', return_value=15)
    def test_calculate_distances_called_pythagoras_distance_function_correctly(self, mocked_calculate_pythagoras_distance):
        src_name = 'IUST'
        dst_name = 'AmirKabir'
        self.location_1.__setattr__('name', src_name)
        self.location_2.__setattr__('name', dst_name)
        OnWalkDistanceCalculator().calculate_distances(graph=None,
                                                       location_1=self.location_1,
                                                       location_2=self.location_2)
        mocked_calculate_pythagoras_distance.assert_called_once_with(self.location_1, self.location_2)
        
    def test_calculate_pythagoras_distance_from_coordinate_origin(self):
        self.location_1.__setattr__('longitude', 0)
        self.location_1.__setattr__('latitude', 0)
        self.location_2.__setattr__('longitude', 5)
        self.location_2.__setattr__('latitude', 12)
        
        distance = OnWalkDistanceCalculator._OnWalkDistanceCalculator__calculate_pythagoras_distance(self.location_1, self.location_2)
        self.assertEqual(distance, 13)
    
    def test_calculate_pythagoras_distance_is_removable(self):
        self.location_1.__setattr__('longitude', 0)
        self.location_1.__setattr__('latitude', 0)
        self.location_2.__setattr__('longitude', 5)
        self.location_2.__setattr__('latitude', 12)
        
        distance_1 = OnWalkDistanceCalculator._OnWalkDistanceCalculator__calculate_pythagoras_distance(self.location_1, self.location_2)
        distance_2 = OnWalkDistanceCalculator._OnWalkDistanceCalculator__calculate_pythagoras_distance(self.location_2, self.location_1)
        self.assertEqual(distance_1, distance_2)
    
    def test_calculate_pythagoras_distance_is_zero(self):
        self.location_2.__setattr__('longitude', 5)
        self.location_2.__setattr__('latitude', 12)
        
        distance = OnWalkDistanceCalculator._OnWalkDistanceCalculator__calculate_pythagoras_distance(self.location_2, self.location_2)
        self.assertEqual(distance, 0)
    
    def test_calculate_pythagoras_distance_with_negative_coordinates(self):
        self.location_1.__setattr__('longitude', -2)
        self.location_1.__setattr__('latitude', -3)
        self.location_2.__setattr__('longitude', 1)
        self.location_2.__setattr__('latitude', -7)
        
        distance = OnWalkDistanceCalculator._OnWalkDistanceCalculator__calculate_pythagoras_distance(self.location_1, self.location_2)
        self.assertEqual(distance, 5)
    
    def test_calculate_pythagoras_distance_with_decimal_coordinates(self):
        self.location_1.__setattr__('longitude', 1.5)
        self.location_1.__setattr__('latitude', 0)
        self.location_2.__setattr__('longitude', 0)
        self.location_2.__setattr__('latitude', 2)
        
        distance = OnWalkDistanceCalculator._OnWalkDistanceCalculator__calculate_pythagoras_distance(self.location_1, self.location_2)
        self.assertEqual(distance, 2.5)
    
    def test_calculate_pythagoras_distance_with_dumb_coordinates(self):
        self.location_1.__setattr__('longitude', 17)
        self.location_1.__setattr__('latitude', 3)
        self.location_2.__setattr__('longitude', 0)
        self.location_2.__setattr__('latitude', 14)
        
        distance = OnWalkDistanceCalculator._OnWalkDistanceCalculator__calculate_pythagoras_distance(self.location_1, self.location_2)
        self.assertEqual(distance, (17**2+11**2)**(1/2))


class OnRideDistanceCalculatorTestCase(TestCase):
    SRC_NAME = 'IUST'
    DST_NAME = 'AmirKabir'
    
    def setUp(self):
        self.graph = MockGraph()
        self.location_1 = BaseObject()
        self.location_2 = BaseObject()
        self.location_1.__setattr__('name', self.SRC_NAME)
        self.location_2.__setattr__('name', self.DST_NAME)
    
    def tearDown(self):
        del self.graph
        del self.location_1
        del self.location_2
    
    @mock.patch.object(OnRideDistanceCalculator, '_OnRideDistanceCalculator__sort_pathes_by_distance', return_value='mocked_sorted_output')
    def test_calculate_distances_result(self, mocked_sort):
        distances = OnRideDistanceCalculator().calculate_distances(graph=self.graph,
                                                                  location_1=self.location_1,
                                                                  location_2=self.location_2)
        self.assertEqual(distances, 'mocked_sorted_output')
    
    @mock.patch.object(OnRideDistanceCalculator, '_OnRideDistanceCalculator__sort_pathes_by_distance', return_value='mocked_sorted_output')
    def test_calculate_distances_called_graph_get_all_paths_correctly(self, mocked_sort):
        self.graph.get_all_paths = mock.MagicMock(return_value="mocked!")
        OnRideDistanceCalculator().calculate_distances(graph=self.graph,
                                                       location_1=self.location_1,
                                                       location_2=self.location_2)
        self.graph.get_all_paths.assert_called_once_with(self.SRC_NAME, self.DST_NAME)
    
    @mock.patch.object(OnRideDistanceCalculator, '_OnRideDistanceCalculator__sort_pathes_by_distance', return_value='mocked_sorted_output')
    def test_calculate_distances_called_sort_pathes_by_distance_correctly(self, mocked_sort):
        OnRideDistanceCalculator().calculate_distances(graph=self.graph,
                                                       location_1=self.location_1,
                                                       location_2=self.location_2)
        graph_pathes = self.graph.get_all_paths(self.SRC_NAME, self.DST_NAME)
        mocked_sort.assert_called_once_with(graph_pathes)
    
    def test_sort_pathes_by_distance(self):
        pathes = [
            {'distance': 7, 'path': '1 2 7 5'},
            {'distance': 13, 'path': '1 2 7 8 4 5'},
            {'distance': 2, 'path': '1 5'},
            {'distance': 10, 'path': '1 8 4 5'},
            {'distance': 5, 'path': '1 6 5'}
        ]
        expected_sorted_pathes = [
            {'distance': 2, 'path': '1 5'},
            {'distance': 5, 'path': '1 6 5'},
            {'distance': 7, 'path': '1 2 7 5'},
            {'distance': 10, 'path': '1 8 4 5'},
            {'distance': 13, 'path': '1 2 7 8 4 5'}
        ]
        sorted_pathes = OnRideDistanceCalculator._OnRideDistanceCalculator__sort_pathes_by_distance(pathes)
        self.assertEqual(sorted_pathes, expected_sorted_pathes)


class OnWalkNavigatorTestCase(TestCase):
    SRC_NAME = 'IUST'
    DST_NAME = 'AmirKabir'
    
    def setUp(self):
        self.navigator = OnWalkNavigator()
        self.graph = MockGraph()
        self.location_1 = BaseObject()
        self.location_2 = BaseObject()
        self.location_1.__setattr__('name', self.SRC_NAME)
        self.location_2.__setattr__('name', self.DST_NAME)
    
    def tearDown(self):
        del self.navigator
        del self.graph
        del self.location_1
        del self.location_2
    
    def test_navigate_result(self):
        self.location_1.__setattr__('longitude', 4)
        self.location_1.__setattr__('latitude', -2)
        self.location_2.__setattr__('longitude', 1)
        self.location_2.__setattr__('latitude', 2)
        distance = OnWalkNavigator().navigate(self.graph, self.location_1, self.location_2)
        expected_distance = [{'distance': 5, 'path': [self.location_1, self.location_2]}]
        self.assertEqual(distance[0]['path'], expected_distance[0]['path'])
        self.assertTrue('distance' in list(distance[0].keys()))
    
    def test_calculate_distances_called_correctly(self):
        self.navigator._OnWalkNavigator__distanceCalculator = mock.MagicMock()
        self.navigator.navigate(self.graph, self.location_1, self.location_2)
        self.navigator._OnWalkNavigator__distanceCalculator.calculate_distances.assert_called_once_with(self.graph, self.location_1, self.location_2)
    
    def test_distance_result_correctly_returned(self):
        self.navigator._OnWalkNavigator__distanceCalculator = mock.MagicMock()
        self.navigator._OnWalkNavigator__distanceCalculator.calculate_distances.return_value = [{'distance': 8}, {'distance': 10}]
        distance = self.navigator.navigate(self.graph, self.location_1, self.location_2)
        expected_distance = [{'distance': 8, 'path': [self.location_1, self.location_2]}]
        self.assertEqual(distance, expected_distance)


class OnRideNavigatorTestCase(TestCase):
    SRC_NAME = 'AzadiSq'
    DST_NAME = 'IUST'
    
    def setUp(self):
        self.navigator = OnRideNavigator(max_path_count=2)
        self.graph = MockGraph()
        self.location_1 = BaseObject()
        self.location_2 = BaseObject()
        self.location_1.__setattr__('name', self.SRC_NAME)
        self.location_2.__setattr__('name', self.DST_NAME)
    
    def tearDown(self):
        del self.navigator
        del self.graph
        del self.location_1
        del self.location_2
    
    def test_navigate_result(self):
        distances = self.navigator.navigate(self.graph, self.location_1, self.location_2)
        expected_distances = [
            {'distance': 19, 'path': [self.SRC_NAME, 'tehran_university', self.DST_NAME]},
            {'distance': 20, 'path': [self.SRC_NAME, 'tehran_university', 'resalat_sq', self.DST_NAME]}]
        self.assertEqual(distances, expected_distances)
    
    def test_calculate_distances_called_correctly(self):
        self.navigator._OnRideNavigator__distanceCalculator = mock.MagicMock()
        self.navigator.navigate(self.graph, self.location_1, self.location_2)
        self.navigator._OnRideNavigator__distanceCalculator.calculate_distances.assert_called_once_with(self.graph, self.location_1, self.location_2)
    
    def test_distance_result_correctly_returned(self):
        self.navigator._OnRideNavigator__distanceCalculator = mock.MagicMock()
        all_pathes = self.graph.get_all_paths(self.SRC_NAME, self.DST_NAME)
        self.navigator._OnRideNavigator__distanceCalculator.calculate_distances.return_value = all_pathes
        distances = self.navigator.navigate(self.graph, self.location_1, self.location_2)
        expected_distances = [{'distance': 19, 'path': ['AzadiSq', 'tehran_university', 'IUST']}, {'distance': 20, 'path': ['AzadiSq', 'tehran_university', 'resalat_sq', 'IUST']}]
        self.assertEqual(distances, expected_distances)
    
    def test_get_normalizer_max_path_count_by_input(self):
        navigator = OnRideNavigator(4)
        distance = navigator._OnRideNavigator__get_normalized_max_path_count(2)
        self.assertEqual(distance, 2)
    
    def test_get_normalizer_max_path_count_by_default(self):
        navigator = OnRideNavigator(4)
        distance = navigator._OnRideNavigator__get_normalized_max_path_count(6)
        self.assertEqual(distance, 4)
    
    def test_get_normalizer_max_path_count_equel(self):
        navigator = OnRideNavigator(max_path_count=5)
        distance = navigator._OnRideNavigator__get_normalized_max_path_count(5)
        self.assertEqual(distance, 5)
    
    
if __name__=='__main__':
    unittest.main()
