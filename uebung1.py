#! /usr/bin/env python3

import math, random
import matplotlib.pyplot as plt
import numpy as np
import os



def read_file(data):
	for line in data:
		x,y = line.split("\t")
		x.strip()
		y.strip()
		x_val.append(float(x))
		y_val.append(float(y))

def h_theta(x, theta_list):
	value = 0
	for j in range(len(theta_list)):
		value += theta_list[j] * x ** j
	return value

def loop():
	for i in range(100):
		h_th = h_theta(x_val[i],theta_val)
		for j in range(len(theta_val)):
			theta_val[j] = theta_val[j] + alpha * (y_val[i] - h_th) * (x_val[i]**j)

def e_theta():
	summe = 0
	for x,y in zip(x_val,y_val):
		summe += (h_theta(x, theta_val) - y) ** 2
	return 0.5 * summe

def erms():
	return math.sqrt((2 * e_theta())/len(x_val))

#--------- main ----------#

x_val = []
y_val = []

iteration = 10000 
alpha = 0.001
poly_grade = 4
theta_val_orig = [random.randint(-5,5)/10 for x in range(poly_grade + 1)]
theta_val = theta_val_orig.copy()

try:
	data = open("values.txt","r")
	read_file(data)
except:
	print("Generate new rnd-value file")
	x_val = [random.randint(0,100)/100 for x in range(100)]
	x_val.sort()
	y_val = [math.sin(2*math.pi*x) + random.randint(-30,30)/100 for x in x_val]

	try:
		f = open("values.txt","x")
		for x, y in zip(x_val,y_val):
			f.write(f"{x}\t{y}\n")
		f.close
	except:
		print ("File handle error")
		exit(1)

#----- logic -----#

print (f"[6")

error_val = []

for i in range(iteration):
	loop()
	error_val.append(erms())

#----- plot -----#
fig, ax = plt.subplots(figsize =(10,6.18))
ax.grid(True)
ax.scatter(x_val, y_val, color='c', marker =".",label="input data")
ax.plot(np.arange(0,1,0.01), np.sin(2 * np.pi * np.arange(0,1,0.01)),
        color="green", label="sine")
ax.plot(np.arange(0,1,0.01), h_theta(np.arange(0,1,0.01), theta_val_orig),
        color="black", label="h_start")
ax.plot(np.arange(0,1,0.01), h_theta(np.arange(0,1,0.01), theta_val),
        color="blue", label="h_end")
ax.legend(loc="upper right")
fig.savefig("A1.pdf")

fig2, ax2 = plt.subplots(figsize =(10,6.18))
ax2.plot(np.arange(0,iteration,1), error_val, 'k')
ax2.legend(loc="upper right")
fig2.savefig("A2.pdf")

plt.show()
