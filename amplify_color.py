import cv2
img = cv2.imread('ii.jpg')
cv2.imshow('originaol', img)
cv2.waitKey()

B, G, R = cv2.split(img)

     
merged = cv2.merge([B+100, G, R])
cv2.imshow('amplfies', merged)
cv2.waitKey()
cv2.destroyAllWindows()
