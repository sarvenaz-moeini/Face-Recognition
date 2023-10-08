import cv2
import numpy as np
img=cv2.imread("image.png",0)
kernel=np.ones((3,3),np.uint8)
dilation=cv2.dilate(img,kernel)
cv2.imshow("img",img)
cv2.imshow("dilation",dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
