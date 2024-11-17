import cv2
import numpy as np
import requests

def url_to_image(url: str) -> np.ndarray:
    
    # URL에서 이미지 데이터를 가져옴
    response = requests.get(url)
    # 이미지를 bytearray로 변환하여 NumPy 배열로 변환
    image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    # OpenCV를 사용하여 이미지를 디코딩하여 ndarray로 변환
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    return image

def main():
    # 테스트할 이미지 URL
    image_url = 'https://raw.githubusercontent.com/dsaint31x/OpenCV_Python_Tutorial/master/images/opencv-logo.png'
    
    # URL에서 이미지를 읽어들여 ndarray로 변환
    image = url_to_image(image_url)
    
    # 이미지가 제대로 로드되었는지 확인
    if image is None:
        print("이미지를 불러올 수 없습니다.")
        return
    
    # 이미지를 화면에 표시
    cv2.imshow('Loaded Image', image)
    
    # ESC 키를 누르면 창이 닫히고 프로그램이 종료됨
    while True:
        if cv2.waitKey(10) & 0xFF == 27:  # ESC 키 코드
            break
    
    # 모든 윈도우 종료
    cv2.destroyAllWindows()

# main 함수가 main 스크립트로 실행될 때만 실행
if __name__ == '__main__':
    main()
