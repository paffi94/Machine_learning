#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import math, random

## Only for printing
def x_2(theta, x): 
	return ((theta[0]+theta[1]*x)*(-1/theta[2]))
#--------------


def z(theta, x1x2): # Linearfunktion mit x1 und x2 
	h = theta[0] + (theta[1] * x1x2[0]) + (theta[2] * x1x2[1])
	return h

def sigmoid(theta, x1x2):
	return 1/(1+np.exp(-z(theta,x1x2)))

def stochastic_gradient_descent():
	for i in range(len(x)):
		h_th = sigmoid(theta_val, xy[i,:]) # übergebe das richtige x1x1 (ursprünglich x & y) Paar
		
		for j in range(len(theta_val)):

			# Wenn j == 0 kein x1 oder x2 benötigt
			if j == 0: 
				theta_val[j] = theta_val[j] + alpha * (label[i] - h_th)
			elif j== 1 or j == 2:
				theta_val[j] = theta_val[j] + alpha * (label[i] - h_th) * xy[i][j-1]

###--- MAIN ---###
# Parameter
iteration = 100
alpha = 0.1
theta_val_orig = [random.randint(-10,10)/1000 for x in range(3)]
theta_val = theta_val_orig.copy()

# Read data --- Matrix in "mat"
try:
	mat = np.genfromtxt('data.txt')
except:
	print("Cant open file")
	exit(1)

# Logic ---
x = mat[:,0]
y = mat[:,1]
xy = mat[:,0:2] # sind die x1 und x2 werte in der z funktion
label = mat[:,2] # sind in der Updatefunktion die y - Werte

for run in range(iteration):
	stochastic_gradient_descent() # Run Forest! Run!

print(f"zufällige Start Werte: {theta_val_orig}")
print(f"angepasste End Werte: {theta_val}")

# Plot ---
group_0 = np.matrix([i for i in mat if i[2] == 0])
group_1 = np.matrix([i for i in mat if i[2] == 1])

plt.plot(group_0[:,0],group_0[:,1],'or')
plt.plot(group_1[:,0],group_1[:,1],'og')
plt.plot(x, x_2(theta_val_orig, x), color ="blue")
plt.plot(x, x_2(theta_val, x), color ="black")

plt.show()
