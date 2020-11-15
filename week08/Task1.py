import timeit
import numpy as np
import matplotlib.pyplot as plt
#Списками
def z(x,y):
    x = [randint(1,10) for i in range(10)]
    y = [randint(1,10) for i in range(10)]
    z = 2*x**2 + 4*y
    return z
r= []
for i in range(1,10):
    r.append(timeit.timeit("z", setup="from __main__ import z", number=1))
#Numpy
def z1(x,y):
    x = np.random.randint(1, 10, size = (10,10))
    y = np.random.randint(1, 10,size =(10,10))
    z = 2*np.dot(x,x) + 4*y
    return z
l = []
for i in range(1,10):
    l.append(timeit.timeit("z1", setup="from __main__ import z1", number=1))

plt.plot(l)
plt.plot(r)

plt.show()


import timeit
import numpy as np
import matplotlib.pyplot as plt
#Списками
def matrix_m(x,y):
    x = [[random.randrange(1,10) for i in range(30)] for j in range(30)]
    y = [[random.randrange() for i in range(30)] for j in range(30)]
    z = x*y
r= []
for i in range(1,10):
    r.append(timeit.timeit("matrix_m", setup="from __main__ import matrix_m", number=1))
#Numpy
def matrix_m_numpy():
    x = np.random.randint(1, 10, size = (30,30))
    y = np.random.randint(1, 10, size = (30,30))
    z = np.dot(x,y)
    return z
l = []
for i in range(1,10):
    l.append(timeit.timeit("matrix_m_numpy", setup="from __main__ import matrix_m_numpy", number=1))

plt.plot(l)
plt.plot(r)

plt.show()
