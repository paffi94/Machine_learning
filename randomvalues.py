#!/usr/bin/env python3
import math, random
import matplotlib.pyplot as plt

# random artifical data pointpairs (xi,yi) 
# xi in [0,1]
# yi = sin(2pi * xi) + e : e rnd in [-0.3, 0.3]

xPoints = [x/100 for x in range(100)]

yPoints = [math.sin(2*math.pi*x) + random.randint(-30,30)/100 for x in xPoints]

try:
	f = open("values.txt","x")
except:
	print ("File exists")
	exit(1)

for x, y in zip(xPoints,yPoints):
	f.write(f"{x}\t{y}\n")


