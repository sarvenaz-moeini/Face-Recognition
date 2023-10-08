import cv2
import numpy as np
img=cv2.imread('logo.jpg')
canny=cv2.Canny(img,500,200)
cv2.imshow('original',img)
cv2.imshow('canny',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Canny() Function in OpenCV is used to detect the edges in an image.