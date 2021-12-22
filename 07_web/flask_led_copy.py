# 동적으로 만들기!
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
@app.route("/led/<op>") # op 말고 cmd라고 해도 됨. ->값을 정적이 아닌 동적으로 처리하겠다.
def led_op(op): # ()안에 op를 꼭 써주어야 한다. ->@app.route("/led/<op>") == def led_op의 주고 받는 값이 같아야 하니까 설정해주어야 한다!! 둘은 자동적으로 같다고 설정되지 않으니까!
    if op == "on":
     return '''
        <p>LED ON</p>
        <a href="/">Go Home</a>
    '''
    elif op == "off":
     return '''
        <p>LED OFF</p>
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