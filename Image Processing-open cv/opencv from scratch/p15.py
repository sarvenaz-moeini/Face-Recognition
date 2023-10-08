import cv2
img=cv2.imread('img.jpg')
cv2.imshow('image1',img)
img=cv2.line(img,(200,300),(300,400),(255,255,255),9)
img=cv2.rectangle(img,(200,250),(300,350),(0,120,255),3)
cv2.imshow('image2',img)
cv2.waitKey()
cv2.destroyAllWindows()

