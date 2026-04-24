class 구글:
    def __init__(self,이름,이메일):
        self.이름 = 이름
        self.이메일 = 이메일

    def 로그인(self):
        print(f'{self.이름} 구글 로그인 완료')

    def 프로필출력(self):
        print(f'이름: {self.이름}, 이메일 {self.이메일}')

class 유튜브(구글):
    def __init__(self,이름,이메일,채널명):
        super().__init__(이름, 이메일)
        self.채널명 = 채널명

    def 영상업로드(self):
        print(f'{self.채널명} 채널에 영상 업로드 완료')

    def 구독자확인(self):
        print(f'{self.채널명} 채널 구독자 확인중')

public class Main {
public static void main(String[] args) {
유튜브 철수 = new 유튜브("철수", "철수@gmail.com", "철수TV");

철수.로그인();
철수.프로필출력();
철수.영상업로드();
철수.구독자확인();


'''
위 자바 코드를 파이썬으로 바꿔봐

조건
1. class 구글 만들기
2. class 유튜브 가 구글 상속받기
3. super() 써서 부모 __init__ 호출하기
4. 메서드 4개 똑같이 만들기
5. 객체 만들어서 전부 호출하기

철수 구글 로그인 완료
이름: 철수, 이메일: 철수@gmail.com
철수TV 채널에 영상 업로드 완료
철수TV 채널 구독자 확인중
'''