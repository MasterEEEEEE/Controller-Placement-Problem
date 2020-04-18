import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from Change import *

G = nx.Graph()
node = 24
G.add_nodes_from([i for i in range(0, node)])
G.add_edges_from([(0, 1), (0, 10), (0, 2), (0, 15),
                  (1, 11), (2, 23), (2, 3), (3, 6), (4, 22),
                  (4, 5), (5, 8), (6, 7), (7, 12), (8, 9),
                  (9, 13), (11, 12), (12, 13),
                  (14, 15), (14, 23), (16, 17),
                  (16, 20), (16, 21), (17, 18), (18, 19),
                  (18, 20), (20, 23), (21, 22)])
position = {0: [26.7, 60.86667], 1: [25.66151, 60.98267],
            2: [27.27227, 61.68857], 3: [25.73333, 62.23333],
            4: [22.83333, 62.8], 5: [21.78333, 61.48333],
            6: [23.78712, 61.49911], 7: [24.46434, 60.99596],
            8: [21.51127, 61.12724], 9: [22.26869, 60.45148],
            10: [26.91667, 60.46667], 11: [24.93545, 60.16952],
            12: [24.6522, 60.2052], 13: [23.13333, 60.38333],
            14: [29.76667, 62.6], 15: [28.18871, 61.05871],
            16: [25.46816, 65.01236], 17: [25.35233, 65.17654],
            18: [25.71667, 66.5], 19: [26.6, 67.41667],
            20: [28.21667, 64.5], 21: [23.13066, 63.83847],
            22: [21.61577, 63.096], 23: [27.67703, 62.89238]}
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
