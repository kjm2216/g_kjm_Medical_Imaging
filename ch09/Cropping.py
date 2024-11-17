import matplotlib.pyplot as plt
import cv2

zoomed_cat = cv2.cvtColor(zoomed_cat,cv2.COLOR_RGB2BGR)
zoomed_cat_NN = cv2.cvtColor(zoomed_cat_NN,cv2.COLOR_RGB2BGR)

cropped_img0 = zoomed_cat[150:300,250:450]
#cv2_imshow(cropped_img0)
cropped_img1 = zoomed_cat_NN[150:300,250:450]
#cv2_imshow(cropped_img1)

plt.figure(figsize=(12,12))
plt.subplot(121); plt.imshow(cropped_img0) # expects distored color
plt.subplot(122); plt.imshow(cropped_img1) # expects true color
plt.show()

#--------------------------------------
# be careful to modify the cropped img.
tmp = cropped_img0.copy()
cropped_img0[:]=0

#cv2_imshow(zoomed_cat)
#cv2_imshow(tmp)
plt.imshow(zoomed_cat)
plt.show()
plt.imshow(tmp)
plt.show()

zoomed_cat[150:300,250:450]=tmp
#cv2_imshow(zoomed_cat)
plt.imshow(zoomed_cat)
plt.show()
