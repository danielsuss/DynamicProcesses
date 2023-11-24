import random
import matplotlib.pyplot as plt
from functions import *

lm = 2
c = 1
a = 0.15

fig, axes = plt.subplots(2, 4)

for i in range(4):
    x1 = random.randint(0, 200)
    y1 = random.randint(0, 200)
    X, Y = simulation(x1, y1, lm, c, a, n=30)
    axes[0, i].plot(X, label=f"Host Population {i+1}")
    axes[0, i].set_title(f'Host Population {i+1}, init: {x1}')
    axes[1, i].plot(Y, label=f"Parasite Population {i+1}")
    axes[1, i].set_title(f'Parasite Population {i+1}, init: {y1}')

plt.show()