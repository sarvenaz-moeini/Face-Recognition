import cv2
img=cv2.imread('cat.jpg')
blur=cv2.blur(img,(9,9))
cv2.imshow('orgimg',img)
cv2.imshow('blur',blur)
cv2.waitKey()
cv2.destroyAllWindows()
