'''
방법 2가지 존재
1: request + BeautifulSoup

2: newspaper3k 뉴스 수집 전용 라이브러리로 수집하는 방법
pip install newspaper3k
'''
import re

import pandas as pd
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
    content = soup.find("div", class_="article_view")
    reporter = soup.find("span", class_="info_reporter")
    제목 = title.text if title else "못참음"
    내용 =content.text.strip() if content else "못참음"
    기자 =reporter.text.strip() if reporter else "못참음"

    # 수집해서 제목과 내용과 기자에 넣어둔 데이터를 csv 파일로 저장
    df = pd.DataFrame({'제목':[제목],'기자':[기자],'내용':[내용]})
    df.to_csv('daum_뉴스.csv',index=False,encoding='utf-8-sig')
    print('저장완료')


#방법1번()

import newspaper
import nltk
nltk.download('punkt_tab')

def 방법2번():
    주소 = "https://v.daum.net/v/20260428091147574"

    article = newspaper.article(주소, language="ko")
    article.parse()

    제목 = article.title
    내용 = article.text
    # 코딩테스트에서 많이 쓰는 문법
    # 정규식을 이용해서 이메일 패턴 찾기 예 : email@email.co.kr
    # 내용에서 이메일 형식을 찾아 0번째에 존재하는 이메일데이터를 기자 공간 추가
    # re.findall 정규식을 이용해서 찾아라!

    # re.findall('정규식문법이나 특정 단어 문자열', '특정 단어나 문자열을 찾을 내용')

    이메일데이터 = re.findall(r'[\w.]+@[\w.]+',내용)
    기자 = 이메일데이터[0] if 이메일데이터 else '못 찾음'
    날짜 =article.publish_date
    # 수집해서 제목과 내용과 기자에 넣어둔 데이터를 csv 파일로 저장
    df = pd.DataFrame({'제목':[제목],'기자':[기자],'내용':[내용]})
    df.to_csv('newspapaer_daum_뉴스.csv',index=False,encoding='utf-8-sig')
    print('저장완료')

방법2번()
