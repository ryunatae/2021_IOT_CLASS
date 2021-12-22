import picamera
import time

path = '/home/pi/src5/06_multimedia' #putty에서 pwd 입력하여 현재주소 확인후 복사하여 붙여넣기! 쓰기 번거로우니까!


camera = picamera.PiCamera()

try:
    camera.resolution = (640,480) # 사진 사이즈 조정(가로길이,세로길이)
    camera.start_preview() #카메라 시작 알림, 반복해서 사진을 찍을때에도 한번만 써주면 됨.
    time.sleep(3) #카메라 촬영시 준비시간
    # camera.capture('%s/photo.jpg' % path) #사진찍기
    camera.start_recording('%s/video.h264' % path) #동영상찍기
    # time.sleep(5) -> 이렇게 쓰면 시간을 계속 바꾸어야 하니
    input('press enter to stop') # 이렇게 쓰면 입력값을 받지 않고 enter한번만 누르면(입력하면) 동영상 마침.
    camera.stop_recording()
finally:
    camera.stop_preview() # 반복해서 사진을 찍을 때에도 한번만 이 명령어를 써주면 됨.