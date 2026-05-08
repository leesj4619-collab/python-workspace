from playwright.sync_api import sync_playwright
from konlpy.tag import Okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import time

# ===========================
# 1단계 : 크롤링
# ===========================
def 맛집리뷰수집():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # TODO : 검색할 맛집 키워드 리스트 선언 ["강남 맛집", "홍대 맛집", "명동 맛집"]
    키워드목록 = ["강남 맛집", "홍대 맛집", "명동 맛집"]

    결과리스트 = []
    for 키워드 in 키워드목록:
        # TODO : 네이버 검색 URL 로 이동 (query= 에 키워드 넣기) 하던대로 하면 됩니다. 💡
        page.goto(f'https://search.naver.com/search.naver?query={키워드}')
        time.sleep(2)

        # TODO : 페이지 제목 가져오기
        제목 = page.title()

        # TODO : body 태그 전체 텍스트 가져오기
        본문 = page.locator('body').inner_text()

        # TODO : 결과리스트에 [키워드, 제목, 본문 앞 500자] 추가
        결과리스트.append([키워드, 제목, 본문[:500]])
        time.sleep(2)

    # TODO : browser 닫기
    browser.close()
    # TODO : playwright 종료
    p.stop()
    return 결과리스트


# ===========================
# 2단계 : CSV 저장
# ===========================
def csv저장(결과리스트):
    # TODO : 결과리스트로 DataFrame 생성, 컬럼명 = ["키워드", "제목", "본문"]
    df = pd.DataFrame(결과리스트, columns=["키워드", "제목", "본문"])

    # TODO : "맛집크롤링결과.csv" 로 저장, index 없이, 한글깨짐 방지
    df.to_csv("맛집크롤링결과.csv",index=False,encoding='utf-8-sig')

    print("맛집크롤링결과.csv 저장 완료")
    return df


# ===========================
# 3단계 : WordCloud
# ===========================
def 워드클라우드생성(df):
    # TODO : df["본문"] 열 전체를 공백으로 합쳐서 all_text 에 저장
    all_text = ' '.join(df['본문'])

    # TODO : Okt 객체 생성
    okt = Okt()

    # TODO : all_text 에서 명사 추출 후 nouns 에 저장
    nouns = okt.nouns(all_text)

    # TODO : 기존 불용어 + 네이버 UI 노이즈 불용어 추가
    # 기존 : {'것', '수', '등', '곳', '더', '이', '맛집', '네이버'}
    # 추가할 것 : 'NAVER', '검색', '영역', '바로가기', '로그인', '서비스',
    #             '본문', '메뉴', '다음', '이전', '안내', '결과', '지도',
    #             '업체', '광고', '영업', '예약', '주문', '포장', '쿠폰',
    #             '필터', '전체', '등록', '확대', '축소', '이미지', '뉴스',
    #             '블로그', '카페', '쇼핑', '동영상', '지식', '도서',
    #             '플레이스', '플러스', '레이어', '사용자', '링크', '입력기'

    stopwords = {'것', '수', '등', '곳', '더', '이', '맛집', '네이버',
    'NAVER', '검색', '영역', '바로가기', '로그인', '서비스',
    '본문', '메뉴', '다음', '이전', '안내', '결과', '지도',
    '업체', '광고', '영업', '예약', '주문', '포장', '쿠폰',
    '필터', '전체', '등록', '확대', '축소', '이미지', '뉴스',
    '블로그', '카페', '쇼핑', '동영상', '지식', '도서',
    '플레이스', '플러스', '레이어', '사용자', '링크', '입력기'
}

    # TODO : 불용어 제거 + 2글자 이상 필터링 후 filtered 에 저장
    filtered = [w for w in nouns if w not in stopwords and len(w) >= 2]

    # TODO : Counter 로 단어 빈도 계산 후 counts 에 저장
    counts = Counter(filtered)

    # TODO : 상위 10개 키워드 출력
    print(counts.most_common(10))

    # TODO : 한글 폰트 경로 설정
    font_path = 'C:/Windows/Fonts/malgun.ttf'

    # TODO : WordCloud 생성 (font_path, width=800, height=400, background_color='white', colormap='Set2')
    wc = WordCloud(
        font_path=font_path,
        width=800,
        height=400,
        background_color='white',
        colormap='Set2'
    # TODO : 빈도 딕셔너리로 WordCloud 생성
    ).generate_from_frequencies(counts)

    plt.figure(figsize=(12, 6))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')

    # TODO : '맛집_wordcloud.png' 저장, dpi=150
    plt.savefig('맛집_wordcloud.png', dpi=150)
    plt.show()


# ===========================
# 💡💡💡💡💡 실행 💡💡💡💡💡
# ===========================
결과 = 맛집리뷰수집()
df = csv저장(결과)
워드클라우드생성(df)


'''
    # 추가
    'NAVER', '검색', '영역', '바로가기', '로그인', '서비스',
    '본문', '메뉴', '다음', '이전', '안내', '결과', '지도',
    '업체', '광고', '영업', '예약', '주문', '포장', '쿠폰',
    '필터', '전체', '등록', '확대', '축소', '이미지', '뉴스',
    '블로그', '카페', '쇼핑', '동영상', '지식', '도서',
    '플레이스', '플러스', '레이어', '사용자', '링크', '입력기',
    # 1차 결과 보고 추가와 같은 식으로 불용어 제거하기
    '자동', '클립', '어학', '사전', '공유', '숏텐츠', '인플루언서',
    '학술', '정보', '백과', '완성', '장소', '리스트', '실시간',
    '토리', '취미', '대기', '시네마', '마루', '티포',
    # 2차 결과 보고 추가
		'한글', '올리언즈', '플루', '바로', '오프', '대화',
		'화산', '정점', '마을', '산채', '히노', '군자',
		'백화점', '역삼', '신사', '남산타워', '목멱산'


'''