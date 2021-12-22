import cv2

# 카메라 장치 열기
cap = cv2.VideoCapture('output.avi') #파일을 열수도 있음 #0쓰면 카메라 여는거 파일명 쓰면 파일 여는거

#방어코드(안정장치)
if not cap.       d():
    print('camera open failed')
    exit()

#카메라 사진 찍기
#ret, frame = cap.read() #함수에 return값이 두개??(하나의 튜플이라서 하나지~) ^^ 가능 

#cv2.imshow('frame', frame) #사진 보여주기
#cv2.imwrite('output.jpg', frame) #사진 저장

#이 코드가 없으면 사진 보여주지 않아요!!
#cv2.waitKey(0) #10000면 10초 기다림. 0이면 무한정 기다림.

#동영상 촬영하기
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)

# 1000 = 1초, 10 = 0.01초
    if cv2.waitKey(10) == 13:
        break

# 사용자 자원 해제
cap.release()
cv2.destroyAllWindows()

#동영상 촬영 코드는 저장은 시키지 않고 화면에 실시간으로 촬영하고 있는 모습을 보여주는 코드