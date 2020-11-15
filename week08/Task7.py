a = np.arange(10,100,1)
np.save('saved_a',a)
loaded_a = np.load('saved_a.npy')
loaded_a