import cv2
import numpy as np
img=cv2.imread('cat.jpg')
cv2.imshow('image1',img)
pts=np.array([[50,100],[120,200],[250,100],[400,20]])
img=cv2.polylines(img,[pts],False,(255,255,255),3)
cv2.imshow('image2',img)
cv2.waitKey()
cv2.destroyAllWindows()
