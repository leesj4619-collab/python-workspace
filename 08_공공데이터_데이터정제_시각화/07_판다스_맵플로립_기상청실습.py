import pandas as pd
import matplotlib.pyplot as plt

# TODO: 한글 깨짐 방지 2줄 작성
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# TODO: csv 파일 불러오기 (인코딩 주의)
df = pd.read_csv('기상청_관광코스별_관광지_상세날씨_조회_지점_정보_20200110..csv',encoding='cp949')

# TODO: 상위 5개 행 출력
print(df.head())

# TODO: 하위 5개 행 출력
print(df.tail())

# TODO: 행과 열의 개수 출력
print(df.shape)

# TODO: 데이터 타입 및 결측치 정보 출력
df.info()

# TODO: 통계 요약 정보 출력
print(df.describe())

# TODO: '관광지명', '테마명', '실내구분', '이동시간' 4개 컬럼만 출력
df_선택 = df[['관광지명', '테마명', '실내구분', '이동시간']]
print(df_선택)

# TODO: 테마명이 '자연/힐링' 인 행만 필터링
df_자연 = df[df['테마명'] == '자연/힐링']
print("자연/힐링 관광지 수 : ", len(df_자연))

# TODO: 이동시간이 10분 이상인 행만 필터링
df_장거리 = df[df['이동시간'] >= 10]
print("이동시간 10분 이상 : ", len(df_장거리))

# TODO: 각 컬럼별 결측치 개수 확인
print(df.isnull().sum())

# TODO: 결측치 행 삭제
print(df.dropna())

# TODO: 결측치 0으로 채우기
print(df.fillna(0))

# TODO: 결측치 숫자 컬럼 평균으로 채우기
print(df.fillna(df.mean(numeric_only=True)))

# TODO: 테마명별 관광지 수 집계
테마별_수 = df['테마명'].value_counts()

# TODO: 막대 그래프 그리기
# x축 = 테마명, y축 = 관광지 수
# 제목 = "테마별 관광지 수"
# x축 글자 45도 기울이기
plt.bar(테마별_수.index, 테마별_수.values)
plt.title('테마별 관광지 수 집계')
plt.xlabel('테마명')
plt.ylabel('관광지 수')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# TODO: 실내구분별 수 집계
실내외_수 = df['실내구분'].value_counts()

# TODO: 파이 차트 그리기
# 퍼센트 소수점 1자리 표시
# 제목 = "실내/실외 관광지 비율"
plt.pie(
    실내외_수.values,
labels=실내외_수.index,
autopct='%1.1f%%'
)
plt.title('실내구분별 수 집계')
plt.show()

# TODO: 이동시간 컬럼 가져오기
df_이동시간 = df['이동시간']

# TODO: 히스토그램 그리기
# 구간 10개, 제목 = "관광지 이동시간 분포"
# x축 = "이동시간 (분)", y축 = "관광지 수"
plt.hist(df_이동시간, bins=10)
plt.title('관광지 이동시간 분포')
plt.xlabel('이동시간 (분)')
plt.ylabel('관광지 수')
plt.show()

# TODO: 경도, 위도 결측치 제거
df_위치 = df[['경도', '위도']].dropna()

# TODO: 산점도 그리기
# x축 = 경도(도), y축 = 위도(도), 투명도 0.3
# 제목 = "관광지 위치 분포"
plt.scatter(df_위치['경도(도)'], df_위치['위도(도)'], alpha=0.3)
plt.title('관광지 위치 분포')
plt.xlabel('경도')
plt.ylabel('위도')
plt.show()

# TODO: '관광지명', '테마명', '실내구분', '이동시간' 컬럼만 추출하여
# "관광지_정제완료.csv" 로 저장
# 인덱스 저장 X, 한글 깨짐 방지
df[['관광지명', '테마명', '실내구분', '이동시간']].savefig("관광지_정제완료.csv", index=False, encoding='utf-8-sig')