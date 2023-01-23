import json
import copy

from context import Context
from src.graph import Graph
from src.navigation import OnWalkNavigator, OnRideNavigator
from src.user import User
from src.location import MapLocation, PrivateLocation


graph = Graph()
graph.add_node(node_name='azadi_sq')
graph.add_node(node_name='tehran_university')
graph.add_node(node_name='amirkabir_university')
graph.add_node(node_name='IUST')
graph.add_node(node_name='resalat_sq')
graph.add_edge('azadi_sq', 'tehran_university', edge_weight=9)
graph.add_edge('tehran_university', 'amirkabir_university', edge_weight=2)
graph.add_edge('amirkabir_university', 'IUST', edge_weight=12)
graph.add_edge('tehran_university', 'IUST', edge_weight=10)
graph.add_edge('amirkabir_university', 'resalat_sq', edge_weight=7)
graph.add_edge('tehran_university', 'resalat_sq', edge_weight=8)
graph.add_edge('IUST', 'resalat_sq', edge_weight=5)
graph.add_edge('resalat_sq', 'IUST', edge_weight=3)
graph.add_edge('IUST', 'azadi_sq', edge_weight=28)
graph.add_edge('IUST', 'amirkabir_university', edge_weight=11)


onWalkNavigator = OnWalkNavigator()
onRideNavigator = OnRideNavigator()

map_location_1 = MapLocation(2, 5, name='azadi_sq', location_type='square', rates=[])
map_location_2 = MapLocation(7, 18, name='tehran_university',  location_type='university', rates=[])
map_location_3 = MapLocation(21, 45, name='amirkabir_university',  location_type='university', rates=[])
map_location_4 = MapLocation(12, 19, name='IUST',  location_type='university', rates=[])
map_location_5 = MapLocation(0, 13, name='resalat_sq', location_type='square', rates=[])


user_1 = User(username='user_1', password='pwd_1', favourite_locations=[])
user_2 = User(username='user_2', password='pwd_2', favourite_locations=[])

private_location_1 = PrivateLocation(15, 11, name='imamhossein_sq', user=user_1)
private_location_2 = PrivateLocation(7, 23, name='home', user=user_2)

locations_1 = [map_location_1, map_location_2, map_location_3, map_location_4, map_location_5, private_location_1]
locations_2 = [map_location_1, map_location_2, map_location_3, map_location_4, map_location_5, private_location_2]


graph_1 = copy.deepcopy(graph)
graph_2 = copy.deepcopy(graph)
graph_1.add_node(private_location_1.name)
graph_1.add_edge(private_location_1.name, 'tehran_university', edge_weight=6)
graph_1.add_edge('resalat_sq', private_location_1.name, edge_weight=5)
graph_2.add_node(private_location_2.name)
graph_2.add_edge(private_location_2.name, 'amir_kabir_university', edge_weight=2)
graph_2.add_edge('tehran_university', private_location_1.name, edge_weight=1)

context_1 = Context(navigator=onWalkNavigator, user=user_1, locations=locations_1, graph=graph_1)
context_2 = Context(navigator=onRideNavigator, user=user_2, locations=locations_2, graph=graph_2)


# Call context functionalities:

# امکان تعریف مکان جدید در نقشه
context_1.add_new_map_location()

# امکان علامت گذاری مکانی در نقشه
context_1.add_new_private_location()

# سرچ کردن بدنبال یک مکان با اسم آن
context_1.search_location_by_name()

# مسیریابی از نقطه ای به نقطه ی دیگر بصورت مسیر پیاده رو
routes_1 = context_1.navigate(map_location_1, map_location_4)
print(routes_1[0]['distance'])

# مسیریابی از نقطه ای به نقطه ی دیگر بصورت مسیر ماشین رو
routes_2 = context_2.navigate(map_location_1, map_location_4)
print(json.dumps(routes_2, sort_keys=True, indent=4))

# پیدا کردن نزدیک ترین نوع از یک مکان
context_1.find_the_nearest_location_by_type()

# دیدن جزییات مکان توسط کاربر
context_1.get_location_info()

# فیوریت کردن یک مکان خاص روی نقشه
context_1.make_location_favourite()

# ریت دادن به یک مکان خاص از نقشه از طرف کاربر
context_1.rate_location()
