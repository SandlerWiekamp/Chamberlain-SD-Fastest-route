This code will run and make a fastes route to the town of Chamberlain South Dakota

Prerequisites:
-create a virtual environment
-sphinx documentation

type: uv pip install osmnx networkx

imports needed:
-osmnx as os
-networkx as nx

Functions:
    -dijkstra_fastest_route
        Finds the fastest route between two in a graph using Dijktra's algorith
        
        Parameters:
            -Graph: A NetworkX grapsh where edges have a 'travel_time' attribute
            -start: The starting node
            -end: The destination node
            -return: A tuple containing the total travel time and the path as a list of nodes