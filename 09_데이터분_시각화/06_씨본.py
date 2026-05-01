'''
Seaborn python 데이터 시각화 라이브러리
matplotlib 기반으로 만들어졌지만 훨씬 적은 코드로 예쁜 그래프 그릴 수 있다.
판다스 DataFrame과 함께 데이터 분석할 때 자주 사용

주 종류
scatterplot 산점도 분포 파악
lineplot    선 그래프 추세 파악
histplot    히스토그램
barplot     바그래프 카테고리별 평균
boxplot     부포 이상치 확인
heatmap     색상으로 상관관계

설치 방법
pip install seaborn
'''
import os
import time

import seaborn as sns
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 그래프로 확인할 데이터셋 선택
df =sns.load_dataset('tips')
# seaborn 회사에 tips.csv와 같은 형태로 데이터가 csv 형태로 보관되어 있는 데이터를
# seaborn 회사에서 .csv 없이 사용할 수 있도록 코딩 세팅을 해놓았기 때문에
# tips라는 명칭으로 가볍게 우리가 seaborn 테스트할 수 있는 것

def 판다스를_이용하여_데이터구조확인():
    print(df.head())
    print("=="*80)
    print(df.shape)
    print("=="*80)
    print(df.columns)
    print("=="*80)
    print(df.dtypes)
    print("=="*80)
    print(df.describe())
#판다스를_이용하여_데이터구조확인()

def 맷플로립을_이용하여_데이터눈으로확인():
    sns.scatterplot(data=df, x='total_bill',y='tip',hue='sex')
    plt.title('계산서 vs 팁')
    plt.show()

def seaborn에서_만든데이터_나의컴퓨터에_판다스로_csv로_저장하기():
    df.to_csv('seaborn.csv',index=False,encoding='utf-8-sig')
    print("seaborn에서_만든데이터_나의컴퓨터에_판다스로_csv로_저장완료")
#seaborn에서_만든데이터_나의컴퓨터에_판다스로_csv로_저장하기()

def seaborn_dataset_all_save():
    저장할폴더 = 'seaborn_data'
    os.makedirs(저장할폴더,exist_ok=True)

    dataset=['tips','titanic','iris','penguins','flights','diamonds','mpg']
    for name in dataset:
        df =sns.load_dataset(name)
        df.to_csv(f'{저장할폴더}/seaborn_{name}.csv',index=False,encoding='utf-8-sig')
        time.sleep(1)
        print(f'seaborn_{name}.csv 저장완료')

seaborn_dataset_all_save()

