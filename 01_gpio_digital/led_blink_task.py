import RPi.GPIO as GPIO
import time

RED_PIN = 4
YELLOW_PIN = 24
GREEN_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)


GPIO.output(RED_PIN, GPIO.HIGH)
print("led on")
time.sleep(2)
GPIO.output(RED_PIN, GPIO.LOW)
print("led off")
GPIO.output(YELLOW_PIN, GPIO.HIGH)
print("led on")
time.sleep(2)
GPIO.output(YELLOW_PIN, GPIO.LOW)
print("led off")
GPIO.output(GREEN_PIN, GPIO.HIGH)
print("led on")
time.sleep(2)
GPIO.output(GREEN_PIN, GPIO.LOW)
print("led off")


GPIO.cleanup()