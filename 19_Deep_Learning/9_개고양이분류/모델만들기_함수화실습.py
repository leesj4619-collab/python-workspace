import os
import tensorflow as tf
import pathlib
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Rescaling

데이터경로 = pathlib.Path(r"PetImages")

def 깨진파일제거(경로, 폴더목록=["Cat", "Dog"]):
    for 폴더 in 폴더목록:
        for 파일 in (경로 / 폴더).glob("*.jpg"):
            try:
                img = tf.io.read_file(str(파일))
                tf.image.decode_jpeg(img)
            except:
                print(f"깨진파일 삭제 : {파일}")
                os.remove(파일)

def 각폴더별_데이터개수확인(경로, 폴더목록=["Cat", "Dog"]):
    # 각 폴더별 데이터 개수가 몇개인지 print 조회
    전체합계=0
    for 폴더 in 폴더목록:
        폴더경로 = 경로 / 폴더
        개수 = len(list(폴더경로.glob('*.jgp')))
        전체합계 += 개수
        print(f'{폴더} : {개수:,}장')

        print(f'전체 합계 : {전체합계}장')

# =============================================
# 전처리 def 호출
# =============================================
def 데이터불러오기(경로, 이미지크기=(64, 64), 배치=32):
    """
    훈련데이터와 검증데이터를 불러오고 정규화까지 하는 함수
    경로     : 데이터 폴더 경로
    이미지크기: 이미지 resize 크기 (기본값 64x64)
    배치     : batch_size (기본값 32)
    """
    # TODO: 훈련데이터 불러오는 코드를 작성하세요
    훈련 = image_dataset_from_directory(
        경로,
        image_size=이미지크기,        # 힌트: 매개변수 이미지크기 사용
        batch_size=배치,            # 힌트: 매개변수 배치 사용
        validation_split=0.2,
        subset='training',
        seed=42
    )
    # TODO: 검증데이터 불러오는 코드를 작성하세요
    검증 = image_dataset_from_directory(
        경로,
        image_size=이미지크기,        # 힌트: 매개변수 이미지크기 사용
        batch_size=배치,            # 힌트: 매개변수 배치 사용
        validation_split=0.2,
        subset='validation',
        seed=42
    )
    # TODO: 정규화 코드를 작성하세요 (1./255)
    norm = Rescaling(1./255)
    훈련 = 훈련.map(lambda x, y: (norm(x), y)).prefetch(1)
    검증 = 검증.map(lambda x, y: (norm(x), y)).prefetch(1)

    # TODO: 훈련, 검증 두 개를 반환하세요
    return 훈련, 검증

# =============================================
# 뇌 만들기 def 호출
# =============================================
def 모델만들기(이미지크기=(64, 64)):
    """
    CNN 모델을 만들고 컴파일까지 하는 함수
    이미지크기: Input shape 에 사용 (기본값 64x64)
    """
    # TODO: Sequential 모델을 완성하세요
    모델 = Sequential([
        # 이미지크기=(64,64)에서 맨 앞 64를 가져올 때는 이미지크기(0) 와 같이 작성
        # 이미지크기=(64,64)에서 맨 뒤 64를 가져올 때는 이미지크기(1) 와 같이 작성
        Input(shape=(이미지크기[0],  이미지크기[1], 3)),   # 힌트: 이미지크기[0], 이미지크기[1]
        Conv2D(32, (3, 3), activation='relu'),
        MaxPooling2D(),                          # 힌트: MaxPooling2D
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(),                          # 힌트: MaxPooling2D
        Flatten(),                          # 힌트: Flatten
        Dense(64, activation='relu'),
        Dense(1,  activation='sigmoid'),     # 힌트: 2분류니까 sigmoid
    ])
    # TODO: compile 을 완성하세요
    모델.compile(
        optimizer='adam',                # 힌트: adam
        loss='binary_crossentropy',                     # 힌트: binary_crossentropy
        metrics=['accuracy']                 # 힌트: accuracy
    )
    return 모델

# =============================================
# 모델저장 def 호출 사용
# =============================================
def 모델저장(모델, 폴더='models', 파일명='dog_cat_model.keras'):
    """
    모델을 저장하고 결과를 출력하는 함수
    모델  : 저장할 모델
    폴더  : 저장할 폴더명 (기본값 models)
    파일명: 저장할 파일명 (기본값 dog_cat_model.keras)
    """
    # TODO: 폴더 만들기 (이미 있어도 에러 안나게)
    os.makedirs(폴더, exist_ok=True)

    # TODO: 저장 경로 만들기
    # 힌트: 폴더 + '/' + 파일명
    저장경로 = 폴더 + '/' + 파일명

    # TODO: 모델 저장하기
    모델.save(저장경로)
    print(f"모델 저장 완료! → {저장경로}")

    # TODO: 저장 확인하기
    if os.path.exists(저장경로):
        print("저장 성공!")
    else:
        print("저장 실패!")

# =============================================
# 함수 실행 (여기는 수정하지 않아도 됩니다)
# =============================================
# 깨진파일제거(데이터경로)

훈련데이터, 검증확인데이터 = 데이터불러오기(데이터경로)

로봇뇌 = 모델만들기()

로봇뇌.fit(훈련데이터, epochs=5, validation_data=검증확인데이터)

모델저장(로봇뇌)
