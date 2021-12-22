from typing import SupportsComplex
import cv2

# 카메라 장치 열기
cap = cv2.VideoCapture(0) #파일을 열수도 있음

#방어코드(안정장치)
if not cap.isOpened():
    print('camera open failed')
    exit()

# fourcc(four character code): DIVX(avi), MP4V(mp4), X264(h264)


#동영상 촬영하기
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    cv2.imshow('frame1', cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)) # 괄호 안에  (window주소(이건 마음대로 써도됨),출력할 영상 데이터) 써주기
    cv2.imshow('frame2',  cv2.Canny(frame, 50, 100))
     
# 1000 = 1초, 10 = 0.01초
    if cv2.waitKey(10) == 13:
        break

# 사용자 자원 해제
cap.release()
cv2.destroyAllWindows()

#동영상 촬영 코드는 저장은 시키지 않고 화면에 실시간으로 촬영하고 있는 모습을 보여주는 코드