import numpy as np
import matplotlib.pyplot as plt
x = np.array((1, 2, 3, 4, 5, 6))
y = np.array((1,1.42,1.76,2,2.24,2.5))

p1, i = np.polyfit(x, y, deg=1, cov=True)
polynomial_1 = np.poly1d(p1)
y1 = polynomial_1(x)

p2, i = np.polyfit(x, y, deg=2, cov=True)
polynomial_2 = np.poly1d(p2)
y2 = polynomial_2(x)

plt.plot(x, y, '--o')
plt.plot(x, y1, 'r-')
plt.plot(x, y2)
plt.xlim(0, 7)
plt.show()