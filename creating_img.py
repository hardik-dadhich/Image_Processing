import cv2
import numpy as np

#creating a black image
image = np.zeros((512, 512, 3), np.uint8)

#making this image black and white
image_bw = np.zeros((512, 512), np.uint8)

#image show
cv2.imshow('black object', image)
cv2.imshow('black and white', image_bw)
cv2.waitKey()
#making line of thickness 5
cv2.line(image, (0,0), (240,540), (211,45,88), 5)

cv2.imshow('line show', image)
cv2.waitKey()

#making circle
cv2.circle(image, (330,440), 100, (22,200, 144), -1)
cv2.imshow('circle', image)
cv2.waitKey()
#show rectangel
cv2.rectangle(image, (240,300), (700,390), (30,99,100), -1)
cv2.imshow('rectangle', image)
cv2.waitKey()
cv2.destroyAllWindows()
