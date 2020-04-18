import numpy as np
from TopoInfo_Bsonet_Cal import distance

# 重要参数：a1=0.0000519015 a2=5.67699719 G=[-4,25]*[40,61]
Switches = np.array([(14.42076, 50.08804), (8.68333, 50.11667),
                     (10.0, 53.55), (12.56553, 55.67594),
                     (-3.70256, 40.4165), (6.14569, 46.20222),
                     (9.18951, 45.46427), (4.34878, 50.85045),
                     (4.88969, 52.37403), (24.93545, 60.16952),
                     (18.0649, 59.33258), (10.74609, 59.91273),
                     (-0.12574, 51.50853), (2.3488, 48.85341)])

Alpha = [100 for i in range(0, 14)]

Distances = distance