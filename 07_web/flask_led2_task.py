from flask import Flask,render_template
import RPi.GPIO as GPIO

RED_PIN = 4
BLUE_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN,GPIO.OUT)
GPIO.setup(BLUE_PIN,GPIO.OUT)

app = Flask(__name__)



@app.route("/")
def hello_world():
    return render_template("led2.html")


@app.route("/led/<cl>/<op>")
def led_op(cl,op):
    if cl == "red" and op == "on":
        GPIO.output(RED_PIN,GPIO.HIGH)
        return "RED LED ON"

    elif cl == "red" and op == "off":
        GPIO.output(RED_PIN,GPIO.LOW)
        return "RED LED OFF"

    elif cl == "blue" and op == "on":
        GPIO.output(BLUE_PIN,GPIO.HIGH)
        return "BLUE LED ON"

    elif cl == "blue" and op == "off":
        GPIO.output(BLUE_PIN,GPIO.LOW)
        return "BLUE LED OFF"

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        print("clean up")
        GPIO.cleanup