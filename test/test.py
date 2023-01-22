from unittest import TestCase
import unittest
import mock

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)

from src.my_code import DataSaver


class ClassBasedSaverTestCase(TestCase):
    
    
    def setUp(self):
        # self.database_patcher = mock.patch('src.my_code_class_based.connectMongoDB', return_value=(mocked_tunnel, mocked_person_collection))
        # self.database_patcher.start()
        pass


    def tearDown(self):
        # self.database_patcher.stop()
        pass
    
    
    @mock.patch('src.my_code.DataSaver._DataSaver__TO_PRINT', 'mocked in test')
    @mock.patch.object(DataSaver, '_DataSaver__prv_func', return_value='returned in mocked test')
    def test_mock_variable_works(self, a):
        saver = DataSaver()
        a = saver.call_prv_func()
        b = saver._DataSaver__prv_func()
        c = saver._DataSaver__TO_PRINT
        c = 2
    
    
if __name__=='__main__':
    unittest.main()
