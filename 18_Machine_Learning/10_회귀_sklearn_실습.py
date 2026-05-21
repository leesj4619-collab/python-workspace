from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
import numpy as np

# 1. 데이터 불러오기
data = fetch_california_housing()
X,y = data.data,data.target

#print(dir(data))
'''
['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__type_params__', '__wrapped__', '_skl_parameter_constraints']
'''

# 2. 학습 / 테스트 분리작업
# X = 훈련용                   _train = 데이터 _test = 정답지
# y = 훈련제대로 되엇는지 (시험용) _train = 데이터 _test = 정답지
# test_size=0.2,random_state=42 이 숫자가 100% 좋은 수는 아니다.
# 단순히 초반에 시작할 때 많이 설정하는 숫자값
# 숫자값은 변경이 계속 된다.
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# 3. 학습용과 학습제대로 되었는지 확이하기 위한 데이터 분리를 바탕으로
#    모델 학습
# 모델을 학습하기 위해서 모델을 선택하고 선택한 모델로 학습을 시킨다.
# 3-1. 모델 선택해서 model 변수공간에 저장하기
model = LinearRegression()

# 3-2. 선택한 모델로 훈련시키기
model.fit(X_train,y_train)

# 4. 예측하기
# 예측을 할 때 X_test만 사용하는 이유
# fit으로 만들어진 임시 모델을 컴퓨터에서 잠시 보유
# 임시 모델을 이용해서 X_test 데이터 정답을 제대로 맞추고 있는지 확인
y_pred = model.predict(X_test)


# 5. 평가
# Root Mean Squared Error = 오차의 크기
# - numpy에 존재하는 sqrt() 기능과 mean_square_error(y_test,y_pred) 기능 사용
# -- mean_square_error(y_test,y_pred)
# -- 실제값이랑 예측값의 차이를 계산하는 기능
# -- y_test = 실제 집값
# -- y_pred = 모델이 예측한 집값
# -- np.sqrt() 제곱근 함수
#    mean_square_error 평균의 제곱근형태로 결과 반환
#    그것을 원래대로 되돌려 놓는 것 0과 -1 처럼 잘못된 데이터로 추출되는것을 방지하기 위하여 제곱근 반환
# R²(R-Squared)           = 내 모델이 데이터를 얼마나 잘 표현하고 있는가
# - r2_score(y_test, y_pred)
print(f"RMSE : {np.sqrt(mean_squared_error(y_test,y_pred)):.4f}")
print(f'R² : {r2_score(y_test,y_pred):.4f}')

'''

(X,y test_size=0.2, random_state=42)
RMSE : 0.7456*10만 = 평균적으로 예측이 7만 4천달러 정도 빗나간다.
R² : 0.5758 = 내 모델이 57% 정확하다

R² 기준으로
0.9이상 -> 매우 좋음
0.7 ~ 0.9 -> 좋음
0.5 ~ 0.7 -> 보통
0.5 -> 별로

LinearRegression(OLS)은 단순 직선 모델이라 한계가 있다.
0.5 0.9로 만들기 위해서 모델 교체 데이터 나누는 것도 다시 세팅 피처 넣어보고 다양한 방법 존재하기 시작
'''

