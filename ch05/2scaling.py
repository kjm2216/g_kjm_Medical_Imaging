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
# 이미지 확대 (CUBIC 보간법 사용)
zoomed_cat = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# 또는
# zoomed_cat = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
# -------------------

# 수정된 이미지의 차원 출력
print("modified dimension :", zoomed_cat.shape)

# 확대된 이미지 출력
cv2.imshow('zoomed_cat', zoomed_cat)

# Nearest-Neighbor 보간법을 사용한 확대
zoomed_cat_NN = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_NEAREST)
cv2.imshow('zoomed_cat_NN', zoomed_cat_NN)

# 키 입력 대기 후 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()
