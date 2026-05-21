'''
데이터 분석 대회 사이트
kaggle(=전세계),데이콘(=한국)
https://www.kaggle.com/
https://dacon.io/
loan  - 대출 승인 관련 csv 난이도 하(615 rows)
churn - 고객 이탈 관련 csv 난이도 중(7044 rows)
spam  - 스팸 탐지 관련 csv 난이도 중(5572 rows)
fraud - 사기 탐지 관련 csv 난이도 상(101 rows) 컬럼이 많을수록 전처리가(데이터 전부 처리) 힘듬
rows 수는 그렇게까지 막 힘들지 않음.. 단 컬럼이 많으면 힘듬(전처리 때문에)
'''
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


# csv 나 외부 데이터를 분석하는 순간부터 데이터 훈련용 / 시험용으로 나누기 전에
# 반드시 데이터를 확인하고 전처리(전체 데이터 문제없도록 다듬기 처리) 작업을 해주어야한다.

def loan_dataset():
    # 1. 데이터 불러오기
    df = pd.read_csv('csvs/loan.csv')

    # 2. 데이터 크기 확인
    print('shape(행,열) : ',df.shape)

    # 3. 첫 5줄 확인
    print(df.head())

    # 4. 컬럼 목록 + 데이터 타입
    print(df.dtypes)

    # 5. 빈값 확인
    print(df.isnull().sum())

    # 6. 숫자 컬럼 통계(평균, 최소, 최대 등)
    print(df.describe())

    # 7. 정답 비율 확인
    print(df['Loan_Status'].value_counts())


def 데이터분석(  data  ,  name  ):   # 매개변수 2개 넣기
    print("=" * 40)
    print("shape(행, 열) : ", data.shape)
    print(data.head())
    print(data.dtypes)
    print(data.isnull().sum())
    print(data.describe())
    print(f"정답({name}) 비율:")
    print(data[name].value_counts())
    print("=" * 40)

# 전처리 자체는 중요하지 않다.
# 어떤 모델을 사용하는지 중요하지 않다.
# 전처리와 모델 데이터는 모두다 회사에서 사업을 하는 방향 / 개발자가 개발을 하는 방향에 따라 결정되는 것
# 모든 전처리는 데이터가 어떻게 생겼는지에 따라 전처리를 해야하는 방향 결정된다.
# 사업 방향 / 어떤 데이터를 수집할 것인가 / 수집한 데이터를 어떻게 활용할 것인가
# 결정되지 않으면 전처리와 모델도 결정할 수 없다.

# 전처리
# 데이터 수집에 대한 결과가 나오지 않으면 방향을 잡을 수 없다.
# 위도 경도 없다. -> 데이터를 다시 수집하거나, 알 수 없는 위치라고 텍스트 띄우기

# 분류 / 회귀 -> 특정 주제 테마에서 가장 많이 사용되는 모델은 무엇인가
# 다른 개발자들이 해본 추천 모델을 이용하며 우리 회사에 맞는 모델을 찾을 수 있다.

def loan_dataset():
    # 1. 데이터 호출 후 데이터 분석하기
    df = pd.read_csv("csvs/loan.csv")
    데이터분석(df, 'Loan_Status')   # 함수 호출

    # 2. 전처리 작업 시작
    # 2-1. 필요없는 컬럼 제거
    df = df.drop('Loan_ID', axis=1) # axis = 0 axis =1
    # 2-2. 빈값 제거
    df = df.dropna() # nan 빈값 drop
    # 2-3. 문자 -> 숫자
    le = LabelEncoder() # 문자를 숫자로 바꿔주는 도구
    '''
    예
    data = ['banana', 'apple', 'grape', 'kiwi','apple','grape', 'kiwi', ...]
    데이터가 있을 때
    
    LabelEncoder() = 를 사용하면 오름차순 정렬하여 중복 제거하고 알파벳 순번 정렬
    
    1.
    data = ['apple', 'banana', 'grape', 'kiwi']
    2.         0        1         2        3
    3.  각 글자를 숫자로 변환처리
    data = ['banana', 'apple', 'grape', 'kiwi','apple','grape', 'kiwi', ...]
    data = [   1   ,     0  ,     2   ,   3 ,    0   ,    2  ,    3 ,    ...]
    
    로지스틱회귀라서 그렇다!!
    문자를 숫자로 바꾸는가
    컴퓨터는 문자끼리 더하면 문자 이어붙이기 진행하지 더하기 빼기를 못한다.
    로지스틱회귀 모델이 하는일 : 입력값들을 저너부 더하고 곱해서 확률을 계산하는 것
    (나이 * 0.3) + (소득 * 0.5) + (성별 * 0.2) = 대출 승인 확률을 계산하는 것
    
    로지스틱 회귀는 계산 결과 = 각 컬럼에 존재하는 문자들에 임의적으로 오름차순 기준으로 0번부터 숫자 부여
    --> 0이면 무조건 1이다. 에러!!
    ---> 원-핫 인코딩 (내일 배울 것) 순서가 의미 없는 데이터 계산을 위하여 존재하는 방법
    
    '''
    for col in df.select_dtypes(include='str').columns:
        df[col] = le.fit_transform(df[col])
        '''
        fit - 평균 표준편차 기준으로 계산
        transform - 그 기준으로 변환
        
        fit_transform
        - 모든 데이터가 아니라 훈련 데이터만 가지고 변환작업을 해서 무언갈 할거다.  
        transform
        - 모든 데이터가 아니라 훈련이 제대로 되었는지 확인용 데이터만 변환작업을 해서 무언가 할거다. 
        '''
    # 1번 경고 pandas가 버전이 올라가면서 object

    # 3. X(입력), y(정답) 나누기
    X = df.drop("Loan_Status", axis=1)
    y = df["Loan_Status"]

    # 4. 훈련용 시험용 tts 분류
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
    '''
     2번 경고 훈련을 하기에 1000번은 부족하다.! 좀 더 많이 훈련 시켜라
    Increase the number of iterations to improve the convergence (max_iter=1000).
    You might also want to scale the data as shown in: 
    '''

    # 5. 모델 선택하고 선택한 모델로 학습하기
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train,y_train)

    # 6. 결과 확인
    print(f'정확도 : {model.score(X_test,y_test)}')

loan_dataset()

# churn
# 전처리 해야하는 이유
# customerID 제거
# 고유 번호는 의미가 없다 id의 모든 값이 달라서 패턴을 찾을 수 없다.
# 고유 번호가 0~순차적으로 부여가 되었거나, 지역이름=번호 이런식으로 했다면
# 아 년월며칠 몇시에 가입한 고객들이 탈퇴를 하고 있구나
# 아~ 어떤 지역 사람들이 탈퇴를 하고 있구나 -> 그 지역사람들은 왜 탈퇴를 하는가? 분석
# TotalCharges -> 숫자처럼 생겼지만 문자열로 저장되어 있는 숫자
# 공백이 섞여 있어 그냥 두면 계산 불가
# 숫자 ok " " 변환 불가한 계산의 경우 Nan으로 변경해서 빈값이다 컬럼에 표기
# 빈값이다 라고 표기된 컬럼을 dropna() 제거
# 빈값의 경우 계산이 되지 않기 때문 1+2+26.5+" " => 계산 에러 발생

def churn_dataset():
    df = pd.read_csv("csvs/churn.csv")
    데이터분석(df, "Churn")  # ← target 컬럼 이름 확인

    # TODO 1. 필요없는 ID 컬럼 제거
    # 힌트 : loan 에서는 "Loan_ID"  제거
    #        churn 에서 ID 역할을 하는 컬럼 이름은 무엇인가? (dtypes 출력 참고)
    df = df.drop("customerID", axis=1)

    # TODO 2. TotalCharges 컬럼 문자 → 숫자 변환
    # 힌트 : 이 컬럼은 숫자처럼 생겼지만 사실 문자(object) 타입
    #        pd.to_numeric(df["___"], errors="coerce") 를 사용
    #        errors="coerce" = 변환 못하면 NaN(빈값) 으로 바꾸기
    df["TotalCharges"] = pd.to_numeric(df["str"], errors="coerce")

    # TODO 3. 빈값 제거
    # 힌트 : loan 에서 썼던 방법과 동일
    df = df.dropna()

    # TODO 4. 문자 → 숫자
    le = LabelEncoder()
    for col in df.select_dtypes(include="str").columns:
        df[col] = le.fit_transform(df[col])

    # TODO 5. X, y 나누기
    # 힌트 : target 컬럼 이름
    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    # TODO 6. 훈련/시험 나누기 + 학습 + 결과 출력
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=10000)
    model.fit(X_train, y_train)
    print(f"정확도 : {model.score(X_test, y_test)}")
    #print(classification_report(y_test, model.predict(X_test)))


# spam
# spam v3 v4 v5 모두 빈값으로 필요없는 컬럼을 들고 다닐 이유가 없다.
# TfidfVectorizer  문자메세지는 단순히 LabelEncoder 로 가볍게 변경할 데이터가 아니다.
# LabelEncoder    = 카테고리
# TfidfVectorizer = 문장/문단 (긴 텍스트)
def spam_dataset():
    df = pd.read_csv("csvs/spam.csv", encoding="latin-1")

    # TODO 1. 필요한 컬럼만 선택하고 이름 바꾸기
    # 힌트 : spam.csv 는 컬럼이 v1, v2, v3... 으로 되어 있다
    #        v1 = label(spam/ham), v2 = 문자 내용
    #        필요한 건 v1, v2 두 개뿐
    df = df[["v1", "v2"]]
    df.columns = ["label", "message"]

    데이터분석(df, "label")

    # TODO 2. TF-IDF 로 문자 → 숫자 변환
    # 힌트 : 문자 데이터는 LabelEncoder 대신 TfidfVectorizer 사용
    #        단어를 숫자로 바꿔주는 도구
    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidf = TfidfVectorizer(max_features=1000)
    X = tfidf.fit_transform(df["str"])

    # TODO 3. y 만들기
    # 힌트 : spam 이면 1, ham 이면 0 으로 바뀜
    y = (df["label"] == "___").astype(int)

    # TODO 4. 훈련/시험 나누기 + 학습 + 결과 출력
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=10000)
    model.fit(X_train, y_train)
    print(f"정확도 : {model.score(y_test, X_test)}")
    #print(classification_report(___, model.predict(___)))

# fraud
# 컬럼마다 숫자 크기가 중구난방
# Amount    :  0 ~ 25,000 엄청 큼
# v1 ~ v28 :  -3 ~ -3     엄청 작음
# 위와 같을 경우 큰 숫자가 결과를 독차지하고 작은 컬럼은 무시됨
# 그래서 -3 ~ -3 범위로 숫자 범위 맞춰줌
# 키(cm) vs 몸무게(kg) 단위가 달라 비교 못함
# 표준화하여 공평하게 비교
def fraud_dataset():
    df = pd.read_csv("csvs/fraud.csv")
    데이터분석(df, "Class")

    # TODO 1. X, y 나누기
    # 힌트 : target 컬럼 이름 "Class"
    X = df.drop("Class", axis=1)
    y = df["Class"]

    # TODO 2. StandardScaler 로 스케일링
    # 힌트 : fraud 는 숫자 컬럼만 있어서 LabelEncoder 필요 없다
    #        대신 숫자 크기가 너무 달라서 StandardScaler 로 맞춰줘야 한다
    #        (예: Amount 는 크고 V1~V28 은 작다)
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X = scaler.fit_transform(_)

    # TODO 3. 훈련/시험 나누기 + 학습 + 결과 출력
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=10000)
    model.fit(X_train, y_train)
    print(f"정확도 : {model.score(X_test, y_test)}")
    #print(classification_report(___, model.predict(___)))


