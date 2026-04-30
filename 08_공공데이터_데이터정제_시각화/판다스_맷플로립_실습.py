import pandas as pd
import matplotlib.pyplot as plt

# 한글 깨짐 방지
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('행정안전부_착한가격업소_현황_20260331.csv',encoding='cp949')

# 막대그래프를 이용해서 시도별 업소 수 집계
# .values_counts() = 시도별로 몇 개 씩 존재하는지 세어준다.
# 예 ) 서울특별시 2500 경기도 2000 부산광역시 1000
# len(df['시도']) = 시도에 총~ 데이터가 몇 개 존재하는지 세어준다.
# len(df['시도']=='서울특별시') -> .values_counts() 처럼 쓸 수 있으나
# 이러한 경우에는 컬럼내 동일 데이터가 몇개 존재하는지 개발자가 개수 확인

def bar():
    시도별_업소수 = df['시도'].value_counts() # 값데이터 개수 확인
    print('시도별 업소수 : ',시도별_업소수)
    plt.bar(시도별_업소수.index, 시도별_업소수.values)
    plt.title('시도별 착한업소 수')
    plt.xlabel('시도')
    plt.ylabel('업소 수')
    plt.xticks(rotation=45) # x축 글자 45도 기울기
    plt.tight_layout()      # 레이아웃 자동 정리 바 하나의 축에 여러개 있을때
    plt.show()
#bar
def pie():
    # 업종별 비율
    업종별_수 = df['업종'].value_counts()
    plt.pie(업종별_수.values,
            labels=업종별_수.index,
            autopct='%1.1f%%')
    plt.title('업종별 착한가격업소 비율')
    plt.show()
#pie()
def 히스토그램():
    # 가격대가 얼마나 퍼져있나
    df_가격 = df['가격1'].dropna() # 결측치를 위해서 가격 없는 행 제거 또는 0으로 만들기
    df_가격_숫자변환 = pd.to_numeric(df_가격, errors='coerce') # 판다스에서 제공하는 csv에서 문자 -> 숫자 변환
    df_가격_숫자변환_실패한데이터_제거 = df_가격_숫자변환.dropna() # 변환 실패한 NaN 한번 더 제거
    # bins = 몇 개의 구간으로 나눌 것인가
    # 가격 범위 250~330,000 너무 넓어 줄여도 한쪽 몰리는 현상 발생
    # 30000원 이하만 본다던지 가격 범위를 설정하고 보는 것을 추천

    # 개발자가 숫자 자리 라고 표기해서 input 과 같은 틀을 만들어주지 않는
    # 모든 숫자는 문자열으로 이루어져 있다 -> 숫자 깨짐 방지
    df_가격범위_3만원 = df_가격_숫자변환_실패한데이터_제거[df_가격_숫자변환_실패한데이터_제거 <= 30000]
    plt.hist(df_가격범위_3만원, bins=10)
    plt.title('착한 가격업소 가격 분포')
    plt.xlabel('가격 (원)')
    plt.ylabel('업소 수')
    plt.show()
#히스토그램()
def 스카터():
    # 가격1과 가격2 비교
    df_가격비교 = df[['가격1','가격2']].dropna() # 가격1과 가격2 결축치(빈 값)제거
    # 숫자로 변환
    df_가격비교['가격1'] = pd.to_numeric(df_가격비교['가격1'],errors='coerce')
    df_가격비교['가격2'] = pd.to_numeric(df_가격비교['가격2'],errors='coerce')
    df_가격비교_결측치제거 = df_가격비교.dropna()

    df_가격비교_3만원이하 = df_가격비교_결측치제거[(df_가격비교_결측치제거['가격1'] <= 30000) & (df_가격비교_결측치제거['가격2'] <= 30000)]
    plt.scatter(df_가격비교_3만원이하['가격1'],df_가격비교_3만원이하['가격2'], alpha=0.5)
    plt.title('메뉴1 가격 vs 메뉴2 가격')
    plt.xlabel('메뉴1 가격')
    plt.ylabel('메뉴2 가격')
    plt.show()
스카터()

