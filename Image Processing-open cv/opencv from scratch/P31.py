import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(1):
  _,frame=cap.read()
  laplacian=cv2.Laplacian(frame,cv2.CV_8U)
  cv2.imshow('original',frame)
  cv2.imshow('laplacian',laplacian)
  if (cv2.waitKey(5)&0xFF)==27:
    break
cv2.destroyAllWindows()
cap.release()
  


  # ```python
#laplacian = cv2.Laplacian(frame, cv2.CV_8U)


# Here, numpy is used implicitly by OpenCV's `cv2.Laplacian()` function to perform calculations on the `frame` array.

