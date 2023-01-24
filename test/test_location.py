from unittest import TestCase
import unittest

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)

from src.location import GeneralLocation, MapLocation, PrivateLocation
from mock_classes import BaseObject


class GeneralLocationTestCase(TestCase):
    
    def setUp(self):
        self.longitude = 'the_username'
        self.latitude = 'the_password'
        self.name = 'the_name'
        self.general_location = GeneralLocation(self.longitude, self.latitude, self.name)
    
    def tearDown(self):
        del self.general_location
    
    def test_initialize_general_location(self):
        self.assertEqual(self.general_location.longitude, self.longitude)
        self.assertEqual(self.general_location.latitude, self.latitude)
        self.assertEqual(self.general_location.name, self.name)
    
    def test_attributes_are_private(self):
        self.assertEqual(self.general_location._GeneralLocation__longitude, self.longitude)
        self.assertEqual(self.general_location._GeneralLocation__latitude, self.latitude)
        self.assertEqual(self.general_location._GeneralLocation__name, self.name)


class MapLocationTestCase(TestCase):
    
    def setUp(self):
        self.longitude = 'the_username'
        self.latitude = 'the_password'
        self.name = 'the_name'
        self.location_type = 'the_type'
        self.phone = 'phone'
        self.info = 'info'
        self.map_location = MapLocation(self.longitude, self.latitude, self.name,
                                        self.location_type, phone=self.phone, info=self.info)
    
    def tearDown(self):
        del self.map_location
    
    def test_initialize_map_location(self):
        self.assertEqual(self.map_location.longitude, self.longitude)
        self.assertEqual(self.map_location.latitude, self.latitude)
        self.assertEqual(self.map_location.name, self.name)
        self.assertEqual(self.map_location.type, self.location_type)
    
    def test_attributes_are_private(self):
        self.assertEqual(self.map_location._GeneralLocation__longitude, self.longitude)
        self.assertEqual(self.map_location._GeneralLocation__latitude, self.latitude)
        self.assertEqual(self.map_location._GeneralLocation__name, self.name)
        self.assertEqual(self.map_location._MapLocation__type, self.location_type)
        self.assertEqual(self.map_location._MapLocation__phone, self.phone)
        self.assertEqual(self.map_location._MapLocation__info, self.info)
        self.assertEqual(self.map_location._MapLocation__rates, [])
    
    def test_rated_users(self):
        user_1 = BaseObject()
        user_2 = BaseObject()
        rate_1 = BaseObject()
        rate_2 = BaseObject()
        rate_1.__setattr__('user', user_1)
        rate_2.__setattr__('user', user_2)
        self.map_location._MapLocation__rates = [rate_1, rate_2]
        self.assertEqual(self.map_location.rated_users, [user_1, user_2])
    
    def test_rate_location_user_not_in_rated_users(self):
        user = BaseObject()
        rate = BaseObject()
        rate.__setattr__('user', user)
        self.map_location.rate_location(rate)
        self.assertEqual(self.map_location._MapLocation__rates, [rate])
    
    def test_rate_location_user_in_rated_users(self):
        user = BaseObject()
        rate_1 = BaseObject()
        rate_2 = BaseObject()
        rate_1.__setattr__('user', user)
        rate_2.__setattr__('user', user)
        self.map_location._MapLocation__rates = [rate_1]
        self.map_location.rate_location(rate_2)
        self.assertEqual(self.map_location._MapLocation__rates, [rate_1])


class PrivateLocationTestCase(TestCase):
    
    def setUp(self):
        self.longitude = 'the_username'
        self.latitude = 'the_password'
        self.name = 'the_name'
        self.user = BaseObject()
        self.private_location = PrivateLocation(self.longitude, self.latitude, self.name, self.user)
    
    def tearDown(self):
        del self.private_location
    
    def test_initialize_map_location(self):
        self.assertEqual(self.private_location.longitude, self.longitude)
        self.assertEqual(self.private_location.latitude, self.latitude)
        self.assertEqual(self.private_location.name, self.name)
        self.assertEqual(self.private_location.user, self.user)
    
    def test_attributes_are_private(self):
        self.assertEqual(self.private_location._GeneralLocation__longitude, self.longitude)
        self.assertEqual(self.private_location._GeneralLocation__latitude, self.latitude)
        self.assertEqual(self.private_location._GeneralLocation__name, self.name)
        self.assertEqual(self.private_location._PrivateLocation__user, self.user)


if __name__=='__main__':
    unittest.main()
