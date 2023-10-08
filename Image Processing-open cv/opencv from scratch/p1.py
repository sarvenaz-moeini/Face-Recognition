import cv2
img=cv2.imread('cat.jpg')
print(img)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()
