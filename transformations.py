import cv2
import numpy as np
img = cv2.imread('ii.jpg')

height, width = img.shape[:2]
qu_hi, qu_we =  height/4, width/4

#translation matrix
T = np.float32([[1, 0, qu_we], [0, 1, qu_hi]])

#using warpAffine to transfrom the image into T
img_transation = cv2.warpAffine(img, T, (width,height))
cv2.imshow('Translation', img_transation)
cv2.waitKey()
cv2.destroyAllWindows()
