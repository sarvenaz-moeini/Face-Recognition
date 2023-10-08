import cv2
img1=cv2.imread('cat.jpg')
img2=cv2.imread('logo.jpg')
cv2.imshow('first img cat',img1)
cv2.imshow('first img logo',img2)
width=img1.shape[1]   # calculates and assigns the width of 'img1' to the variable 'width'.
height=img1.shape[0]  
img2=cv2.resize(img2,(width,height))
cv2.imshow('resize img',img2)
cv2.waitKey()


# gets 2 pics resize one of them to size of the other one of them