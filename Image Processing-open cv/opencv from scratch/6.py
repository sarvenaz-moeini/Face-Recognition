import cv2
import numpy as np

cap = cv2.VideoCapture("eye_recording.flv")

while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    roi=frame[269:795,537:1316]
    #cv2.imshow("roi", roi)
    gray_roi=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray_roi", gray_roi)
    kernel = np.ones((7, 7), np.uint8)
    bilateralFilter = cv2.bilateralFilter(gray_roi, 10, 15, 15)
    cv2.imshow("bilateralFilter",bilateralFilter)
    erode = cv2.erode(gray_roi, kernel, iterations=3)
    cv2.imshow("erode",erode)
    _,threshold = cv2.threshold(gray_roi,3, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("threshold",threshold)
    contours,_ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[-2:]
    contours = sorted(contours, key=lambda x:cv2.contourArea(x),reverse=True)
    for cnt in contours:
        cnt=cv2.drawContours(roi,[cnt],-1,(0,0,255),1)
        break
    cv2.imshow("cnt", cnt)
    key=cv2.waitKey(10)
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()
