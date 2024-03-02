import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x=np.linspace(-5*np.pi,5*np.pi,10**7)
y1=np.random.normal(-10,7,10**7)
y2=np.random.normal(10,5,10**7)
y3=np.random.normal(25,10,150)
y=np.concatenate([y1,y2,y3])
plt.hist(y,range=(-5*np.pi, 5*np.pi),bins=100,density=True)
plt.show()