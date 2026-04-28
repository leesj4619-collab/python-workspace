# 뉴스보다 상품이 더 까다로움
# h2 id="title_area" div id="contents" span class="byline_s" https://n.news.naver.com/article/277/0005755604?ntype=RANKING
# headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
#     }
import requests
from bs4 import BeautifulSoup
import newspaper
from newspaper import article

주소 = "https://n.news.naver.com/article/277/0005755604?ntype=RANKING"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}
# 네이버 뉴스 랭킹 페이지에서 URL 20개 자동 수집
def 주소목록가져오기():
    랭킹주소: "https://news.naver.com/main/ranking/popularDay.naver"

    res = requests.get(랭킹주소, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    랭크목록 = []
    태그들 = soup.select('a.list_title')

    for 태그 in 태그들[:20]: # 최대 20개까지만 설정 0~19까지
        링크 = 태그.get('href')
        if 링크 and 'article' in 링크 :
            if 링크.startswith('/'):
                링크 = 'https://news.naver.com' + 링크
            랭크목록.append(링크)
    print(f'총 {len(랭크목록)} 개 주소 수집 완료')
    return 랭크목록

def 기사수집(주소):
    article = newspaper.article(주소, language='ko')
    article.parse()

    res = requests.get(주소, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    기자태그 = soup.find('span', class_='byline_s')
    날짜태그 = soup.find('span', class_='media_end_head_info_datestamp_time')

    제목 = article.title
    내용 = article.text[:100] + '...' # 내용이 너무 길면 100자까지만 가져오고 나머진 ...
    기자 = 기자태그.text.strip() if 기자태그 else '못찾음'
    날짜 = 날짜태그.text.strip() if 날짜태그 else '못찾음'


