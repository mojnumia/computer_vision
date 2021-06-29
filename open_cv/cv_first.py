import cv2
import  numpy as np
image= cv2.imread('lena.png')
cv2.imshow('lena',image)

cv2.waitKey(100)
cv2.destroyAllWindows()
x=np.ones((2,3),dtype=float)
y=np.random.randint(1,6)
m=image.shape
zero= np.zeros((3,4))

print(x,y,m,zero)
def myfuntion():
    pass