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
ret,binary=cv2.threshold(img,50,255,cv2.THRESH_BINARY) #The tenth line applies a binary thresholding operation on "img" using cv2.threshold(),
# with a threshold value of 50. It assigns both the thresholded image and return value (ret) to variables "binary" and "ret" respectively.
showimage(binary)


#grayscale and assigning thresholds for the same picture
# TRESH_BINARY