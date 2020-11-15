import numpy as np
y = np.random.randint(100,size= 5)
#print(y)
a = np.random.sample()
#print(a)

b = int(y[np.where(np.abs(y-a) == np.abs(y-a).min())])
