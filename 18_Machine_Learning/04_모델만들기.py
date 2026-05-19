import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
'''
파이썬 모델
- 데이터 학습을 완료하고, 예측을 할 수 있는 상태가 된 것

모델 파일
- 학습과 결과를 파일로 저장한 형태

1. pickle(.pkl)
- 파이썬 기본 내장 도구
- 가장 많이 사용하는 방식
- 파이썬에서만 열 수 있다.
- 아무 모델이나 저장 가능

2. joblib(.pkl or .joblib)
- scikit-learn 공식 추천 방식
- pickle 보다 큰 데이터를 저장할 때 빠름
- scikit-learn 모델에는 이게 적합
- 실무에서 pickle 보다 많이 사용됨

3. ONNX(.onnx)
- 파이썬 말고 다른 언어에서도 열 수 있는 모델
- 자바, C++, 자바스크립트 등에서 사용가능
- 앱이나 다른 서버에 모델을 올릴 때 사용
- 입문 단계에서는 난이도 있다.

4. h5/keras (.h5)
- 딥러닝(tensorflow, keras) 전용
- scikit-learn 모델엔 사용 안 함
- 나중에 딥러닝 배울 때 배울 모델

웹사이트 확장자에 .jsp .html 이 존재하고,
엑셀 파일 .xlsx .csv 
이미지 파일 .jsp . png 등
존재하는 것처럼 모델에도 다양한 확장자가 사용 상황에 따라 존재할 뿐 동일한 상태이다.
'''