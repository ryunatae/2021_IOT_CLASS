import cv2

# image 파일 읽기
img = cv2.imread('BTS.jpg') # 괄호 안에는 파일명입력
img = cv2.resize(img, (600,400))

#엣쥐선 추출
edge = cv2.Canny(img, 50, 100) #인자 값이 작을 수로 엣쥐선 추출이 세밀함.
edge1 = cv2.Canny(img, 100, 150) 
edge2 = cv2.Canny(img, 150, 200) 


cv2.imshow('BTS', img) # 괄호 안에  (window주소(이건 마음대로 써도됨),출력할 영상 데이터) 써주기
cv2.imshow('edge', edge)


# 키보드 입력을 기다림(millisecond)
# 기본값 0,0인 경우 키보드 입력이 있을 때까지 계속 기다림
cv2.waitKey(0)

# 열려있는 모든 창 닫기
cv2.destroyAllWindows()                                                       