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