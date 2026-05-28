from sklearn.svm import SVC, SVR
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris, load_digits, load_wine, load_breast_cancer, load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV

def SVC_붓꽃():
    # TODO 1-1: load_iris 데이터 불러오기
    X, y = load_iris(return_X_y=True)

    # TODO 1-2: train_test_split (test_size=0.2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=42,test_size=0.2)

    # TODO 1-3: 스케일링
    스케일러 = StandardScaler()
    X_train = 스케일러.fit_transform(X_train)
    X_test  = 스케일러.transform(X_test)

    # TODO 1-4: 그리드파람 채우기
    그리드파람 = {
        'C'     : [0.1, 1, 10, 100],   # 0.1, 1, 10, 100
        'gamma' : [0.001, 0.01, 0.1, 1],   # 0.001, 0.01, 0.1, 1
        'kernel': ['rbf', 'linear'],   # rbf, linear
    }

    # TODO 1-5: GridSearchCV 완성
    모델 = GridSearchCV(SVC(), 그리드파람, cv=5, scoring='accuracy', n_jobs=-1, verbose=1)

    # TODO 1-6: 학습
    모델.fit(X_train,y_train)
    pred = 모델.predict(X_test)

    # TODO 1-7: 결과 출력
    print("최적 파라미터 :", 모델.best_params_)
    print("최적 CV 정확도:", 모델.best_score_)
    print("테스트 정확도 :", 모델.score(X_test,y_test))

#SVC_붓꽃()

def SVC_유방암():
    # TODO 2-1: load_breast_cancer 데이터 불러오기
    X, y = load_breast_cancer(return_X_y=True)

    # TODO 2-2: train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=42,test_size=0.2)

    # TODO 2-3: 스케일링
    스케일링 = StandardScaler()
    X_train = 스케일링.fit_transform(X_train)
    X_test = 스케일링.transform(X_test)

    # TODO 2-4: 그리드파람 채우기
    그리드파람 = {
        'C'     : [0.1, 1, 10, 100],   # 0.1, 1, 10, 100
        'gamma' : [0.001, 0.01, 0.1, 1],   # 0.001, 0.01, 0.1, 1
        'kernel': ['rbf', 'linear'],   # rbf, linear
    }

    # TODO 2-5: GridSearchCV 완성 + 학습
    모델 = GridSearchCV(SVC(), 그리드파람, cv=5, scoring='accuracy', n_jobs=1, verbose=1)
    모델.fit(X_train,y_train)

    # TODO 2-6: 결과 출력
    print("최적 파라미터 :", 모델.best_params_)
    print("최적 CV 정확도:", 모델.best_score_)
    print("테스트 정확도 :", 모델.score(X_test,y_test))

#SVC_유방암()
def 랜덤포레스트_와인():
    # TODO 3-1: load_wine 데이터 불러오기
    X,y = load_wine(return_X_y=True)

    # TODO 3-2: train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=42,test_size=0.2)

    # TODO 3-3: 스케일링
    스케일링 = StandardScaler()
    X_train = 스케일링.fit_transform(X_train)
    X_test = 스케일링.transform(X_test)

    # TODO 3-4: 그리드파람 채우기
    그리드파람 = {
        'n_estimators': [10, 100, 200],   # 10, 100, 200  나무 개수
        'max_depth'   : [None, 3, 5, 10],   # None, 3, 5, 10 나무 깊이
    }

    # TODO 3-5: GridSearchCV 완성 + 학습 + 결과출력
    모델 = GridSearchCV(SVC(), 그리드파람, cv=5, scoring='accuracy', n_jobs=1, verbose=1)
    모델.fit(X_train,y_train)

    print("최적 파라미터 :", 모델.best_params_)
    print("최적 CV 정확도:", 모델.best_score_)
    print("테스트 정확도 :", 모델.score(X_test,y_test))

랜덤포레스트_와인()

def KNN_손글씨():
    # TODO 4-1: load_digits 데이터 불러오기
    X,y = load_digits(return_X_y=True)

    # TODO 4-2: train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=42,test_size=0.2)

    # TODO 4-3: 스케일링
    스케일링 = StandardScaler()
    X_train = 스케일링.fit_transform(X_train)
    X_test = 스케일링.transform(X_test)

    # TODO 4-4: 그리드파람 채우기
    그리드파람 = {
        'n_neighbors': [3, 5, 7, 9],   # 3, 5, 7, 9  이웃 몇개 볼지
        'weights'    : ['uniform', 'distance'],   # uniform, distance
    }

    # TODO 4-5: GridSearchCV 완성 + 학습 + 결과출력
    모델 = GridSearchCV(SVC(), 그리드파람, cv=5, scoring='accuracy', n_jobs=1, verbose=1)
    모델.fit(X_train,y_train)
    print("최적 파라미터 :", 모델.best_params_)
    print("최적 CV 정확도:", 모델.best_score_)
    print("테스트 정확도 :", 모델.score(X_test,y_test))

KNN_손글씨()

def SVR_당뇨병():
    # TODO 5-1: load_diabetes 데이터 불러오기
    X,y = load_diabetes(return_X_y=True)

    # TODO 5-2: train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=42,test_size=0.2)

    # TODO 5-3: X, y 둘다 스케일링 (SVR은 y도 스케일링!)
    스케일러_X = StandardScaler()
    스케일러_y = StandardScaler()
    X_train = 스케일러_X.fit_transform(X_train)
    X_test  = 스케일러_X.transform(X_test)
    y_train_s = 스케일러_y.fit_transform(y_test.reshape(-1, 1)).ravel()

    # TODO 5-4: 그리드파람 채우기
    그리드파람 = {
        'C'      : [0.1, 1, 10, 100],   # 0.1, 1, 10, 100
        'epsilon': [0.01, 0.1, 0.5, 1],   # 0.01, 0.1, 0.5, 1
        'kernel' : ['rbf', 'linear'],   # rbf, linear
    }

    # TODO 5-5: GridSearchCV 완성 + 학습
    모델 = GridSearchCV(SVC(), 그리드파람, cv=5, scoring='neg_mean_squared_error', n_jobs=-1, verbose=1)
    모델.fit(X_train,y_train)

    # TODO 5-6: 예측값 원래 단위로 복원 후 출력
    pred_s = 모델.best_estimator_.predict(X_test)
    pred   = 스케일러_y.inverse_transform(pred_s.reshape(-1, 1)).ravel()
    print("최적 파라미터 :", 모델.best_params_)
    print("MSE :", mean_squared_error(y_train_s, pred))

SVR_당뇨병()













