# 네이버 / 다음 / 네이트 외 크롤링 가능한 뉴스 사이트 2곳에서
# 기사 데이터를 다수 수집하여 CSV 파일로 저장하는 실습
#
# 사용 가능한 사이트 예시 (둘 중 하나 선택하거나 둘 다 도전)
# - 연합뉴스  : https://www.yna.co.kr/ranking/popular
# - SBS 뉴스  : https://news.sbs.co.kr/news/programMain.do?prog_cd=R1
# - 한겨레    : https://www.hani.co.kr/arti/RANKING
# - 조선일보  : https://www.chosun.com/ranking/news
#
# 힌트: F12 개발자도구 → 기사 링크 태그 확인 후 select() 작성

import requests
import newspaper
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}


# =============================================
# 첫 번째 뉴스 사이트
# =============================================

def 사이트1_url목록가져오기():
    랭킹주소 = "https://news.sbs.co.kr/news/programMain.do?prog_cd=R1"
    res = requests.get(랭킹주소, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    # TODO: F12 개발자도구로 기사 링크 태그 확인 후 select() 작성
    태그들 = soup.select('news')

    랭크목록 = []
    for 태그 in 태그들[:10]:
        링크 = 태그.get('href')
        if not 링크:
            continue

        # TODO: 상대경로면 절대경로로 변환 (startswith 사용)
        if 링크.startswith("/"):
            링크 = "https://news.sbs.co.kr" + 링크  # TODO: 앞에 사이트 도메인 작성 예) "https://www.yna.co.kr"

        랭크목록.append(링크)

    print(f"사이트1 총 {len(랭크목록)}개 URL 수집 완료!")
    return 랭크목록


def 사이트1_기사수집(url):
    # TODO: newspaper.article() 로 기사 객체 만들기 (language="ko")
    아티클 = newspaper.article(url ,language='ko')
    아티클.parse()

    # TODO: requests.get() 으로 요청 보내기
    res = requests.get(url, headers=headers)

    # TODO: BeautifulSoup 으로 HTML 파싱하기
    soup = BeautifulSoup(res.text ,'html.parser')

    # TODO: F12 개발자도구로 날짜 태그 확인 후 find() 작성
    날짜태그 = soup.find('date')

    제목 = 아티클.title or "못 찾음"
    내용 = 아티클.text[:100] + "..." if 아티클.text else "못 찾음"
    # TODO: 날짜태그에서 텍스트 꺼내기, 없으면 "못 찾음"
    날짜 = 날짜태그.text if 날짜태그.text else "못 찾음"

    return 제목, 내용, 날짜


def 사이트1_뉴스수집():
    url목록 = 사이트1_url목록가져오기()
    수집결과 = []

    for i, url in enumerate(url목록):
        print(f"\n[ 사이트1 - {i + 1}번째 기사 ]")
        try:
            # TODO: 사이트1_기사수집() 호출해서 변수에 저장
            제목, 내용, 날짜 = 사이트1_기사수집(url)

            print("제목 :", 제목)
            print("날짜 :", 날짜)
            print("내용 :", 내용)

            # TODO: 수집결과에 dict() 로 append 하기
            수집결과.append(
                dict(
                    제목=제목,
                    날짜=날짜,
                    내용=내용
            ))

        except Exception as e:
            print(f"오류: {e}")

        time.sleep(2)

    # TODO: pd.DataFrame() 으로 수집결과 변환
    df = pd.DataFrame(수집결과)

    # TODO: to_csv() 로 "사이트1_뉴스수집.csv" 저장
    #       index=False, encoding="utf-8-sig"
    df.to_csv('사이트_뉴스수닙.csv',index=False,encoding='utf-8-sig')
    print("사이트1_뉴스수집.csv 저장 완료!")


# =============================================
# 두 번째 뉴스 사이트
# =============================================

def 사이트2_url목록가져오기():
    # TODO: 선택한 두 번째 뉴스 사이트 랭킹 주소 작성
    랭킹주소 = ""  # TODO: 이 줄을 수정하세요

    # TODO: requests.get() 으로 요청 보내기
    res = None  # TODO: 이 줄을 수정하세요

    # TODO: BeautifulSoup 으로 HTML 파싱하기
    soup = None  # TODO: 이 줄을 수정하세요

    # TODO: F12 개발자도구로 기사 링크 태그 확인 후 select() 작성
    태그들 = []  # TODO: 이 줄을 수정하세요

    랭크목록 = []
    for 태그 in 태그들[:20]:
        # TODO: 태그에서 href 꺼내기
        링크 = None  # TODO: 이 줄을 수정하세요

        if not 링크:
            continue

        # TODO: 상대경로면 절대경로로 변환 (startswith 사용)
        if 링크.startswith("/"):
            링크 = "" + 링크  # TODO: 앞에 사이트 도메인 작성

        랭크목록.append(링크)

    print(f"사이트2 총 {len(랭크목록)}개 URL 수집 완료!")
    return 랭크목록


def 사이트2_기사수집(url):
    # TODO: newspaper.article() 로 기사 객체 만들기 (language="ko")
    아티클 = None  # TODO: 이 줄을 수정하세요
    아티클.parse()

    # TODO: requests.get() 으로 요청 보내기
    res = None  # TODO: 이 줄을 수정하세요

    # TODO: BeautifulSoup 으로 HTML 파싱하기
    soup = None  # TODO: 이 줄을 수정하세요

    # TODO: F12 개발자도구로 날짜 태그 확인 후 find() 작성
    날짜태그 = None  # TODO: 이 줄을 수정하세요

    제목 = 아티클.title or "못 찾음"
    내용 = 아티클.text[:100] + "..." if 아티클.text else "못 찾음"
    # TODO: 날짜태그에서 텍스트 꺼내기, 없으면 "못 찾음"
    날짜 = None  # TODO: 이 줄을 수정하세요

    return 제목, 내용, 날짜


def 사이트2_뉴스수집():
    url목록 = 사이트2_url목록가져오기()
    수집결과 = []

    for i, url in enumerate(url목록):
        print(f"\n[ 사이트2 - {i + 1}번째 기사 ]")
        try:
            # TODO: 사이트2_기사수집() 호출해서 변수에 저장
            제목, 내용, 날짜 = None, None, None  # TODO: 이 줄을 수정하세요

            print("제목 :", 제목)
            print("날짜 :", 날짜)
            print("내용 :", 내용)

            # TODO: 수집결과에 dict() 로 append 하기
            수집결과.append()  # TODO: 이 줄을 수정하세요

        except Exception as e:
            print(f"오류: {e}")

        time.sleep(2)

    # TODO: pd.DataFrame() 으로 수집결과 변환
    df = None  # TODO: 이 줄을 수정하세요

    # TODO: to_csv() 로 "사이트2_뉴스수집.csv" 저장
    #       index=False, encoding="utf-8-sig"
    print("사이트2_뉴스수집.csv 저장 완료!")


# =============================================
# 실행
# =============================================
사이트1_뉴스수집()
#사이트2_뉴스수집()