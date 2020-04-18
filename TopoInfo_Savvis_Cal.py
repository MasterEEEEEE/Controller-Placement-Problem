import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from Change import *

G = nx.Graph()
node = 19
G.add_nodes_from([i for i in range(0, node)])
G.add_edges_from([(0,1),(0,3),(1,6),(2,10),
                  (2,3),(4,5),(4,7),(5,8),(6,7),
                  (8,18),(8,14),(9,18),(10,18),(11,12),
                  (11,15),(12,13),(12,14),(15,16),
                  (16,17),(17,18)])
position = {0: [-74.00597, 40.71427], 1: [-75.16379, 39.95234],
            2: [-83.04575, 42.33143], 3: [-79.99589, 40.44062],
            4: [-95.36327, 29.76328], 5: [-97.74306, 30.26715],
            6: [-77.03637, 38.89511], 7: [-84.38798, 33.749],
            8: [-96.80667, 32.78306], 9: [-88.24338, 40.11642],
            10: [-87.65005, 41.85003], 11: [-122.41942, 37.77493],
            12: [-118.24368, 34.05223], 13: [-117.15726, 32.71533],
            14: [-112.07404, 33.44838], 15: [-111.89105, 40.76078],
            16:[-104.9847,39.73915],17:[-94.62746,39.11417],
            18:[-90.19789,38.62727]}
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
#                 np.linalg.norm(np.array(position[path[k]]) - np.array(position[path[k + 1]]))

print(distance)

