import RPi.GPIO as GPIO
import time

TRIGGER_PIN = 4
ECHO_PIN = 14
LED_PIN = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

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

        if distance <= 20:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print('led on')
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            print('led off')
            
        time.sleep(0.1)
finally:
    GPIO.cleanup()
    print('cleanup and exit')