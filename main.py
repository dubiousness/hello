import time
import hello

def tak(x, y, z):
    if x <= y:
        return z
    return tak(tak(x - 1, y, z), tak(y - 1, z, x), tak(z - 1, x, y))

start = time.time()
res = tak(20, 10, 0)
t1 = time.time() - start
print("python:\t{0}\t{1}\t{2}".format(t1, res, float(t1/t1)))

start = time.time()
res = hello.tak(20, 10, 0)
t2 = time.time() - start
print("cython:\t{0}\t{1}\t{2}".format(t2, res, float(t1/t2)))

start = time.time()
res = hello.sbtak(20, 10, 0)
t3 = time.time() - start
print("cython:\t{0}\t{1}\t{2}".format(t3, res, float(t1/t3)))

start = time.time()
res = hello.stak(20, 10, 0)
t4 = time.time() - start
print("cython:\t{0}\t{1}\t{2}".format(t4, res, float(t1/t4)))
