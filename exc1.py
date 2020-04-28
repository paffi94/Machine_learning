import matplotlib.pyplot as plt
import numpy as np

def generate_random():
    sample_size = 100
    x_values = np.sort(np.random.random(sample_size))
    #random noise (b - a) * random_sample() + a
    epsilon = np.random.random(sample_size) * 0.6 - 0.3
    y_values = np.sin(x_values * 2 * np.pi)+epsilon
    return x_values, y_values

x, y = generate_random()

### Plot settings
fig, ax = plt.subplots(figsize =(10,6.18))
ax.grid(True)
ax.scatter(x, y, color='c', marker =".",label="input data")
ax.plot(np.arange(0,1,0.01), np.sin(2 * np.pi * np.arange(0,1,0.01)),
        color="green", label="sine")
ax.legend(loc="upper right")
fig.savefig("A1.pdf")
