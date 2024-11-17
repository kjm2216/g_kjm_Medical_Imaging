import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255,0,0] #BGR

fstr = './opencv-logo.png'
fstr = './opencv-logo.png'

# ----------------------------
# Convert the transparent part of PNG into white
img1 = cv2.imread(fstr,cv2.IMREAD_UNCHANGED)
alpha_channel = img1[:, :, 3]
_, mask = cv2.threshold(alpha_channel, 254, 255, cv2.THRESH_BINARY)  # binary mask
color = img1[:, :, :3]
img1 = cv2.bitwise_not(cv2.bitwise_not(color, mask=mask))

print(img1.shape)

replicate  = cv2.copyMakeBorder(img1,100,100,100,100,cv2.BORDER_REPLICATE)
reflect    = cv2.copyMakeBorder(img1,100,100,100,100,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,100,100,100,100,cv2.BORDER_REFLECT_101)
wrap       = cv2.copyMakeBorder(img1,100,100,100,100,cv2.BORDER_WRAP)
constant   = cv2.copyMakeBorder(img1,100,100,100,100,cv2.BORDER_CONSTANT,value=BLUE)


#for matplotlib
img1       = img1[:,:,::-1]    
replicate  = replicate[:,:,::-1]
reflect    = reflect[:,:,::-1]
reflect101 = reflect101[:,:,::-1]
wrap       = wrap[:,:,::-1]
constant   = constant[:,:,::-1]


print('See the result above. (Image is displayed with matplotlib. So RED and BLUE planes will be interchanged):')
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.xticks([]);plt.yticks([])
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.xticks([]);plt.yticks([])
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.xticks([]);plt.yticks([])
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.xticks([]);plt.yticks([])
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.xticks([]);plt.yticks([])
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.xticks([]);plt.yticks([])
#plt.axis('off')

plt.show()