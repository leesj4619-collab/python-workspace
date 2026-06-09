# TODO___ 아래 라이브러리를 import 하세요
# 힌트: pandas, numpy, matplotlib.pyplot
# 힌트: sklearn.preprocessing 에서 MinMaxScaler
# 힌트: tensorflow.keras.models 에서 Sequential
# 힌트: tensorflow.keras.layers 에서 Input, LSTM, Dense

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense, LSTM

# 1.

plt.rcParams['font.family'] = 'D2coding'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('SK하이닉스.csv', index_col=0, skiprows=[1,2])
df.index = pd.to_datetime(df.index)
df.columns = ['Close','High','Low','Open','Volume']
close = df[['Close','Volume']]
print(close.tail())

scaler = MinMaxScaler()
scaled = scaler.fit_transform(close)

X, y = [], []
for i in range(60, len(scaled)):
    X.append(scaled[i - 60:i]) # 0 번부터 60일치의 데이터만 가져오겠다.
    y.append(scaled[i])
X, y = np.array(X), np.array(y)
print(X.shape)  # (날짜수, 60, 1)

split = int(len(X) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

model = Sequential([
    Input(shape=(60,2)),
    LSTM(64, return_sequences=True),
    LSTM(32),
    Dense(1)
])
# binary = 둘 중 하나 선택
# sparse_category_crossentropy
model.compile(optimizer='adam', loss='mse')
model.summary()

model.fit(X_train, y_train,
          epochs=20,
          batch_size=32,
          validation_split=0.1)

pred = model.predict(X_test)
pred_price = scaler.inverse_transform(pred)
real_price = scaler.inverse_transform(y_test)

plt.figure(figsize=(12,5))
plt.plot(pred_price, label='실제 주가')
plt.plot(real_price, label='예측 주가')
plt.title('SK하이닉스 주가 예측 (LSTM)')
plt.legend()
plt.show()