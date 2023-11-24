import random
import matplotlib.pyplot as plt
from functions import *

lm = 2
c = 1
a = 0.15

fig, axes = plt.subplots(1, 4)

for i in range(4):
    x1 = random.randint(0, 200)
    y1 = random.randint(0, 200)
    X, Y = simulation(x1, y1, lm, c, a, n=1000)
    axes[i].scatter(X, Y, label=f"Host Population {i+1}")
    axes[i].set_title(f'{i+1}, init: x={x1}, y={y1}')

plt.show()