import cv2
import numpy as np
img=np.zeros([800,800])
print(img)
cv2.imwrite('image1.jpg',img)
cv2.waitKey()
cv2.destroyAllWindows()
