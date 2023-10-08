import cv2
import numpy as np
def showimage(img):               # 2 YELLOW CIRCLES INSIDE EACHOTHER
  cv2.imshow('img',img)
  cv2.waitKey()
  cv2.destroyAllWindows()
img=np.zeros((500,500,3))
img=cv2.circle(img,center=(250,250),radius=10,color=(0,255,255),thickness=3)
img=cv2.circle(img,center=(250,250),radius=50,color=(0,255,255),thickness=3)
showimage(img) 
