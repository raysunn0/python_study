from flask import Flask

# __name__ : 파일의 이름
app = Flask(__name__) #F 대문자니까 Class 구나 추측 가능


@app.route("/")  # 127.0.0.1 : 5000/ 로 접속 했을 때 바로 밑에 함수를 실행하겠다.
def index(): #함수 이름 상관없음
    return "Hello World"

# 127.0.0.1:5000/second 웹 브라우저를 이용하여 요청을 했을 때 바로 밑에 함수를 실행
@app.route("/second")
def second():
    return "Second Page"

app.run() 