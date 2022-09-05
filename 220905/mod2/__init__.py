import pandas as pd

# mod2 모듈 내용 수정

class Class_df():
    def __init__ (self, _path): #_path : _는 입력받은 값을 의미
        self.df = pd.read_csv(_path)

    def change(self, _column):
        # 공백제거
        self.df[_column] = self.df[_column].str.replace(" ", "") # .str.upper()여기 붙여도 됨
        # 대문자로 변환
        self.df[_column] = self.df[_column].str.upper()
        return self.df

    def change_time(self, _column, _format = ""):
        if _format == "":
            self.df[_column] = pd.to_datetime(self.df[_column])
        else:
            self.df[_column] = pd.to_datetime(self.df[_column], format = _format)
        return self.df

    def create_date(self, _column):
        self.df['year'] = self.df[_column].dt.strftime("%Y")
        self.df['month'] = self.df[_column].dt.strftime("%m")
        self.df['day'] = self.df[_column].dt.strftime("%d")
        return self.df

    def review(self):
        return self.df 