import cv2
import numpy as np

square = np.zeros((300,300), np.uint8)
#making  a rectangle image
cv2.rectangle(square, (50,50), (250,250), 250, -1)
cv2.imshow('rectangle', square)
cv2.waitKey()
#making a eclipes image
eclips = np.zeros((300,300), np.uint8)
cv2.ellipse(eclips, (150,150), (150,150), 30, 0,180, 255, -1)
cv2.imshow("eclipse", eclips)
cv2.waitKey()


#perorming bitwise and operation
And = cv2.bitwise_and(square, eclips)
cv2.imshow('and_img', And)
cv2.waitKey(0)

#performing bitwisw or operation
Or = cv2.bitwise_or(square, eclips)
cv2.imshow('or_img', Or)
cv2.waitKey()

#perorming bitwise Xor operations
Xor = cv2.bitwise_xor(square, eclips)
cv2.imshow('Xor_img', Xor)
cv2.waitKey()

#performing not operation
b_Not = cv2.bitwise_not(square,eclips)
cv2.imshow('NOt_img', b_Not)
cv2.waitKey()


cv2.destroyAllWindows()


