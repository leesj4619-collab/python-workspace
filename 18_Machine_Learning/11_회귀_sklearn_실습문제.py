from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# TODO 1. 데이터 불러오기
data = load_diabetes
X, y = data.data, data.target

# TODO 2. 데이터 크기 확인
print("X shape:", X.shape)
print("y shape:", y.shape)

# TODO 3. 학습/테스트 데이터 분리 (테스트 20%, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# TODO 4. Ridge 모델 생성 (alpha=1.0)
model = Ridge()

# TODO 5. 모델 학습
model.fit(X_train,y_train)

# TODO 6. 테스트 데이터로 예측
y_pred = model.predict(X_test)

# TODO 7. 성능 평가 출력
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
print(f"R²: {r2_score(y_test, y_pred):.4f}")

# TODO 8. 계수 확인 (어떤 피처가 영향을 많이 주는지)
# print("피처별 계수:", ___________)
# print("피처 이름:", ___________)