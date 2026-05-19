import pickle
from sklearn.datasets import load_iris, load_wine, load_breast_cancer, load_digits
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

train_test = 0.2
train_test_random_state = 42

def 붓꽃모델저장():
    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    with open(f"iris_model{acc * 100:.1f}.pkl", "wb") as f:
        pickle.dump(model, f)

    print("모델 저장완료")

def 와인등급모델저장():
    wine = load_wine()
    X = wine.data
    y = wine.target

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    with open(f'wine_model{acc * 100:.1f}.pkl','wb') as f:
        pickle.dump(model,f)
    print('와인등급모델 저장 완료')

def 손글씨숫자모델저장():
    digits = load_digits()
    X = digits.data
    y = digits.target

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    with open(f'digits_model{acc*100:.1f}pkl','wb') as f:
        pickle.dump(model, f)
    print('손글씨숫자모델 저장완료')

def 유방암모델저장():
    breast = load_breast_cancer()
    X = breast.data
    y = breast.target

    X_train, X_test,y_train, y_test = train_test_split(X,y,test_size=train_test,random_state=train_test_random_state)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    with open(f'breast_model{acc*100:.1f}pkl','wb') as f:
        pickle.dump(model, f)
    print('유방암모델 저장완료')
    print(f'정확도 :{acc*100:.1f}')

와인등급모델저장()
손글씨숫자모델저장()
유방암모델저장()