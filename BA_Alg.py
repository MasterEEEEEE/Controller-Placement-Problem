import matplotlib.pyplot as plt
import random
# from TopoInfo_ANS import *
# from TopoInfo_Bsonet import *
# from TopoInfo_Ernet import *
# from TopoInfo_Funet import *
from TopoInfo_Rnp import *
# from TopoInfo_Savvis import *

n = 40
T = 45
c = 4
s = 28
# fmin = -0.56382868
# fmax = -0.09450248
# Beta = 0.75304097
# Gamma = 0.38183858
# # SAVVIS的参数

fmin = -0.03946731
fmax = -0.50748953
Beta = 0.47603857
Gamma = 0.61752558
# Rnp的参数

# fmin = 0.10290294
# fmax = 0.37846481
# Beta = 0.18330422
# Gamma = 0.74546022
# # ANS的参数

# fmin = 0.2282425
# fmax = 0.67364989
# Beta = 0.89923318
# Gamma = 0.97173117
# # Bsonet的参数

# fmin = 0.16590739
# fmax = 0.4291139
# Beta =  0.17709363
# Gamma = 0.65957418
# # Ernet的参数

# fmin = -0.84839614
# fmax = 0.27410772
# Beta = 0.18536283
# Gamma = 0.89195266
# # Funet的参数


def BACP(T, n, c, s, Switches, Distances, fmin, fmax, Beta, Gamma):
    r = 10
    R = [1 for i in range(0, n)]
    A = [10 for i in range(0, n)]
    A_mean = np.sum(A) / n
    OOO = np.ones((1, c)).astype(int)
    ddd = np.ones((1, c))
    LLL = np.ones((1, c))
    # 蝙蝠算法的基本初始量
    x = np.ones((n, 2 * c))
    # 坐标初始矩阵x
    v = np.ones((n, 2 * c))
    # 速度初始矩阵
    O = np.ones((n, c)).astype(int)
    # 索引矩阵O
    D = np.ones((c, s))
    # 与现有离散的部署方案的距离
    LABEL = np.ones((n, s)).astype(int)
    # 交换机与控制器的映射关系
    delay = np.ones((n, s))
    delay_tmp = np.ones((c, c))
    delay_cs_mean = np.ones((n, 1))
    delay_cs_max = np.ones((n, 1))
    delay_cc_mean = np.ones((n, 1))
    delay_cc_max = np.ones((n, 1))
    DELAY = np.ones((n, 1))

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

    for i in range(0,n):
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
        for j in range(0, c):
            for k in range(0, c):
                delay_tmp[j, k] = distance[O[i, j],O[i, k]]
        delay_cc_mean[i, 0] = np.sum(delay_tmp)/(c*(c-1))
        delay_cc_max[i, 0] = np.max(delay_tmp)
    delay_cs_mean = np.sum(delay, axis=1)/s
    delay_cs_max = np.max(delay, axis=1)
    for i in range(0, n):
        DELAY[i] = 1 * delay_cs_mean[i] + 0 * delay_cs_max[i] + 0 * delay_cc_mean[i] + 0 * delay_cc_max[i]
    # print(DELAY)
    # 根据距离矩阵计算LABEL值和平均传输时延DELAY
    Best = x[np.argmin(DELAY), :]
    Best_Obj = np.min(DELAY)
    # 计算当前最优的值和坐标

    t = 1
    while t <= T:
        print(mmm, t)
        for i in range(0, n):
            for j in range(0, 2 * c):
                v[i, j] = v[i, j] + random.uniform(fmin, fmax) * (x[i, j] - Best[j])
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
            for j in range(0, c):
                for k in range(0, c):
                    delay_tmp[j, k] = distance[O[i, j], O[i, k]]
            delay_cc_mean[i, 0] = np.sum(delay_tmp) / (c * (c - 1))
            delay_cc_max[i, 0] = np.max(delay_tmp)
        delay_cs_mean = np.sum(delay, axis=1) / s
        delay_cs_max = np.max(delay, axis=1)
        # print(delay_cs_max,delay_cs_mean,delay_cc_max,delay_cc_mean)
        for i in range(0, n):
            DELAY[i] = 1 * delay_cs_mean[i] + 0 * delay_cs_max[i] + 0 * delay_cc_mean[i] + 0 * delay_cc_max[i]
        # 根据距离矩阵计算LABEL值和平均时延DELAY

        for i in range(0, n):
            rand = random.random()
            if rand > R[i]:
                xxx = x[i] + [random.uniform(-1, 1) for j in range(0, n)] * A_mean
                for k in range(0, 2 * c, 2):
                    Select_pos = [0 for i in range(0, s)]
                    for m in range(0, s):
                        controller = [xxx[k], xxx[k + 1]]
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
                if rand < A[i] and DDD < Best_Obj:
                    x[i] = xxx
                    DELAY[i] = DDD
                    A[i] = Beta * A[i]
                    R[i] = r * (1 - np.exp(-Gamma * t))
            A_mean = np.mean(A)
            Best = x[np.argmin(DELAY), :]
            Best_Obj = np.min(DELAY)
        t = t + 1

    # c1x=x[:, 0]
    # c1y=x[:, 1]
    # c2x=x[:, 2]
    # c2y=x[:, 3]
    # c3x=x[:, 4]
    # c3y=x[:, 5]
    # c4x=x[:, 6]
    # c4y=x[:, 7]
    # plt.scatter(c1x, c1y, c = 'red')
    # plt.scatter(c2x, c2y,c = 'blue')
    # plt.scatter(c3x, c3y,c = 'black')
    # plt.scatter(c4x, c4y,c = 'deeppink')
    # plt.show()
    # print(np.min(DELAY),x[np.argmin(DELAY),:],LABEL[np.argmin(DELAY),:])
    # 输出全局平均实验最低值,控制器坐标,以及控制器-交换机的映射关系
    # print(x)

    DDDDD[mmm, :] = np.min(DELAY) / 200
    C_S_MEAN[mmm, :] = delay_cs_mean[np.argmin(DELAY)]/200
    C_S_MAX[mmm, :] = delay_cs_max[np.argmin(DELAY)]/200
    C_C_MEAN[mmm, :] = delay_cc_mean[np.argmin(DELAY)]/200
    C_C_MAX[mmm, :] = delay_cc_max[np.argmin(DELAY)]/200
    # print(x[np.argmin(DELAY),:])
    # for i in range(0, n):
    #     print(DELAY[i] / 200)
    #
    # print(O)
    # LLLLL[mmm, :] = LABEL[np.argmin(DELAY), :]
    # XXXXX[mmm, :] = x[np.argmin(DELAY), :]


if __name__ == '__main__':

    TTT = 100
    DDDDD = np.ones((TTT, 1))
    C_S_MEAN = np.ones((TTT, 1))
    C_S_MAX = np.ones((TTT, 1))
    C_C_MEAN = np.ones((TTT, 1))
    C_C_MAX = np.ones((TTT, 1))
    # LLLLL = np.ones((TTT, s))
    # XXXXX = np.ones((TTT, 2*c))
    for mmm in range(0, TTT):
        BACP(T, n, c, s, Switches, Distances, fmin, fmax, Beta, Gamma)
    # print(DDDDD)
    print(DDDDD.mean(), C_S_MEAN.mean(), C_S_MAX.mean(), C_C_MEAN.mean(), C_C_MAX.mean())
    # print(LLLLL[np.argmin(DDDDD), :])
    # print(XXXXX[np.argmin(DDDDD), :])
