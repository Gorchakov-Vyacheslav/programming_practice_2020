a = 7
b = 3
n = np.random.randint(1, 100)
m = np.random.randint(1, 100)
y = np.full((m, n), a, dtype = int)
#print(y)

y[:,[0,-1]] = b
y[[0,-1]] = b
#y