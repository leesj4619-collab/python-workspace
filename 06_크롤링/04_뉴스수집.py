'''
방법 2가지 존재
1: request + BeautifulSoup

2: newspaper3k 뉴스 수집 전용 라이브러리로 수집하는 방법
pip install newspaper3k
'''
import requests
from bs4 import BeautifulSoup


def 방법1번():
    주소 = "https://v.daum.net/v/20260428091147574"

    # 기계가 아니라 사람이 브라우저 접근한 척
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
    }

    웹사이트_응답 = requests.get(주소, headers=headers)
    soup = BeautifulSoup(웹사이트_응답.text, "html.parser")
    # soup = request로 가져온 텍스트를 분해했고, 분해한 데이터가 들어있는 공간
    # 제목
    # 분해한 공간에서 하나의 데이터찾기
    #

    #제목
    title = soup.find("h3", class_="tit_view")
    print("제목 :", title.text if title else "못참음")

    #본문
    content = soup.find("div", class_="article_view")
    print("내용 :", content.text.strip() if content else "못참음")

    #기자 이름 & 이메일
    reporter = soup.find("span", class_="info_reporter")
    print("기자 :", reporter.text.strip() if reporter else "못참음")


# 방법1번()
# class 객체이름:

'''
구버전 newspaper3k 없데이트 중단되었음
pip install newspaper3k
최신 버전
pip install newspaper4k lxml_html_clean
설치된 라이브러리 삭제하는 방법
pip uninstall newspaper3k un을 붙이면 삭제

'''
import newspaper
import nltk
nltk.download('punkt_tab')

def 방법2번():
    주소 = "https://v.daum.net/v/20260428091147574"

    # article = Article 구버전
    article = newspaper.article(주소, language="ko")
    #article.download()
    article.parse()

    print("제목 : ", article.title)
    print("내용 : ", article.text)
    print("기자 : ", article.authors)
    print("날짜 : ", article.publish_date)

방법2번()
