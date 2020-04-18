import matplotlib.pyplot as plt
import math
import random
# from TopoInfo_Savvis import *
from TopoInfo_Rnp import *

n = 100
T = 100
c = 5
s = 28


def FACP(T, n, c, s, Switches, Distances):
    x = np.ones((n, 2*c)).astype(int)
    # 坐标初始矩阵x
    O = np.ones((n, c)).astype(int)
    # 索引矩阵O
    D = np.ones((c, s)).astype(int)
    # 与现有离散的部署方案的距离
    LABEL = np.ones((n, s)).astype(int)
    # 交换机与控制器的映射关系
    delay = np.ones((n, s)).astype(int)
    for i in range(0, n):
        for j in range(0, 2 * c, 2):
            x[i, j] = random.uniform(-70, -30)
        for j in range(1, 2 * c + 1, 2):
            x[i, j] = random.uniform(-31, 5)
        # for j in range(0, 2 * c, 2):
        #     x[i, j] = random.uniform(-125, -70)
        # for j in range(1, 2 * c + 1, 2):
        #     x[i, j] = random.uniform(29, 45)
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

    t = 1
    Des = np.ones((100,1)).astype(int)
    DesFill = np.ones((100,1)).astype(int)
    while t <= T:
        print(mmm, t)
        if (3*T/5 - t) > 0:
            Ri = 3*T/5 - t+10
        else:
            Ri = 10

        for i in range(0, n):
            B = [0 for k in range(0, n)]
            for j in range(0, n):
                B[j] = DELAY[j]*math.exp(Ri*(0.001)*np.linalg.norm(x[i,:]-x[j,:]))
            Des[i,:] = np.argmin(B)
            DesFill[i,:] = np.min(B)
        # print(Des)

        for i in range(0,n):
            rand_mov = [random.random() for j in range(0,2*c)]
            x[i,:] = (x[Des[i,:],:]-x[i,:])*(t/T)+x[i,:]+1.6*((T-0.9*t)/T)*np.array(rand_mov)

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

        t = t+1

    # c1x=x[:,0]
    # c1y=x[:,1]
    # c2x=x[:,2]
    # c2y=x[:,3]
    # c3x=x[:,4]
    # c3y=x[:,5]
    # c4x=x[:,6]
    # c4y=x[:,7]
    # plt.scatter(c1x, c1y, c = 'red')
    # plt.scatter(c2x, c2y,c = 'blue')
    # plt.scatter(c3x, c3y,c = 'black')
    # plt.scatter(c4x, c4y,c = 'deeppink')
    # plt.show()
    # print(np.min(DELAY),x[np.argmin(DELAY),:],LABEL[np.argmin(DELAY),:])
    # 输出全局平均实验最低值,控制器坐标,以及控制器-交换机的映射关系
    # print(x)


    # LLL[mmm, :] = LABEL[np.argmin(DELAY),:]
    # for i in range(0, s):
    #     if LLL[mmm, i] == 0:
    #         PPP[mmm, 0] = PPP[mmm, 0] + 1
    #     elif LLL[mmm, i] == 1:
    #         PPP[mmm, 1] = PPP[mmm, 1] + 1
    #     elif LLL[mmm, i] == 2:
    #         PPP[mmm, 2] = PPP[mmm, 2] + 1
    #     else:
    #         PPP[mmm, 3] = PPP[mmm, 3] + 1

    DDD[mmm, :] = np.min(DELAY)/200
    for i in range(0, n):
        print(DELAY[i]/200)



if __name__ == '__main__':

    # LLL = np.ones((5, s))
    # PPP = np.zeros((5, c))
    DDD = np.ones((1, 1))
    for mmm in range(0,1):
        FACP(T,n,c,s,Switches,Distances)
    print(DDD.mean())
