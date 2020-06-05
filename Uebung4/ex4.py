#!/usr/bin/env python3

import numpy as np
import imageio
from sklearn import svm
from grid import *
import sys
import glob

def read_images(path):
	img_lst = []
	for image_path in glob.glob(path):
		#print (image_path)
		img = imageio.imread(image_path)
		#R_mean = avg[0], G_mean = avg[1], B_mean = avg[2]
		avg = np.mean(img, axis=(0, 1))
		#R_mean = avg[0], G_mean = avg[1], B_mean = avg[2]
		#R_min, G_min, B_min
		min_val = np.amin(img, axis=(0,1))
		features=[avg[0],avg[1],avg[2],min_val[0],min_val[1],min_val[2]]
		img_lst.append(features)
	return img_lst

def do_this_shit(k, x=0):
	svc = svm.SVC(kernel=k, degree=x, gamma=g, C=c)
	svc.fit(compl_data_list, labels)
	pred_svc = svc.predict(compl_data_list)

	if x:
		print(f"{k} {x} kernel \tNr of SupportVec: {svc.n_support_} \t length pred {len(pred_svc)}")
		for i in range(len(pred_svc)):
			if(pred_svc[i] != labels[i]):
				print (f"\tPrediction fail {k} {x} kernel at {i}")
	else:
		print(f"{k} kernel \tNr of SupportVec: {svc.n_support_} \t length pred {len(pred_svc)}")
		for i in range(len(pred_svc)):
			if(pred_svc[i] != labels[i]):
				print (f"\t Prediction fail {k} kernel at {i}")

	

### --- main --- ###

# Read Data
try:
	neg_lst = read_images("./negatives/*")
	pos_lst = read_images("./positives/*")
except:
	print("problem with image reading")
	exit(1)

# join data
compl_data_list = neg_lst +pos_lst
labels = len(neg_lst)* [0] + len(pos_lst) * [1]

# make data file for find_parameters() from grid
data_file = open("data_file.txt", 'w')
for i in range(len(labels)):
	data_file.write("{} {} {} {} {} {} {}\n".format(labels[i],
													compl_data_list[i][0],
													compl_data_list[i][1],
													compl_data_list[i][2],
													compl_data_list[i][3],
													compl_data_list[i][4],
													compl_data_list[i][5]))
data_file.close()

# get parameters c and g from grid's find_parameters()
save_stdout = sys.stdout
sys.stdout = open('trash', 'w')
rate, param = find_parameters('data_file.txt', '-svmtrain /usr/local/Cellar/libsvm/3.24/bin/svm-train')
sys.stdout = save_stdout

c = param['c']
g = param['g']
print("\n")
print (f"c = {c} and g = {g}")

# --- Make SVM's --- #
# Linear SVM
do_this_shit('linear')
# Polynomiel SVM's
for x in [1,2,3,4]:
	do_this_shit('poly', x)
# Radial Basis SVM
do_this_shit('rbf')
# Sigmoid kernel SVM
do_this_shit('sigmoid')

print("done")

