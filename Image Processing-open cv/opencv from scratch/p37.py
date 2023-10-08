import cv2
import numpy as np
faceXML=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeXML=cv2.CascadeClassifier('haarcascade_eye.xml')
face=cv2.imread('face.jpg')
gray=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
faces=faceXML.detectMultiScale(gray)
for(x,y,w,h) in faces:
    cv2.rectangle(face,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray=gray[y:y+h , x:x+w]
    roi_color=face[y:y+h , x:x+w]
    eyes=eyeXML.detectMultiScale(roi_gray)
    for(ex,ey,ew,eh) in eyes:
      cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),5)
cv2.imshow('face',face)
cv2.waitKey(0)
cv2.destroyAllWindows()
