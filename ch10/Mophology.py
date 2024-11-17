import cv2
import numpy as np
import matplotlib.pyplot as plt
import urllib.request

# Download the image from the URL
url = 'https://t1.daumcdn.net/cfile/tistory/9983894C5B93B3AA04'
resp = urllib.request.urlopen(url)
img_array = np.asarray(bytearray(resp.read()), dtype=np.uint8)
img = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)

# Apply thresholding
_, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

print(img.shape)

# Structuring element and morphological transformations
k = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 13))
erosion = cv2.erode(img, k)
dilation = cv2.dilate(img, k)

# Plotting the images
plt.figure('src vs. erosion vs. dilation', figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.title('Original')

plt.subplot(1, 3, 2)
plt.imshow(erosion, cmap='gray')
plt.axis('off')
plt.title('Erosion')

plt.subplot(1, 3, 3)
plt.imshow(dilation, cmap='gray')
plt.axis('off')
plt.title('Dilation')

plt.show()
