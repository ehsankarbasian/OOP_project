from unittest import TestCase
import unittest
import mock

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)

from src.location import GeneralLocation, MapLocation, PrivateLocation
from mock_classes import BaseObject


class LocationTestCase(TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    # @mock.patch.object(Graph, '_Graph__get_not_weighted_graph', return_value={'a': [], 'b': []})
    def test_(self):
        pass


if __name__=='__main__':
    unittest.main()
