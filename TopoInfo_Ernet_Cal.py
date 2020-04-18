import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from Change import *


G = nx.Graph()
node = 16
G.add_nodes_from([i for i in range(0, node)])
G.add_edges_from([(0,3),(0,7),(1,3),(2,7),
                  (3,8),(4,8),(5,8),(6,7),(6,15),
                  (7,8),(7,15),(8,11),(8,13),(9,13),
                  (10,11),(11,12),(13,14),(13,15)])
position = {0: [73.85535, 18.51957], 1: [75.8333, 22.71792],
            2: [76.91667, 8.48333], 3: [72.84794, 19.01441],
            4: [72.61667, 23.03333], 5: [75.81667, 26.91667],
            6: [80.27847, 13.08784], 7: [77.60329, 12.97623],
            8: [77.22445, 28.63576], 9: [91.75095, 26.18617],
            10: [75.68333, 29.45], 11: [80.35, 26.46667],
            12: [81.85, 25.45], 13: [88.36972, 22.56972],
            14: [85.83333, 20.23333], 15: [78.47444, 17.37528]}
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
                distance[i, j] = distance[i,j] + getDistance(position[path[k]][0], position[path[k]][1],
                                                             position[path[k+1]][0], position[path[k+1]][1])

