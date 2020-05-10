import matplotlib.pyplot as plt
import numpy as np
import sys
### Daten einlesen x, y, label
if len(sys.argv) != 2:
  sys.stderr.write('Usage: {} <inputfile>\n'.format(sys.argv[0]))
  exit(1)

filename = sys.argv[1]
try:
    matrix  = np.genfromtxt(filename, delimiter=" ")
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(filename,err))
  exit(1)

x = matrix[:,0]
y = matrix[:,1]
truelabels=matrix[matrix[:,2] != 0.0]
falselabels=matrix[matrix[:,2] == 0.0]
assert(len(x)==len(y))
assert(len(truelabels)==len(falselabels))
##### z = theta_0 + theta_i * x_i +.....+ theta_n * x_n
def z(theta, x):
    h = 0
    for i in range(len(theta)):
        h += theta[i] * x
    return h

####sigmoid function
def sigmoid(theta, x):
    return 1/(1+np.exp(-z(theta,x)))

def h_theta(theta, x):
    return sigmoid(theta, x)
### stochastic gradient
def stochastic_gradient_descent(x,y,alpha,degree_poly):
    ##initial random theta
    theta = np.random.random(degree_poly)*0.02 - 0.01
    y_prediction = np.zeros(100)
    #error
    #err = np.zeros(iterations)
    for iter in range(100):
        m = 100
        for i in range(m):
            for j in range(degree_poly):
                y_prediction[i] = h_theta(theta,x[i])
                theta[j] = theta[j] + alpha * (y[i] - y_prediction[i]) * x[j]
        #err[iter] = J(theta, y, y_prediction)
        #err[iter] = np.sqrt(2 *(0.5 * np.sum( (y_prediction - y)**2)/m))
    return theta #err

def f(theta, x):
    return (theta[0] +theta[1]*x)*(-1/theta[2])

theta = stochastic_gradient_descent(x,y,0.1,3)
x2=[-3,3]
y2=[f(theta,x2[0]),f(theta,x2[1])]

print(theta)

'''

plt.scatter(truelabels[:,0], truelabels[:,1], marker="o", color="green")
# plt.plot(color="black")
plt.scatter(falselabels[:,0], falselabels[:,1], marker="o", color="red")
# plt.plot(color="black")
plt.plot(x2, y2, color="black")
plt.show()
'''
