from 회원 import 회원
from 로그인기능 import 로그인기능
from 알림기능 import 알림기능

class 프리미엄회원(회원, 로그인기능, 알림기능):

    def __init__(self, 이름, 나이, 이메일):
        super().__init__(이름, 나이, 이메일)

    def 혜택안내(self):
        print(f"{self.이름}님의 혜택: 프리미엄 적립 10% + 전용 CS")