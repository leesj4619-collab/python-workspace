import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import LSTM
import pandas as pd

삼성전자 = yf.download('005930.KS', interval='5m', period='60d')
삼성전자.to_csv('samsung.csv')


'''
====================================
STEP 1 : 모델 학습 & 저장

이 파일에서 하는 일 :
1. 삼성전자 5분봉 데이터를 야후 파이낸스 기능 다운로드
2. 데이터를 MinMax 스케일러를 이용해서 0~1 사이로 정규화
3. LSTM 신경망 모델 학습
4. 학습된 모델과 스케일러를 모델파일 keras로 저장

과거 몇 개 봉을 들고 다음을 예측할 것인지
전체 데이터를 몇 번 반복할 것인지
한 번에 몇 개 씩 묶어서 학습할 지
몇 분 봉을 기준으로 할 것인지는 스스로 선택
'''
