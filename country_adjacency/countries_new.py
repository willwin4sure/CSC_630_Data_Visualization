import json
from pyvis.network import Network
import networkx as nx
import matplotlib.pyplot as plt
import datapane as dp 

report = []

net = Network()

net.add_nodes(
    [1, 2, 3, 4, 5, 6],
    label=["Alex", "Cathy", "Michael", "Ben", "Oliver", "Olivia"],
    color=["#00bfff", "#ffc0cb", "#3da831", "#9a31a8", "#3155a8", "#eb4034"],
)

net.add_edge(1, 5)
net.add_edges([(2, 5), (3, 4), (1, 6), (2, 6), (3, 5)])
net.show("edges.html")
