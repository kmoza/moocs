import cv2
import numpy as np

# create a black image using numpy
blackImage = np.zeros([150, 200, 1], 'uint8')

# create a white image using numpy
whiteImage = np.ones([150, 200, 3], 'uint16')
whiteImage *= (2**16 - 1)

cv2.imshow("Black", blackImage)
cv2.imshow("White", whiteImage)

color = whiteImage.copy()
color[:, :] = (255, 0, 0)
cv2.imshow("Blue", color)
cv2.waitKey(0)
