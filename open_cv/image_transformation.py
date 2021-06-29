import cv2
from rescale import rescaleFrame
import nltk
import numpy as np
import tensorflow as tf
lena= cv2.imread('lena.png')
lena_scaled= rescaleFrame(lena,0.4)
cv2.imshow('lena',lena)
cv2.imshow('lena_sale',lena_scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()