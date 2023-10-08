import cv2
img=cv2.imread('cat.jpg')
cv2.imshow('image1',img)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'cat',(200,250),font,1,(255,255,255),2)
cv2.imshow('image2',img)
cv2.waitKey()
cv2.destroyAllWindows()
