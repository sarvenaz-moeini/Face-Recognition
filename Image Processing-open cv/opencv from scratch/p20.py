import cv2
img=cv2.imread('img.jpg',cv2.IMREAD_COLOR)  #The second argument, `cv2.IMREAD_COLOR`, specifies that the image should be loaded in color mode
px=img[100:200,100:200]  #This line extracts a region of interest (ROI) from the loaded image. It selects a rectangular area starting from row 100 to row 199 and column 100 to column 199. The selected region is assigned to the variable `px`
print(px)


#In summary, this code reads an image file, extracts a specific region of interest from it,
#  and then prints the extracted region's value.