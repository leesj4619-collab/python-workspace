import pandas as pd
from pandas.core.common import random_state
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
import xgboost as xgb
import lightgbm as lgb

def 데이터분석하기():
    df = pd.read_csv('../csvs/seoulBike/SeoulBikeData.csv', encoding='latin1')

    # =================================
    # 1. 데이터 분석하는 메서드와 속성을 이용해서
    #   행 열 개수 컬럼 이름 목록 각 컬럼 타입 결측값 개수 컬럼별 결측값 정확히 보기
    #   평균 최소최대 표준편차
    #   문자 커럼 어떤 값들이 들어있는지
    #   그룹별 평균 비교
    # =================================
    print('='*20, '행 열의 개수','='*20)
    print(df.shape)
    print('='*20, '컬럼 목록','='*20)
    print(df.columns)
    print('='*20, '상위 5개의 행','='*20)
    print(df.head())
    print('='*20, '타입 + 결측 값','='*20)
    print(df.info())
    print('='*20, '결측값 개수','='*20)
    print(df.isnull().sum())

#데이터분석하기()
'''
==================== 행 열의 개수 ====================
(8760, 14)
==================== 컬럼 목록 ====================
Index(['Date', 'Rented Bike Count', 'Hour', 'Temperature(°C)', 'Humidity(%)',
       'Wind speed (m/s)', 'Visibility (10m)', 'Dew point temperature(°C)',
       'Solar Radiation (MJ/m2)', 'Rainfall(mm)', 'Snowfall (cm)', 'Seasons',
       'Holiday', 'Functioning Day'],
      dtype='str')
==================== 상위 5개의 행 ====================
         Date  Rented Bike Count  Hour  ...  Seasons     Holiday  Functioning Day
0  01/12/2017                254     0  ...   Winter  No Holiday              Yes
1  01/12/2017                204     1  ...   Winter  No Holiday              Yes
2  01/12/2017                173     2  ...   Winter  No Holiday              Yes
3  01/12/2017                107     3  ...   Winter  No Holiday              Yes
4  01/12/2017                 78     4  ...   Winter  No Holiday              Yes

[5 rows x 14 columns]
==================== 타입 + 결측 값 ====================
<class 'pandas.DataFrame'>
RangeIndex: 8760 entries, 0 to 8759
Data columns (total 14 columns):
 #   Column                     Non-Null Count  Dtype  
---  ------                     --------------  -----  
 0   Date                       8760 non-null   str    
 1   Rented Bike Count          8760 non-null   int64  
 2   Hour                       8760 non-null   int64  
 3   Temperature(°C)            8760 non-null   float64
 4   Humidity(%)                8760 non-null   int64  
 5   Wind speed (m/s)           8760 non-null   float64
 6   Visibility (10m)           8760 non-null   int64  
 7   Dew point temperature(°C)  8760 non-null   float64
 8   Solar Radiation (MJ/m2)    8760 non-null   float64
 9   Rainfall(mm)               8760 non-null   float64
 10  Snowfall (cm)              8760 non-null   float64
 11  Seasons                    8760 non-null   str    
 12  Holiday                    8760 non-null   str    
 13  Functioning Day            8760 non-null   str    
dtypes: float64(6), int64(4), str(4)
memory usage: 958.3 KB
None
==================== 결측값 개수 ====================
Date                         0
Rented Bike Count            0
Hour                         0
Temperature(°C)              0
Humidity(%)                  0
Wind speed (m/s)             0
Visibility (10m)             0
Dew point temperature(°C)    0
Solar Radiation (MJ/m2)      0
Rainfall(mm)                 0
Snowfall (cm)                0
Seasons                      0
Holiday                      0
Functioning Day              0
dtype: int64

'''
# 남이 만들어놓은 데이터를 이용해서 문제를 풀려 하기 때문에
# 데이터 분석 -> 데이터 전처리가 어려운 것

# 개발자나 분석가가 수집할 데이터의 기준을 정하고, 어떻게 사용하겠다
# 목표를 확실하게 정하면 분석과 전처리는 굉장히 쉬울 것이다.
# 강아지 고양이 돼지 수집 컬럼하나에 분류 강아지 고양이 돼지 작성

# 내가 목표로한 데이터가 아니고 남이 만든 데이터에 남이 만든 가정을 따라서
# 결과를 도달하려 하기 때문에 힘들다.
from sklearn.model_selection import train_test_split

# ================================
# 데이터 불러오기
# ================================
df = pd.read_csv('../csvs/seoulBike/SeoulBikeData.csv', encoding='latin1')

"""
==============================================
서울 따릉이 대여량 예측 프로젝트
==============================================

목표
시간대, 날씨, 계절 등의 데이터를 보고
따릉이 대여 횟수를 예측하는 모델 만들기

컬럼 정리
Date                      → 날짜          (버리기)
Rented Bike Count         → 대여횟수      (← 정답 y)
Hour                      → 시간
Temperature(°C)           → 기온
Humidity(%)               → 습도
Wind speed (m/s)          → 풍속
Visibility (10m)          → 가시거리
Dew point temperature(°C) → 이슬점
Solar Radiation           → 태양복사량
Rainfall(mm)              → 강우량
Snowfall (cm)             → 강설량
Seasons                   → 계절         (문자 → 숫자 변환 필요)
Holiday                   → 공휴일 여부  (문자 → 숫자 변환 필요)
Functioning Day           → 운영여부     (문자 → 숫자 변환 필요)

미션 1 - 데이터 파악
  df.shape, df.info(), df.isnull().sum() 으로
  데이터 크기 / 타입 / 결측값 확인하기

미션 2 - 전처리
  1) Date 컬럼 제거
  2) Seasons / Holiday / Functioning Day 문자 → 숫자 변환
     힌트 : .map() 사용
  3) X(입력), y(정답) 분리
     y → Rented Bike Count
     X → 나머지 전부
  4) train_test_split 으로 학습/검증 데이터 나누기
     test_size=0.2, random_state=42

미션 3 - 모델 학습
  아래 모델 중 최소 2개 이상 골라서 학습시키기
  ① LinearRegression
  ② GradientBoostingRegressor
  ③ XGBRegressor
  ④ LGBMRegressor

  주의 : 대여횟수는 숫자 예측 = 회귀 문제
         Classifier 쓰면 안 됨

미션 4 - 성능 비교
  .score() 로 R² 점수 출력
  0.8 이상 → 잘 된 것
  0.9 이상 → 매우 잘 된 것

미션 5 (도전)
  R² 0.90 이상 달성해보기
  힌트 : n_estimators, learning_rate, max_depth 조절
==============================================
"""

# 여기서부터 작성
df = df.drop(columns = ['Date'])
df['Seasons'] = df['Seasons'].map(
    {'Spring':0,
    'Summer':1,
    'Autumn':2,
    'Winter':3})
df['Holiday'] = df['Holiday'].map(
    {'Holiday':0,
    'No Holiday':1})
df['Functioning Day'] = df['Functioning Day'].map(
    {'Yes':0,
     'No':1})

X = df.drop(columns=['Rented Bike Count'])
y = df['Rented Bike Count']

X_train,X_text,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
lr_model = LinearRegression()
lr_model.fit(X_train,y_train)
print(f'LinearRegression R²: {lr_model.score(X_text,y_test):.4f}')

gbm_model = GradientBoostingRegressor()
gbm_model.fit(X_train,y_train)
print(f'GradientBoostingRegressor R²: {gbm_model.score(X_text,y_test):.4f}')

xgb_model = xgb.XGBRegressor()
xgb_model.fit(X_train,y_train)
print(f'xgb R²: {xgb_model.score(X_text,y_test):.4f}')

lgb_model = lgb.LGBMRegressor()
lgb_model.fit(X_train,y_train)
print(f'lgb R²: {lgb_model.score(X_text,y_test):.4f}')
'''
LinearRegression R²: 0.5128
GradientBoostingRegressor R²: 0.8311
xgb R²: 0.8644
lgb R²: 0.8746
'''
lgb_tuned = lgb.LGBMRegressor(
    n_estimators=500,   # 트리를 더 심오하고 많게 설정
    learning_rate=0.05, # 학습률 낮게, 더 정교하게
    max_depth=7,        # 트리 깊이 늘리기
    random_state=42
)
lgb_tuned.fit(X_train,y_train)
print(f'lgb 튜닝 R² : {lgb_tuned.score(X_text,y_test):.4f}')
'''
n_estimators
- 만약 작성하지 않으면 기본값으로 100 자동 설정
- 생성할 결정 트리의 개수 (부스팅 반복 횟수)
- 숫자가 클수록 학습을 더 많이 -> 성능 향상 가능, 하지만 과적합 속도 저하 위험
- 보통 100~ 1000 사이 많이 사용
- * 과적합 : 훈련데이터에만 적합되어 있어서 새로운 데이터는 틀리는 현상
-   지나칠  과
-   딱맞을  적
-   들어맞을 합 
    지나치게 훈련에만 딱 맞아버리는 결과 응용 X 

learning_rate
- 기본값 0.1
- 각 트리가 이전 트리의 오차를 얼마나 빠르게 교정할지 결정
- 낮을수록 -> 천천히 꼼꼼하게 학습(과적합 방지)
- 높을수록 -> 빠르게 학습하지만 제대로 살펴보지 않아 불안정
- 일반적으로 learning_rate 낮게 n_estimators 늘려서
-- 세부적으로 보고보고 또 보면서 제대로 꼼꼼하게 학습


max_depth
- 기본값 -1(제한없음)
- 개별 트리의 최대 깊이(가지를 몇 단계 까지 뻗을 수 있는가)
- 깊을수록 -> 복잡한 패턴 학습 가능, 하지만 과적합 위험
- 얕을수록 -> 단순하지만 과소적합 위험
- LightGBM은 max_depth 설정제한을어떻게 하느냐가 많이 중요
random_state
- 기본값 None(매번 다른 결과 발생)
- 기본값을 세팅한 후, 정확도가 높은 시작을 기준으로 고정하여 사용
- 어떤 시작 숫자가 좋은지는 아무도 모른다.
- 그것을 각 데이터와 모델별로 찾는 것이 일
- 시작을 42에서 출발하겠다.

트리 : 나무처럼 위에서 아래로 뻗어가는 구조
머신러닝에서 결정 트리 : 질문을 던지면서 답을 찾아가는 구조
루트 노드 : 맨 위 첫번째 질문
가지 : 질문의 Yes/No 경로
잎 노드 : 최종 답(더 이상 질문 x)
깊이 : 질문이 몇 단계까지 이어지는가

max_depth=7
예를 들어 집값 예측 데이터 -> 머신러닝에서 우선 데이터를 쭉~ 살펴본다.


'''















