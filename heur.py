from math import hypot
import cv2

def calculate_h(x1, y1, x2, y2):
    return hypot((x1 - x2), (y1 - y2))

ans = calculate_h(500,200,250,1000)
print(ans)

ans = cv2.resize(cv2.imread('checkpoint.png'),(64,64))
cv2.imwrite("check_flag_64x64.png",ans)