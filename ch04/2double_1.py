import cv2
import time, os
import numpy as np

# image 초기화 
img = None

# mouse callback function
def db_click(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK: # Left Double Click
        cv2.circle(img,
                    (x,y),       # 중심
                    10,          # 반지름 
                    (255,0,0),   # Blue
                    -1)          # 두께 : 채워진 원

    print(f'{event = }')  # event 종류 출력

if __name__ == "__main__":
    img = np.zeros((512,300,3), 
                   dtype=np.uint8,)   # 검은색 이미지 unsigned int 8 생성
    
    cv2.namedWindow('mcb')   # 'mcb'라는 이름의 창 생성
    cv2.setMouseCallback('mcb', db_click )
    
    # cv2.waitKey(0)
    
    # 창이 열려 있는 동안 반복하여 화면 갱신
    while True:
        cv2.imshow('mcb', img)
        if cv2.waitKey(20) & 0xFF == 27: # ESC
            break
        if cv2.getWindowProperty('mcb', cv2.WND_PROP_VISIBLE ) <1:
            break
        # 창이 닫혔는지 확인 -> 루프 종료
        
    cv2.destroyAllWindows() # 모든 OpenCV 창 닫기
