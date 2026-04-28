# h2 id="title_area" div id="contents" span class="byline_s" https://n.news.naver.com/article/277/0005755604?ntype=RANKING
# headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
#     }
import requests
from bs4 import BeautifulSoup
import newspaper
주소 = "https://n.news.naver.com/article/277/0005755604?ntype=RANKING"

def 방법1번():


    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
    }

    웹사이트_응답 = requests.get(주소, headers=headers)
    soup = BeautifulSoup(웹사이트_응답.text,"html.parser")

    #제목
    title = soup.find("h2",id="title_area")
    print('제목 : ', title.text.strip() if title else '못찾음')
    #내용(본문)
    content = soup.find("article",id="dic_area")
    print('내용 : ', content.text.strip() if content else '못찾음')
    #기자
    reporter = soup.find("span",class_="byline_s")
    print('기자 : ', reporter.text.strip() if reporter else '못찾음')

#방법1번()

'''
import newspaper
import nltk
nltk.download('punkt_tab')
nltk 안에 있는 punkt_tab 가져와서 설치하기를 최초 1회 실행하고 나면 매번 작성 X

보통 뉴스들의 형식을 자동으로 nltk 분석해서 제공
newspaper 모듈에서 article기능 안에 punkt_tab 분석해서 제목 내용 등 를 추출하는 기능이 들어있다.
'''
def 방법2번():
    article = newspaper.article(주소, language="ko")
    article.parse()

    print('제목 : ', article.title)
    print('내용 : ', article.text)
    print('기자 : ', article.authors)      # 한국의 기자와 날짜를 자동으로 못 읽는 현상
    print('날짜 : ', article.publish_date) # BeautifulSoup 조합해서 사용

방법2번()


