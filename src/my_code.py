
import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)


class DataSaver:
    __TO_PRINT = 'original in class'
    
    def __prv_func(self):
        return 'returned in the original function'
    
    def call_prv_func(self):
        return self.__prv_func()
