import numpy as np
import random
import matplotlib.pyplot as plt
import networkx as nx
from Change import *

G = nx.Graph()
node = 19
G.add_nodes_from([i for i in range(0, node)])
G.add_edges_from([(0, 1), (0, 3), (1, 6), (2, 10),
                  (2, 3), (4, 5), (4, 7), (5, 8), (6, 7),
                  (8, 18), (8, 14), (9, 18), (10, 18), (11, 12),
                  (11, 15), (12, 13), (12, 14), (15, 16),
                  (16, 17), (17, 18)])
position = {0: [-74.00597, 40.71427], 1: [-75.16379, 39.95234],
            2: [-83.04575, 42.33143], 3: [-79.99589, 40.44062],
            4: [-95.36327, 29.76328], 5: [-97.74306, 30.26715],
            6: [-77.03637, 38.89511], 7: [-84.38798, 33.749],
            8: [-96.80667, 32.78306], 9: [-88.24338, 40.11642],
            10: [-87.65005, 41.85003], 11: [-122.41942, 37.77493],
            12: [-118.24368, 34.05223], 13: [-117.15726, 32.71533],
            14: [-112.07404, 33.44838], 15: [-111.89105, 40.76078],
            16: [-104.9847, 39.73915], 17: [-94.62746, 39.11417],
            18: [-90.19789, 38.62727]}
nx.draw_networkx(G, pos=position)
# plt.axis('equal')
# plt.show()
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
t = 100
C = [15, 18, 13, 0, 5]
c = 5
c_s = ([15, 16], [2, 9, 10, 17, 18], [11, 12, 13, 14], [0, 1, 3, 6, 7], [4, 5, 8])

s0_load = [0 for i in range(t)]
c_load=([0 for i in range(t)], [0 for i in range(t)],
        [0 for i in range(t)], [0 for i in range(t)], [0 for i in range(t)])

S = [0 for i in range(-1, node)]

c_c = ([], [], [], [], [])
# print(type(c_c))
# print(type(c_c[2]))
for j in range(c):
    for k in range(c):
        if j == k:
            continue
        path_cc = nx.dijkstra_path(G, C[j], C[k])
        vvv = 0
        for m in path_cc:
            xxx = c_s[j] +c_s[k]
            if not xxx.__contains__(m):
                vvv = vvv + 1
        if vvv == 0:
            c_c[j].append(k)
print(c_c)
print(c_s)
for i in range(t):
    for j in range(node):
        if j == 11:
            if i <50:
                sss = 1
            else:
                sss = 2
            S[j] = random.lognormvariate(sss, 0.25)
        else:
            S[j] = random.lognormvariate(1, 0.25)
    s0_load[i] = S[11]
    for j in c_s[0]:
        c_load[0][i] = c_load[0][i] + S[j]
    for j in c_s[1]:
        c_load[1][i] = c_load[1][i] + S[j]
    for j in c_s[2]:
        c_load[2][i] = c_load[2][i] + S[j]
    for j in c_s[3]:
        c_load[3][i] = c_load[3][i] + S[j]
    for j in c_s[4]:
        c_load[4][i] = c_load[4][i] + S[j]

    for o in range(c):
        if c_load[o][i] > 20:
            yyy = c_c[o][0]
            zzz = c_s[o][0]
            # 判断邻接的转移控制器
            for j in c_c[o]:
                if c_load[j] < c_load[yyy]:
                    yyy = j
            # 在过载的控制域中寻找与目标控制器最近的交换机
            for j in c_s[o]:
                if distance[j, yyy] > distance[zzz, yyy]:
                    zzz = j
            print(zzz)
            # 完成迁移
            c_s[o].remove(zzz)
            c_s[yyy].append(zzz)
            c_c = ([], [], [], [], [])
            for j in range(c):
                for k in range(c):
                    if j == k:
                        continue
                    path_cc = nx.dijkstra_path(G, C[j], C[k])
                    vvv = 0
                    for m in path_cc:
                        xxx = c_s[j] + c_s[k]
                        if not xxx.__contains__(m):
                            vvv = vvv + 1
                    if vvv == 0:
                        c_c[j].append(k)
print(c_c)
print(c_s)


for i in range(t):
    print(s0_load[i])
for i in range(t):
    print(c_load[0][i])
for i in range(t):
    print(c_load[1][i])
for i in range(t):
    print(c_load[2][i])
for i in range(t):
    print(c_load[3][i])
for i in range(t):
    print(c_load[4][i])
