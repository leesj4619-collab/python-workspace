from playwright.sync_api import sync_playwright
import requests
import os
import time

def 단일이미지():
    p=sync_playwright().start()
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    os.makedirs("나무위키이미지", exist_ok=True)
    page.goto("https://namu.wiki/w/늑대")
    time.sleep(2)

    이미지데이터=page.locator('.D3JLvbdh').all()
    # 나무위키처럼 img .D3JLvbdh 명칭이 동일할 경우
    이미지주소 = None
    for 이미지 in 이미지데이터:
        alt = 이미지.get_attribute('alt') or ""
        주소 = 이미지.get_attribute("src")

        if 주소 and "아이콘" not in alt:
            이미지주소 = 주소
            break

    if 이미지주소.startswith("//"):
        이미지주소 = "https:" + 이미지주소

    # 확장자 감지하고 그대로 저장
    #       가져온 src를 분리하겠다    맨뒤에 최초로오는 .을 기준으로 .확장자이름만 갖고오겠다.
        확장자 = 이미지주소.split(".")[-1].split("?")[0] # ? 뒤에 존재하는 파라미터 제거
        if 확장자 not in ['jpg','jpeg','png','webp','gif']:
            확장자 = 'jpg' # 확장자가 위 해당하지 않는 확장자라면 jpg기본값으로 세팅
        try:
            응답 = requests.get(이미지주소, timeout=5)
            파일이름 = "나무위키이미지/늑대.jpg"
            f=open(파일이름,"wb")
            f.write(응답.content)
            f.close()
            print(f'저장완료 : {파일이름}')
        except:
            print(f'이미지가 없습니다.')
        browser.close()
        p.stop()
        print('저장 완료!')
단일이미지()

def 다수이미지():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # TODO 1: 이미지를 저장할 폴더를 만드세요
    os.makedirs('나무위키다수이미지', exist_ok=True)

    # TODO 2: 검색할 키워드 리스트를 만드세요
    키워드목록 = ['거미','늑대','나비']

    for 키워드 in 키워드목록:

        # TODO 3: 나무위키 URL로 이동하세요
        page.goto(f"https://namu.wiki/w/{키워드}")
        time.sleep(2)

        # TODO 4: .D3JLvbdh 클래스의 이미지 태그를 전부 가져오세요
        이미지데이터 = page.locator('.D3JLvbdh').all()

        이미지주소 = None
        for 이미지 in 이미지데이터:
            alt = 이미지.get_attribute('alt') or ""
            주소 = 이미지.get_attribute('src')

            # TODO 5: 아이콘을 제외하고 실제 이미지 주소만 추출하세요
            if 주소 and '아이콘' not in alt:
                이미지주소 = 주소 # alt 명칭으로 아이콘을 제외하고 해당 주소만 이미지주소로 넣겠다
                break

        if 이미지주소:
            # TODO 6: //로 시작하면 https: 를 붙여주세요
            if 이미지주소.startswith("//"):
                이미지주소 = 'https:' + 이미지주소

            # TODO 7: 확장자를 감지해서 저장하세요
            확장자 = 이미지주소.split(".")[-1].split("?")[0]
            if 확장자 not in ["jpg","png","jpeg","webp","gif"]:
                확장자 = "jpg"

            try:
                응답 = requests.get(이미지주소, timeout=5)

                # TODO 8: 파일 이름을 완성하세요
                # 예: "나무위키이미지/토끼.webp"
                파일이름 = f"나무위키이미지/{키워드}.{확장자}"

                f = open(파일이름, "wb")
                f.write(응답.content)
                f.close()
                print(f"저장완료 : {파일이름}")
            except:
                print(f"{키워드} 이미지 저장 실패")
        else:
            print(f"{키워드} 이미지 URL 없음")

        # TODO 9: 다음 키워드 검색 전 대기시간을 설정하세요
        time.sleep(4)

        # TODO 10: 열었던 순서 반대로 닫기
    browser.close()
    p.stop()
    print("전체 저장 완료")

#다수이미지()