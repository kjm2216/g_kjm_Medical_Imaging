import cv2
import os

d_path = os.path.dirname(__file__)
f_path = f"{d_path}/messi5.jpg"

img = cv2.imread(f_path)

# 이미지의 각 색상 채널(BGR)을 분리하여 각각 b, g, r 변수에 저장 
b,g,r = cv2.split(img)

# 이미지와 각 채널의 크기를 출력 
print(f'{img.shape = }')   # (height, width, channels)
print(f'{b.shape = }')     # Blue (height, width)
print(f'{g.shape = }')     # Green (height, width)
print(f'{r.shape = }')     # Red (height, width)

# r, g, b 순서로 채널을 병합하여 RGB 이미지 생성 
img_rgb = cv2.merge((r,g,b))
print(f'{img_rgb.shape = }')

import matplotlib.pyplot as plt
plt.figure('ori')    # 원본 (BGR)
plt.imshow(img)   
# BGR 이미지임에도 불구하고 Matplotlib은 RGB로 해석하여 색상이 왜곡됨

plt.figure('rgb')    # 제대로된 RGB 이미지
plt.imshow(img_rgb)
plt.show()