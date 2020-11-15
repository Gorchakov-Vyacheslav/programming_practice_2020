import random
import numpy as np
n = random.randint(10,100)
y = np.random.randint(100,size=(n,n))

max_el = y.max()
max_el

summ = y.sum()
summ

y = y/max_el

y = y - y.mean(axis=1, keepdims=True)

y[np.where(y == y.max())] = -1