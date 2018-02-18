import cv2
import numpy as np

from matplotlib import pyplot as plt

image = cv2.imread('ii.jpg')
cv2.imshow('origional', image)
cv2.waitKey()

histogram = cv2.calcHist([image], [0], None, [256], [0,256])

#plot histoogram using ravel function

plt.hist(image.ravel(),256, [0, 256]);plt.show()

#viewing seperate color chnnels
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histogram2 = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram2, color = col)
    plt.xlim([0,256])


plt.show()    
    
