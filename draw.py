import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
X=np.arange(1,10,1)
Y=np.arange(1,20,1)
X, Y = np.meshgrid(X, Y)
Z = X**3 + Y**2
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
         cmap=cm.jet,linewidth=0, antialiased=False)
ax.set_zlim3d(0,1000)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()