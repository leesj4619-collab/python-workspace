import os
import tensorflow as tf
import pathlib
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Rescaling

데이터경로 = pathlib.Path("butterfly")

# ↓↓↓ 여기 숫자들을 바꿔가며 실습 ↓↓↓

# TODO: 아래 값들을 바꿔보세요
EPOCHS     = 15   # 기본값 10 → 20 으로 늘려보기
BATCH_SIZE = 16   # 기본값 32 → 16, 64 로 바꿔보기
DENSE_수   = 512   # 기본값 256 → 512 로 늘려보기
CONV_필터  = 32   # 기본값 32  → 64 로 늘려보기

# TODO: 모델 이름 빈칸 채우기
# 힌트: f"models/butterfly_ep{____}_batch{____}_dense{____}.keras"
모델이름 = f"models/butterfly_ep{EPOCHS}_batch{BATCH_SIZE}_dense{DENSE_수}.keras"
print(f"저장될 모델 이름: {모델이름}")

훈련데이터 = image_dataset_from_directory(
    데이터경로 / 'train', image_size=(224, 224), batch_size=BATCH_SIZE, seed=42
)
검증데이터 = image_dataset_from_directory(
    데이터경로 / 'valid', image_size=(224, 224), batch_size=BATCH_SIZE, seed=42
)
norm = Rescaling(1./255)
훈련데이터 = 훈련데이터.map(lambda x, y: (norm(x), y)).prefetch(1)
검증데이터 = 검증데이터.map(lambda x, y: (norm(x), y)).prefetch(1)

# TODO: CONV_필터, DENSE_수 빈칸 채우기
로봇뇌 = Sequential([
    Input(shape=(224, 224, 3)),
    Conv2D(CONV_필터, (3, 3), activation='relu'),    # ← CONV_필터
    MaxPooling2D(),
    Conv2D(CONV_필터*2, (3, 3), activation='relu'),    # ← CONV_필터 * 2
    MaxPooling2D(),
    Conv2D(CONV_필터*4, (3, 3), activation='relu'),    # ← CONV_필터 * 4
    MaxPooling2D(),
    Conv2D(CONV_필터*8, (3, 3), activation='relu'),    # ← CONV_필터 * 8
    MaxPooling2D(),
    Flatten(),
    Dense(DENSE_수, activation='relu'),             # ← DENSE_수
    Dense(100, activation='softmax'),           # 100종류 고정
])

로봇뇌.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
로봇뇌.fit(훈련데이터, epochs=EPOCHS, validation_data=검증데이터)

os.makedirs('models', exist_ok=True)
로봇뇌.save(모델이름)
print(f"저장 완료 → {모델이름}")