import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt
import pandas as pd

df1 = np.array(pd.read_csv(r'pc1.csv'))
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

U = np.append(normalised_x_data, normalised_y_data, axis=1)
U = np.append(U, normalised_z_data, axis=1)
TL_Matrix = np.dot(U.T,U)
w, v = np.linalg.eig(TL_Matrix)
B = v[:,0]
print("B is")
print(B)

