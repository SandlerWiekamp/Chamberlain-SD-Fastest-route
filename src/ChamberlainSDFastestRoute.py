"""
ChamberlainSDFastestRoute.py
====================================
This is an example file with correct docstring examples

| Author: Sandler Wiekamp
| Date: 2025 November 25
"""

import osmnx as ox
import networkx as nx

G = ox.graph_from_place('Chamberlain, South Dakota, USA', network_type='drive')
