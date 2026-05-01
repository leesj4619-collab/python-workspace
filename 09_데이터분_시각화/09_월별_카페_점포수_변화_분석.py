import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure

df = pd.read_csv("소상공인시장진흥공단_전국_카페_점포수_11_04_2019.csv", encoding="cp949")
업소수 = np.array(df["업소수"])

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus']=False

def 데이터확인():
    print(df.head())
    print(df.shape)
    print(업소수)
#데이터확인()

def 통계분석():
    print(업소수.sum())
    print(업소수.max())
    print(업소수.min())
    print(업소수.mean())
    print(업소수.std()) # 표준편차가 크게 차이가 날수록 평균에서 값이 멀다.
    print(np.median(업소수))
#통계분석()

def 인덱싱_슬라이싱_필터링():
    print(업소수[0])
    print(업소수[-1])
    print(업소수[5:16])
    print(업소수[업소수 >= 80000])
    평균 = 업소수.mean() # np.mean(업소수)
    print(업소수[업소수 > 평균])
#인덱싱_슬라이싱_필터링()

def 배열연산응용():
    만단위 = 업소수/10000
    print(만단위)
    #2. 업소수가 전월 대비 증가했는지 보려면 어떤 연산이 필요할지
    #생각해보고, 두 번째 달부터 마지막 달까지의 배열과
    #첫 번째 달부터 마지막 직전 달까지의 배열을 빼서 출력하세요
    print(업소수[1:] - 업소수[:-1])
#배열연산응용()

def 시각화():
    # 1. 기준월을 x축, 업소수를 y축으로 꺾은선 그래프를 그리세요
    plt.figure(figsize=(12,5))
    plt.plot(df['기준월'],df['업소수'],marker='o')
    # 2. 제목을 "전국 카페 월별 점포수 변화"로 설정하세요
    plt.title("전국 카페 월별 점포수 변화")
    # 3. x축 이름을 "기준월", y축 이름을 "업소수"로 설정하세요
    plt.xlabel('기준월')
    plt.ylabel('업소수')
    # 4. x축 레이블이 겹치지 않도록 rotation=45 를 적용하세요
    plt.xticks(rotation=45)
    # 5. 그래프를 출력하세요
    plt.show()
시각화()