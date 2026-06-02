from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Flatten, Dense

labels = ['티셔츠', '바지', '스웨터', '드레스', '코트',
          '샌들', '셔츠', '스니커즈', '가방', '부츠']

def run_fashion_mnist():
    # Step 1. 데이터 불러오기
    (X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

    # Step 2. 정규화
    # TODO: X_train, X_test 를 255.0 으로 나누어 정규화 하세요
    X_train, X_test = X_train / 255.0, X_test / 255.0

    # Step 3. 모델 설계
    model = Sequential([
        Input(shape=(28, 28)),
        Flatten(),
        # TODO: 뉴런 256개, 활성화함수 relu 를 채우세요
        Dense(256, activation='relu'),
        # TODO: 출력층 - 옷 종류 10개, 확률 변환 활성화함수를 채우세요
        Dense(10, activation='softmax')
    ])

    # Step 4. 컴파일
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    # Step 5. 학습
    # TODO: epochs 를 30으로 설정하세요
    model.fit(X_train, y_train, epochs=30, verbose=1, batch_size=32)

    # Step 6. 평가
    loss, acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"[Fashion MNIST] 정확도: {acc*100:.1f}%")

    # Step 7. 모델 저장
    # TODO: 모델을 'fashion_model.keras' 파일명으로 저장하세요
    model.save('fashion_model.keras')
    print("모델 저장 완료")

run_fashion_mnist()