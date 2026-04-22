# 파이썬 개발자들이 만들어서 기본으로 제공하는 기능
# 개발자들이 print() 만큼 자주 사용하지 않는 기능들은 import로 가져와서 사용
# 이미 파이썬 언어를 설치할 때 세팅이 되어 있고, 무겁지만 엄청나게 사용하지 않는
# 기본 모듈은 import로 가져와서 사용한다.(=또는 무거워서)
import random

def 로또번호생성():
    # sample = 중복없이 랜덤으로 뽑는 기능
    # sample(리스트, 뽑을 개수)
    숫자들 = random.sample(range(1,46),6)
    숫자들.sort() # 오름차순 정렬
    print("로또번호: ", 숫자들)

#로또번호생성()
def 로또번호여러줄생성():
    구매_원하는_줄수 = int(input('로또 번호 몇 장 필요하신가요? : '))
    for i in range(1, 구매_원하는_줄수+1):
        숫자들 = random.sample(range(1,46),6)
        숫자들.sort()
        print(f"{i}줄: {숫자들}")
#로또번호여러줄생성()
    # 소비자가 원하는 줄 수 만큼 로또번호를 출력
    # 1줄: [2, 27,35,40,43,45]
    # 2줄: [2, 27,35,40,43,45]
    # 3줄: [2, 27,35,40,43,45]
def 로또번호여러줄생성_응용버전():
    while True:
        try:
            구매_원하는_줄수 = int(input('로또 번호 몇 장 필요하신가요? : '))
            break
        except ValueError:
            print("숫자만 입력해주세요!")
        for i in range(1, 구매_원하는_줄수+1):
            숫자들 = random.sample(range(1,46),6)
            숫자들.sort()
            print(f"{i}줄: {숫자들}")

def 로또번호여러줄():
    로또번호줄 = int(input("로또번호 몇장이 필요하신가요?"))
    for i in range(1, 로또번호줄 + 1):
        숫자들 = random.sample(range(1,46) ,6)
        print(f"{i}번 :{숫자들}")
#로또번호여러줄()

def 로또번호():
    로또번호줄 = int(input("로또 구매 입력 : "))
    for i in range(1, 로또번호줄+1):
        숫자들 = random.sample(range(1,46),6)
        숫자들.sort()
        print(f"{i}줄 {숫자들}번호")
로또번호()