import cv2
img1=cv2.imread('cat.jpg')
img2=cv2.imread('logo.jpg')
width=img1.shape[1]
height=img1.shape[0]
img2=cv2.resize(img2,(width,height))
blend=cv2.addWeighted(img1,0.5,img2,0.5,1)
cv2.imwrite("belnding.jpg",blend)
cv2.imshow("belnding.jpg",blend)
cv2.waitKey()
cv2.destroyAllWindows()
# blendign 2 pics with eachother with controlable extent with alpha and beta

