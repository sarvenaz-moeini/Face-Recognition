import cv2
import numpy as np
img=cv2.imread('logo.jpg')
laplacian=cv2.Laplacian(img,cv2.CV_8U)
cv2.imshow('original',img)
cv2.imshow('laplacian',laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
  


  #لاپلاسین در مقایسه با مرتبه اول، محلی سازی لبه بهتری را ارائه می دهد

# لاپلاسین یک تصویر، نواحی با تغییر شدت سریع را برجسته می کند
#  و بنابراین اغلب برای تشخیص لبه استفاده می شود.

# The Laplacian of an image highlights regions of rapid intensity change and 
# is therefore often used for edge detection 