
import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.absolute())
sys.path.append(path)


class BaseObject:
    pass


class MockGraph:
    
    def get_all_paths(self, source_name, destination_name):
        result = [{'distance': 23, 'path': [source_name, 'tehran_university', 'amirkabir_university', destination_name]},
                  {'distance': 21, 'path': [source_name, 'tehran_university', 'amirkabir_university', 'resalat_sq', destination_name]},
                  {'distance': 19, 'path': [source_name, 'tehran_university', destination_name]},
                  {'distance': 20, 'path': [source_name, 'tehran_university', 'resalat_sq', destination_name]}]
        return sorted(result, key=lambda x: x['distance'])
