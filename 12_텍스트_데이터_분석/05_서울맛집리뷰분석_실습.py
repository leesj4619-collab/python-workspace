from bdb import bar

import pandas as pd
from konlpy.tag import Okt
from pandas.core.interchange.dataframe_protocol import DataFrame
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

# ===========================
# 1단계 : 샘플 데이터 만들기
# ===========================

data = {
    '식당명': ['맛있는 삼겹살', '강남 스시', '홍대 파스타', '명동 칼국수', '이태원 버거'],
    '지역':  ['마포구', '강남구', '마포구', '중구', '용산구'],
    '별점':  [4.5, 4.8, 4.2, 4.0, 4.6],
    '리뷰':  [
        '고기가 신선하고 맛있어요 직원도 친절하고 분위기도 좋아요 재방문 의사 있어요',
        '스시가 정말 신선해요 가격이 비싸지만 맛은 최고 분위기도 고급스러워요',
        '파스타 면이 쫄깃하고 소스가 진해요 양도 많고 가격도 합리적이에요',
        '칼국수 국물이 진하고 맛있어요 줄 서서 먹을 만해요 양도 푸짐해요',
        '패티가 두툼하고 육즙이 풍부해요 빵도 신선하고 감자튀김도 맛있어요'
    ]
}

# TODO : data 를 DataFrame 으로 변환 후 df 에 저장
# 딕셔너리 형태의 데이터로 변환
df = pd.DataFrame(data)

# TODO : df 출력
df = pd.read_csv('서울맛집리뷰분석.csv')

# TODO : df 정보 출력
print(df.info())


# ===========================
# 2단계 : 기본 분석
# ===========================

# TODO : 별점 열 평균 출력
print(df['별점'].mean)

# TODO : 지역 열 값 개수 출력
print(df['지역'].value_counts()) # 지역 열에서 각 값이 몇 번 등장하는지 세서 많은 순으로 출력
# 마포구 2번 등장 강남구가 1번등장 중구 1번 등장 처럼 개수 세기
# TODO : 별점 높은 순으로 정렬 출력
print(df.sort_values('별점',ascending=False)) # 별점 열을 기준으로 DataFrame 전체를 정렬해서 출력
#ascending=True 기본값 오름차순


# ===========================
# 3단계 : 리뷰 WordCloud
# ===========================

# TODO : 리뷰 열 전체를 공백으로 합쳐서 all_reviews 에 저장
all_reviews = ' '.join(df['리뷰'])
# '구분방법'.join() = 리스트의 요소들을 특정 문자열로 이어붙이는 기능
# 단어들 = ['사과', '바나나', '딸기']
# ' '.join(단어들) 사과 바나나 딸기 공백으로 연결
# '!!!'.join(단어들) 사과!!!바나나!!!딸기!!!로 연결
# TODO : Okt 객체 생성
okt = Okt()

# TODO : all_reviews 에서 명사 추출 후 nouns 에 저장
nouns = okt.nouns(all_reviews) # 은 는 이가 처럼 기본 불용어 제거

# nouns에서 제공하지 않고, 개발자가 원하는 결과에 필요하지 않은 불용어를 추가로 작성
stopwords = {'것', '수', '등', '정말', '매우', '너무'}

# TODO : 불용어 제거 + 2글자 이상 필터링 후 filtered 에 저장
filtered = [w for w in nouns if w not in stopwords and len(w) >= 2]
'''
filtered = []
for w in nouns:
    if w not in stopwords and len(w) > 1:
        filtered.append(w)
'''

# TODO : Counter 로 단어 빈도 계산 후 counts 에 저장
counts = Counter(filtered)

# TODO : 자주 나온 키워드 상위 5개 출력
print(counts.most_common(5))

# TODO : 한글 폰트 경로 설정
font_path = 'C:/Windows.Fonts/malgun.ttf'

# TODO : WordCloud 생성 (font_path, width=800, height=400, background_color='white', colormap='Set2')
wc = WordCloud(
    font_path=font_path,
    width=800,
    height=400,
    background_color='white',
    colormap='Set2'
).generate_from_frequencies(counts)

plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')

# TODO : 'review_wordcloud.png' 저장, dpi=150
plt.savefig('review_wordcloud.png', dpi=150)
plt.show()

plt.rcParams['font.family']="Malgun Gothic"
plt.rcParams['axes.unicode_minus']=False

# ===========================
# 4단계 : 별점 막대그래프
# ===========================
plt.figure(figsize=(8, 4))
# TODO : 식당명을 x축, 별점을 y축으로 막대그래프 (color='coral')
plt.bar(df['식당명'],df['별점'],color='coral')
# TODO : y축 범위 3.5 ~ 5.0 으로 설정
plt.ylim(3.5,5.0)
plt.title('식당별 별점')
# TODO : x축 라벨 15도 회전
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('rating_bar.png', dpi=150)
plt.show()