import cv2
import os

# 현재 파일의 디렉토리 경로를 기준으로 이미지 파일 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(BASE_DIR, 'messi5.jpg')

# 이미지를 불러오기
img = cv2.imread(img_path)

# 이미지가 제대로 로드되었는지 확인
if img is None:
    print(f"이미지 파일을 찾을 수 없습니다: {img_path}")
    exit()

# 사용자가 선택한 ROI (Region of Interest) 받아오기
x, y, w, h = cv2.selectROI("Select ROI", img, False)

# 선택된 ROI가 유효한지 확인
if w and h:
    # ROI 선택 영역을 img_roi 변수에 저장
    img_roi = img[y:y+h, x:x+w]

    # 원본 이미지의 크기 정보 얻기
    img_height, img_width = img.shape[:2]

    # 새로운 이미지를 만들기 위해 원본 이미지를 복사
    new_img = img.copy()

    # ROI를 붙일 위치 계산 (왼쪽 하단에 붙이기 위해)
    # new_img의 높이가 img_height를 초과하지 않도록 함
    roi_position_y = img_height - h
    # new_img의 너비가 0부터 시작하므로 x 위치는 0
    roi_position_x = 0

    # ROI를 원본 이미지의 왼쪽 하단에 붙이기
    new_img[roi_position_y:roi_position_y+h, roi_position_x:roi_position_x+w] = img_roi

    # 새로운 이미지를 파일로 저장
    new_img_path = os.path.join(BASE_DIR, 'new_img.jpg')
    cv2.imwrite(new_img_path, new_img)
    print(f"새로운 이미지가 저장되었습니다: {new_img_path}")

    # 새 이미지를 (0,0) 위치에 새로운 윈도우로 띄우기
    cv2.imshow('New Image with ROI', new_img)
    cv2.moveWindow('New Image with ROI', 0, 0)
else:
    print("유효한 ROI를 선택하지 않았습니다.")

# 'Select ROI' 창과 'New Image with ROI' 창이 닫히지 않는 동안 반복문 실행
while cv2.getWindowProperty('Select ROI', cv2.WND_PROP_VISIBLE) >= 1 or \
      cv2.getWindowProperty('New Image with ROI', cv2.WND_PROP_VISIBLE) >= 1:
    key_code = cv2.waitKey(50) & 0xff
    # ESC 키 (ASCII=27) 누르면 반복문 종료
    if key_code == 27:
        break

cv2.destroyAllWindows()
