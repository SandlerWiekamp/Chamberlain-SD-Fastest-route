This code will run and make a fastes route to the town of Chamberlain South Dakota

Prerequisites:
-create a virtual environment
-sphinx documentation

type: pip install osmnx networkx matplotlib

imports needed:
-osmnx as os
-networkx as nx

Overview:
This project calculates the fastest travel-time route between two street addresses in Chamberlain, South Dakota, using:
    OSMnx to download the real road network.
    NetworkX graphs.
    Dijkstra’s Algorithm (implemented manually).
    Dynamic travel-time calculation using road length & speed limits.
    Matplotlib route visualization via ox.plot_graph_route.
    The script takes two real-world addresses, converts them to graph nodes using geocoding, and computes:

Fastest route
Total travel time (in minutes)
Complete ordered path of nodes
A visual map of the route

Features:
    Real geographic routing using live OSM street data.
    Fastest path computing (not shortest distance).
    Custom Dijkstra implementation for clarity and educational use.
    Automatic speed limits with fallbacks when OSM lacks data.
    Clean route visualization on a real city map.
    Easy to adapt to any city or addresses.

Functions:
    -dijkstra_fastest_route
        Finds the fastest route between two in a graph using Dijktra's algorith
        
        Parameters:
            -Graph: A NetworkX grapsh where edges have a 'travel_time' attribute
            -start: The starting node
            -end: The destination node
            -return: A tuple containing the total travel time and the path as a list of nodes

How to use:
    -Input inteaded start street address in 
        start_street_address
    -Input intended destination street address in 
        end_street_address

Output:
    Total Travel Time
    The Path taken
    A map of path taken

    