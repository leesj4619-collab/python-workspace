from playwright.sync_api import sync_playwright
import time
import pandas as pd
import matplotlib.pyplot as plt


def 네이버영화검색결과():
    영화목록 = ["왕과 사는 남자", "범죄도시4", "파묘", "서울의봄", "탑건매버릭"]
    결과리스트 = []  # TODO: 결과 담을 빈 리스트

    # TODO: playwright 시작
    p = sync_playwright().start()
    # TODO: 크롬 열기 (창 보이게)
    browser = p.chromium.launch(headless=False)
    # TODO: 새 페이지 열기
    page = browser.new_page()

    for 영화 in 영화목록:
        # TODO: 네이버에서 영화 검색
        # URL 형태: https://search.naver.com/search.naver?query=왕과 사는 남자+영화
        page.goto(f"https://search.naver.com/search.naver?query={영화}+영화")
        time.sleep(2)

        # TODO: 페이지 제목 가져오기
        제목 = page.title()

        # TODO: body 전체 텍스트 가져오기
        본문 = page.locator('body').inner_text()

        # 평점은 본문에 포함되어 있어서 body에서 찾기
        # 예: 본문에 "실관람객 평점 8.87" 같은 텍스트가 포함됨
        print(f"=== {영화}")
        print(f"제목 : {제목}")
        print(f"본문 앞부분 : {본문[:300]}")  # TODO: 앞 300자만 출력

        # TODO: 결과리스트에 [영화, 제목, 본문 앞 300자] 추가
        결과리스트.append([영화, 제목, 본문[:300]])

        time.sleep(2)
    browser.close()
    p.stop()

    # TODO: 결과리스트로 DataFrame 만들기
    # 컬럼명 = "영화명", "페이지제목", "본문"
    df = pd.DataFrame(결과리스트, columns=["영화명", "페이지제목", "본문"])

    # TODO: "네이버_영화검색결과.csv" 로 저장
    # 인덱스 저장 X, 한글 깨짐 방지
    df.to_csv('네이버_영화검색결과.csv', index=False, encoding='utf-8-sig')
    print("저장 완료")

def 시각화세팅():
    # TODO: 한글 깨짐 방지 2줄
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False

    # TODO: 아래 데이터로 DataFrame 만들어서 "영화평점.csv" 로 저장
    # 컬럼: 영화명, 실관람객평점, 네티즌평점, 관객수(만), 장르
    data = {
        "영화명":       ["왕과 사는 남자", "범죄도시4", "파묘", "서울의봄", "탑건매버릭",
                      "아바타2", "한산", "범죄도시2", "모가디슈", "엘리멘탈"],
        "실관람객평점": [8.87, 8.20, 7.80, 9.30, 8.90,
                   7.60, 8.50, 8.60, 8.70, 7.90],
        "네티즌평점":   [9.18, 7.80, 7.20, 9.10, 8.80,
                    7.90, 8.30, 8.50, 8.60, 8.00],
        "관객수":       [1673, 1150, 1039, 1312, 826,
                      1028, 726, 1269, 361, 490],
        "장르":         ["드라마", "액션", "공포", "드라마", "액션",
                       "SF", "액션", "액션", "드라마", "애니"]
    }

    df = pd.DataFrame(data)
    df.to_csv("영화평점.csv", index=False, encoding='utf-8-sig')
    df = pd.read_csv('영화평점.csv', encoding='utf-8-sig')
    # TODO: 막대 그래프
    # x축 = 영화명, y축 = 실관람객평점
    # 제목 = "영화별 실관람객 평점"
    # x축 글자 45도 기울이기
    plt.bar(df['영화명'], df['실관람객평점'])
    plt.title("영화별 실관람객 평점")
    plt.xlabel('영화명')
    plt.ylabel('실관람객평점')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # TODO: 장르별 수 집계
    장르별_수 = df['장르'].value_counts()

    # TODO: 파이 차트
    # 퍼센트 소수점 1자리, 제목 = "장르별 영화 비율"
    plt.pie(
        장르별_수.values,
    labels=장르별_수.index,
    autopct='%1.1f%%'
    )
    plt.title('장르별 영화 비율')
    plt.show()
    # TODO: 히스토그램
    # 관객수 컬럼, 구간 5개
    # 제목 = "영화 관객수 분포"
    # x축 = "관객수 (만명)", y축 = "영화 수"
    plt.hist(df["관객수 (만명)","영화 수"], bins=5)
    plt.title("영화 관객수 분포")
    plt.xlabel("관객수 (만명)")
    plt.ylabel("영화 수")
    plt.show()

    plt.bar(df["영화명"], df["실관람객평점"])
    plt.title("영화별 실관람객 평점")
    plt.xticks(rotation=45)
    plt.tight_layout()
    # TODO: "영화평점_차트.png" 로 저장
    plt.savefig("영화평점_차트.png")
    plt.show()

시각화세팅()
