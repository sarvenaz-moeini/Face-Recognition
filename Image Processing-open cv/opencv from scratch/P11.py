#thresh trunc,tozero
import cv2
def showimage(img):
  cv2.imshow('img',img)
  cv2.waitKey()
  cv2.destroyAllWindows()
img=cv2.imread('index.jpg')
showimage(img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
showimage(img)
ret,binaryinv=cv2.threshold(img,70,255,cv2.THRESH_BINARY_INV)
showimage(binaryinv)
