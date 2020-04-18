import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from Change import *


G = nx.Graph()
node = 14
G.add_nodes_from([i for i in range(0, node)])
G.add_edges_from([(0,1),(1,8),(1,5),(1,13),
                  (2,8),(2,3),(3,10),(4,13),
                  (5,13),(5,6),(6,13),(7,8),(7,13),
                  (8,10),(8,12),(9,10),
                  (10,11),(11,12),(12,13)])
position = {0: [14.42076, 50.08804], 1: [8.68333, 50.11667],
            2: [10.0, 53.55], 3: [12.56553, 55.67594],
            4: [-3.70256, 40.4165], 5: [6.14569, 46.20222],
            6: [9.18951, 45.46427], 7: [4.34878, 50.85045],
            8: [4.88969, 52.37403], 9: [24.93545, 60.16952],
            10: [18.0649, 59.33258], 11: [10.74609, 59.91273],
            12: [-0.12574, 51.50853], 13: [2.3488, 48.85341]}
nx.draw_networkx(G, pos=position)
plt.axis('equal')
plt.show()
distance = np.zeros((node, node))
for i in range(0, node):
    for j in range(0, node):
        if i == j:
            distance[i, j] = 0
        else:
            path = nx.dijkstra_path(G, i, j)
            for k in range(0, len(path) - 1):
                distance[i, j] = distance[i, j] + getDistance(position[path[k]][0], position[path[k]][1],
                                                          position[path[k + 1]][0], position[path[k + 1]][1])

