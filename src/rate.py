
import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)


class Rate:
    
    def __init__(self, comment, score, user, location):
        self.comment = comment
        self.score = score
        self.user = user
        self.location = location
