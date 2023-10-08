import cv2
import numpy as np
img=cv2.imread("image.png",0)
kernel=np.ones((9,9),np.uint8)
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
cv2.imshow("img",img)
cv2.imshow("gradient",gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
