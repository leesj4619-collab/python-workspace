import os
import tensorflow as tf
import pathlib
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Rescaling

데이터경로 = pathlib.Path("weather")

'''
데이터셋에 존재하는 폴더이름과 날씨폴더목록의 폴더이름이 다르면
잘못된 데이터 훈련
반드시 폴더 명칭 순서도 동일하게 작성
날씨폴더목록 = [
    "shine", "rain", "cloudy", "snow", "fogsmog",
    "thunder", "rainbow", "sandstorm", "lightning", "tornado", "frost"
]
'''
날씨폴더목록 = [
    "dew", "fogsmog", "frost", "glaze", "hail",
    "lightning", "rain", "rainbow", "rime", "sandstorm", "snow"
]

# for 폴더 in 날씨폴더목록:
#     for 파일 in (데이터경로 / 폴더).glob("*.jpg"):
#         try:
#             img = tf.io.read_file(str(파일))
#             tf.image.decode_jpeg(img)
#         except:
#             os.remove(파일)

# ↓↓↓ 여기 숫자들을 바꿔가며 실습 ↓↓↓

# TODO: 아래 값들을 바꿔보세요
EPOCHS     = 30  # 기본값 10  → 20 으로 늘려보기
BATCH_SIZE = 32   # 기본값 32  → 16, 64 로 바꿔보기
DENSE_수   = 256   # 기본값 128 → 256 으로 늘려보기
CONV_필터  = 64   # 기본값 32  → 64 로 늘려보기

# TODO: 모델 이름을 세팅값으로 자동 설정되게 빈칸 채우기
# 힌트: f"models/weather_ep{____}_batch{____}_dense{____}.keras"
모델이름 = f"models/weather_ep{EPOCHS}_batch{BATCH_SIZE}_dense{DENSE_수}.keras"
print(f"저장될 모델 이름: {모델이름}")

훈련데이터 = image_dataset_from_directory(
    데이터경로, image_size=(150, 150),
    batch_size=BATCH_SIZE,
    validation_split=0.2, subset='training', seed=42
)
검증데이터 = image_dataset_from_directory(
    데이터경로, image_size=(150, 150),
    batch_size=BATCH_SIZE,
    validation_split=0.2, subset='validation', seed=42
)

norm = Rescaling(1./255)
훈련데이터 = 훈련데이터.map(lambda x, y: (norm(x), y)).prefetch(1)
검증데이터 = 검증데이터.map(lambda x, y: (norm(x), y)).prefetch(1)

# TODO: CONV_필터, DENSE_수 빈칸 채우기
로봇뇌 = Sequential([
    Input(shape=(150, 150, 3)),
    Conv2D(CONV_필터, (3, 3), activation='relu'),    # ← CONV_필터 넣기
    MaxPooling2D(),
    Conv2D(CONV_필터, (3, 3), activation='relu'),    # ← CONV_필터 * 2 넣기
    MaxPooling2D(),
    Conv2D(CONV_필터, (3, 3), activation='relu'),    # ← CONV_필터 * 4 넣기
    MaxPooling2D(),
    Flatten(),
    Dense(DENSE_수, activation='relu'),             # ← DENSE_수 넣기
    Dense(11, activation='softmax'),
])

로봇뇌.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
기록 = 로봇뇌.fit(훈련데이터, epochs=EPOCHS, validation_data=검증데이터)

os.makedirs('models', exist_ok=True)
로봇뇌.save(모델이름)
print(f"저장 완료 → {모델이름}")

최종훈련정확도 = 기록.history['accuracy'][-1]
최종검증정확도 = 기록.history['val_accuracy'][-1]

print('\n' + '='*30)
print(f'최종훈련정확도 : {최종훈련정확도*100:.2f}%')
print(f'최종검증정확도 : {최종검증정확도*100:.2f}%')
print('='*30)

'''


EPOCHS     = 15   
BATCH_SIZE = 16  
DENSE_수   = 256   
CONV_필터  = 32   
최종훈련정확도 : 97.39%
최종검증정확도 : 69.07%
=========================
EPOCHS     = 30   
BATCH_SIZE = 32  
DENSE_수   = 256   
CONV_필터  = 64   
최종훈련정확도 : 98.00%
최종검증정확도 : 67.69%
'''

