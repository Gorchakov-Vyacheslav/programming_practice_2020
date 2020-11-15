def sortmatrix(y):
    column = int(input())
    y = y[y[:,column].argsort()[::-1]]
    return y
#y = np.random.randint(1, 10, size = (5,5))
#print(y)
#print(sortmatrix(y))