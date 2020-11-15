#y = np.random.randint(-100,100,size=(10,10))
def norm(y):
    return y/max(abs(y.max()),abs(y.min()))