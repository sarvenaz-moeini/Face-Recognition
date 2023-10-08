import cv2
import numpy as np
img=cv2.imread("image.png",0)
kernel=np.ones((3,3),np.uint8)
closeing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
cv2.imshow("img",img)
cv2.imshow("closeing",closeing)
cv2.waitKey(0)
cv2.destroyAllWindows()
