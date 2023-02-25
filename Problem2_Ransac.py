import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt
import pandas as pd
import math 
import random

df1 = np.array(pd.read_csv(r'pc1.csv'))
data = np.array([df1])
x_data = np.array([df1[:,0]])
y_data = np.array([df1[:,1]])
z_data = np.array([df1[:,2]])
x_data = x_data.T
y_data = y_data.T
z_data = z_data.T
x_mean = np.mean(x_data)
y_mean = np.mean(y_data)
z_mean = np.mean(z_data)
Data_points_to_give_ip = np.append(x_data, y_data, axis=1)
Data_points_to_give_ip = np.append(Data_points_to_give_ip, z_data, axis=1)
p = 0.95
t = 13
num_outlier = 6
max_inlier_count = 0
e = num_outlier/x_data.size
min_num_data_points = 3 
N = int(math.log(1-p)/math.log(1-(1-e)**min_num_data_points))
def LS_Sol (rand_data_points):
    x_data = np.array([rand_data_points[:,0]])
    y_data = np.array([rand_data_points[:,1]])
    z_data = np.array([rand_data_points[:,2]])
    vec_of_ones = np.ones((y_data.size,1))
    X = np.append(x_data, y_data, axis=1)
    X = np.append(X, vec_of_ones, axis=1)
    Y = z_data
    B = np.dot(np.linalg.inv(np.dot(X.T,X)), np.dot(X.T,Y))
    return B
for i in range(N):
    inlier_count = 0
    rand_data_points = random.sample(data, min_num_data_points)
    equ_of_plane = LS_Sol(rand_data_points)
    y_from_equ_of_plane = np.dot(Data_points_to_give_ip, equ_of_plane)
    error = np.linalg.norm(y_from_equ_of_plane-z_data)
    if distance <= t:
        inlier_count +=1
if inlier_count > max_inlier_count:
    max_inlier_count = inlier_count
    best_model = equ_of_plane    
    