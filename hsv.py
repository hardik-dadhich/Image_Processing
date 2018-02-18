import cv2
input = cv2.imread('ii.jpg')
#show origional image
cv2.imshow('origional', input)
cv2.waitKey()

gray_img = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray_img', gray_img)
cv2.waitKey()

hsv_img = cv2.cvtColor(input, cv2.COLOR_BGR2HSV)

cv2.imshow('hsv_image', hsv_img)
cv2.imshow('hue_channel', hsv_img[:, : ,0])
cv2.imshow('channl', hsv_img[:, :, 1])
cv2.imshow('value_channel', hsv_img[:, :, 2])
cv2.waitKey()
cv2.destroyAllWindows()
