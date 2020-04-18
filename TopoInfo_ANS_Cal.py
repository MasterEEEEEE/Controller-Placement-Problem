import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from Change import *

G = nx.Graph()
node = 18
G.add_nodes_from([i for i in range(0, node)])
G.add_edges_from([(0, 1), (0, 3), (1, 3), (1, 6), (1, 7), (2, 3), (2, 9), (2, 11), (4, 5),
                  (4, 6), (5, 17), (6, 7), (7, 8), (7, 9), (8, 9), (8, 13), (8, 17),
                  (10, 11), (10, 12), (11, 12), (12, 13), (12, 14), (14, 15),
                  (15, 16), (15, 17)])

position = {0: [-72.68509, 41.76371], 1: [-74.00597, 40.71427],
            2: [-87.65005, 41.85003], 3: [-81.69541, 41.4995],
            4: [-79.79198, 36.07264], 5: [-84.38798, 33.749],
            6: [-77.03637, 38.89511], 7: [-77.3411, 38.96872],
            8: [-96.80667, 32.78306], 9: [-90.19789, 38.62727],
            10: [-122.33207, 47.60621], 11: [-104.9847, 39.73915],
            12: [-122.41942, 37.77493], 13: [-121.89496, 37.33939],
            14: [-118.24368, 34.05223], 15: [-106.65114, 35.08449],
            16: [-157.85833, 21.30694], 17: [-95.36327, 29.76328]}
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
print(distance)
