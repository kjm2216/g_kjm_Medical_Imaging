import cv2
import numpy as np
import os

# 현재 파일의 절대 경로를 기준으로 디렉토리 경로 설정 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  

# img_path = '/home/dsaint31/lecture/OpenCV_Python_Tutorial/images/lena.png'
# img_path = os.path.join(BASE_DIR,"messi5.jpg")
img_path = f"{BASE_DIR}/messi5.jpg"    # 경로 설정 

# 이미지를 읽어서 img 변수에 저장 
img = cv2.imread(img_path)
cv2.imshow('img', img)    # 'img' 창 표시
# 사용자가 선택한 ROI의 x,y 좌표 / 너비(w),높이(h)를 반환
x,y,w,h = cv2.selectROI('img', img, False)

# ROI 선택 후 너비와 높이가 0이 아닐 경우 처리 
if w and h:
    # 선택된 ROI 영역을 slicing -> roi 변수에 저장
    roi = img[y:y+h, x:x+w]
    cv2.imshow('roi', roi)      # 'roi' 창 표시 
    cv2.moveWindow('roi',0,0)   # 'roi' 창을 좌측상단 (0,0)위치 이동 
    cv2.imwrite(f'{BASE_DIR}/roi2.png', roi)  # 선택된 ROI를 'roi2.png' 파일로 저장

# 'img' 창이 닫히지 않는 동안 반복문 실행 
while cv2.getWindowProperty('img', cv2.WND_PROP_VISIBLE) >=1:
    key_code = cv2.waitKey(50)&0xff 
    # 50ms 동안 키보드 입력 대기 (입력된 키의 ASCII 값을 반환)
    print(key_code)  # 출력 
    # ESC 키 (ASCII=27) 누르면 반복문 종료
    if key_code == 27: 
        break

cv2.destroyAllWindows()
