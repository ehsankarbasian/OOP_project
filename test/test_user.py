from unittest import TestCase
import unittest
import mock

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)

from src.user import User
from mock_classes import BaseObject


class UserTestCase(TestCase):
    
    def setUp(self):
        self.username = 'the_username'
        self.password = 'the_password'
        self.user = User(self.username, self.password)
    
    def tearDown(self):
        del self.user
    
    def test_initialize_user(self):
        self.assertEqual(self.user.username, self.username)
        self.assertEqual(self.user.favourite_locations, [])
        self.assertEqual(self.user.special_permissions, User._User__DEFAULT_SPECIAL_PERMISSIONS)
    
    def test_attributes_are_private(self):
        self.assertEqual(self.user._User__username, self.username)
        self.assertEqual(self.user._User__password, self.password)
        self.assertEqual(self.user._User__favourite_locations, [])
        self.assertEqual(self.user._User__spicial_permissions, User._User__DEFAULT_SPECIAL_PERMISSIONS)
    
    def test_create_custom_permissioned_user(self):
        custom_permissions = ['_MapLocation__info']
        custom_permissioned_user = User(self.username, self.password, spicial_permissions=custom_permissions)
        self.assertEqual(custom_permissioned_user._User__username, self.username)
        self.assertEqual(custom_permissioned_user._User__password, self.password)
        self.assertEqual(custom_permissioned_user._User__favourite_locations, [])
        self.assertEqual(custom_permissioned_user._User__spicial_permissions, custom_permissions)
    
    def test_check_password_is_true(self):
        check = self.user.check_password(self.password)
        self.assertTrue(check)
    
    def test_check_password_is_false(self):
        check = self.user.check_password('the_wrong_password')
        self.assertFalse(check)
    
    def test_add_one_favourite_location(self):
        location = BaseObject()
        self.user.add_favourite_location(location=location)
        self.assertEqual(self.user._User__favourite_locations, [location])
    
    def test_add_multiple_favourite_location(self):
        location_1 = BaseObject()
        location_2 = BaseObject()
        location_3 = BaseObject()
        self.user.add_favourite_location(location=location_1)
        self.user.add_favourite_location(location=location_2)
        self.user.add_favourite_location(location=location_3)
        self.assertEqual(self.user._User__favourite_locations, [location_1, location_2, location_3])


if __name__=='__main__':
    unittest.main()
