import numpy as np
from TopoInfo_Rnp_Cal import distance

#重要参数a1 = 0.0000483956110 a2 =-0.698411812    G=[-70,-30]*[-31,2]
Switches = np.array([(-34.88111, -8.05389), (-35.73528, -9.66583),
                     (-35.88111, -7.23056), (-34.86306, -7.115),
                     (-47.92972, -15.77972), (-43.93778, -19.92083),
                     (-37.07167, -10.91111), (-38.51083, -12.97111),
                     (-40.33778, -20.31944), (-43.2075, -22.90278),
                     (-60.025, -3.10194), (-49.25389, -16.67861),
                     (-56.09667, -15.59611), (-49.27306, -25.42778),
                     (-51.23, -30.03306), (-48.54917, -27.59667),
                     (-46.63611, -23.5475), (-63.90389, -8.76194),
                     (-67.81, -9.97472), (-48.36028, -10.21278),
                     (-54.64639, -20.44278), (-42.80194, -5.08917),
                     (-35.20944, -5.795), (-60.67333, 2.81972),
                     (-51.06639, 0.03889), (-48.50444, -1.45583),
                     (-44.30278, -2.52972), (-38.54306, -3.71722)])

Alpha = [100 for i in range(0, 28)]

Distances = distance
