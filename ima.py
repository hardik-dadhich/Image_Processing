import cv2
input = cv2.imread('ii.jpg')
cv2.imshow('origional', input)
cv2.waitKey()
#cv2.destroyAllWindows()

img2 = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayImg', img2)
cv2.waitKey()
cv2.destroyAllWindows()
