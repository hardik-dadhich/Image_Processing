import cv2
import numpy as np

img = cv2.imread('hardik.png', 0)
cv2.imshow('origional', img)
cv2.waitKey()

# deine the kernal size
ker = np.ones((5,5), np.uint8)
#now erode fin

erosion = cv2.erode(img, ker, iterations = 1)
cv2.imshow('erosion', erosion)
cv2.waitKey()

dialute = cv2.dilate(img, ker, iterations = 2)
cv2.imshow('dialatiohn', dialute)
cv2.waitKey()
cv2.destroyAllWindows()



