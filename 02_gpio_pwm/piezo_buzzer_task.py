# 학교종이 땡땡땡 연주하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10)

melody = [392, 392, 440, 440, 392, 392, 330, 392, 392, 330, 330, 294, 392, 392, 440, 440, 392, 392, 330, 392, 330, 294, 330, 262]

try:
    for i in melody:
         pwm.ChangeFrequency(i)  #주파수를 변경하는 것(음계변경-도->레...), duty cycle 10값은 고정
         time.sleep(0.5)

finally:
    pwm.stop()
    GPIO.cleanup()