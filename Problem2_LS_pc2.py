import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt
import pandas as pd

df1 = np.array(pd.read_csv(r'pc2.csv'))
x_data = np.array([df1[:,0]])
y_data = np.array([df1[:,1]])
z_data = np.array([df1[:,2]])
x_data = x_data.T
y_data = y_data.T
z_data = z_data.T
x_mean = np.mean(x_data)
y_mean = np.mean(y_data)
z_mean = np.mean(z_data)
normalised_x_data = x_data-x_mean
normalised_y_data = y_data-y_mean
normalised_z_data = z_data-z_mean
vec_of_ones = np.ones((y_data.size,1))
X = np.append(x_data, y_data, axis=1)
X = np.append(X, vec_of_ones, axis=1)
Y = z_data
B = np.dot(np.linalg.inv(np.dot(X.T,X)), np.dot(X.T,Y))
print("B matrix is")
print(B)

