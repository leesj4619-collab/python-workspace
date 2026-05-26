from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# TODO 1. 데이터 불러오기
data = load_diabetes()
'''
당뇨병 환자 데이터를 이용해서 1년 후 당뇨 진행 정도 예측
샘플 수 : 442명
피 처 : 나이, 성별, 체질량지수, 혈압 등 10개 존재
타겟(y) : 1년 후 당뇨 진행 수치(숫자가 클수록 악화)
'''
X, y = data.data, data.target

# TODO 2. 데이터 크기 확인
print("X shape:", X.shape)
print("y shape:", y.shape)

# TODO 3. 학습/테스트 데이터 분리 (테스트 20%, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# TODO 4. Ridge 모델 생성 (alpha=1.0)
model = Ridge(alpha=1.0)

# TODO 5. 모델 학습
model.fit(X_train,y_train)

# TODO 6. 테스트 데이터로 예측
y_pred = model.predict(X_test)

# TODO 7. 성능 평가 출력
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
print(f"R²: {r2_score(y_test, y_pred):.4f}")

# TODO 8. 계수 확인 (어떤 피처가 영향을 많이 주는지)
print("피처별 계수:", model.coef_)
print("피처 이름:", data.feature_names)
'''
feature_names = 피처 이름
model.coef_ = 피처별 계수
              각 변수가 당뇨 진행에 얼마나 영향을 주는지 숫자로 나타낸 것
s1,s2 ... = 혈액 검사 수치들 총 콜레스테롤 나쁜콜레스테롤 좋은콜레스테롤 ... 혈당수치 관련된 것들
피처 이름  : [      'age',        'sex', '      bmi',          'bp', '        s1',             
피처별 계수: [  45.36737726  -76.66608563  291.33883165  198.99581745   -0.53030959
         's2',      's3',         's4',         's5',          's6']
  -28.57704987 -144.51190505  119.26006559  230.22160832  112.14983004]
절대값 = 음수 -> 양수
계수 절대값이 클수록 그 피처가 예측에 많은 영향을 준다
음수면 그 피처가 올라갈수록 당뇨 수치가 내려간다.
'''