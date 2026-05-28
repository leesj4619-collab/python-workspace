from sklearn.svm import SVC
from sklearn.datasets import load_iris, load_breast_cancer, load_digits, load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler # SVM은 스케일링 필수다.

def 붓꽃실습():
    X,y = load_iris(return_X_y=True)
    # cvs 파일을 가져오지 않고 제공하는 데이터 셋을 사용할 땐 위와같이 작성
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    clf = SVC(kernel='rbf', C=1.0, gamma='scale')
    clf.fit(X_train,y_train)

    print('SVC 정확도 :',clf.score(X_test, y_test))
    print('예측값 :',clf.predict(X_test[:5]))
    print('실제값 :',y_test[:5])
    '''
    SVC 정확도 :  1.0
    # 문제가 있는 것 붓꽃의 경우 너무 완벽하게 정제된 데이터라
    # 1.0이 정상
    # 붓꽃과 같이 정제된 데이터가 아니면 비정상
    예측값 : [1 0 2 1 1] <- 모델이 예측한 꽃 종류
    실제값 : [1 0 2 1 1] <- 실제로 정답인 꽃 종류
    모델이 예측한 답이랑 실제 정답을 나란히 놓고 비교한 상황
    숫자는 꽃 종류 번호
    '''


def 유방암실습():
    X,y = load_breast_cancer(return_X_y=True)
    print(X.shape) # (569, 30) 데이터 569개 컬럼개수 30개
    print(set(y))  # {np.int64(0), np.int64(1)} 0 = 악성, 1 = 양성

    X_train,X_test,y_train,y_test = train_test_split(
        X,
        y,
        random_state=42,
        test_size=0.2
    )
    스케일준비 = StandardScaler()
    X_train = 스케일준비.fit_transform(X_train)
    # X_train 데이터만 스케일준비에서 스탠다드 스케일 도구를 꺼내어 정제시키겠다.
    X_test = 스케일준비.transform(X_test)

    clf = SVC(kernel='rbf', C=1.0, gamma='scale') # 알아서 번호 자동 세팅
    clf.fit(X_train, y_train)
    print(f'정확도 : {clf.score(X_test, y_test):.4f}') # 정확도 : 0.9825
def 손글씨맞추기실습():
    X,y = load_digits(return_X_y=True)
    print(X.shape)# (1797, 64) 1797 데이터 64개의 컬럼 손글씨를 64개
    print(set(y)) # {np.int64(0), np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7), np.int64(8), np.int64(9)}

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,train_size=42)
    스케일러 = StandardScaler()
    X_train = 스케일러.fit_transform(X_train)
    X_test = 스케일러.transform(X_test)

    clf = SVC(kernel='rbf', C=1.0, gamma='scale')
    clf.fit(X_train,y_train)

    print(f'정확도 : {clf.score(X_test,y_test)}')  # 정확도 : 0.6861111111111111
    print(f'예측값 : {clf.predict(X_test[:5])}')   # 예측값 : [4 5 0 3 5]
    print(f'실제값 : {y_test[:5]}')                # 실제값 : [1 9 0 3 1]

def 와인실습():
    X,y = load_wine(return_X_y=True)
    print(X.shape)# (178, 13)
    print(set(y)) # {np.int64(0), np.int64(1), np.int64(2)}

    X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=42,test_size=0.2)

    스케일러 = StandardScaler()
    X_train = 스케일러.fit_transform(X_train)
    X_test = 스케일러.transform(X_test)

    clf = SVC(kernel='rbf', C=1.0, gamma='scale')
    clf.fit(X_train,y_train)
    print(f'정확도 : {clf.score(X_test,y_test)}')  # 정확도 : 1.0
    print(f'예측값 : {clf.predict(X_test[:5])}')   # 예측값 : [0 0 2 0 1]
    print(f'실제값 : {y_test[:5]}')                # 실제값 : [0 0 2 0 1]

와인실습()



