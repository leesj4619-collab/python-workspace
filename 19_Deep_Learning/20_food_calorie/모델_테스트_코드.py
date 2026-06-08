from transformers import pipeline

# TODO 1: pipeline 함수를 사용해서 이미지 분류 모델을 불러오세요
# 힌트: task는 "image-classification", model은 "nateraw/food"
음식분류 = pipeline(
    'image-classification',
    model='nateraw/food'
)

# TODO 2: 음식 사진 파일 경로를 넣어서 분류 결과를 변수에 저장하세요
# 힌트: 음식분류("파일이름.jpg") 형태로 호출
결과 = 음식분류('햄버거.jpg')

# TODO 3: 결과를 출력하세요
# 힌트: print()
print(결과)

# TODO 4: 결과에서 1등 음식 이름(label)과 확률(score)만 뽑아서 출력해보세요
# 힌트: 결과는 리스트 형태, 결과[0]["label"] 로 접근 가능
print("1등 음식:", 결과[0]['label'])
print("확률:", 결과[0]['score'])