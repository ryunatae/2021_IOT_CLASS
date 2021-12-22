import cv2

# 카메라 장치 열기
cap = cv2.VideoCapture(0) #파일을 열수도 있음

#방어코드(안정장치)
if not cap.isOpened():
    print('camera open failed')
    exit()

# fourcc(four character code): DIVX(avi), MP4V(mp4), X264(h264)
fourcc= cv2.VideoWriter_fourcc(*'DIVX') #*쓰기 싫으면 ('D', 'I', 'V', 'X')라 써도 됨. -> 파일 설정작업

out = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480)) # (동영상 파일명, fourcc,초당 프레임 수,프레임의 사이즈(튜플데이터 타입-함수 인자를 두개입력도 하나로 취급))

#동영상 촬영하기 
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    out.write(frame) #파일 저장작업코드

# 1000 = 1초, 10 = 0.01초
    if cv2.waitKey(10) == 13:
        break

# 사용자 자원 해제
cap.release()
out.release()
cv2.destroyAllWindows()

#동영상 촬영 코드는 저장은 시키지 않고 화면에 실시간으로 촬영하고 있는 모습을 보여주는 코드