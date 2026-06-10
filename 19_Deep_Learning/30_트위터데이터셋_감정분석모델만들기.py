import pandas as pd
import torch
from transformers import pipeline

# =======================================================
# 1. 데이터 불러오기
# =======================================================
# TODO: pd.read_csv 로 csv 파일 불러오기
#       encoding='latin-1', header=None
#       names = ['감성', '아이디', '날짜', '쿼리', '유저', '트윗']
df = pd.read_csv(
    'training.1600000.processed.noemoticon.csv',
    encoding='latin-1',
    header='None',
    names=['감성', '아이디', '날짜', '쿼리', '유저', '트윗']
)

# TODO: 트윗, 감성 컬럼만 남기고 100개만 자르기
df = df['감성','트윗'].head(100)

# TODO: 감성 값 변환  0=부정, 4=긍정  ->  0, 1 로 변환
#       힌트: df['감성'].map({0: 0, 4: 1})
df['감성'] = df['감성'].map({0:0, 4:1})

# TODO: 데이터 3개만 출력해서 확인하기
for i, 행 in df.head(3).iterrows():
    print(f"트윗 : {행['트윗'][:80]}")
    print(f"감성 : {행['감성']}  1=긍정, 0=부정")
    print('-'*10)

# =======================================================
# 2. 허깅페이스 pipeline 준비
# =======================================================
# TODO: GPU 있으면 0, 없으면 -1 로 장치 설정
#       힌트: torch.cuda.is_available()
장치 = torch.cuda.is_available()

print(f"사용 장치: {'GPU' if 장치 == 0 else 'CPU'}")

# TODO: pipeline 으로 감성분석기 만들기
#       task   = 'sentiment-analysis'
#       model  = 'distilbert-base-uncased-finetuned-sst-2-english'
#       device = 장치
#       처음 실행할 때만 모델 자동 다운로드 (약 300MB)
감성분석기 = pipeline(
    'sentiment-analysis',
    model  = 'distilbert-base-uncased-finetuned-sst-2-english',
    device = 장치

)

# =======================================================
# 3. 예측하기
# =======================================================
# TODO: df 에서 트윗 목록만 리스트로 뽑기
#       힌트: df['트윗'].tolist()
트윗목록 = df['트윗'].tolist()

# TODO: 감성분석기로 트윗목록 전체 예측하기
#       truncation=True, max_length=64
결과목록 = 감성분석기(트윗목록, truncation=True, max_length=64)

# =======================================================
# 4. 결과 출력 + 정확도 계산
# =======================================================
맞춘개수 = 0

for i, (트윗, 결과) in enumerate(zip(트윗목록, 결과목록)):
    # TODO: 결과['label'] 이 'POSITIVE' 면 1, 아니면 0
    예측 = 1 if 결과['label'] == 'POSITIVE' else 0
    정답 = df['감성'].iloc[i]
    맞춤 = 'O' if 예측 == 정답 else 'X'

    print(f"트윗 : {트윗[:60]}")
    print(f"예측 : {'긍정' if 예측 == 1 else '부정'}  정답: {'긍정' if 정답 == 1 else '부정'}  {맞춤}")
    print('---')

    # TODO: 예측이 정답이면 맞춘개수 + 1
    if 예측 == 정답:
        맞춘개수 += 1

# TODO: 최종 정확도 출력
#       힌트: 맞춘개수 / len(트윗목록) * 100
print(f"정확도 : {맞춘개수}/{len(트윗목록)*100:.1f}%")

# =======================================================
# 5. 직접 문장 테스트
# =======================================================
내문장들 = [
    "I love this so much!!",
    "This is absolutely terrible",
    "Today was an okay day",
]

# TODO: 내문장들 반복하면서 감성분석기로 예측 후 출력
#       힌트: 감성분석기(문장)[0] 으로 결과 하나 가져오기
#       결과['label'] == 'POSITIVE' 면 긍정
#       결과['score'] 로 확률 출력
for 문장 in 내문장들:
    결과 = 감성분석기(문장)[0]
    print(f"문장 : {문장}")
    print(f"결과 : {'긍정' if 결과['label'] == 'POSITIVE' else '부정'}"
          f"(확률 : {결과['score']:.2f})")
    print('---')