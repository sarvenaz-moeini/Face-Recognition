import cv2
import numpy as np
img=cv2.imread('not_declared.jpg')
cv2.imshow('image',img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('image gray',gray)
ret,threshold=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
cv2.imshow('threshold',threshold)
th=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,0)
cv2.imshow('threshold_adaptive',th)
cv2.waitKey(0)
cv2.destroyAllWindows()


#In summary, this code reads an image, displays it along with its grayscale version, 
# applies both fixed and adaptive thresholding operations on the grayscale image,
#  and displays the results in separate windows for visual inspection.
