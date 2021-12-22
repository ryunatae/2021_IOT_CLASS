import cv2

# xml 분류기 파일 로드
face_cascade = cv2.CascadeClassifier('./xml/face.xml')

#gray 스케일 이미지로 변환
img = cv2.imread('./AVENG.jpg') # 또는 ./없이 써도 무방
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

# 이미지에서 얼굴 검출
faces = face_cascade.detectMultiScale(gray)

# 얼굴 위치에 사각형 출력하기(좌표정보 가져오기)
for (x,y,w,h) in faces:
    # 원본이미지에 얼굴 위치 표시
    cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2) # 시작지정,시작포인트와 끝포인트,그릴 크기,선굵기

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()  

# Haar cascade 객체 검출 방법 사용.