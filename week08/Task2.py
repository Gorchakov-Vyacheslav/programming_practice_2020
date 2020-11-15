import numpy as np
l = np.arange(2, 75, step=1)
l1 = [x for x in l if x%2]
l2 = [x for x in l if x%2]
l3 = list(map(lambda x:-1 if x%2 else x,l))