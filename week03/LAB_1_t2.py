import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-10, 10.01, 0.01)
plt.plot(x, x*x-x-6)
plt.xlim(-2.5,3.5)
plt.show()