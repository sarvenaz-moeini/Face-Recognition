import cv2
import numpy as np
img=np.zeros((500,500,3))  # 3 color channels (BGR)
img=cv2.rectangle(img,pt1=(10,10),pt2=(100,100),color=(0,255,255),thickness=3)
#Draws a rectangle on the image "img" using the OpenCV function "cv2.rectangle". 
# The rectangle starts at point (10, 10) and ends at point (100, 100). 
# The color of the rectangle is specified as (0, 255, 255), which 
# corresponds to yellow in RGB color space.
# The thickness of the rectangle's border is set to 3 pixels.
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()
