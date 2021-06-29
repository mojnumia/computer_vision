import cv2
import  numpy as np
lena= cv2.imread('lena.png')
cv2.imshow('lena',lena)
def rescaleFrame(image_variable, scale=0.8):
    width= int(image_variable.shape[1]*scale)
    height= int(image_variable.shape[0]*scale)
    dimention=(width,height)
    rescaled_image= cv2.resize(image_variable,dimention,interpolation=cv2.INTER_AREA)
    return rescaled_image

image= rescaleFrame(lena,0.5)
cv2.imshow('lena_scaled',image)


cv2.waitKey(0)
cv2.destroyAllWindows()