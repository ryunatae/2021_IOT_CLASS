import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11 #소스파일 사용
DHT_PIN = 4

try:
    while True:
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if h is not None and t is not None:
            print('Temperature = %.1f*, Humidity=%.1f%%' % (t, h)) # %%는 데이터 자체의 퍼센트를 의미하며 %는 서식문자를 의미한다. 그래서 습도뒤에 %%해줘야함.
        else:
            print('Read Error')
finally:
    print('bye')