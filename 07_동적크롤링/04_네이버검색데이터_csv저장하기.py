from playwright.sync_api import sync_playwright
import time
import csv # pandas를 사용하면 쓸 일이 없다.
import pandas as pd
def 기본CSV버전():
    p = sync_playwright().start() # 크롤링을 시작하겠다!
    웹사이트 = p.chromium.launch(headless=False) # 크롬을 이용해서 검색 시작하겠다. head는 없다
    page = 웹사이트.new_page() # 웹사이트 새 페이지 띄우기 기능
    # 검색어 리스트로 강아지 고양이 토끼 넣고 for 문을 이용해서 강아지 검색 ~ 토끼 검색하기
    검색어목록 = ['강아지','고양이','토끼']

    # 검색된 결과를 담을 목록 세팅
    검색결과리스트=[]
    for 검색어 in 검색어목록:
        page.goto(f"https://search.naver.com/search.naver?query={검색어}")
        제목 = page.title()
        검색결과리스트.append([검색어, 제목])
        time.sleep(2) # 2초 대기후 다음 검색
    # ↓ pandas 도구를 이용하지 않은 구버전 방식 ↓
    f = open('네이버검색결과.csv','w',newline="",encoding="uft-8-sig") # 작성할 파일 생성하며 열기 작성모드 한글깨짐 방짐
    writer = csv.writer(f)
    writer.writerow(["검색어","페이지제목"]) #컬럼이름
    writer.writerows(검색결과리스트) # 각 컬럼에 해당하는 데이터들
    f.close()
    웹사이트.close() # 웹사이트 창 닫기
    p.stop()       # 크롤링 종료

def 판다버전():
    p = sync_playwright().start() # 크롤링을 시작하겠다!
    웹사이트 = p.chromium.launch(headless=False) # 크롬을 이용해서 검색 시작하겠다. head는 없다
    page = 웹사이트.new_page() # 웹사이트 새 페이지 띄우기 기능
    # 검색어 리스트로 강아지 고양이 토끼 넣고 for 문을 이용해서 강아지 검색 ~ 토끼 검색하기
    검색어목록 = ['강아지','고양이','토끼']

    # 검색된 결과를 담을 목록 세팅
    검색결과리스트=[]
    for 검색어 in 검색어목록:
        page.goto(f"https://search.naver.com/search.naver?query={검색어}")
        제목 = page.title()
        검색결과리스트.append([검색어, 제목])
        time.sleep(2) # 2초 대기후 다음 검색
    df = pd.DataFrame(검색결과리스트, columns=["검색어","페이지제목"])
    df.to_csv('네이버검색결과.csv',index=False,encoding="utf-8-sig")
    웹사이트.close() # 웹사이트 창 닫기
    p.stop()       # 크롤링 종료
판다버전()