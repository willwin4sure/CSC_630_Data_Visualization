import json
from pyvis.network import Network
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from math import log2
from math import sqrt

def area_to_size(area):
    # return log2(area)
    return max(sqrt(area)/100, 2)

df = pd.read_csv('land-area-km.csv')

df = df[df['Year'] == 2018]

area_dict = dict(zip(df['Entity'], df['Land area (sq. km)'].apply(area_to_size)))
print(min(df['Land area (sq. km)'].apply(area_to_size)))
# print(area_dict)

with open('country_adj_fullname.json') as json_file:
    data = json.load(json_file)

    # print(data)

    G = nx.Graph(data)

    nt = Network(bgcolor='#222222', font_color='white', width='100%', height='100%')

    for country in data.keys():
        try:
            area = area_dict[country]
        except KeyError:
            print(country)
            print('No area')
            area = 1

        nt.add_node(country, size=area)

    for k, v in data.items():
        for i in v:
            nt.add_edge(k, i, value=(len(data[k]) + len(data[i]))/200)

    nt.show('nt.html')
    
    # pos=nx.spring_layout(G)
    # nx.draw(G, pos, with_labels=True, node_size=5, font_size=1)
    # nx.draw_networkx_edges(G, pos, edgelist=G.edges(), alpha=0.5, edge_color='b')

    # plt.savefig('countries.png')
