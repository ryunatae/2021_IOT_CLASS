# 정적으로 만들기!
from flask import Flask

# Flask 객체 생성
# __name__은 파일명
app = Flask(__name__)

# 라우팅을 위한 뷰 함수
@app.route("/") # '''를 세개 찍으면 문자열이됨.(줄이 나누어지는!!)
def hello_world():
    return '''   
        <p>Hello, Flask!!</p>
        <a href="/led/on">LED ON</a>
        <a href="/led/off">LED OFF</a>
'''
#함수마다 routing을 걸어주어야함.
@app.route("/led/on")
def led_on():
    return '''
        <p>LED ON</p>
        <a href="/">Go Home</a>
    '''

@app.route("/led/off")
def led_off():
    return '''
        <p>LED OFF</p>
        <a href="/">Go Home</a>
    '''

# 터미널에서 직접 실행시킨 경우
if __name__ == "__main__":
    app.run(host="0.0.0.0")