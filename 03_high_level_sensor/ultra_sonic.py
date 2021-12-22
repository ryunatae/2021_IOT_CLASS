# 실행했을때 거리가 변하지 않으면 3.3V에 연결한 거임. -> VCC를 5V에 연결해야 합니다.->그런데 그러면 라즈베리가 벅차함으로 3.3v로 변환시켜야함->저항달기
import RPi.GPIO as GPIO
import time

TRIGGER_PIN = 4
ECHO_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

try:
    while True:
        GPIO.output(TRIGGER_PIN, GPIO.HIGH)
        time.sleep(0.00001)  # 10us (마이크로세컨드) (1us -> 0.000001s)
        GPIO.output(TRIGGER_PIN, GPIO.LOW)

        while GPIO.input(ECHO_PIN) == 0:
            pass
        start = time.time()  # 시작시간 (1이 되는 순간!)

        while GPIO.input(ECHO_PIN) == 1:
            pass
        stop = time.time() # 종료시간
    
        duration_time = stop - start  #걸린시간
        distance = 17160 * duration_time #거리

        print('Distance: %.1fcm' % distance)
        time.sleep(0.1)
finally:
    GPIO.cleanup()
    print('cleanup and exit')