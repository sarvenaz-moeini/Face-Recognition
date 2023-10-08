import cv2
img1=cv2.imread('img.jpg')
img2=cv2.imread('cat.jpg')
width=img1.shape[1]
print(width)
height=img1.shape[0]
img3=cv2.resize(img2,(width,height))
add=img1+img3
cv2.imshow('image',add)
cv2.waitKey()
cv2.destroyAllWindows()
