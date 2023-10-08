import cv2
from matplotlib import pyplot as plt
img=cv2.imread('cat.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
plt.imshow(img,cmap='gray')
hist=plt.plot([100,400],[200,300],'g',linewidth=3)
plt.show()
