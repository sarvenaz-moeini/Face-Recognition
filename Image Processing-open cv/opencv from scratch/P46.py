import cv2
import numpy as np
img=cv2.imread("image.png",0)
kernel=np.ones((9,9),np.uint8)
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
cv2.imshow("img",img)
cv2.imshow("opening",opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
