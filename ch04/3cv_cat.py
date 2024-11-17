import cv2
import numpy as np
import os 

# 현재 파일의 directory 경로를 가져옴 
# 현재 파일(__file__)이 위치한 directory를 가져와 d_path변수에 저장
d_path = os.path.dirname(__file__)
# 이미지 파일의 전체 경로를 설정 
f_path = os.path.join(d_path, "cat_cv.tif")

# Read GrayScale
src = cv2.imread(f_path, cv2.IMREAD_GRAYSCALE)
print(f'{src[100,100] = }')  # (100, 100) 좌표의 픽셀 값을 출력
print(f'{src[10,100] = }')   # (10, 100) 좌표의 픽셀 값을 출력

# Read Color 
src = cv2.imread(f_path, cv2.IMREAD_COLOR)
print(f'{src[100,100,0] = }')   # (100,100) 좌표의 B채널값을 출력 
print(f'{src[10,100] = }')      # (10,100) 좌표의 모든 채널 값을 출력 