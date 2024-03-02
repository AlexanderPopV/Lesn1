import numpy as np
def closest(vecs,v,r,atoms):
    for i in range(4):
        if np.power(np.sum(np.power(np.subtract(vecs[v],vecs[i]),2)),1/2)<r:
            atoms=atoms+1
    return atoms
vecs=np.array([[1.0, 0.0, 2.0],[-1.0, 0.5, 2.0],[-2.0, 1.5, 0.0],[2.5, -1.2, -0.5], [1.5, 0.2, -0.2]])
print(closest(vecs, 1, 0.1, 0))