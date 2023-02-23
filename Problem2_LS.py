import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt
import pandas as pd

df1 = np.array(pd.read_csv(r'pc1.csv'))
df2 = pd.read_csv('pc2.csv')
# print(df1)
# print(df1)
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
print(f"x: {x_data} y: {y_data} z: {z_data} vec_of_ones: {vec_of_ones}")
X = np.append(x_data, y_data, axis=1)
X = np.append(X, vec_of_ones, axis=1)
Y = z_data
print(f"x: {X} y: {Y}")
B = np.dot(np.linalg.inv(np.dot(X.T,X)), np.dot(X.T,Y))
print("B matrix is")
print(B)
# fig = plt.figure()
# ax = plt.add_subplot(projection='3d')
# ax.plot3D(x_data, y_data, z_data, 'gray')
# ax.scatter3D(x_data, y_data, z_data, c=z_data, cmap='Greens')
# plt.show()

