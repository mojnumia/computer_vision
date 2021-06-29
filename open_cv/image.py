import cv2
import numpy as np
img= cv2.imread('lena.png')
#cv2.imshow('lena',img)
img_array=np.array(img)
img_array= img_array/255
new_img= np.arange(1,10)
print(img_array,img_array.shape,img_array.max(),img_array.mean(),new_img)


cv2.waitKey(0)
cv2.destroyAllWindows()