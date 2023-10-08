import cv2
import numpy as np
img=cv2.imread('logo.jpg')
sobelx=cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3) # applies the Sobel operator in the x-direction to detect horizontal edges in the image.
sobely=cv2.Sobel(img,cv2.CV_8U,0,1,ksize=5) #applies the Sobel operator in the y-direction to detect vertical edges in the image.
cv2.imshow('original',img)
cv2.imshow('sobelx',sobelx)
cv2.imshow('sobely',sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()


#This code performs edge detection using the Sobel operator 
# on an image and displays the original image, as well as the 
# horizontal and vertical edges detected


#Overall, this code reads an image file, applies Sobel edge detection
#  in both x and y directions, and displays three windows 
# showing the original image and detected horizontal and vertical edges.



#Sobel uses horizontal and vertical kernels,
#  while Laplacian uses one symmetrical kernel.