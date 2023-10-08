import cv2
import numpy as np
img=np.ones([800,800])  # Creates a NumPy array of size 800x800 filled with ones, representing an image.
img[0:800,0:800]=255    #Sets all pixels in the image to have a value of 255 (white), effectively making the entire image white.
img[100:200,100:200]=127  #Sets a specific region of the image (from row 100 to 199 and column 100 to 199) to have a value of 127 (gray).
cv2.imwrite('image.jpg',img) #Saves the modified image as a JPEG file named "image.jpg".
cv2.waitKey()  
cv2.destroyAllWindows()  #Closes all open windows created by OpenCV.

