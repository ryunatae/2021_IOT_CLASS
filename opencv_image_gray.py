import cv2

# image 파일 읽기
img = cv2.imread('BTS.jpg') # 괄호 안에는 파일명입력
img = cv2.resize(img, (600,400))

# 흑백 이미지로 바꾸기
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

cv2.imshow('BTS', img) # 괄호 안에  (window주소(이건 마음대로 써도됨),출력할 영상 데이터) 써주기
cv2.imshow('BTS_GRAY', gray)

# 키보드 입력을 기다림(millisecond)
# 기본값 0,0인 경우 키보드 입력이 있을 때까지 계속 기다림

#특정 키를 입력받았을 경우에만 창 닫기
while True:
    if cv2.waitKey(0) == 13: # (아스키코드로 13은 enter키를 나타냄, esc는 27, A는 65)
        break

# 파일 저장시키기
cv2.imwrite('BTS_GRAY.jpg', gray)

# 열려있는 모든 창 닫기
cv2.destroyAllWindows()