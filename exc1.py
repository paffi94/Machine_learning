import matplotlib.pyplot as plt
import numpy as np

def generate_random():
    sample_size = 100
    x_values = np.sort(np.random.random(sample_size))
    #random noise
    epsilon = np.random.uniform(-0.3,0.3)
    y_values = np.sin(x_values * 2 * np.pi)+epsilon
    return x_values, y_values

x, y = generate_random()



fig, ax = plt.subplots(figsize =(10,6.18))
ax.plot(x, y, color='blue')
fig.savefig("A1.pdf")
