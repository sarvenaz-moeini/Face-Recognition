import cv2
import numpy as np
img1=cv2.imread('cat.jpg')
img2=cv2.imread('logo.jpg')
cv2.imshow('src',img2)
rows,cols,channels=img2.shape
roi=img1[0:rows,0:cols]
img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('src_gray',img2gray)
ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY)
cv2.imshow('mask',mask)
mask_inv=cv2.bitwise_not(mask)
cv2.imshow('mask_inv',mask_inv)
img1_bg=cv2.bitwise_and(roi,roi,mask=mask)
cv2.imshow('mask_bg',img1_bg)
img2_fg=cv2.bitwise_and(img2,img2,mask=mask_inv)
cv2.imshow('mask_fg',img2_fg)
dst=cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols]=dst
cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
