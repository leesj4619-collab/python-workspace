import pandas as pd
import matplotlib.pyplot as plt

# TODO: 한글 깨짐 방지 설정 2줄을 작성하시오. (윈도우 기준)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("국토교통부_외국인_조종사_국적별_현황_20250331.csv", encoding="cp949")

# 항공사 컬럼만 추출 (국적 컬럼 제외)
항공사목록 = df.columns[1:]        # TODO: 국적 제외하고 항공사만 가져오시오.
항공사별_합계 = df[항공사목록].sum()  # TODO: 각 항공사별 전체 합계를 구하시오.

plt.bar(항공사별_합계.index, 항공사별_합계.values)                    # TODO: x축 항공사명, y축 합계로 막대그래프를 그리시오.
plt.title('항공사 총 개수')                        # TODO: 적절한 제목을 작성하시오.
plt.xlabel('항공사명')
plt.ylabel('항공사별 합계')
plt.xticks(rotation=45)             # TODO: X축 글자가 겹치지 않게 기울이시오.
plt.tight_layout()
plt.show()

# 대한항공 조종사가 1명 이상인 국적만 필터링
df_대한항공 = df[df['대한항공'] >= 1]

plt.pie(
    df_대한항공['대한항공'],        # TODO: 대한항공 수치 컬럼
labels=df_대한항공['국적'], # TODO: 국적 컬럼
autopct='%1.1f%%')              # TODO: 퍼센트 소수점 1자리 표시
plt.title('대한항공 비율')
plt.show()

# 각 국적별로 전체 항공사 합계 구하기
df['전체합계'] = df[df.columns[1:]].sum(axis=1)
# TODO: 각 행(국적)의 합계를 구해 '전체합계' 컬럼에 저장하시오.
# axis=1 이면 행 방향(가로) 합계

# 전체합계가 0보다 큰 국적만 필터링
df_합계 = df[df['전체합계'] > 0]

plt.barh(df_합계['국적'], df_합계['전체합계'])  # TODO: y축 국적, x축 전체합계
plt.title("국적별 항공사 전체 외국인 조종사 수")
plt.xlabel('각 항공사 조종사 수')
plt.tight_layout()
plt.show()

plt.hist(df['대한항공'], bins=10)   # TODO: 대한항공 컬럼, 구간 10개
plt.title('막대 그래프')
plt.xlabel("조종사 수")
plt.ylabel("국적 수")
plt.show()

항공사별_합계 = df[df.columns[1:]].sum()

plt.bar(항공사별_합계.index, 항공사별_합계.values)
plt.title("항공사별 외국인 조종사 수")
plt.xticks(rotation=45)
plt.tight_layout()
# save
plt.savefig( "외국인조종사_차트.png")    # TODO: "외국인조종사_차트.png" 로 저장하시오.
plt.show()