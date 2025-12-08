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
    
    """Priority queue to store (travel_time, current_node, path)"""
    queue = [(0, start, [start])]
    visited = set()

    """Main loop"""
    while queue:
        travel_time, current_node, path = heapq.heappop(queue)

        """Skip if already visited"""
        if current_node in visited:
            continue
        visited.add(current_node)

        """Check if we reached the destination"""
        if current_node == end:
            return travel_time, path

        """Explore neighbors"""
        for neighbor in graph.neighbors(current_node):
            edge_data = graph.get_edge_data(current_node, neighbor)
            time = edge_data[0]['travel_time']  # Assuming single edge between nodes
            heapq.heappush(queue, (travel_time + time, neighbor, path + [neighbor]))
        
    """If no path is found"""
    return float("inf"), []  # Return infinity if no path is found

if __name__ == "__main__":
    
    """Defines the place and downloads the street map data from OSM."""
    place = "Platte, South Dakota, USA"
    graph = ox.graph_from_place(place, network_type='drive')

    """Calculates travel time for each edge based on length and speed limit."""
    for u, v, data in graph.edges(data=True):
        speed_kmh = data.get('speed_kmh', 35)  # Default speed if not provided
        length_m = data['length']
        travel_time = (length_m / 1000) / (speed_kmh / 60)  # in minutes
        data['travel_time'] = travel_time

    """Geocodes the start and end street addresses."""
    start_street_address = "912 S Ohio Ave, Platte, SD"
    geocode_result = ox.geocode(start_street_address)

    end_street_address = "35271 270th St, Platte, SD" 
    geocode_result_end = ox.geocode(end_street_address)

    """
    Example usage: 
        912 S Ohio Ave, Platte, SD  
        35271 270th St, Platte, SD
    Expected output:
        Total travel time: 3.4204882324378127 minutes
        Path:[78935294, 78949911, 78942214, 78950712, 78952511, 78935494, 78935496, 78935503, 78944845, 12095769949, 78944852, 12095769952, 78946690, 78946688, 78947392, 78955765, 12095769944, 8366430695, 8366430704]

    or

    Example usage:
        224 West Lawler Ave, Chamberlain, SD
        1200 Main St, Chamberlain, SD
    Expected output:
        Total travel time: 2.277611436079074 minutes
        Path: [78780758, 78782733, 78779989, 78779987, 78777767, 78777322, 78781885, 78781880, 78781836, 78777762, 78764373, 78780844, 78782041, 78777880, 78782782]

    """

    start_node = ox.nearest_nodes(graph, geocode_result[1], geocode_result[0])
    end_node = ox.nearest_nodes(graph, geocode_result_end[1], geocode_result_end[0])

    total_time, path = dijkstra_fastest_route(graph, start_node, end_node)

    print(f"Total travel time: {total_time} minutes")
    print(f"Path: {path}")

    plt = ox.plot_graph_route(graph, path, route_linewidth=6, node_size=0)
    plt.show()