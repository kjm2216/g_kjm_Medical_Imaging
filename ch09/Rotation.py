from skimage import data
from skimage import img_as_ubyte,img_as_float
import cv2
import numpy as np
import matplotlib.pyplot as plt

cat = data.chelsea() # take the test image of cat!
img = cv2.cvtColor(cat, cv2.COLOR_RGB2GRAY)
# img = cv2.imread('cat_cv.tif',0)

rows,cols = img.shape # there is no channel

#------------------------------------
# getRotationMatrix2D
# the rotation center is given by Tupple.
# (center.x cneter.y), rotation degree, scale
M = cv2.getRotationMatrix2D((cols/2,rows/2),30,1)
print(M)

dst = cv2.warpAffine(img,M,(cols,rows))

# cv2.imshow('img',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.figure(figsize=(12,12))
plt.subplot(121); plt.imshow(img, cmap='gray'), plt.axis('off')
plt.subplot(122); plt.imshow(dst, cmap='gray'), plt.axis('off')
plt.show()
