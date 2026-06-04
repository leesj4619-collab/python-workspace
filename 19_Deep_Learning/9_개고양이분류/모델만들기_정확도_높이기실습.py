import os
import tensorflow as tf
import pathlib
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Rescaling

데이터경로 = pathlib.Path(r"PetImages")

# 깨진 데이터 전처리
# for 폴더 in ["Cat", "Dog"]:
#     for 파일 in (데이터경로 / 폴더).glob("*.jpg"):
#         try:
#             img = tf.io.read_file(str(파일))
#             tf.image.decode_jpeg(img)
#         except:
#             os.remove(파일)

# ↓↓↓ 여기 숫자들을 바꿔가며 실습 ↓↓↓

# TODO: 아래 값들을 바꿔보세요
EPOCHS     = 20   # 기본값 5  → 10, 20 으로 늘려보기
BATCH_SIZE = 32   # 기본값 32 → 16, 64 로 바꿔보기
DENSE_수   = 256   # 기본값 64 → 128, 256 으로 늘려보기
CONV_필터  = 64   # 기본값 32 → 64 로 늘려보기

# TODO: 모델 이름을 세팅값으로 자동 설정되게 빈칸 채우기
# 힌트: f"models/cat_dog_ep{____}_batch{____}_dense{____}.keras"
모델이름 = f"models/cat_dog_ep{EPOCHS}_batch{BATCH_SIZE}_dense{DENSE_수}.keras"
print(f"저장될 모델 이름: {모델이름}")

# 데이터 불러오기
훈련데이터 = image_dataset_from_directory(
    데이터경로, image_size=(64, 64),
    batch_size=BATCH_SIZE,          # ← BATCH_SIZE 적용
    validation_split=0.2, subset='training', seed=42
)
검증확인데이터 = image_dataset_from_directory(
    데이터경로, image_size=(64, 64),
    batch_size=BATCH_SIZE,          # ← BATCH_SIZE 적용
    validation_split=0.2, subset='validation', seed=42
)

norm = Rescaling(1./255)
훈련데이터     = 훈련데이터.map(lambda x, y: (norm(x), y)).prefetch(1)
검증확인데이터 = 검증확인데이터.map(lambda x, y: (norm(x), y)).prefetch(1)

# TODO: CONV_필터, DENSE_수 빈칸 채우기
로봇뇌 = Sequential([
    Input(shape=(64, 64, 3)),
    Conv2D(CONV_필터, (3, 3), activation='relu'),   # ← CONV_필터 넣기
    MaxPooling2D(),
    Conv2D(CONV_필터, (3, 3), activation='relu'),   # ← CONV_필터 * 2 넣기
    MaxPooling2D(),
    Flatten(),
    Dense(DENSE_수, activation='relu'),            # ← DENSE_수 넣기
    Dense(1, activation='sigmoid'),
])

로봇뇌.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
로봇뇌.fit(훈련데이터, epochs=EPOCHS, validation_data=검증확인데이터)
loss, acc = 로봇뇌.evaluate(훈련데이터)
print(f'정확도 : {acc*100:.1f}%')

# 모델 저장
os.makedirs('models', exist_ok=True)
로봇뇌.save(모델이름)
print(f"저장 완료 → {모델이름}")