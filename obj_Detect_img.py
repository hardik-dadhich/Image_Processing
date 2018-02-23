import cv2
import numpy as np

img = cv2.imread('find_pep.jpg')
cv2.imshow('origional imag', img)
cv2.waitKey()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#load template image
template = cv2.imread('find_pep_tem.jpg', 0)

#template matching
result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF) #this is the method of finding img
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#creating bounding box arround the match

top_left = max_loc
bottom_right = (top_left[0] + 70, top_left[1] + 50)
cv2.rectangle(img, top_left, bottom_right, (0,0,255), 5)

#show the img
cv2.imshow('found_img', img)
cv2.waitKey()
cv2.destroyAllWindows()
