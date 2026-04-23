def problem1():
    과일들 = ['사과','딸기','포도']
    print("과일 개수:",len(과일들))
#problem1()

def 문제2(a,b):
    return a*b
result = 문제2(6, 7)
print(f"a,'곱하기',b,'은',{result},'입니다.'")

def 문제3():
    name=input('이름을 작성해주세요: ')
    print(f'{name}님, 환영합니다!')
#문제3()
def 문제4(a,b,c):
    return (a+b+c) / 3
#평균=문제4(10,20,30)
#print(평균)

def 문제4_1(*args):
    return sum(args)/len(args)
#평균=문제4_1(10,20,30)
#print(평균)

def 문제5(name,greeting='좋은하루에요'):
    print(f"{greeting}, {name}님!")
# 문제5('지수')
# 문제5('민준', '오랜만이에요')

def order(menu, size, temperature):
    print(f"{temperature} {size} {menu} 주문 완료!")
order('라지','아메리카노','아이스')

def is_even(n):
    return n % 2 ==0
print(f"4는 짝수입니다:{is_even(4)}")
print(f"7는 홀수입니다:{is_even(7)}")


#기본값이 있는 매개변수가 () 안에 존재할 경우에는 반드시 기본값 없는 매개변수 뒤에 위치하고,
# 매개변수 안에서 기본값이 없는 매개변수들이 맨 앞으로 위치해야한다.
def introduce(name, age=20, city="서울"):
    print(f"{name} / {age}세 / {city}")

def profile(age=23, name="하은"):
    print(f"이름:{name},나이 : {age}세")
profile()


def add(a,b):
    return a+ b

def show(n):
    print(f"결과는 {n} 입니다")
show(add(7, 8))
print(add(7,8))
