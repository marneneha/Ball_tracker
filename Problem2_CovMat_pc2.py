import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt
import pandas as pd

df1 = np.array(pd.read_csv(r'pc2.csv'))
x_data = df1[:,0]
y_data = df1[:,1]
z_data = df1[:,2]
x_mean = np.mean(x_data)
y_mean = np.mean(y_data)
z_mean = np.mean(z_data)
normalised_x_data = x_data-x_mean
normalised_y_data = y_data-y_mean
normalised_z_data = z_data-z_mean
COV_xx = np.dot(normalised_x_data.T, normalised_x_data)/x_data.size
COV_yy = np.dot(normalised_y_data.T, normalised_y_data)/y_data.size
COV_zz = np.dot(normalised_z_data.T, normalised_z_data)/z_data.size
COV_xy = np.dot(normalised_x_data.T, normalised_y_data)/z_data.size
COV_xz = np.dot(normalised_x_data.T, normalised_z_data)/z_data.size
COV_yz = np.dot(normalised_y_data.T, normalised_z_data)/z_data.size
print(f"COV_xx: {COV_xx} COV_yy: {COV_yy} COV_zz: {COV_zz}")
print(f"COV_xy: {COV_xy} COV_xz: {COV_xz} COV_yz: {COV_yz}")
covarance_matrix = np.array([[COV_xx, COV_xy, COV_xz], [COV_xy, COV_yy, COV_yz], [COV_xz, COV_yz, COV_zz]])
print("covariance matrix is")
print(covarance_matrix)
w, v = np.linalg.eig(covarance_matrix)
normal = np.cross(v[:,1], v[:,2])
print("normal is")
print(normal)