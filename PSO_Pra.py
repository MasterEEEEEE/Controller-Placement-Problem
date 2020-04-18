import numpy as np
import random
from BA_Alg_Ref import BACP
# from TopoInfo_ANS import *
# from TopoInfo_Bsonet import *
# from TopoInfo_Ernet import *
from TopoInfo_Funet import *
# from TopoInfo_Rnp import *
# from TopoInfo_Savvis import *


# print(BACP(T, n, c, s, Switches, Distances, a1, a2))
def PSO_Pra(T_P, T_B, n_P, n_B, c, s, Switches, Distances):
    a = np.ones((n_P, 4))
    personal_best_coor = np.zeros((n_P, 4))
    personal_best = [0.0 for i in range(0, n_P)]
    for i in range(0, n_P):
        a[i, 0] = random.uniform(0, 0.6)
        a[i, 1] = random.uniform(0.6, 1.2)
        a[i, 2] = random.random()
        a[i, 3] = random.random()

        personal_best[i] = BACP(T_B, n_B, c, s, Switches, Distances, a[i, 0], a[i, 1], a[i, 2], a[i, 3])
        personal_best_coor[i, :] = a[i, :]
    [global_best, global_best_id] = [np.min(personal_best), np.argmin(personal_best)]

    t = 0
    while t <= T_P:
        for i in range(0,n_P):
            for j in range(0,2):
                a[i, j] = 0.8*a[i, j] + 2*(personal_best_coor[i, j] - a[i, j])*random.random() \
                          + 2*(a[global_best_id,j] - a[i, j])*random.random()
            xxx = BACP(T_B, n_B, c, s, Switches, Distances,  a[i, 0], a[i, 1], a[i, 2], a[i, 3])
            if xxx<personal_best[i]:
                personal_best[i] = xxx
                personal_best_coor[i,:] = a[i,:]
        [global_best, global_best_id] = [np.min(personal_best), np.argmin(personal_best)]
        print(t)
        t = t+1

    return a[global_best_id]




if __name__ == '__main__':
    T_P = 30
    T_B = 30
    n_P = 30
    n_B = 30
    c = 4
    s = 24

    sss = PSO_Pra(T_P, T_B, n_P, n_B, c, s, Switches, Distances)
    print(sss)
