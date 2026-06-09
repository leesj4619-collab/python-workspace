'''
기본적인 주식 용어 정리
가격 관련
시가     - 그 날 장 시작할 때 첫 거래 가격
종가     - 그 날 장 마감할 때 마지막 거래 가격(보통 예측 대상)
고가/저가 - 그 날 중 제일 높았던 / 낮았던 가격
전일 대비 - 어제 종가 대비 오늘 얼마나 올랐는지 / 내렸는지
52주 최고/최저 - 1년 중 제일 높았던/낮았던 가격

거래 관련
거래량 - 그 날 몇 주를 사고 팔았는가
거래 대금 - 거래량 X 가격 (총 얼마어치 거래되었는가)
호가 - 사겠다/ 팔겠다 올려놓은 가격
매수 호가 - 사려는 사람이 부른 가격
매도 호가 - 팔려는 사람이 부른 가격

시장 관련
코스피 - 삼성전자, 현대차 같은 대형 기업이 모인 시장
코스닥 - 중소 / 벤처기업 위주 시장
상한가/하한가 - 하루에 오를 수 있는 최대 / 내릴 수 있는 최대

LSTM으로 예측할 때 쓰는 것들

Close   종가  주로 이것으로 가격 예측
Open    시가  보조로 가끔 사용
High    고가  보조로 가끔 사용
Low     저가  보조로 가끔 사용
Volume 거래량 같이 넣으면 정확도 올라간다.

'''
'''
미국 주식 숫자와 국가를 붙이지 않음
이외 다른 주식은 숫자와 국가를 붙여 표기
애 플   AAPL
엔비디아 NVDA
구 글   GOOGLE

한국 숫자 6자리 표기 .KS .KQ
KS 대기업 기준
삼성전자 005930.KS
SK하이닉스 000660.KS
KQ 중견 중소 스타트업 기준
코스닥
숫자여섯자리 .KQ

미국 주식의 경우 환율을 계산해서 원화로 표기해야하는 번거로움 발생 
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, LSTM, Dense

plt.rcParams['font.family'] = 'Malgum Gothic'
plt.rcParams['axes.unicode_minus'] = False

def 데이터불러오기(경로):
    # 아래 방법은 csv를 가져올 때 가져올 컬럼과 행까지 한번에 전처리하여
    # csv 파일을 가져오는 방법
    # header csv 파일에서 헤더가 두 가로줄 이상으로 나뉘어져 있을 때
    #           어디서부터 어디까지의 가로줄이 컬럼이다. 표기하는 방법
    #           거의 사용할 일 없다.
    # index_col = 0 첫 번째 컬럼(Date)를 인덱스로 사용할 때 표기
    #               안 쓰면 날짜가 그냥 일반 컬럼으로 사용된다.
    # skiprows = 2 쓸모 없는 가로줄 제거 0,1,2 ...... 에서 2에 해당하는 가로줄 제거
    # df = pd.read_csv(경로, header=[0,1], index_col=0, skiprows=2)
    # samsung.csv 파일에서 날짜를 순번으로 사용하고, 가로 1번째줄, 2번째줄 제거
    # 의미 없는 가로 두 줄 데이터이기 떄문
    df = pd.read_csv(경로, index_col=0, skiprows=[1,2])
    '''
    row 0 번째 Price,Close,High,Low,Open,Volume
    row 1 번째 Ticker,005930.KS,005930.KS,005930.KS,005930.KS,005930.KS
    row 2 번째 Date,,,,,
    
    skiprows=[1,2]
    row 1,2 첫번째 두번째 줄 삭제
    '''
    df.index = pd.to_datetime(df.index)     # 위에서 선택한 인덱스를 날짜 형식 반환
    df.columns = ['Close','High','Low','Open','Volume'] # 컬럼명 직접 지정
    return df[['Close']] # 종가 컬럼만 가져와서 사용하겠다.

def 정규화(종가):
    스칼라 = MinMaxScaler()              # 0~1 변환기 생성
    스케일처리 = 스칼라.fit_transform(종가) # 실제 0~1로 변환
    return 스케일처리, 스칼라              # 변환한 데이터와 나중에 되돌릴 때 필요해서 스칼라

def 시퀀스만들기(데이터, window=60):
    X,y = [], []
    for i in range(window, len(데이터)):
        X.append(데이터[i - window:i]) # 60일치를 훈련 데이터로 넣고
        y.append(데이터[i])            # 그 다음날 정답 예측
    return np.array(X), np.array(y)

def 학습_테스트_모델분리(X,y,분류기준=0.8):
    분리하기 = int(len(X) * 분류기준)           # 전체 80%가 되는 개수 확인 총데이터 수 0.8
    # X_train에는 0에서부터 80% 데이터를 넣고
    # X_test 에는 81  부터 20% 데이터를 모두 가져오겠다.
    X_train, X_test = X[:분리하기],X[분리하기:] # 앞 80% 학습용 / 뒤 20% 테스트용 사용
    y_train, y_test = y[:분리하기],y[분리하기:] # 앞 80% 학습용 / 뒤 20% 테스트용 사용
    return X_train,X_test,y_train,y_test



# 힌트: Sequential 안에 Input → LSTM(64, return_sequences=True) → LSTM(32) → Dense(1) 순서
# 힌트: compile 은 optimizer='adam', loss='mse'
def 모델만들기(window=60):
    model = Sequential([
        Input(shape=(window, 1)),
        LSTM(64, return_sequences=True),
        LSTM(32),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    model.summary()
    return model

# 힌트: model.fit() 사용
# 힌트: epochs=20, batch_size=32, validation_split=0.1
def 학습하기(model, X_train, y_train):
    model.fit(X_train, y_train,
              epochs=30,
              batch_size=64,
              validation_split=0.1)
    return model

# 힌트: model.predict() 로 예측
# 힌트: 예측값이 0~1 이라서 스칼라.inverse_transform() 으로 실제 주가로 되돌려야 함
def 예측하기(model, X_test, y_test, 스칼라):
    예측 = model.predict(X_test)
    예측주가 = 스칼라.inverse_transform(예측)
    실제주가 = 스칼라.inverse_transform(y_test)
    return 예측주가, 실제주가

# 힌트: plt.figure(figsize=(12, 5))
# 힌트: plt.plot() 두 번 — 실제주가, 예측주가
# 힌트: plt.legend() 로 범례 표시
def 그래프그리기(실제주가, 예측주가):
    plt.figure(figsize=(12,5))
    plt.plot(실제주가, label='실제 주가')
    plt.plot(예측주가, label='예측 주가')
    plt.title('삼성전자 주가 예측 (LSTM)')
    plt.legend()
    plt.show()

# 힌트: 위에서 만든 함수들을 순서대로 연결
종가                             = 데이터불러오기('samsung.csv')
스케일처리, 스칼라                 = 정규화(종가)
X, y                             = 시퀀스만들기(스케일처리, window=60)
X_train, X_test, y_train, y_test = 학습_테스트_모델분리(X, y)
model                            = 모델만들기()
model                            = 학습하기(model, X_train, y_train)
예측주가, 실제주가                  = 예측하기(model, X_test, y_test, 스칼라)
# 그래프그리기(실제주가, 예측주가)

def 내일주가예측(종가,스칼라,model,window=60):
    최근60일 = 종가.values[-window:]
    최근60일_스케일처리 = 스칼라.transform(최근60일)
    입력 = 최근60일_스케일처리.reshape(1,window,1)
    예측 = model.predict(입력)
    내일주가 = 스칼라.inverse_transform(예측)

    print(f'내일 예측 주가 : {내일주가[0][0]:.1f}원')
    return 내일주가

내일주가예측(종가,스칼라,model)
# 에측 주가를 현재 삼전과 근사하게 조절하기
