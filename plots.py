import numpy as np
from matplotlib import pyplot as plt
import math


def f(x):
    return math.exp(x)


X = np.linspace(-5, 5, 1000)
Y = [f(x) for x in X]


plt.plot(X, Y)
plt.show()
