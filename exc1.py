import matplotlib.pyplot as plt
import numpy as np

#### random data set
def generate_random():
    sample_size = 100
    x_values = np.sort(np.random.random(sample_size))
    #random noise (b - a) * random_sample() + a
    epsilon = np.random.random(sample_size) * 0.6 - 0.3
    y_values = np.sin(x_values * 2 * np.pi)+epsilon
    return x_values, y_values

x, y = generate_random()

### prediction model h_theta
def h_theta(theta, x_i):
    h_theta = 0
    for i in range(len(theta)):
        h_theta += theta[i] * x_i**i
    return h_theta
##############
#def J(theta, y, pred_y):
    #return 0.5 * np.sum( (pred_y - y)**2 )

### stochastic gradient
def stochastic_gradient_descent(x,y,alpha,degree_poly, iterations):
    ##initial random theta
    theta = np.random.random(degree_poly) - 0.5
    y_prediction = np.zeros(100)
    #error
    err = np.zeros(iterations)
    for iter in range(iterations):
        m = 100
        for i in range(m):
            for j in range(degree_poly):
                y_prediction[i] = h_theta(theta, x[i])
                theta[j] = theta[j] + alpha * (y[i] - y_prediction[i]) * x[i]**j
        #err[iter] = J(theta, y, y_prediction)
        err[iter] = np.sqrt(2 *(0.5 * np.sum( (y_prediction - y)**2)/m))
    return theta, err

####training set
theta_j, err = stochastic_gradient_descent(x,y,0.01,10,10000)
y_model = np.zeros(100)
for i in range(100):
    y_model[i] = h_theta(theta_j, x[i])

### Plot settings
fig, ax = plt.subplots(figsize =(10,6.18))
ax.grid(True)
plt.figure(1)
ax.scatter(x, y, color='c', marker =".",label="input data")
ax.plot(np.arange(0,1,0.01), np.sin(2 * np.pi * np.arange(0,1,0.01)),
        color="green", label="sine")#
ax.plot(x, y_model, color="m", label="calculated model")
ax.legend(loc="upper right")

fig.savefig("A1.pdf")
plt.figure(2)
#plt.xlabel('iteration')
#plt.ylabel('error')
fig, ax = plt.subplots(figsize =(10,6.18))
ax.plot(err, color="r",label="error")
fig.savefig("error.pdf")
