#스위치로 LED제어하기
import RPi.GPIO as GPIO

LED_PIN1 = 16
SWITCH_PIN1 = 14
LED_PIN2 = 20
SWITCH_PIN2 = 15
LED_PIN3 = 21
SWITCH_PIN3 = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
#내부풀다운저항 (안 눌렀을 때 : 0, 눌렀을 때 : 1)
GPIO.setup(SWITCH_PIN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN2, GPIO.OUT)
#내부풀다운저항 (안 눌렀을 때 : 0, 눌렀을 때 : 1)
GPIO.setup(SWITCH_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN3, GPIO.OUT)
#내부풀다운저항 (안 눌렀을 때 : 0, 눌렀을 때 : 1)
GPIO.setup(SWITCH_PIN3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        val1 = GPIO.input(SWITCH_PIN1)
        print(val1)
        GPIO.output(LED_PIN1, val1)  #GPIO.HIGH(1), GPIO.LOW(0)
        val2 = GPIO.input(SWITCH_PIN2)
        print(val2)
        GPIO.output(LED_PIN2, val2)  #GPIO.HIGH(1), GPIO.LOW(0)
        val3 = GPIO.input(SWITCH_PIN3)
        print(val3)
        GPIO.output(LED_PIN3, val3)  #GPIO.HIGH(1), GPIO.LOW(0)
finally:
    GPIO.cleanup()
    print('cleanup and exit')