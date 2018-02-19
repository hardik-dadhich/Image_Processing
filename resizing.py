import cv2
img = cv2.imread('ii.jpg')

#resize image but with blurr
smaller = cv2.pyrDown(img)
#enlarge img but with blurr
larger = cv2.pyrUp(smaller)

cv2.imshow('origional', img)
cv2.imshow('smaller', smaller)
cv2.imshow('larzer', larger)
cv2.waitKey(0)
cv2.destroyAllWindows()

