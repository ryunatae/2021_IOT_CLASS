from typing import SupportsComplex
import cv2

# 카메라 장치 열기
cap = cv2.VideoCapture(0) #파일을 열수도 있음

#방어코드(안정장치)
if not cap.isOpened():
    print('camera open failed')
    exit()

# xml 분류기 파일 로드
face_cascade = cv2.CascadeClassifier('./xml/face.xml')

#동영상 촬영하기
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # 이미지에서 얼굴 검출
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    # 얼굴 위치에 사각형 출력하기
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),2) # 시작지정,시작포인트와 끝포인트,그릴 크기,선굵기
    cv2.imshow('frame', frame)
# 1000 = 1초, 10 = 0.01초
    if cv2.waitKey(10) == 13:
        break

# 사용자 자원 해제
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()  


