"""
Minimum connections to connect all airports
"""


class AirportNode:
    def __init__(self, airport):
        self.airport = airport
        self.connections = []
        self.unreachable_connections = []
        self.is_reachable = True


# Time: O(a+r+a*(a+r)+a*log(a)) | Space: O(a+r)
def airport_connections(airports, routes, starting_airport):
    airport_graph = create_airport_graph(airports, routes)
    unreachable_airport_nodes = get_unreachable_airport_nodes(airport_graph, airports, starting_airport)
    mark_unreachable_connections(airport_graph, unreachable_airport_nodes)
    return get_min_number_of_new_connections(airport_graph, unreachable_airport_nodes)


# Time Complexity: O(a+r) | Space Complexity: O(a+r)
def create_airport_graph(airports, routes):
    airport_graph = {}
    for airport in airports:
        airport_graph[airport] = AirportNode(airport)
        # Fill up airport connections based on routes
    for route in routes:
        airport, connection = route
        airport_graph[airport].connections.append(connection)
    return airport_graph


# Time: O(a+r) for DFS | Space: O(a) for recursive call stack
def get_unreachable_airport_nodes(airport_graph, airports, starting_airport):
    visited_airports = {}
    depth_first_traverse_airports(airport_graph, starting_airport, visited_airports)
    unreachable_airport_nodes = []
    for airport in airports:
        if airport in visited_airports:
            continue
        airport_node = airport_graph[airport]
        airport_node.is_reachable = False
        unreachable_airport_nodes.append(airport_node)
    return unreachable_airport_nodes


def depth_first_traverse_airports(airport_graph, airport, visited_airports):
    if airport in visited_airports:
        return
    visited_airports[airport] = True
    for connection in airport_graph[airport].connections:
        depth_first_traverse_airports(airport_graph, connection, visited_airports)


# Time: O(a*(a+r)) | Space: O(a) for recursive call stack
def mark_unreachable_connections(airport_graph, unreachable_airport_nodes):
    for airport_node in unreachable_airport_nodes:
        airport = airport_node.airport
        unreachable_connections = []
        depth_first_add_unreachable_connections(airport_graph, airport, unreachable_connections, {})
        airport_node.unreachable_connections = unreachable_connections


def depth_first_add_unreachable_connections(airport_graph, airport, unreachable_connections, visited_airports):
    if airport_graph[airport].is_reachable:
        return
    if airport in visited_airports:
        return
    visited_airports[airport] = True
    unreachable_connections.append(airport)
    for connection in airport_graph[airport].connections:
        depth_first_add_unreachable_connections(airport_graph, connection, unreachable_connections, visited_airports)


# Time: O(alog(a)) for sorting + O(a+r) for exploring airports and their connections | Space: O(1)
def get_min_number_of_new_connections(airport_graph, unreachable_airport_nodes):
    minimum_connections = 0
    # Sort the connections by unreachable connections
    unreachable_airport_nodes.sort(key= lambda airport: airport.unreachable_connections, reverse=True)
    for airport_node in unreachable_airport_nodes:
        if airport_node.is_reachable:
            continue
        minimum_connections += 1
        for connection in airport_node.unreachable_connections:
            airport_graph[connection].is_reachable = True
    return minimum_connections

