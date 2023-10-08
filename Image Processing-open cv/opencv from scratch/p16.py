import cv2
img=cv2.imread('img.jpg')
cv2.imshow('image',img)
img=cv2.circle(img,(350,250),50,(120,0,55),3)
cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()
