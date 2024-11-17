import cv2
import numpy as np

# 고주파 패턴 이미지 생성
size = 512

def create_concentric_circles(size, frequency=100):
    x = np.linspace(-1, 1, size)
    y = np.linspace(-1, 1, size)
    xx, yy = np.meshgrid(x, y)
    return (np.sin(frequency * np.sqrt(xx**2 + yy**2))*255).astype(np.uint8)

def create_simple(size):
  high_freq_pattern = np.zeros((size, size), dtype=np.uint8)
  high_freq_pattern[::2, ::2] = 255
  high_freq_pattern[1::2, 1::2] = 255
  return high_freq_pattern

high_freq_pattern = create_concentric_circles(size)
# high_freq_pattern = create_simple(size)

# 이미지 크기 줄이기 (모아레 아티팩트 생성)
reduced_size = (size // 5*3, size // 5*3)  # 3으로 나누어 더 뚜렷한 모아레 패턴 생성
resized_nearest = cv2.resize(high_freq_pattern, reduced_size, interpolation=cv2.INTER_NEAREST)

# 결과 저장

# 이미지 크기 줄이기 (모아레 아티팩트 방지)
resized = cv2.resize(high_freq_pattern, (size//5*3, size//5*3), interpolation=cv2.INTER_AREA)

# 결과 저장
cv2.imwrite('no_moire_artifact.png', resized)
cv2.imwrite('moire_artifact.png', resized_nearest)
cv2.imwrite('original.png', high_freq_pattern)
