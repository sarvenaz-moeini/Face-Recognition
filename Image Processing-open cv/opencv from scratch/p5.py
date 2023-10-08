import cv2
import numpy as np
img=np.zeros([500,500])
img[100:200,100:200]=100
cv2.imwrite('image.jpg',img)
cv2.waitKey()
cv2.destroyAllWindows()
