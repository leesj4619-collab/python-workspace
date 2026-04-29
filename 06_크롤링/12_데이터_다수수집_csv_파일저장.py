# 뉴스보다 상품이 더 까다로움
# 06번 뉴스 데이터 다수 수집 기준
# 뉴스를 보고 분석
import time

import requests
from bs4 import BeautifulSoup
import newspaper
import pandas as pd # 이 줄 하나 추가

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
    수집결과 = [] # 수집한 데이터 담을 리스트 준비

    # 순서번호, 데이터 하나씩 , start=1을 작성하지 않으면 i는 0번부터 실행
    for i, 주소 in enumerate(주소목록):
        print(f'\n[{i+1}번째 뉴스 기사]')
        제목,내용,기자,날짜 = 기사수집(주소)
        print('제목 : ', 제목)
        print('제목 : ', 내용)
        print('제목 : ', 기자)
        print('제목 : ', 날짜)
        # 중간에 수집한 데이터를 수집결과 리스트에 append 추가
        수집결과.append(dict(
            제목=제목,
            기자=기자,
            날짜=날짜,
            내용=내용
        ))
        time.sleep(1)
    # 반복 끝나고 최종적으로 데이터를 한 번에 저장
    df = pd.DataFrame(수집결과)
    df.to_csv('naver뉴스수집.csv',index=False,encoding='utf-8-sig')
    print('수집완료')
뉴스20개수집()


