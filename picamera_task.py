import picamera
import time

path = '/home/pi/src5/06_multimedia' #putty에서 pwd 입력하여 현재주소 확인후 복사하여 붙여넣기! 쓰기 번거로우니까!


camera = picamera.PiCamera()
now_str = time.strftime("%Y%m%d_%H%M%S")


try:
    camera.start_preview() #카메라 시작 알림, 반복해서 사진을 찍을때에도 한번만 써주면 됨.
    while True:
        cmd = input('photo: 1, video: 2, exit:9 >')
        if cmd == '1':
            camera.capture('%s/photo_%s.jpg' % (path,now_str)) #사진찍기
            print('사진 촬영')
        elif cmd == '2':
            camera.start_recording('%s/video_%s.h264' % (path,now_str)) #동영상찍기
        
            break
        else:
            print('incorrect cmd')
    
finally:
        camera.stop_preview() # 반복해서 사진을 찍을 때에도 한번만 이 명령어를 써주면 됨.
        camera.stop_recording()