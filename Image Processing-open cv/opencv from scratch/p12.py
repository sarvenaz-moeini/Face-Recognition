import cv2
import matplotlib.pyplot as plt
img=cv2.imread('index.jpg',1) # 1: the image should be read in color mode
cv2.imshow('img',img)
histogram=cv2.calcHist([img],[0],None,[256],[0,255])  #image chanal mask size range
hist=plt.plot(histogram)
plt.show()


#HISTOGRAM