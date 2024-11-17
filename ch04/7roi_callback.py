import cv2
import numpy as np
import os
import pyautogui   # 자동화 작업 / 키보드 입력을 위한 module

# 드래그 상태 및 시작 좌표, 사각형의 폭과 높이 초기화
is_dragging = False    # 드래그 중인지 여부를 나타내는 플래그 변수
x0,y0 = -1,-1          # 드래그 시작 지점의 좌표
w0,h0 = -1,-1          # 드래그로 선택한 사각형의 폭과 높이
red = (0,0,255)        # 빨간색 (RGB) -> 사각형

# 마우스 이벤트 처리 함수 정의 
def onMouse(event, x, y, flags, params):

    global is_dragging
    global x0,y0,w0,h0   # 전역 변수 선언 

    # 왼클릭 했을 때 
    if event == cv2.EVENT_LBUTTONDOWN: 
        is_dragging = True  # 드래그 시작
        x0 = x              # 시작 x 좌표 설정
        y0 = y              # 시작 y 좌표 설정 
        print(x0,y0)

    # mouse move 
    elif event == cv2.EVENT_MOUSEMOVE:
        if is_dragging:       # 드래그 상태일 때  
            tmp = img.copy()  # 원본 이미지를 복사하여 임시 이미지 생성 
            cv2.rectangle(tmp,     # 드래그 중인 사각형을 빨간색으로 그림 
                          (x0,y0), 
                          (x,y), 
                          red, 
                          2)
            cv2.imshow('roied_img', tmp)  # 드래그 중인 사각형이 포함된 이미지 표시 

    # 왼클릭 뗐을 때 
    elif event == cv2.EVENT_LBUTTONUP:
        if is_dragging:          # 드래그가 완료되면 
            is_dragging = False  # 드래그 상태 종료
            w = x-x0           # 선택한 사각형의 폭 계산
            h = y-y0           # 선택한 사각형의 높이 계산 

            # 폭과 높이가 0보다 크면 유효한 ROI
            if w>0 and h > 0:
                tmp = img.copy()  # 원본 이미지를 복사하여 임시 이미지 생성 

                cv2.rectangle(tmp,  # 선택된 사각형을 그린 이미지 생성
                              (x0,y0), 
                              (x,y), 
                              red, 
                              3)
                cv2.imshow('roied_img', tmp) # 선택된 ROI가 포함된 이미지 표시
                
                roi = img[y0:y0+h, x0:x0+w]  # 선택된 영역을 잘라내어 roi 변수에 저장 

                cv2.imshow('roi', roi)     # 'roi'창에 표시
                cv2.moveWindow('roi',0,0)  # 'roi' 창을 좌측상단(0,0) 위치로 이동
                
                cv2.imwrite('./roi_mouse.png',roi)  # 선택된 ROI를 'roi_mouse.png' 파일로 저장
                
                print('roi is cropped and saved!')
            
            # 유효하지 않은 ROI (폭 또는 높이가 0이하)
            else:
                cv2.imshow('roi', img)      # 원본 이미지를 다시 표시
                print('unvalid roi!. select roi carefully')

     # main thread로 돌아가기 위한 key event 발생.
    pyautogui.press('e')
    return

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(BASE_DIR, "messi5.jpg")
img = cv2.imread(img_path)   # 이미지 읽기 

# 'roied_img'라는 창에 원본 이미지 표시 
cv2.imshow('roied_img', img)
# 'roied_img' 창에 mouse event callback 함수 설정 
cv2.setMouseCallback('roied_img',onMouse)

# 'roied_img' 창이 닫히지 않는 동안 반복문 실행 
while cv2.getWindowProperty('roied_img', cv2.WND_PROP_VISIBLE) >= 1:
    key_code = cv2.waitKey(20) 
    if key_code == 27:
        # print('ESC')
        break
    elif cv2.getWindowProperty('roied_img', cv2.WND_PROP_VISIBLE) < 1:   # 'roied_img' 창이 닫혔을 때
        break 
    elif cv2.getWindowProperty('roi', cv2.WND_PROP_VISIBLE) < 1:     # 'roi' 창이 닫혔을때 

        cv2.destroyWindow('roi')   
cv2.destroyAllWindows()
