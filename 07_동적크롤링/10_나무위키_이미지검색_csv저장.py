from playwright.sync_api import sync_playwright
import requests
import os
import time
import pandas as pd

def 단일이미지():
    p=sync_playwright().start()
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    os.makedirs("나무위키이미지", exist_ok=True)
    검색어 = '너구리'
    page.goto(f"https://namu.wiki/w/{검색어}")

    제목 = page.title()
    본문 = page.locator('body').inner_text()

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
        확장자 = 이미지주소.split(".")[-1].split("?")[0]
        if 확장자 not in ['jpg','jpeg','png','webp','gif']:
            확장자 = 'jpg'
        try:
            응답 = requests.get(이미지주소, timeout=5)
            파일이름 = "나무위키이미지/늑대.jpg"
            f=open(파일이름,"wb")
            f.write(응답.content)
            f.close()
            print(f'저장완료 : {파일이름}')
        except:
            print(f'이미지가 저장 실패.')
        else:
            print('이미지가 URL 없음')

        browser.close()
        p.stop()
        # CSV 저장

        #결과 데이터 가져와서 정렬
        결과데이터 = [[검색어, 제목, 본문[:300], 이미지주소, 파일이름]]
        df = pd.DataFrame(결과데이터, columns=["검색어","제목","본문(300자)","이미지주소","파일이름"])
        df.to_csv('너구리_나무위키',index=False,encoding="utf-8-sig")
        print('저장 완료!')
#단일이미지()

def 다수이미지():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # TODO 1: 이미지를 저장할 폴더를 만드세요
    os.makedirs('나무위키다수이미지2', exist_ok=True)

    # TODO 2: 검색할 키워드 리스트를 만드세요
    키워드목록 = ["사람","킹크랩","딸기"]

    for 키워드 in 키워드목록:

        # TODO 3: 나무위키 해당 키워드 URL로 이동하세요
        page.goto(f"https://namu.wiki/w/{키워드}")
        time.sleep(2)

        # TODO 4: 나무위키 이미지 클래스 선택자로 이미지 태그를 전부 가져오세요
        이미지데이터 = page.locator('.D3JLvbdh').all()

        이미지주소 = None
        for 이미지 in 이미지데이터:

            # TODO 5: alt 속성과 src 속성을 각각 가져오세요
            alt = 이미지.get_attribute('alt') or ""
            주소 = 이미지.get_attribute('src')

            # TODO 6: 실제 이미지 주소만 추출하는 조건을 작성하세요
            if 주소 and "아이콘" not in alt:
                이미지주소 = 주소
                break

        if 이미지주소:

            # TODO 7: 프로토콜이 없는 URL을 올바른 형태로 변환하세요
            if 이미지주소.startswith("//"):
                이미지주소 = "https:" + 이미지주소

            # TODO 8: 이미지 확장자를 URL에서 추출하세요
            확장자 = 이미지주소.split(".")[-1].split("?")[0]

            # TODO 9: 유효하지 않은 확장자일 경우 기본값을 설정하세요
            if 확장자 not in ['jpeg','jpg','webp','gif','png']:
                확장자 = 'jpg'

            try:
                응답 = requests.get(이미지주소, timeout=5)

                # TODO 10: 저장할 파일 이름을 완성하세요 (예: 나무위키이미지/너구리.webp)
                파일이름 = f"나무위키이미지다수이미지/{키워드}.{확장자}"

                f = open(파일이름, "wb")
                f.write(응답.content)
                f.close()
                print(f"저장완료 : {파일이름}")
            except:
                print(f"{키워드} 다운로드 실패")
        else:
            print(f"{키워드} 이미지 없음")

        # TODO 11: 다음 키워드 전환 전 대기시간을 설정하세요
        time.sleep(2)

    # TODO 12: 열었던 순서의 반대로 닫으세요
    browser.close()
    p.stop()
    print("전체 저장 완료")

다수이미지()
