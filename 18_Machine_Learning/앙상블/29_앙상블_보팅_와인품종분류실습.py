'''
앙상블 실습 - 와인 품종 분류
- 와인의 알콜, 산도, 색상 등 13개 성분으로 와인 품종 3가지를 분류
- 아이리스보다 KNN이 약해서 보팅(모델 투표를 통한 결과) 효과가 더 잘 보임

예)
    와인 데이터를 X에 넣으면 품종을 예측
    X = [[알콜, 산도, 생상강도, 플라보노이드,...]]

    lr.predict(X) # 로지스틱 회귀가 판단 -> [0] (1등급 와인) -> 경계선 그려 판단
    dt.predict(X) # 결정 트리가 판단    -> [0] (1등급 와인) -> 스무고개 방식으로 판단
    knn.predict(X) # KNN이 판단        -> [0] (1등급 와인) -> 비슷한 와인을 찾아서 판단
    다수 모델의 다수결로 최종 결정
'''
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_wine  # 데이터만 붓꽃에서 와인으로 교체
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 데이터를 데이터셋과 어떤 데이터인지 정답으로 분리하기
X,y = load_wine(return_X_y=True)
X_tarin, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

로지스틱모델 = LogisticRegression(max_iter=20000)# LogisticRegression 확률에 따른 분류
# STOP: TOTAL NO. OF ITERATIONS REACHED LIMIT
# 학습하는 양이 적으면 위 문구가 나옴 *에러는 아님*
결정트리모델 = DecisionTreeClassifier()
KNN모델    = KNeighborsClassifier()

def 하드투표기능():
    하드투표 = VotingClassifier(
        estimators=[
            ('lr',로지스틱모델),
            ('dt',결정트리모델),
            ('knn',KNN모델)
        ],
        voting = 'hard'
    )
    하드투표.fit(X_tarin,y_train)
    결과 = 하드투표.predict(X_test)
    print(f'하드 보팅 정확도 : {accuracy_score(결과,y_test):.4f}')

def 소프트투표기능():
    소프트투표 = VotingClassifier(
        estimators=[
            ('lr',로지스틱모델),
            ('dt',결정트리모델),
            ('knn',KNN모델)
        ],
        voting = 'soft'
    )
    소프트투표.fit(X_tarin,y_train)
    결과 = 소프트투표.predict(X_test)
    print(f'소프트 보팅 정확도 : {accuracy_score(결과,y_test):.4f}')

def 하드_소프트_투표기능():
    하드투표 = VotingClassifier(
        estimators=[
            ('lr',로지스틱모델),
            ('dt',결정트리모델),
            ('knn',KNN모델)
        ],
        voting = 'hard'
    )
    소프트투표 = VotingClassifier(
        estimators=[
            ('lr',로지스틱모델),
            ('dt',결정트리모델),
            ('knn',KNN모델)
        ],
        voting = 'soft'
    )
    # 학습 & 평가 version 1 = 하드인가 소프트인가 확인
    for 이름, 모델 in [('하드투표',하드투표),('소프트투표',소프트투표)]:
        모델.fit(X_tarin,y_train)
        결과 = 모델.predict(X_test)
        print('='*20,이름,'='*20)
        print(f'{이름} 정확도 : {accuracy_score(결과,y_test):.4f}')
    # 학습 & 평가 version 2 = 로지스틱 / 결정트리 / KNN 모델별 정확도 확인
    for 이름, 모델 in [
        ('lr',로지스틱모델),
        ('dt',결정트리모델),
        ('knn',KNN모델)]:
        모델.fit(X_tarin,y_train)
        결과 = 모델.predict(X_test)
        print('='*20,이름,'='*20)
        print(f'{이름} 정확도 : {accuracy_score(결과,y_test):.4f}')

하드_소프트_투표기능()

''' 
==================== 하드투표 ====================
하드투표 정확도 : 1.0000
==================== 소프트투표 ====================
소프트투표 정확도 : 0.9722
==================== lr ====================
lr 정확도 : 1.0000
==================== dt ====================
dt 정확도 : 0.9444
==================== knn ====================
knn 정확도 : 0.7222

'''
