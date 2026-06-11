import os
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
import matplotlib.pyplot as plt


#=========================================================================
# 2. preprocessing
#=========================================================================

이미지크기 = 64  # 64×64 픽셀로 통일

def 이미지불러오기(폴더경로):
    이미지목록 = []
    for 파일명 in os.listdir(폴더경로):
        if not 파일명.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        try:
            경로 = os.path.join(폴더경로, 파일명)
            img = Image.open(경로)

            # 힌트: 흑백/RGBA 등 다양한 포맷을 RGB로 통일
            img = img.convert("RGB")               # (1) "RGB" 입력

            # 힌트: 모든 이미지를 동일한 크기로 리사이즈
            img = img.resize((이미지크기, 이미지크기))        # (2) (이미지크기, 이미지크기) 입력

            이미지목록.append(np.array(img))
        except Exception as e:
            print(f"실패: {파일명} - {e}")
    print(f"불러온 이미지 수: {len(이미지목록)}")
    return np.array(이미지목록)


토끼데이터 = 이미지불러오기("rabbit")

# 힌트: 픽셀값 0~255를 0~1 범위로 정규화 (255.0으로 나누기)
토끼데이터 = 토끼데이터.astype("float32") / 255.0   # (3) 255.0 입력

# 힌트: (N, 64, 64, 3) 형태를 (N, 12288)로 펼치기
# 64 * 64 * 3 = 12288
토끼_펼친것 = 토끼데이터.reshape(-1, 이미지크기 * 이미지크기 * 3)  # (4) 이미지크기, 이미지크기, 3 입력

print(f"최종 데이터 형태: {토끼_펼친것.shape}")
# 예상 출력: (이미지수, 12288)

# 훈련 80% / 테스트 20% 분리
훈련, 테스트 = train_test_split(토끼_펼친것, test_size=0.2, random_state=42)
print(f"훈련: {훈련.shape}, 테스트: {테스트.shape}")


#=========================================================================
# 3. autoencoder
#=========================================================================

입력크기 = 이미지크기 * 이미지크기 * 3  # 12288

로봇뇌 = Sequential([
    Input(shape=(입력크기,)),

    # ── 인코더 (압축) ──────────────────────────
    Dense(1024, activation="relu"),   # (5) 1024
    Dense(512, activation="relu"),   # (6) 512
    Dense(256, activation="relu"),   # (7) 256
    Dense(128, activation="relu"),   # (8) 128  ← 잠재벡터 (병목)

    # ── 디코더 (복원) ──────────────────────────
    Dense(256, activation="relu"),   # (9)  256
    Dense(512, activation="relu"),   # (10) 512
    Dense(1024, activation="relu"),   # (11) 1024

    # 힌트: 출력층은 입력과 같은 크기, 픽셀값 0~1이므로 sigmoid 사용
    Dense(입력크기, activation="sigmoid"),   # (12) 입력크기, "sigmoid"
])

# 힌트: 복원 오차는 MSE(평균제곱오차)로 측정
로봇뇌.compile(optimizer="adam", loss="mse")  # (13) "mse"
로봇뇌.summary()

# 힌트: 오토인코더는 입력 = 정답 (자기 자신을 복원)
로봇뇌.fit(
    훈련, 훈련,        # (14) 훈련 (입력과 정답이 동일)
    epochs=50,
    batch_size=32,
    validation_split=0.1,
    verbose=1
)

# 복원 결과 시각화
복원이미지 = 로봇뇌.predict(테스트[:5])

그림, 축 = plt.subplots(2, 5, figsize=(15, 6))
for i in range(5):
    축[0, i].imshow(테스트[i].reshape(이미지크기, 이미지크기, 3))
    축[1, i].imshow(복원이미지[i].reshape(이미지크기, 이미지크기, 3))
    for j in range(2):
        축[j, i].axis("off")
축[0, 0].set_ylabel("원본")
축[1, 0].set_ylabel("복원")
plt.suptitle("토끼 이미지 오토인코더 복원 결과")
plt.tight_layout()
plt.show()

#=========================================================================
# 4. denoising
#=========================================================================

import numpy as np
import matplotlib.pyplot as plt

# ── 노이즈 추가 함수 ───────────────────────────────────────
def 노이즈추가(데이터, 노이즈강도=0.2):
    # 힌트: 정규분포 난수(randn)를 데이터에 더하고, 0~1로 클리핑
    return np.clip(
        데이터 + 노이즈강도 * np.random.randn(*데이터.shape),  # (15) randn
        0.0,  # (16) 0.0  ← 최솟값
        1.0   # (17) 1.0  ← 최댓값
    )

훈련노이즈 = 노이즈추가(훈련)
테스트노이즈 = 노이즈추가(테스트)

# ── 모델 구조 (3단계와 동일) ──────────────────────────────
노이즈제거뇌 = Sequential([
    Input(shape=(입력크기,)),
    Dense(1024, activation="relu"),
    Dense(512,  activation="relu"),
    Dense(256,  activation="relu"),
    Dense(128,  activation="relu"),
    Dense(256,  activation="relu"),
    Dense(512,  activation="relu"),
    Dense(1024, activation="relu"),
    Dense(입력크기, activation="sigmoid")
])

노이즈제거뇌.compile(optimizer="adam", loss="mse")

# 힌트: 노이즈 이미지 입력 → 깨끗한 원본이 정답
노이즈제거뇌.fit(
    훈련노이즈,   # (18) 훈련노이즈  ← 노이즈 낀 입력
    훈련,   # (19) 훈련       ← 깨끗한 정답
    epochs=50,
    batch_size=32,
    validation_split=0.1,
    verbose=1
)

# 결과 시각화 (원본 / 노이즈 / 복원 3단계)
복원이미지 = 노이즈제거뇌.predict(테스트노이즈[:5])

그림, 축 = plt.subplots(3, 5, figsize=(15, 9))
for i in range(5):
    축[0, i].imshow(테스트[i].reshape(이미지크기, 이미지크기, 3))
    축[1, i].imshow(테스트노이즈[i].reshape(이미지크기, 이미지크기, 3))
    축[2, i].imshow(복원이미지[i].reshape(이미지크기, 이미지크기, 3))
    for j in range(3):
        축[j, i].axis("off")
for j, 이름 in enumerate(["원본", "노이즈", "복원"]):
    축[j, 0].set_ylabel(이름)
plt.suptitle("토끼 노이즈 제거 결과")
plt.tight_layout()
plt.show()

#=========================================================================
# 5. save_load
#=========================================================================

# ── 모델 저장 ─────────────────────────────────────────────

# 힌트: Keras 기본 저장 형식은 .keras (권장)
로봇뇌.save("autoencoder.keras")            # (20) "autoencoder.keras"
노이즈제거뇌.save("denoising_autoencoder.keras")      # (21) "denoising_autoencoder.keras"

print("모델 저장 완료")


# ── 모델 불러오기 ──────────────────────────────────────────
from tensorflow.keras.models import load_model

# 힌트: load_model()로 저장된 모델을 다시 불러옴
불러온_모델       = load_model("autoencoder.keras")   # (22) "autoencoder.keras"
불러온_노이즈모델 = load_model("denoising_autoencoder.keras")   # (23) "denoising_autoencoder.keras"

print("모델 불러오기 완료")
불러온_모델.summary()


# ── 불러온 모델로 예측 ─────────────────────────────────────
복원이미지_저장모델 = 불러온_모델.predict(테스트[:5])

그림, 축 = plt.subplots(2, 5, figsize=(15, 6))
for i in range(5):
    축[0, i].imshow(테스트[i].reshape(이미지크기, 이미지크기, 3))
    축[1, i].imshow(복원이미지_저장모델[i].reshape(이미지크기, 이미지크기, 3))
    for j in range(2):
        축[j, i].axis("off")
축[0, 0].set_ylabel("원본")
축[1, 0].set_ylabel("복원 (저장된 모델)")
plt.suptitle("저장된 모델로 복원한 결과")
plt.tight_layout()
plt.show()