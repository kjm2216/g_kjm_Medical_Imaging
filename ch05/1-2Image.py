import cv2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = np.uint8([250,250,250,250])  # 250으로 채워진 NumPy 배열 생성 (uint8 형식)
y = np.uint8([10,10,10,10])  # 10으로 채워진 NumPy 배열 생성 (uint8 형식)

# OpenCV의 add 함수는 값이 255를 초과하면 255로 클리핑함
# 250 + 10 = 260 이지만 255를 넘어서므로 255로 반환
print(cv2.add(x,y))  # [255 255 255 255]

# NumPy의 더하기 연산은 모듈러 연산을 수행 (값이 256을 넘으면 256으로 나눈 나머지를 반환)
# 250 + 10 = 260 % 256 = 4
print(x+y)  # [4 4 4 4]

# ---------------------------------------------
# Heatmap을 표시하는 함수 정의 
def show_heatmap(ax,title,img):
   #"""이미지를 heatmpa 형태로 표시하는 함수"""
  ax.set_title(title)   # 축 제목 설정 
  sns.heatmap(img,annot=True,fmt='.2f',cmap=plt.cm.gray, ax =ax, # heatmpa을 회색조로 그리기
              cbar=False, linewidth=0, linecolor='blue')  # colorbar 비활성화, 선 색상 파랑색
  # heatmap의 테두리 설정 
  for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_edgecolor('blue')  # 테두리 색상 설정
    spine.set_linewidth(2)  # 테두리 두께 설정
    
# ---------------------------------------------
# 두개의 2D 배열에 대해 여러 연산 수행 

# 배열 x와 y생성
x = np.array([[150,200,100],
              [150,200,100],
              [150,200,100]], dtype=np.uint8) # 3x3 배열 생성 (uint8 형식)
y = np.array([[200,100,50],
              [200,100,50],
              [200,100,50]], dtype=np.uint8) # 또 다른 3x3 배열 생성 (uint8 형식)

# NumPy를 이용해 기본 연산 수행 
add      = x + y   # 덧셈 
subtract = x - y   # 뺄셈
multiply = x * y   # 곱셈
divide   = x / y   # 나눗셈 (float 결과)

add = cv2.add(x ,y)
sub = cv2.subtract(x, y)
mul = cv2.multiply(x ,y)
div = cv2.divide(x ,y)

# 1행 6열의 subplot 생성, 크기 12x2
fig, axs = plt.subplots(1,6, figsize=(12,2))

show_heatmap(axs[0],'x',x)  # 원본 x 배열에 대한 heatmap
show_heatmap(axs[1],'y',y)  # 원본 y 배열에 대한 heatmap
show_heatmap(axs[2],'add by opencv',add)  # OpenCV의 덧셈 연산 결과 heatmap
show_heatmap(axs[3],'subtract by opencv',sub) # OpenCV의 뺄셈 연산 결과 heatmap
show_heatmap(axs[4],'multiply by opencv', mul)  # OpenCV의 곱셈 연산 결과 heatmap
show_heatmap(axs[5],'divide by opencv', div)  # OpenCV의 나눗셈 연산 결과 heatmap
# 200/3 = 66.666..... but in the case of opencv 200/3 = 67

plt.tight_layout()
plt.show()
