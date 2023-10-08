#hsv
import cv2
img=cv2.imread('cat.jpg')
cv2.imshow("img",img)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("img2",img2)
cv2.waitKey(0)
