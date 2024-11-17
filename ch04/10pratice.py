import cv2
import numpy as np
import requests

url = "https://raw.githubusercontent.com/dsaint31x/OpenCV_Python_Tutorial/master/images/opencv-logo.png"
response = requests.get(url)
print(type(response.content))

image_array = bytearray(response.content)
print(type(image_array))

np_array = np.asarray(image_array, dtype=np.uint8)
print(type(np_array))

image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
print(image.shape)

cv2.imshow('Loaded Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()