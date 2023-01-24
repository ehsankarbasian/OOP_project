
import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)


class Rate:
    
    def __init__(self, comment, score, user):
        self.__comment = comment
        self.__score = score
        self.__user = user
    
    @property
    def comment(self):
        return self.__comment
    
    @property
    def score(self):
        return self.__score
    
    @property
    def user(self):
        return self.__user
