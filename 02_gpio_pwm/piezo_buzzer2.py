# 도레미파솔라시도 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 주파수 설정 (262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10)  # duty cycle (0~100)- 역할은 소리의 크기임

# 도레미파솔라시도 
melody = [262, 294, 330, 349, 392, 440, 454, 523]

try:
    for i in melody:
         pwm.ChangeFrequency(i)  #주파수를 변경하는 것(음계변경-도->레...), duty cycle 10값은 고정
         time.sleep(1)

finally:
    pwm.stop()
    GPIO.cleanup()