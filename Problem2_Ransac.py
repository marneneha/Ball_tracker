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

