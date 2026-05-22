import pickle
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ================================
# 1. CSV 불러오기
# ================================
df = pd.read_csv('csvs/google_reviews.csv')          # TODO 1: 지난 과제에서 저장한 CSV 경로

print(df.head())
print(df.shape)
print(df['rating'].value_counts())

# ================================
# 2. 전처리 - 라벨 만들기
# ================================
df = df[df['rating'] != 3]   # TODO 2: 중립인 3점 제거

df = df.dropna(subset=['review'])   # TODO 3: 리뷰 내용이 비어있는 행 제거
#  힌트: 비어있는 컬럼 이름은 'review'

df['label'] = df['rating'].apply(
    lambda x: 'positive' if x >= 4 else 'negative'    # TODO 4: 4점 이상 'positive' / 나머지 'negative'
)

print(df['label'].value_counts())       # positive 몇 개, negative 몇 개 확인

# ================================
# 3. 데이터 분리
# ================================
X = df['review']     # TODO 5: 입력값 - 리뷰 텍스트 컬럼
y = df['label']        # TODO 6: 정답값 - 라벨 컬럼

test_size    = 0.4
random_state = 42

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=random_state    # TODO 7: 위에서 정의한 변수 넣기
)

# ================================
# 4. 텍스트 → 숫자 변환
# ================================
# 리뷰   → 텍스트 데이터       → CountVectorizer 로 먼저 숫자로 바꿔야 함

'''
CountVectorizer 옵션이 존재 옵션을 검색해서 찾은 후 적용
'''
#vectorizer = CountVectorizer()
vectorizer = CountVectorizer()
print(dir(vectorizer))


X_train_vec = vectorizer.fit_transform(X_train)   # TODO 8: 훈련용은 fit_transform / 테스트용은 transform
X_test_vec  = vectorizer.transform(X_test)        # TODO 9: 훈련용은 fit_transform / 테스트용은 transform

# ================================
# 5. 모델 학습
# ================================
model = MultinomialNB()
model.fit(X_train_vec, y_train)         # TODO 10: 학습 메서드

acc = accuracy_score(y_test, model.predict(X_test_vec))
print(f"정확도: {acc * 100:.1f}%")

# ================================
# 6. 모델 저장
# ================================
# digit  → model 만 pkl 저장
# 리뷰   → model + vectorizer 를 딕셔너리로 묶어서 저장
#           → 왜? 나중에 app.py 에서 새 리뷰가 들어오면
#             똑같은 vectorizer 로 글자→숫자 변환을 해야 하기 때문

파일명 = f'models/review_model_{test_size}_{random_state}_{acc * 100:.1f}.pkl'

with open(파일명, 'wb') as f:            # TODO 11: 쓰기모드 'wb'
    pickle.dump({'model': model, 'vectorizer': vectorizer},f)                 # TODO 12: 저장할 것 - {'model': model, 'vectorizer': vectorizer}

print(f"저장완료: {파일명}")