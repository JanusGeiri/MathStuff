from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

Q = np.linspace(0, 20*np.pi, 1000)

x = [np.cos(np.sin(q)) for q in Q]
y = [np.sin(np.sin(q)) for q in Q]
z = 0


ax.plot(x, y, z, c='r')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')


plt.savefig('mynd.png')
plt.show()
