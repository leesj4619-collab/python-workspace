from playwright.sync_api import sync_playwright
import requests
import os
import time

#from tests.demo_without_stealth_test import browser, page

def 단일검색():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    #이미지 저장할 폴더 만들기
    os.makedirs('다운로드이미지',exist_ok=True)# 폴더가 있으면 스킵 없으면 자동 생성
    # GetMapping("search.naver")
    # public String searchPage(@RequestParam String where, @RequestParam String query = "고양이"){}

    page.goto(f"https://search.naver.com/search.naver?where=image&query=고양이")
    time.sleep(2)

    # 고양이 이미지 데이터 가져오기
    이미지목록 = page.locator('._fe_image_tab_content_thumbnail_image').all()
    print(f"=== 고양이 : {len(이미지목록)}개 발견")

    # for 번호, 이미지한장씩 in enumerate(이미지목록): 전부다 저장
    # for 번호, 이미지한장씩 in enumerate(이미지목록, start=1): start=1을 작성하지 않으면 번호매김 0번부터 시작
    for 번호, 이미지한장씩 in enumerate(이미지목록[:5]): # 5개만 저장
        이미지주소 = 이미지한장씩.get_attribute("src") # 이미지 태그에서 속성 데이터 가져오기. src = 이미지 경로 alt = 이미지 없을 때 보여질 별칭 스크린리더

        if not 이미지주소: #만약 이미지주소가 없는게 사실이라면
            continue # 건너뛰기~
        try:
            # 이미지가 있다! 시작!
            응답 = requests.get(이미지주소, timeout=5)

            #파일로 저장
            # f'문 자 열'은 print 상관없이 문자열을 작성하는 어디든지 변수+글자를 섞어서 작성할 때 어디서든 사용 가능
            파일이름 = f'다운로드이미지/고양이_{번호+1}.jpg'
            f=open(파일이름, 'wb') # wb = 바이너리 쓰기모드 (이미지는 바이너리)
            f.write(응답.content)
            f.close()
            print(f'저장완료 : {파일이름}')
        except:
            print(f'{번호+1}번 이미지 저장 실패')
    time.sleep(2)
    browser.close()
    p.stop()
    print('폴더 이미지 저장 완료')

# 단일검색()
