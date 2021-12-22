import cv2

# xml 분류기 파일 로드
face_cascade = cv2.CascadeClassifier('./xml/face.xml')
eye_cascade = cv2.CascadeClassifier('./xml/eye.xml')

img = cv2.imread('./AVENG.jpg') # 또는 ./없이 써도 무방
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

# 이미지에서 얼굴 검출
faces = face_cascade.detectMultiScale(gray)

# 얼굴 위치에 사각형 출력하기
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2) #포인트 시작 좌표,시작포인트와 끝포인트,색깔,선굵기

    # ROI (Region of Interest 즉 관심영역이라함)
    roi_color = img[y:y+h, x:x+w] # []안의 영역만을 확인함. [행,열] 값이다.
    roi_gray = gray[y:y+h, x:x+w]

    #눈 검출하기
    eyes= eye_cascade.detectMultiScale(roi_gray)

    #눈 위치의 사각형 출력하기
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color, (ex,ey),(ex+ew,ey+eh),(0,255,0),2) # 포인트 시작 좌표,시작포인트와 끝포인트,색깔,선굵기


cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()  