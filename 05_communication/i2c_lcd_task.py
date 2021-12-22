from lcd import drivers
import datetime
import Adafruit_DHT

display = drivers.Lcd()
sensor = Adafruit_DHT.DHT11 #소스파일 사용
DHT_PIN = 22

try:
    print('Writing to Display')
    display = drivers.Lcd()
    
    while True: #한번만 출력할것이 아닌것들
        now = datetime.datetime.now()
        display.lcd_display_string(now.strftime("%x%X"), 1) #08/14/21 12:17:10의 형식으로 출력됨(여기서 %x %X라고 처음엔 입력하라 했지만 LCD의 한 줄 당 
                                                            #최대 16칸이기에 출력할 수 있는 글자가 16개이다. 따라서 %x %X사이의 공백을 없애준다.그래야 출력이 안짤린다.)
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        display.lcd_display_string("%.1f*C, %.1f%%"% (t, h), 2)

finally:
    print('cleaning up')
    display.lcd_clear()

    # 시간에 처음에는 제대로 나오지 않아서 putty에서
    # sudo raspi-config => Localisation => TimeZone => Asia => Seoul로 바꾸어 출력!
    # 2-3초 정도의 딜레이가 생김.