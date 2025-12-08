"""
ChamberlainSDFastestRoute.py
====================================
This is an example file with correct docstring examples

| Author: Sandler Wiekamp
| Date: 2025 November 25
"""

import osmnx as ox
import heapq
import networkx as nx

def dijkstra_fastest_route(graph, start, end):
    """
    Finds the fastest route between two points in a graph using Dijkstra's algorithm.

    :param graph: A NetworkX graph where edges have a 'travel_time' attribute.
    :param start: The starting node.
    :param end: The destination node.
    :return: A tuple containing the total travel time and the path as a list of nodes.
    """
    
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        travel_time, current_node, path = heapq.heappop(queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == end:
            return travel_time, path

        for neighbor in graph.neighbors(current_node):
            edge_data = graph.get_edge_data(current_node, neighbor)
            time = edge_data[0]['travel_time']  # Assuming single edge between nodes
            heapq.heappush(queue, (travel_time + time, neighbor, path + [neighbor]))
        
        
    return float("inf"), []  # Return infinity if no path is found

if __name__ == "__main__":
    
    place = "Chamberlain, South Dakota, USA"
    graph = ox.graph_from_place(place, network_type='drive')

    for u, v, data in graph.edges(data=True):
        speed_kmh = data.get('speed_kmh', 35)  # Default speed if not provided
        length_m = data['length']
        travel_time = (length_m / 1000) / (speed_kmh / 60)  # in minutes
        data['travel_time'] = travel_time

    start_street_address = "123 Main St, Chamberlain, SD"
    geocode_result = ox.geocode(start_street_address)

    end_street_address = "224 West Lawler Ave, Chamberlain, SD"
    geocode_result_end = ox.geocode(end_street_address)

    start_node = ox.nearest_nodes(graph, geocode_result[1], geocode_result[0])
    end_node = ox.nearest_nodes(graph, geocode_result_end[1], geocode_result_end[0])

    total_time, path = dijkstra_fastest_route(graph, start_node, end_node)

    print(f"Total travel time: {total_time} minutes")
    print(f"Path: {path}")

    plt = ox.plot_graph_route(graph, path, route_linewidth=6, node_size=0)
    plt.show()