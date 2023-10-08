import cv2
import numpy as np
img=cv2.imread("image.png",0)
kernel=np.ones((8,8),np.uint8)
erosion=cv2.erode(img,kernel)
cv2.imshow("img",img)
cv2.imshow("erosion",erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
