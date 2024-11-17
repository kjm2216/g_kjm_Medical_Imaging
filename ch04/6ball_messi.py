import cv2
import sys
import os

d_str = os.path.dirname(__file__)
f_str = os.path.join(d_str,'messi5.jpg')

img_ori = cv2.imread(f_str)  # 이미지를 파일에서 읽어옴 
# 이미지를 읽지 못했을 경우 프로그램 종료
if img_ori is None:
    sys.exit(f'There is not a file:{f_str}')

cv2.imshow('original image',img_ori)  # 원본 이미지 표시 

img = img_ori.copy()   # 원본 이미지를 복사하여 img 변수에 저장 

# 이미지에서 특정 영역(축구공)을 slicing하여 ball 변수에 저장
ball = img[280:340,330:390] 
print(ball.shape)   # ball의 크기 (행,열,채널 수)

# 축구공을 (273,100) 위치에 복사 
img[273:273+ball.shape[0],100:100+ball.shape[1]] = ball

cv2.imshow('modified image',img)  # 수정된 이미지 표시 

# modified image 창이 열려있는 동안 반복문 실행
while cv2.getWindowProperty('modified image', cv2.WND_PROP_VISIBLE) >= 1:
    k = cv2.waitKey(10)
    if k&0xff == 27:
        break
    # original image 창이 닫히면 반복문 종료
    if cv2.getWindowProperty('original image', cv2.WND_PROP_VISIBLE) < 1:
        break
cv2.destroyAllWindows()
