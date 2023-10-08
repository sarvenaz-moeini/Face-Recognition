import cv2
import numpy as np
img_bgr=cv2.imread('mario.jpg')
img_gray=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)
cv2.imshow('image',img_bgr)
img_template=cv2.imread('template_mario.jpg',0)
cv2.imshow('image_template',img_template)
w,h=img_template.shape[::-1]
print(w,h)
res=cv2.matchTemplate(img_gray,img_template,cv2.TM_CCOEFF_NORMED)
threshold=0.5
loc=np.where(res>=threshold)
for pt in zip(*loc[::-1]):
  cv2.rectangle(img_bgr,pt,(pt[0]+w,pt[1]+h),(255,0,255),5)
cv2.imshow('image_nahayi',img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

#به طور کلی، این کد با یافتن
#  بهترین تطابق بین تصویر الگو و تصویر رنگی ورودی، تطبیق قالب را انجام می دهد و سپس
#  با کشیدن مستطیل روی تصویر رنگی، مطابقت ها را برجسته می کند.
