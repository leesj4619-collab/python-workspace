'''
데이터는 존재하고 데이터에 어떤 모델을 사용하여 학습시키는가
붓꽃은 대부분의 모델에서 활용 가능한 데이터셋
'''
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.datasets import load_iris, load_wine, fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error
import numpy as np

def 붓꽃데이터실습():
    X,y = load_iris(return_X_y=True)
    feature_names = load_iris().feature_names
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    rf = RandomForestClassifier(n_estimators=100,max_features='sqrt',random_state=42)
    rf.fit(X_train,y_train)
    pred = rf.predict(X_test)

    print(f"정확도 : {accuracy_score(y_test,pred)}")
    print(classification_report(y_test,pred,target_names=['세토사','버시컬러','버지니카']))

    print('='*30)
    # 피처 = 컬럼 중요도 순으로 정렬해서 어떤 피처를 중요하게 생각하는지 조회
    중요도 = pd.DataFrame({
        '특성': feature_names,
        '중요도':rf.feature_importances_
    }).sort_values('중요도',ascending=False)
    print(중요도)

def 와인데이터실습():
    # TODO 1: load_wine() 으로 X, y 와 feature_names 불러오기
    X, y = load_wine(return_X_y=True)
    feature_names = load_wine().feature_names

    # TODO 2: train_test_split 으로 훈련/테스트 나누기
    #          test_size=0.2, random_state=42
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    # TODO 3: RandomForestClassifier 모델 만들기
    #          n_estimators=100, max_features='sqrt', random_state=42
    rf = RandomForestClassifier(n_estimators=100,max_features='sqrt',random_state=42)

    # TODO 4: 모델 학습 후 예측하기
    rf.fit(X_train,y_train)
    pred = rf.predict(X_test)

    print(f"와인 정확도 : {accuracy_score(y_test, pred):.4f}")
    print(classification_report(y_test, pred, target_names=['와인1', '와인2', '와인3']))
    print("=" * 30)

    # TODO 5: 붓꽃과 똑같은 방식으로 피처 중요도 출력하기
    중요도 = pd.DataFrame({
        '특성' : feature_names,
        '중요도': rf.feature_importances_
    }).sort_values('중요도',ascending=False)
    print(중요도)


def 집값데이터실습():
    # TODO 1: fetch_california_housing() 으로 X, y 와 feature_names 불러오기
    X, y = fetch_california_housing(return_X_y=True)
    feature_names = fetch_california_housing().feature_names

    # TODO 2: train_test_split 으로 훈련/테스트 나누기
    #          test_size=0.2, random_state=42
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    # TODO 3: RandomForestRegressor 모델 만들기
    #          ★ 집값은 숫자 예측 → Regressor
    #          ★ 회귀는 max_features=None
    #          n_estimators=100, random_state=42
    rf = RandomForestRegressor(n_estimators=100,random_state=42,max_features=None)

    # TODO 4: 모델 학습 후 예측하기
    rf.fit(X_train,y_train)
    pred = rf.predict(X_test)

    # RMSE = 예측값과 실제값의 평균 오차 (낮을수록 좋음)
    rmse = np.sqrt(mean_squared_error(y_test, pred))
    print(f"집값 RMSE (오차) : {rmse:.4f}")
    print("=" * 30)

    # TODO 5: 붓꽃과 똑같은 방식으로 피처 중요도 출력하기
    중요도 = pd.DataFrame({
        '특성': feature_names,
        '중요도':rf.feature_importances_
    }).sort_values('중요도',ascending=False)
    print(중요도)


# ===== 실행 =====
붓꽃데이터실습()
print("=" * 50)
와인데이터실습()
print("=" * 50)
집값데이터실습()

# 붓꽃데이터, 와인데이터, 집값데이터
'''
정확도 : 1.0
              precision    recall  f1-score   support

         세토사       1.00      1.00      1.00        10
        버시컬러       1.00      1.00      1.00         9
        버지니카       1.00      1.00      1.00        11

    accuracy                           1.00        30
   macro avg       1.00      1.00      1.00        30
weighted avg       1.00      1.00      1.00        30

==============================
                  특성       중요도
2  petal length (cm)  0.439994
3   petal width (cm)  0.421522
0  sepal length (cm)  0.108098
1   sepal width (cm)  0.030387
와인 정확도 : 1.0000
              precision    recall  f1-score   support

         와인1       1.00      1.00      1.00        14
         와인2       1.00      1.00      1.00        14
         와인3       1.00      1.00      1.00         8

    accuracy                           1.00        36
   macro avg       1.00      1.00      1.00        36
weighted avg       1.00      1.00      1.00        36

==============================
                              특성       중요도
6                     flavanoids  0.202293
9                color_intensity  0.171202
12                       proline  0.139046
0                        alcohol  0.112398
11  od280/od315_of_diluted_wines  0.111564
10                           hue  0.070891
4                      magnesium  0.036841
1                     malic_acid  0.035703
3              alcalinity_of_ash  0.032425
5                  total_phenols  0.029279
8                proanthocyanins  0.023561
2                            ash  0.021282
7           nonflavanoid_phenols  0.013515
'''
