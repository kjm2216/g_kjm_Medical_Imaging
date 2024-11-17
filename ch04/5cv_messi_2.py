import cv2
import numpy as np
import matplotlib.pyplot as plt
import requests

def get_img(url,is_gray=True):
    image_ndarray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
    mode = cv2.IMREAD_UNCHANGED
    if is_gray:
        mode = cv2.IMREAD_GRAYSCALE
    img = cv2.imdecode(image_ndarray, mode)
    return img

# url = 'https://raw.githubusercontent.com/dsaint31x/OpenCV_Python_Tutorial/master/images/messi5.jpg'
# src = get_img(url,False)

import os 
d_path = os.path.dirname(__file__)
f_path = os.path.join(d_path, "messi5.jpg")

src = cv2.imread(f_path)


if src is None:
    print('Error : Loading image')
else:
    print('OK : Loading image')
    img = src.copy()

intensity = img[100,100]
print(f'img[100,100]={intensity}')

# 특정 영역을 slicing 하여 tmp에 저장 
tmp = img[200:250:1, 300:100:-1]
cv2.imshow('img', tmp)    # slicing 이미지(tmp)를 'img'라는 이름의 창에 표시
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f'{img.shape = }')
print(f'{img.dtype = }')
print(f'{img.size = }')