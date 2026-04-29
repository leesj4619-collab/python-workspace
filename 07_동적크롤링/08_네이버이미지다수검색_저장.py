from playwright.sync_api import sync_playwright
import requests  # 이미지 다운로드 용
import os        # 이미지 폴더 만들기 용
import time      # 잠시 대기하며 다음 검색을 위한 모듈

def 다중검색():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # TODO 1: 검색할 키워드 리스트를 만드세요
    # 강아지, 토끼, 늑대 3가지
    키워드목록 = ['강아지','토끼','늑대']

    for 키워드 in 키워드목록:

        # TODO 2: 키워드별 이미지 저장 폴더를 만드세요
        # 예: "다운로드이미지/강아지" 형태로 만들어야 합니다
        # 힌트: os.makedirs("???", exist_ok=True)
        저장폴더 = f'다운로드이미지/{키워드}'
        os.makedirs(저장폴더, exist_ok=True)

        # TODO 3: 네이버 이미지 검색 URL로 이동하세요
        page.goto(f'https://search.naver.com/search.naver?where=image&query={키워드}')
        time.sleep(2)

        # TODO 4: 이미지 목록을 가져오세요
        이미지목록 = page.locator('._fe_image_tab_content_thumbnail_image').all()
        print(f"=== {키워드} : {len(이미지목록)}개 발견")

    # TODO 5: 이미지 5장만 저장하도록 반복문을 완성하세요
    for 번호, 이미지한장씩 in enumerate(이미지목록):
        이미지주소 = 이미지한장씩.get_attribute("src")

        if not 이미지주소:
            continue

        try:
            응답 = requests.get(이미지주소, timeout=5)

            # TODO 6: 파일 이름을 완성하세요
            파일이름 = f"{저장폴더}_{번호+1}.jpg"

            f = open(파일이름, "wb")
            f.write(응답.content)
            f.close()
            print(f"저장완료 : {파일이름}")
        except:
            print(f"{키워드} {번호+1}번 이미지 저장 실패")

    # TODO 7: 다음 키워드 검색 전에 몇 초 대기할까요?
    time.sleep(2)
    browser.close()
    p.stop()
    print("전체 이미지 저장 완료!")

다중검색()