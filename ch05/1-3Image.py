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


# -------------------------------
# 마스크 생성
mask = np.zeros(shape=(3, 3), dtype=np.uint8)  # 3x3 크기의 0으로 채워진 마스크 배열 생성
mask[1, 1] = 1  # 중앙 위치 (1,1)에 1을 설정 (이 위치에만 연산이 적용됨)
# -------------------------------
# 마스크를 사용한 OpenCV 연산
add_m = cv2.add(x, y, None, mask=mask)  # 마스크를 사용한 덧셈 연산 (중앙 값만 연산됨)
sub_m = cv2.subtract(x, y, None, mask=mask)  # 마스크를 사용한 뺄셈 연산 (중앙 값만 연산됨)
# -------------------------------
# 마스크를 사용하지 않은 OpenCV 연산
add = cv2.add(x, y, None, mask=None)  # 마스크 없이 전체에 대해 덧셈 연산
sub = cv2.subtract(x, y, None, mask=None)  # 마스크 없이 전체에 대해 뺄셈 연산
# -------------------------------
# 연산 결과를 heatmap으로 시각화
fig, axs = plt.subplots(1, 6, figsize=(12, 2))  # 1행 6열의 서브플롯 생성

# 각 배열 및 연산 결과에 대해 heatmap 그리기
show_heatmap(axs[0], 'x', x)  # 원본 x 배열
show_heatmap(axs[1], 'y', y)  # 원본 y 배열
show_heatmap(axs[2], 'add w/ mask', add_m)  # 마스크를 적용한 덧셈 연산 결과
show_heatmap(axs[3], 'sub w/ mask', sub_m)  # 마스크를 적용한 뺄셈 연산 결과
show_heatmap(axs[4], 'add w/o mask', add)  # 마스크 없이 덧셈 연산 결과
show_heatmap(axs[5], 'sub w/o mask', sub)  # 마스크 없이 뺄셈 연산 결과

# -------------------------------
# 레이아웃을 자동으로 조정하여 그래프가 겹치지 않게 함
plt.tight_layout()

# 그래프 출력
plt.show()


