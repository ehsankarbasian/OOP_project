from unittest import TestCase
import unittest
import copy

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)

from src.user import User
from src.graph import Graph
from src.location import MapLocation, PrivateLocation
from src.navigation import OnWalkNavigator, OnRideNavigator

from context import Context


class ContextTestCase(TestCase):
    
    def setUp(self):
        self.graph = Graph()
        self.graph.add_node(node_name='azadi_sq')
        self.graph.add_node(node_name='tehran_university')
        self.graph.add_node(node_name='amirkabir_university')
        self.graph.add_node(node_name='IUST')
        self.graph.add_node(node_name='resalat_sq')
        self.graph.add_edge('azadi_sq', 'tehran_university', edge_distance=9)
        self.graph.add_edge('tehran_university', 'amirkabir_university', edge_distance=2)
        self.graph.add_edge('amirkabir_university', 'IUST', edge_distance=12)
        self.graph.add_edge('tehran_university', 'IUST', edge_distance=10)
        self.graph.add_edge('amirkabir_university', 'resalat_sq', edge_distance=7)
        self.graph.add_edge('tehran_university', 'resalat_sq', edge_distance=8)
        self.graph.add_edge('IUST', 'resalat_sq', edge_distance=5)
        self.graph.add_edge('resalat_sq', 'IUST', edge_distance=3)
        self.graph.add_edge('IUST', 'azadi_sq', edge_distance=28)
        self.graph.add_edge('IUST', 'amirkabir_university', edge_distance=11)
        
        self.onWalkNavigator = OnWalkNavigator()
        self.onRideNavigator = OnRideNavigator()

        self.map_location_1 = MapLocation(2, 5, name='azadi_sq', location_type='square')
        self.map_location_2 = MapLocation(7, 18, name='tehran_university',  location_type='university')
        self.map_location_3 = MapLocation(21, 45, name='amirkabir_university',  location_type='university')
        self.map_location_4 = MapLocation(12, 19, name='IUST',  location_type='university')
        self.map_location_5 = MapLocation(0, 13, name='resalat_sq', location_type='square')

        self.user_1 = User(username='user_1', password='pwd_1')
        self.user_2 = User(username='user_2', password='pwd_2')

        self.private_location_1 = PrivateLocation(15, 11, name='__mi_house__', user=self.user_1)
        self.private_location_2 = PrivateLocation(7, 23, name='home', user=self.user_2)

        self.locations_1 = [self.map_location_1, self.map_location_2, self.map_location_3, self.map_location_4, self.map_location_5, self.private_location_1]
        self.locations_2 = [self.map_location_1, self.map_location_2, self.map_location_3, self.map_location_4, self.map_location_5, self.private_location_2]

        self.graph_1 = copy.deepcopy(self.graph)
        self.graph_2 = copy.deepcopy(self.graph)
        self.graph_1.add_node(self.private_location_1.name)
        self.graph_1.add_edge(self.private_location_1.name, 'tehran_university', edge_distance=6)
        self.graph_1.add_edge('resalat_sq', self.private_location_1.name, edge_distance=5)
        self.graph_2.add_node(self.private_location_2.name)
        self.graph_2.add_edge(self.private_location_2.name, 'amir_kabir_university', edge_distance=2)
        self.graph_2.add_edge('tehran_university', self.private_location_1.name, edge_distance=1)

        self.context_1 = Context(navigator=self.onWalkNavigator, user=self.user_1, locations=self.locations_1, graph=self.graph_1, user_password='pwd_1')
        self.context_2 = Context(navigator=self.onRideNavigator, user=self.user_2, locations=self.locations_2, graph=self.graph_2, user_password='pwd_2')
    
    def tearDown(self):
        del self.context_1
        del self.context_2
        
    # امکان تعریف مکان جدید در نقشه
    def test_define_and_add_new_map_location(self):
        new_map_location_1 = MapLocation(8, 42, name='Milad Tower', location_type='building')
        new_map_location_2 = MapLocation(6, 37, name='Central Bank', location_type='building')
        self.context_1.add_new_location(new_map_location_1)
        self.context_1.add_new_location(new_map_location_2)
        self.assertEqual(self.context_1._Context__map_locations[-1], new_map_location_2)
        self.assertEqual(self.context_1._Context__map_locations[-2], new_map_location_1)
        self.assertEqual(self.context_1._Context__locations[-1], new_map_location_2)
        self.assertEqual(self.context_1._Context__locations[-2], new_map_location_1)
        self.assertEqual(self.context_1._Context__graph._Graph__nodes[-1], 'Central Bank')
        self.assertEqual(self.context_1._Context__graph._Graph__nodes[-2], 'Milad Tower')
    
    # امکان علامت گذاری مکانی در نقشه
    def test_save_a_private_location(self):
        self.context_1.add_new_private_location(9, 33, name='the company')
        self.assertEqual(self.context_1._Context__locations[-1].longitude, 9)
        self.assertEqual(self.context_1._Context__locations[-1].latitude, 33)
        self.assertEqual(self.context_1._Context__locations[-1].name, 'the company')
        self.assertEqual(self.context_1._Context__locations[-1].user, self.user_1)
        self.assertEqual(self.context_1._Context__graph._Graph__nodes[-1], 'the company')

    # سرچ کردن بدنبال یک مکان با اسم آن
    def test_search_for_location_by_name(self):
        result_1 = self.context_1.search_location_by_name('milad tower')
        result_2 = self.context_1.search_location_by_name('MI')
        self.assertEqual(result_1, [])
        self.assertEqual(result_2[0].name, 'amirkabir_university')
        self.assertEqual(result_2[1].name, '__mi_house__')

    # مسیریابی از نقطه ای به نقطه ی دیگر بصورت مسیر پیاده رو
    def test_on_walk_navigation(self):
        routes = self.context_1.navigate(self.map_location_1, self.map_location_4)
        distance = routes[0]['distance']
        self.assertTrue(abs(distance-17.20) < 0.01)

    # مسیریابی از نقطه ای به نقطه ی دیگر بصورت مسیر ماشین رو
    def test_on_ride_navigation(self):
        routes = self.context_2.navigate(self.map_location_1, self.map_location_4)
        expected_routes = [{'distance': 19, 'path': ['azadi_sq', 'tehran_university', 'IUST']},
                           {'distance': 20, 'path': ['azadi_sq', 'tehran_university', 'resalat_sq', 'IUST']},
                           {'distance': 21, 'path': ['azadi_sq', 'tehran_university', 'amirkabir_university', 'resalat_sq', 'IUST']}]
        self.assertEqual(routes, expected_routes)

    # پیدا کردن نزدیک ترین نوع از یک مکان
    def test_find_the_nearest_location_by_type(self):
        the_nearest_location = self.context_1.find_the_nearest_location_by_type(7, 38, location_type='university')
        self.assertEqual(the_nearest_location.name, 'amirkabir_university')

    # دیدن جزییات مکان توسط کاربر
    def test_see_location_info(self):
        info_1 = self.context_1.get_location_info(self.map_location_4)
        info_2 = self.context_1.get_location_info(self.private_location_1)
        info_3 = self.context_1.get_location_info(self.private_location_2)
        info_4 = self.context_1.get_location_info('spam input')
        self.assertEqual(info_1, {'_MapLocation__phone': None, 'longitude': 12, 'latitude': 19, 'name': 'IUST', 'type': 'university', 'rates': []})
        self.assertTrue("'_GeneralLocation__longitude': 15, '_GeneralLocation__latitude': 11, '_GeneralLocation__name': '__mi_house__', 'longitude': 15, 'latitude': 11, 'name': '__mi_house__', 'user': <src.user.User object at " in str(info_2))
        self.assertEqual(info_3, dict({}))
        self.assertEqual(info_4, dict({}))

    # فیوریت کردن یک مکان خاص روی نقشه
    def test_favourite_a_location(self):
        new_map_location = MapLocation(8, 42, name='Milad Tower', location_type='building')
        self.context_1.make_location_favourite(self.map_location_3)
        self.context_1.make_location_favourite(new_map_location)
        self.context_1.make_location_favourite(self.private_location_1)
        self.context_1.make_location_favourite(self.private_location_2)
        self.assertEqual(len(self.context_1._Context__user.favourite_locations), 3)
        self.assertEqual(self.context_1._Context__user.favourite_locations[0], self.map_location_3)
        self.assertEqual(self.context_1._Context__user.favourite_locations[1], new_map_location)
        self.assertEqual(self.context_1._Context__user.favourite_locations[2], self.private_location_1)

    # ریت دادن به یک مکان خاص از نقشه از طرف کاربر
    def test_rate_location(self):
        new_map_location = MapLocation(8, 42, name='Milad Tower', location_type='building')
        self.context_1.rate_location(comment='nice place but expensive', score=4, location=new_map_location)
        self.assertEqual(new_map_location.rates[0].comment, 'nice place but expensive')
        self.assertEqual(new_map_location.rates[0].score, 4)
        self.assertEqual(new_map_location.rates[0].user, self.user_1)
        self.context_1.rate_location(comment='i love my house', score=5, location=self.private_location_1)
        self.assertFalse(hasattr(self.private_location_1, 'rates'))
    
    
    def test_add_a_graph_edge(self):
        new_map_location_1 = MapLocation(8, 42, name='Milad Tower', location_type='building')
        new_map_location_2 = MapLocation(6, 37, name='Central Bank', location_type='building')
        self.context_2.add_new_location(new_map_location_1)
        self.context_2.add_new_location(new_map_location_2)
        self.context_2.add_new_private_location(9, 33, name='the company')
        private_location = self.context_2._Context__locations[-1]
        
        self.context_2.add_edge(new_map_location_1, new_map_location_2, cost=31)
        self.context_2.add_edge(new_map_location_2, private_location, cost=14)
        
        routes = self.context_2.navigate(new_map_location_1, private_location)
        expected_routes = [{'distance': 45, 'path': ['Milad Tower', 'Central Bank', 'the company']}]
        self.assertEqual(routes, expected_routes)


if __name__=='__main__':
    unittest.main()
