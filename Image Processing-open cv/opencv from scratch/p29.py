import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(1):
  _,frame=cap.read()    #Reads a frame from the video capture object.
  hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
  lower_red=np.array([30,100,50])
  upper_red=np.array([255,255,230])
  mask=cv2.inRange(hsv,lower_red,upper_red)   #Creates a binary mask by thresholding the HSV frame
                                              # based on the defined red color range.

  res=cv2.bitwise_and(frame,frame,mask=mask) #Applies bitwise AND operation between the original
                                             #frame and the mask to extract only red regions.
  cv2.imshow('frame',frame)
  cv2.imshow('mask',mask) 
  cv2.imshow('res',res)
  if (cv2.waitKey(5)&0xFF)==27:    #Waits for a key press event for 5 milliseconds and 
                                   #checks if it is 'Esc' key (ASCII value 27).
    break
cv2.destroyAllWindows()
cap.release()


#In summary, this code captures frames from a webcam, 
# converts them to HSV color space, applies a red color filter using a binary mask,
#  and displays both the original frame and filtered result in separate windows until
#  'Esc' key is pressed to exit.