import numpy as np

def y(x):
    return np.log((np.exp(1/(np.sin(x)+1)))/(5/4+1/(x**15)))/np.log(1+x**2)

print(y(1),y(10),y(1000))