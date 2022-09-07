# 가장 기본적인 웹서버 오픈하는 내용

from flask import Flask, render_template, request, redirect
# 회색으로 보여지는 부분은 아래부분에 현재 사용하지 않다는 의미.
# 지워도 상관없다~
import pandas as pd

# -------------------------------------------------------------------------------------


# Flask라는 Class에서 __init__함수에 self를 제외한 매개변수가 1개 있다~
# __name__ : 자기 자신의 파일이름
app = Flask(__name__)
# 사람들이 뭐라고 파일이름을 적을지 모르고, 파일이름을 적을 때 생각보다 에러가 많이 나니까, 
# 이렇게 하면 이름 자동으로 만들어줄게 한 것



# api 생성

# 127.0.0.1:5000
# 5000이라는 숫자는 port 번호
# port? 
# 127.0.0.1 = localhost

# localhost:5000/
@app.route('/') 
# @app.route() -> localhost:5000/ 요청이 있는 경우에 바로 아래에 있는 함수를 실행
# localhost 뒤에 오는 주소를 적어줌
def index():
    return render_template('index.html')
# localhost:5000/index 치면 나옴

# -------------------------------------------------------------------------------------

# get 형식에서 데이터는 url에 실어서 보낸다.
# request -> 유저가 서버에게 보내는 데이터를 dict 형태로 출력
# 유저가 보낸 데이터 중 url에 있는 데이터는 : request.args에 있음 -> 이 형태도 dict 형태.
# 웹은 거의 모든 데이터가 dict의 형태로, dict의 형태로 들어올 것.

@app.route('/second')
def second():
    _id = request.args.get("ID")
    _pass = request.args.get("password")
    # id값과 password값
    # id는 test, password는 1234
    # 위의 조건이 만족해야만 second.html 리턴
    # 위의 조건이 거짓이면 '로그인 실패' 메시지 리턴

    print(request)

#    if _id == 'test' and _pass == '1234': # and를 &로 쓰면 안돌아감
#        return render_template('second.html')
#    else :
#        return redirect('/') # 이 형태로, redirect에 주소를 넣어두는 형태로 넣어두면 다시 / 주소로 (로그인 페이지로) 돌아옴
#        return '로그인 실패' # ('로그인 실패')해도 돌아감

#    print(_id, _pass)
    return render_template('second.html')

# -------------------------------------------------------------------------------------

# localhost:5000/third post형식으로 요청시
@app.route("/third", methods=['post'])
def third():
    _title = request.form['title']
    _content = request.form['content']
    print(_title, _content)
    return render_template('third.html', content=_content, title=_title)

# -------------------------------------------------------------------------------------

@app.route('/dashboard')
def dashboard():
    print("dashbord")
    df = pd.read_csv("../csv/corona.csv")
    #컬럼의 이름 변경
    df.columns = ['인덱스', '등록일시', '사망자', '확진자', '게시글번호', '기준일', '기준시간', '수정일시', '누적의심자', '누적확진률']
    # 등록일시 기준으로 오름차순 정렬
    df.sort_values("등록일시", inplace=True)
    # 일일 확진자, 일일 사망자라는 파생변수 생성
    df['일일확진자'] = df['확진자'] - df['확진자'].shift()
    df['일일사망자'] = df['사망자'].diff()
    data = df.head(50)
    _cnt = len(data)
    _decide_data = data['일일확진자'].tolist()
    _date_list = data['등록일시'].tolist()
    _die_data = data['일일사망자'].tolist()

    return render_template('dashboard.html', cnt=_cnt, date_list=_date_list, decide_data=_decide_data, die_data=_die_data)


# app은 Flask라는 Class
# Flask라는 Class 안에 있는 run()이라는 함수 호출
app.run()

# run 안에 여러 함수가 들어가 있지만 기본값을 호출



## 실제 서버와 유저 간의 데이터 이동
## dict형태의 데이터로 request / response
## request -> 유저가 서버에게 보내는 데이터
## response -> 서버가 유저에게 보내는 데이터
## request{key : value, 
##         key2 : value, 
##         args : {
#                   ID : input에서 입력한 값(ID), 
#                   password : input에서 입력한 값(password)
#                  }
#         }
# ID 값만 찾고 싶으면
# request["args"]["ID"] == request.args.get("ID")