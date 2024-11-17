from skimage import data
from skimage import img_as_ubyte, img_as_float
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지 불러오기
img = cv2.imread('./IMG/cat_cv.tif')

# 이미지의 높이, 너비, 채널 수 확인
height, width, channels = img.shape
print("original dimension : ({}, {}, {})".format(height, width, channels))

# -------------------
x1, y1 = 100, 50  
x2, y2 = 200, 150 

cat_eye = img[y1:y2, x1:x2]

cv2.imshow('cat_eye', cat_eye)

# -------------------
# 이미지 확대 (CUBIC 보간법 사용)
zoomed_eye = cv2.resize(cat_eye, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# 확대된 이미지 출력
cv2.imshow('zoomed_eye', zoomed_eye)

# Nearest-Neighbor 보간법을 사용한 확대
zoomed_eye_NN = cv2.resize(cat_eye, (2 * (x2 - x1), 2 * (y2 - y1)), interpolation=cv2.INTER_NEAREST)
cv2.imshow('zoomed_eye_NN', zoomed_eye_NN)

cv2.waitKey(0)
cv2.destroyAllWindows()
