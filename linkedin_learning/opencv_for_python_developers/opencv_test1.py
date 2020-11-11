import numpy as np 
import cv2
img = cv2.imread("opencv-logo.png")
print(img)

# number of rows in numpy.ndarray
print(len(img))

# number of columns in numpy.ndarray
print(len(img[0]))

# number of channels in an image i.e. RGB channels
print(len(img[0][0]))

print(img.shape)

print(img.dtype)

# print the pixel value in RGB components
print(img[10, 5])
