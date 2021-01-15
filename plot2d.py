import matplotlib.pyplot as plt
import numpy as np

T = np.linspace(0, 2*np.pi, 1000)


def r(theta):
    return 1-np.sin(theta)


def r2(theta):
    return np.sin(theta)


def plotterx(f, theta):
    return f(theta)*np.cos(theta)


def plottery(f, theta):
    return f(theta)*np.sin(theta)


graph1x = [plotterx(r, theta) for theta in T]
graph1y = [plottery(r, theta) for theta in T]

plt.plot(graph1x, graph1y)
plt.show()
