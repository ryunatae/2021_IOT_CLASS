#LED제어(불을 서서히 키고 서서히 끄고)
import RPi.GPIO as GPIO
import time

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# PWM 인스턴스 생성
# 주파수(1초에 사이클을 몇번 반복할건지) 설정(Hz)
pwm = GPIO.PWM(LED_PIN, 50)
pwm.start(0)  # duty cycle (0~100) - 0은 꺼진상태를 의미

try:
    for i in range(0, 3, 1): # 0부터 시작해서 3-1인 2까지를 반복 그러니 총 3번 반복.(0과 1은 생략이 가능)
        #서서히 켜지게 하기
        for j in range(0, 101, 5):  # start, end, step (0부터 시작해서 101-1인 100까지 간격 5로 해서 총 100번 반복)
            pwm.ChangeDutyCycle(j)
            time.sleep(0.1)
            # 서서히 꺼지게 하기(100부터 0까지 5씩 감소하면 됨)
            for j in range(100, -1, -5):
                pwm.ChangeDutyCycle(j)
                time.sleep(0.1)
finally:
    pwm.stop()
    GPIO.cleanup()
    print('cleanup and exit')