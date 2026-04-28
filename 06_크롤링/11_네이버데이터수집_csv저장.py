# 05 번에 위치한 코드를 가져온 후
# 방법 1번은 requests이용한 naver뉴스수집.csv 저장
# 방법 2번은 newspaper이용한 naver뉴스수집.csv 저장
import re

import requests
from bs4 import BeautifulSoup
import newspaper
import pandas as pd

주소 = "https://n.news.naver.com/article/277/0005755604?ntype=RANKING"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}
def 방법1번():


    웹사이트_응답 = requests.get(주소, headers=headers)
    soup = BeautifulSoup(웹사이트_응답.text,"html.parser")

    #제목
    title = soup.find("h2",id="title_area")
    content = soup.find("article",id="dic_area")
    reporter = soup.find("span",class_="byline_s")
    제목데이터 = title.text.strip() if title else '못찾음'
    내용데이터 = content.text.strip() if content else '못찾음'
    기자데이터 = reporter.text.strip() if reporter else '못찾음'

    df = pd.DataFrame(
        dict(
        제목=[제목데이터],
        내용=[내용데이터],
        기자=[기자데이터]
    )
    )
    df.to_csv(
        'naver뉴스수집.csv',
        index=False,
        encoding='utf-8-sig'
    )
    print('저장완료')

#방법1번()

def 방법2번():
    article = newspaper.article(주소, language="ko")
    article.parse()

    제목 = article.title
    내용 = article.text
    이메일데이터 = re.findall(r'[\w.]+@[\w.]+',내용)
    기자 = 이메일데이터[0] if 이메일데이터 else '못 찾음'     # 한국의 기자와 날짜를 자동으로 못 읽는 현상
    날짜 = article.publish_date # BeautifulSoup 조합해서 사용

    df = pd.DataFrame(
        dict(
        제목=[제목],
        내용=[내용],
        기자=[기자]
    )
    )
    df.to_csv(
        'newspaper이용한 naver뉴스수집.csv',
              index=False,
              encoding='utf-8-sig'
    )
    print('저장완료')

#방법2번()


