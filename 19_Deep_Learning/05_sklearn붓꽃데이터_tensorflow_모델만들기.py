# 목표 하나를 개발하는데 방법은 수십 수백만가지가 존재
# 머신러닝 / 딥러닝은 그 중 하나의 방법일 뿐
# 머신러닝이나 딥러닝이 아니어도 코딩으로 목표를 개발할 수 있다.
# 하지만 머신러닝이나 딥러닝에 비해서 개발자의 손이 심하게 많이 갈 뿐

import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X,y = load_iris(return_X_y=True)

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=42,test_size=0.2)
# Sequential = 머신러닝과 같은 AI 모델 만들기 도안
# 반드시 지켜야 할 규칙
# 1. 들어오는 데이터가 어떻게 생겼는데 입력층에 세팅 데이터 1D 2D 3D ... 인지 확인하기
# 2. 데이터에서 사용할 컬럼의 개수 확인
#   꽃받침길이, 꽃받침너비, 꽃잎길이, 꽃잎너비
'''
레거시 방식 ↓
tf.keras.layers.Dense(8,activation='relu',input_shape=(4,)),
Dense가 두가지 일을 동시에 한다 입력 정의 + 계산
DeepLearning의 경우 모델을 세분화 해서 사람 뇌 처럼 AI 뇌도 세분화 하여 만들었으면 좋겠다.
keras = google에서 권장하는 방식

권장 방식 ↓
tf.keras.layers.Input(shape=4,),

'''
model = tf.keras.Sequential([
    # 사람의 뇌처럼 a-z 까지 촘촘하게 AI뇌 신경망을 만들었으면 좋겠다.
    # tf.keras.layers.Dense(8,activation='relu',input_shape=(4,)),
    tf.keras.layers.Input(shape=(4,)), # shape은 반드시 소괄호를 해주어야 한다.
    tf.keras.layers.Dense(8, activation='relu'),

    # softmax는 확률로 바꿔주는 역할
    # 만약 softmax가 없으면 단순 훈련 숫자만 나온다.
    # 단순 훈련 숫자는 무엇인지 알 수 없다.
    # softmax를 이용해서 각각의 숫자들을 3개 결과로 나타날 때 확률로 나타낸다
    # setosa 일 확률 70% versicolor 일 확률 15%, virginica 10%가 나왔다.
    tf.keras.layers.Dense(3,activation='softmax')
])
# 이 세가지 결과 중에서 가장 높은 숫자가 예측 결과로 Sequential 탈출해서 나올 것이다.

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy']
              )
model.fit(X_train,y_train, epochs=1000,verbose=1)
# epochs는 크면 클수록 모델 훈련이 잘 될 수 있고, 과적합(=훈련데이터만 외움) 될 수 있다.
#          크면 클수록 모델이 완성되는 시간이 오래 걸리며, 컴퓨터 성능도 더 좋아야한다.
# verbose = 0 출력안봄 1 출력모두봄 2 진행상황만안봄

loss, acc = model.evaluate(X_test,y_test)
print(f'정확도 : {acc * 100:.1f}%')