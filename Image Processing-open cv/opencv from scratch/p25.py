import cv2
import numpy as np
img1=cv2.imread('img.jpg')
img2=cv2.imread('cat.jpg')
width=img1.shape[1]
height=img1.shape[0]
img3=cv2.resize(img2,(width,height))
add=cv2.addWeighted(img1,0.2,img3,0.8,0)
cv2.imshow('image',add)
cv2.waitKey()
cv2.destroyAllWindows()
