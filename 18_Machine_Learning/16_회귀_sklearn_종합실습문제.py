import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def 광고매출예측_모델():
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False

    df = pd.read_csv('csvs/ad_sales.csv')
    X = df[['광고비용(만원)']]
    y = df['매출액(만원)']

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
    print(f"R²: {r2_score(y_test, y_pred):.4f}")
    print(f"계수(기울기): {model.coef_[0]:.4f}")
    print(f"절편: {model.intercept_:.4f}")

    plt.figure(figsize=(8, 5))
    plt.scatter(X, y, color='steelblue', label='실제 데이터')
    plt.plot(X, model.predict(X), color='red', label='예측 직선')
    plt.xlabel('광고비용(만원)')
    plt.ylabel('매출액(만원)')
    plt.title('광고 비용에 따른 매출액 예측')
    plt.legend()
    plt.tight_layout()
    plt.show()

    with open('ad_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("ad_model.pkl 저장 완료!")

    with open('ad_model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)

    result = loaded_model.predict([[300]])
    print(f"광고비용 300만원 시 예상 매출액: {result[0]:.0f} 만원")
def 운동모델():
    # TODO 1. 한글 폰트 설정
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False

    # TODO 2. 데이터 불러오기 + X, y 분리
    df = pd.read_csv('csvs/exercise_calories.csv')
    X = df[['운동시간(분)']]
    y = df['칼로리소모']

    # TODO 3. 학습/테스트 분리 (테스트 20%, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    # TODO 4. 모델 생성 및 학습
    model = LinearRegression()
    model.fit(X_train, y_train)

    # TODO 5. 예측 및 평가 출력
    y_pred = model.predict(X_test)
    print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
    print(f"R²: {r2_score(y_test, y_pred):.4f}")
    print(f"계수: {model.coef_[0]:.4f}")
    print(f"절편: {model.intercept_:.4f}")

    # TODO 6. 시각화 (산점도 + 예측 직선)
    plt.figure(figsize=(8, 5))
    plt.scatter(X, y, color='steelblue', label='실제 데이터')
    plt.plot(X, model.predict(X), color='red', label='예측 직선')
    plt.xlabel('운동시간(분)')
    plt.ylabel('칼로리소모')
    plt.title('운동 분당 칼로리가 얼마나 소모 될까?')
    plt.legend()
    plt.tight_layout()
    plt.show()

    # TODO 7. pkl 저장
    with open('exercise_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    # TODO 8. pkl 불러오기
    with open('exercise_model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)

    # TODO 9. 내가 90분 운동하면 칼로리가 얼마나 소모될까?
    result = loaded_model.predict([[90]])
    print(f"90분 운동 시 예상 칼로리 소모: {result[0]:.0f} kcal")
운동모델()