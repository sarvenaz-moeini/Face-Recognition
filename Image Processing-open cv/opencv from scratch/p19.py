import cv2
import numpy as np
img=cv2.imread('img.jpg')
px=img[200,200]
print(px)

#Next, it accesses the pixel at coordinates (200, 200) in the image using img[200, 200] and assigns it to the variable "px". 

# Finally, it prints out the value of "px" using print(px).