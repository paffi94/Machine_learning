import math, random
import matplotlib.pyplot as plt
import numpy as np

x_values = []
y_values = []

for i in range(100):
    tmp = random.random()
    x_values.append(tmp)
    y_values.append(math.sin(2*math.pi*tmp))



fig, ax = plt.subplots(figsize =(10,6.18))
ax.plot(x_values, y_values, color='blue')
fig.savefig("test.pdf")
