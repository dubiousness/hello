import time
import datetime

def say():
    while True:
        print("now: {0}".format(datetime.datetime.now()))
        time.sleep(10)

def tak(x, y, z):
    if x <= y:
        return z
    return tak(tak(x - 1, y, z), tak(y - 1, z, x), tak(z - 1, x, y))

cpdef int stak(int x, int y, int z) except? -100000:
    if x <= y:
        return z
    return stak(stak(x - 1, y, z), stak(y - 1, z, x), stak(z - 1, x, y))

def sbtak(int x, int y, int z):
    if x <= y:
        return z
    return sbtak(sbtak(x - 1, y, z), sbtak(y - 1, z, x), sbtak(z - 1, x, y))
