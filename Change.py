import math
# EARTH_REDIUS = 6378.137

def rad(d):
    return d * math.pi / 180.0

def getDistance(lng1, lat1, lng2, lat2 ):
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a/2), 2) + math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b/2), 2)))
    s = s * 6371.393
    return s

if __name__ == '__main__':
    print(getDistance(39.55,116.24,31.14, 121.29 ))