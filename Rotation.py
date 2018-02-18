import cv2

img = cv2.imread('ii.jpg')
height, width = img.shape[:2]

#divide by 2 to rotating the image with its center
#here i  choose .5 for fit display in screen size
rotation_matrix  = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)

rotated_img = cv2.warpAffine(img, rotation_matrix, (width,height))

#now pass the rotated image to transpose funtion to fitted
cv2.transpose(img)
cv2.imread('transpose image', rotated_img)
cv2.waitKey()
cv2.destroyAllWindows()
