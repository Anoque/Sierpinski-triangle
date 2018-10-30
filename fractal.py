import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import time

def init():
    return ln,

def update(frame):
    global current, n, iteration
    
    t = random.randint(1, n)

    if n == 3:
        coord = [(current[0] + first_points[t-1][0]) / 2, (current[1] + first_points[t-1][1]) / 2]
    else:
        coord = [(current[0] + 2 * first_points[t-1][0]) / 3, (current[1] + 2 * first_points[t-1][1]) / 3]

    xdata.append(coord[0])
    ydata.append(coord[1])
    ln.set_data(xdata, ydata)
    
    current = coord
    iteration += 1
    
    return ln,

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro', animated=True)
current = [1.0, 1.0]
last_t = 1
iteration = 0

print("Input 3 for triangle or 4 for carpet:")
n = int(input())

first_points = [
    [10, 10],
    [10, -10],
    [-10, -10],
    [-10, 10]
]

for i in range(n):
    if n == 3:
        temp = [random.randint(-100, 100), random.randint(-100, 100)]
        print(temp)
    else:
        temp = first_points[i]
    
    first_points[i] = temp
    plt.scatter(temp[0], temp[1])

ani = FuncAnimation(fig, update, frames=np.linspace(0, 10000, 10000), init_func=init, interval=1, blit=True)
plt.show()