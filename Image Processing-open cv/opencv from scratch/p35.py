import cv2
import numpy as np
img=cv2.imread('corner.jpg')
cv2.imshow('image',img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)
corners=cv2.goodFeaturesToTrack(gray,50,0.5,10) #It detects N strongest corners in the image
corners=np.int0(corners)  # converts the input array to the default integer type
for corner in corners:
  x,y=corner.ravel()   #برای تغییر یک آرایه دو بعدی یا یک آرایه چند بعدی به یک آرایه مسطح پیوسته استفاده می شود.
  cv2.circle(img,(x,y),6,(0,255,255),1)
cv2.imshow('corners',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Overall, this code reads an image, converts it to grayscale,
#  and applies corner detection. It then visualizes the 
# detected corners by drawing circles on the original image. 
# The code utilizes the `cv2.goodFeaturesToTrack()` function to find
#  good corners based on the specified parameters.
