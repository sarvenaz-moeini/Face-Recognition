import cv2
import numpy as np
img=cv2.imread('cat.jpg')
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv',hsv)
lower_green=np.array([30,100,50])
upper_green=np.array([255,255,255])
mask=cv2.inRange(hsv,lower_green,upper_green)
res=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('image',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()


#This code reads an image of a cat, converts it to the HSV color space, and then 
# applies a green color filter to the image. It creates a mask based on the lower 
# and upper green color thresholds, and then applies this mask to the original 
# image using bitwise AND operation. Finally, it displays the original image,
#  the mask, and the resulting image with only the green pixels visible.

#این کد تصویر یک گربه را می خواند، آن را به فضای رنگی HSV 
# تبدیل می کند و سپس یک فیلتر رنگ سبز روی تصویر اعمال می کند. ماسکی را بر اساس
#  آستانه رنگ سبز پایین و بالایی ایجاد می کند و سپس با استفاده از عملیات بیتی
#  و این ماسک را روی تصویر اصلی اعمال می کند. در نهایت، تصویر اصلی، ماسک
#  و تصویر حاصل را تنها با پیکسل های سبز قابل مشاهده نمایش می دهد.