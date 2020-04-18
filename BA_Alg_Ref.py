import matplotlib.pyplot as plt
import random
import numpy as np
# from TopoInfo_Savvis import *
# from TopoInfo_Rnp import *
# from TopoInfo_ANS import *


def BACP(T, n, c, s, Switches, Distances, fmin, fmax, Beta, Gamma):
    r = 10
    R = [1 for i in range(0,n)]
    A = [10 for i in range(0,n)]
    A_mean = np.sum(A)/n
    OOO = np.ones((1,c)).astype(int)
    ddd = np.ones((1,c))
    LLL = np.ones((1,c))
    # 蝙蝠算法的基本初始量
    x = np.ones((n, 2*c))
    # 坐标初始矩阵x
    v = np.ones((n,2*c))
    # 速度初始矩阵
    O = np.ones((n, c)).astype(int)
    # 索引矩阵O
    D = np.ones((c, s))
    # 与现有离散的部署方案的距离
    LABEL = np.ones((n, s)).astype(int)
    # 交换机与控制器的映射关系
    delay = np.ones((n, s))
    # 计算传输时延中介

    for i in range(0, n):
        # for j in range(0, 2 * c, 2):
        #     x[i, j] = random.uniform(-125, -70)
        # for j in range(1, 2 * c + 1, 2):
        #     x[i, j] = random.uniform(29, 45)
        # # SAVVIS

        # for j in range(0, 2 * c, 2):
        #     x[i, j] = random.uniform(-70, -30)
        # for j in range(1, 2 * c + 1, 2):
        #     x[i, j] = random.uniform(-31, 5)
        # # Rnp

        # for j in range(0, 2 * c, 2):
        #     x[i, j] = random.uniform(-160, -70)
        # for j in range(1, 2 * c + 1, 2):
        #     x[i, j] = random.uniform(20, 50)
        # # ANS

        # for j in range(0, 2 * c, 2):
        #     x[i, j] = random.uniform(-5, 25)
        # for j in range(1, 2 * c + 1, 2):
        #     x[i, j] = random.uniform(40, 61)
        # # Bsonet

        # for j in range(0, 2 * c, 2):
        #     x[i, j] = random.uniform(70, 92)
        # for j in range(1, 2 * c + 1, 2):
        #     x[i, j] = random.uniform(8, 30)
        # # Ernet

        for j in range(0, 2 * c, 2):
            x[i, j] = random.uniform(20, 30)
        for j in range(1, 2 * c + 1, 2):
            x[i, j] = random.uniform(60, 68)
        # Funet
        # 随机生成100组解
        for k in range(0,2*c,2):
            Select_pos = [0 for i in range(0, s)]
            for m in range(0, s):
                controller = [x[i,k],x[i,k+1]]
                Select_pos[m] = np.linalg.norm(controller - Switches[m,:])
            O[i, int(k/2)] = int(np.argmin(Select_pos))
            # 生成离散的部署解
            o = O[i, int(k/2)]
            x[i, k] = Switches[o, 0]
            x[i, k+1] = Switches[o, 1]
            # 根据索引给出100中方案的控制器坐标

    for i in range(0, n):
        for j in range(0, c):
            D[j, :] = Distances[O[i,j],:]
        for k in range(0, s):
            LABEL[i, k] = np.argmin(D[:,k])
            delay[i ,k] = np.min(D[:,k])
    DELAY = (np.sum(delay,axis=1)/s)
    # 根据距离矩阵计算LABEL值和平均时延DELAY

    Best = x[np.argmin(DELAY), :]
    Best_Obj = np.min(DELAY)
    # 计算当前最优的值和坐标


    t = 1
    while t <= T:
        for i in range(0,n):
            for j in range(0, 2*c):
                v[i,j] = v[i, j] + random.uniform(fmin, fmax) * (x[i, j] - Best[j])
        x = x + v

        for i in range(0, n):
            for k in range(0, 2 * c, 2):
                Select_pos = [0 for i in range(0, s)]
                for m in range(0, s):
                    controller = [x[i, k], x[i, k + 1]]
                    Select_pos[m] = np.linalg.norm(controller - Switches[m, :])
                O[i, int(k / 2)] = int(np.argmin(Select_pos))
                # 生成离散的部署解
                o = O[i, int(k / 2)]
                x[i, k] = Switches[o, 0]
                x[i, k + 1] = Switches[o, 1]
                # 根据索引给出100中方案的控制器坐标

        for i in range(0, n):
            for j in range(0, c):
                D[j, :] = Distances[O[i, j], :]
            for k in range(0, s):
                LABEL[i, k] = np.argmin(D[:, k])
                delay[i, k] = np.min(D[:, k])
        DELAY = (np.sum(delay, axis=1) / s)
        # 根据距离矩阵计算LABEL值和平均时延DELAY

        for i in range (0,n):
            rand = random.random()
            if rand > R[i]:
                xxx = x[i] + [random.uniform(-1, 1) for j in range(0,n)] * A_mean
                for k in range(0, 2 * c, 2):
                    Select_pos = [0 for i in range(0, s)]
                    for m in range(0,s):
                        controller = [xxx[k],xxx[k+1]]
                        Select_pos[m] = np.linalg.norm(controller - Switches[m, :])
                    OOO[int(k / 2)] = int(np.argmin(Select_pos))
                    # 生成离散的部署解
                    o = OOO[int(k / 2)]
                    x[i, k] = Switches[o, 0]
                    x[i, k + 1] = Switches[o, 1]
                for j in range(0, c):
                    D[j, :] = Distances[OOO[j], :]
                for k in range(0, s):
                    LLL[k] = np.argmin(D[:, k])
                    ddd[k] = np.min(D[:, k])
                DDD = (np.sum(ddd) / s)
                # 根据距离矩阵计算扰动解的LABEL值和平均时延DELAY（LLL,DDD)
                if rand<A[i] and DDD < Best_Obj:
                    x[i] = xxx
                    DELAY[i] = DDD
                    A[i] = Beta *A[i]
                    R[i] = r * (1 - np.exp(-Gamma*t))
            A_mean = np.mean(A)
            Best = x[np.argmin(DELAY), :]
            Best_Obj = np.min(DELAY)
        t = t+1
    return np.min(DELAY)





if __name__ == '__main__':
    T = 100
    n = 100
    c = 4
    s = 28
    fmin = 20
    fmax = 100
    Beta = 0.5
    Gamma = 0.5
    BACP(T, n, c, s, Switches, Distances, fmin, fmax, Beta, Gamma)
