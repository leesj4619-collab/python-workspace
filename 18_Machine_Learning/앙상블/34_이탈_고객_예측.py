"""
이커머스 고객 이탈 예측
- 실제 쇼핑몰에서 "이 고객 다음 달에 안 올 것 같다" 예측
- RandomForest vs VotingClassifier 비교
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


def 고객이탈예측():
    # TODO 1: CSV 파일 읽기
    df = pd.read_csv('../csvs/ecommerce_customer_data_custom_ratios.csv', encoding='utf-8')

    print("=== 데이터 미리보기 ===")
    print(df.head())
    print(f"\n총 고객 수 : {len(df)}명")
    print(f"이탈 고객 수 : {df['Churn'].sum()}명")
    print(f"유지 고객 수 : {(df['Churn'] == 0).sum()}명")

    df['Gender'] = df['Gender'].map({'Male':0,'Female':1})
    df['Returns'] = df['Returns'].fillna(df['Returns'].mean())
    # 사용할 피처 - 이미 완성
    features = [
        'Product Price',
        'Quantity',
        'Total Purchase Amount',
        'Age',
        'Returns',
        'Gender',
    ]
    X = df[features]
    y = df['Churn']  # 정답: 이탈=1, 유지=0

    # TODO 2: train_test_split (test_size=0.2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

    # TODO 3: RandomForestClassifier 학습 후 예측
    #          n_estimators=100, max_features='sqrt', random_state=42
    rf = RandomForestClassifier(
        n_estimators=100,
        max_features='sqrt',
        random_state=42
    )
    rf.fit(X_train,y_train)
    pred_rf = rf.predict(X_test)

    print("\n=== 랜덤 포레스트 ===")
    print(f"정확도 : {accuracy_score(y_test, pred_rf):.4f}")
    print(classification_report(y_test, pred_rf, target_names=['유지고객', '이탈고객']))

    # TODO 4: VotingClassifier 학습 후 예측
    model1 = RandomForestClassifier(n_estimators=100, random_state=42)
    model2 = DecisionTreeClassifier(random_state=42)
    model3 = LogisticRegression(max_iter=1000, random_state=42)

    voting = VotingClassifier(
        estimators=[('rf',model1),('dt',model2),('lr',model3)],  # TODO: 채우기
        voting='soft'       # TODO: 채우기
    )
    voting.fit(X_train,y_train)
    pred_voting = voting.predict(X_test)

    print("\n=== 보팅 (3개 모델 투표) ===")
    print(f"정확도 : {accuracy_score(y_test, pred_voting):.4f}")
    print(classification_report(y_test, pred_voting, target_names=['유지고객', '이탈고객']))

    # TODO 5: 피처 중요도 - 어떤 게 이탈에 제일 영향을 주는지
    rf2 = RandomForestClassifier(n_estimators=100, random_state=42)
    rf2.fit(X_train, y_train)
    중요도 = pd.DataFrame({
        '특성': features,
        '중요도': rf2.feature_importances_  # TODO: rf2.feature_importances_ 채우기
    }).sort_values('중요도', ascending=False)

    print("\n=== 이탈에 영향을 주는 요소 순위 ===")
    print(중요도)


고객이탈예측()