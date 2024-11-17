from skimage import data
from skimage import img_as_ubyte,img_as_float
import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread('cat_cv.tif',0)
cat = data.chelsea() 
img = cv2.cvtColor(cat, cv2.COLOR_RGB2BGR)

height, width,channel = img.shape[:2]
print("original dimension : ({}, {}, {})".format(height,width,channel))

#-------------------
zoomed_cat = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
#OR
zoomed_cat = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
#-------------------

print("modified dimension :",zoomed_cat.shape)
cv2.imshow('zoomed_cat',zoomed_cat)
# cv2_imshow(zoomed_cat)

zoomed_cat_NN = cv2.resize(img, (2*width,2*height), interpolation = cv2.INTER_NEAREST)
cv2.imshow('zoomed_cat_NN',zoomed_cat_NN)
#cv2_imshow(zoomed_cat_NN)

cv2.waitKey(0)
cv2.destroyAllWindows()
