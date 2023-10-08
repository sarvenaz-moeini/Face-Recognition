import cv2
import numpy as np
cap=cv2.VideoCapture(0)
fg=cv2.createBackgroundSubtractorMOG2()
#cv2.imshow('fg',fg)
while True:
  _,frame=cap.read()
  fmask=fg.apply(frame)
  cv2.imshow('original',frame)
  cv2.imshow('fg',fmask)
  k=cv2.waitKey(27) & 0xFF
  if (k==27):
    break
cv2.destroyAllWindows()
cap.release()


#تفریق پس‌زمینه، تشخیص اجسام متحرک در فریم‌های ویدئویی
#  را امکان‌پذیر می‌سازد و به همین دلیل یک مرحله پیش‌پردازش ویدئویی
#  حیاتی در بسیاری از برنامه‌های بینایی کامپیوتری مانند محیط‌های هوشمند است.


#Overall, this code captures video from the default camera, 
# applies the MOG2 background subtraction algorithm to the video frames, 
# and displays the original frames and the resulting foreground mask
#  in separate windows. The loop continues until the Esc key is pressed.


#به طور کلی، این کد از دوربین پیش‌فرض فیلم می‌گیرد، الگوریتم تفریق پس‌زمینه 
# MOG2 را روی فریم‌های ویدیو اعمال می‌کند و فریم‌های اصلی و ماسک پیش‌زمینه 
# حاصل را در پنجره‌های جداگانه نمایش می‌دهد. این حلقه تا فشار دادن کلید Esc ادامه می یابد.