import cv2
import numpy as np

import requests      # url을 통해 이미지 데이터 가져오기
# url 에서 이미지를 로드하고 디코딩하여 OpenCV 형식의 이미지를 반환하는 함수
def get_img(url,is_gray=True):
    image_ndarray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
    mode = cv2.IMREAD_UNCHANGED
    if is_gray:
        mode = cv2.IMREAD_GRAYSCALE
    img = cv2.imdecode(image_ndarray, mode)
    return img

url = 'https://raw.githubusercontent.com/dsaint31x/OpenCV_Python_Tutorial/master/images/messi5.jpg'
src = get_img(url,False)

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
