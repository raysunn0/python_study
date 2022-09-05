x = "module test"

def func_1(a, b):
    return a + b

#클래스 사용하지 않고 변수만 저장

#클래스 생성

class Class_1():
    def __init__(self, input_data):
        self.data = input_data

    def view_data(self):
        return f"Class에서 입력받은 data의 값은 {self.data}이다."
                #f는 find 함수. ""문자열 안에 {} 중괄호를 표시해서, self.data 데이터를 찾아서 string 형태로 넣어준다.
                #%d보다 더 많이 사용한다.