# 뉴스보다 상품이 더 까다로움
# h2 id="title_area" div id="contents" span class="byline_s" https://n.news.naver.com/article/277/0005755604?ntype=RANKING
# headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
#     }
import time

import requests
from bs4 import BeautifulSoup
import newspaper
from newspaper import article
'''
select vs find_all vs find
soup.select()
- CSS 선택자
- 리스트(여러개)
- 동일한 태그 동일한 id 나 class로 다수 데이터를 가져올 때 사용
- css style에 작성하는 것처럼 .클래스이름 #아이디이름표기
soup.find_all("태그이름", class_="클래스이름", id="아이디이름")
- select와 완전 동일
- css 선택자 스타일 작성이 어려워요.
- 위와 같이 "태그이름", class or id 명칭으로 다수 데이터를 가져올 때 사용

soup.find()
- 하나의 데이터를 가져올 때 사용
- 태그 + 속성 직접 지정

"문자열".startswith("/"):
- ~로 시작하는지 확인하는 기능
- "안녕하세요".startswith("안녕") 안녕하세요는 안녕으로 시작하는게 맞으므로 True
- "안녕하세요".startswith("hi") 안녕하세요는 hi으로 시작하는게 아니므로 False

크롤링을 할 때 웹 사이트 링크는 두 종류로 나뉜다.
# 절대경로 - 주소가 완전히 다 있는 형태
https://n.news.naver.com/article/277/0505005

# 상대 경로 - 앞부분이 생략됨
/article/277/0505005
보통 상대경로는
'''


주소 = "https://n.news.naver.com/article/277/0005755604?ntype=RANKING"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}
# 네이버 뉴스 랭킹 페이지에서 URL 20개 자동 수집
def 주소목록가져오기():
    랭킹주소 = "https://news.naver.com/main/ranking/popularDay.naver"

    res = requests.get(랭킹주소, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    랭크목록 = []
    태그들 = soup.select('a.list_title') # css 선택자 findAll처럼 여러개 갖고올 때 사용

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

    return 제목, 내용, 기자, 날짜

def 뉴스20개수집():
    주소목록 = 주소목록가져오기()

    # 순서번호, 데이터 하나씩 , start=1을 작성하지 않으면 i는 0번부터 실행
    for i, 주소 in enumerate(주소목록):
        print(f'\n[{i+1}번째 뉴스 기사]')
        제목,내용,기자,날짜 = 기사수집(주소)
        print('제목 : ', 제목)
        print('제목 : ', 내용)
        print('제목 : ', 기자)
        print('제목 : ', 날짜)
        time.sleep(1) # 너무 빠르면 로봇인 것을 인지하고 ip 일시 차단된다. 1초씩 쉬면서 데이터 가져오기

    print('수집완료')
뉴스20개수집()


