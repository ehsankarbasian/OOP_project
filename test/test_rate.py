from unittest import TestCase
import unittest

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)

from src.rate import Rate


class RateTestCase(TestCase):
    
    def setUp(self):
        self.comment = 'comment'
        self.score = 'score'
        self.user = 'user'
        self.rate = Rate(self.comment, self.score, self.user)
    
    def tearDown(self):
        del self.rate
    
    def test_initialize_rate(self):
        self.assertEqual(self.rate.comment, self.comment)
        self.assertEqual(self.rate.score, self.score)
        self.assertEqual(self.rate.user, self.user)
    
    def test_attributes_are_private(self):
        self.assertEqual(self.rate._Rate__comment, self.comment)
        self.assertEqual(self.rate._Rate__score, self.score)
        self.assertEqual(self.rate._Rate__user, self.user)
        


if __name__=='__main__':
    unittest.main()
