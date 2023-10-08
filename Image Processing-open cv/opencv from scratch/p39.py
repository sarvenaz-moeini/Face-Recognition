#resize
import cv2
img=cv2.imread('cat.jpg')
cv2.imshow("img",img)
percent=120
w=int(img.shape[1]*percent/100)
h=int(img.shape[0]*percent/100)
dim=(w,h)
img2=cv2.resize(img,dim)
cv2.imshow("img2",img2)
cv2.waitKey(0)
