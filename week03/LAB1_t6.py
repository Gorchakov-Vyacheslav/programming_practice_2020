x = np.arange(-2, 2, 0.001)
a = float(input())
b = float(input())
n = int(input())
s = float(0)

for i in range(0, n+1):
    s += b**i * np.cos(a**i * np.pi * x)
plt.plot(x, s)
plt.show()