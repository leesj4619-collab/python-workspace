import numpy as np
def 배열만들기():
    print(np.zeros(6))
    print(np.ones(5))
    #3. 0부터 30까지 5씩 건너뛰는 배열을 만들고 출력하세요
    print(np.arange(0,30,5))
    #4. 0부터 1까지 균등하게 나눈 값이 8개인 배열을 만들고 출력하세요
    print(np.linspace(0,1,8))
#배열만들기()

def 배열연산():
    a = np.array([10, 30, 50])
    b = np.array([2, 3, 5])


    print(a+b)

    print(a-b)

    print(a*b)

    print(a/b)

    c = [10,30,50]
    d = [2,3,5]
    일반파이썬리스트 = c + d
    print(일반파이썬리스트)
    # 일반파이썬리스트를 더하기하면 리스트가 이어지고, 넘파이리스트를 더하면 연산이 된다.
#배열연산()

def 인덱싱_슬라이싱_필터링():
    a = np.array([10, 20, 30, 40, 50, 60, 70])
    print(a[0])

    print(a[-1])

    print(a[2:6])

    print(a[a > 40])

    print(a[a%20==0])
#인덱싱_슬라이싱_필터링()

def 통계함수():
    scores = np.array([70, 85, 90, 55, 78, 92, 63, 88])
    print(scores.sum())

    print(scores.max())

    print(scores.min())

    print(scores.mean())

    print(scores.std())

    print(np.median(scores))
#통계함수()

def 카페매출분석():

    sales = np.array([30, 15, 42, 27, 38, 19, 50, 33])
    print(sales.sum())
    print(sales.mean())
    print(sales.max(), sales.min())
    평균 = sales.mean()
    print(sales[sales > 평균])
    # 5. 아메리카노 한 잔 가격이 4500원일 때,
    print(sales*4500)
#카페매출분석()