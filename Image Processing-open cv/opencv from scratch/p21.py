import cv2
import numpy as np
img=cv2.imread('img.jpg',cv2.IMREAD_COLOR)
img[100:200,100:200]=[0,0,255]
cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()
