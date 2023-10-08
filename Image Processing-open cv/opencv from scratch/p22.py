import cv2
img=cv2.imread('cat.jpg',cv2.IMREAD_COLOR)
part1=img[100:200,100:200]
img[300:400,300:400]=part1
cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()
