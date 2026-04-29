from playwright.sync_api import sync_playwright
import pandas as pd
import time

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()

검색어목록 = ['강아지','고양이','토끼']
결과리스트 = []

for 검색 in 검색어목록:
    page.goto(f'https://namu.wiki/w/{검색}')
    time.sleep(2)

    제목 = page.title()

    #이미지 태그 찾아서 src 속성 (이미지 URL)갖고오기
    # <img src='이미지경로'>
    이미지목록 = page.locator('img').all() # 이미지 모두~가져오기
    이미지URL = ""
    if 이미지목록: # 이미지가 하나라도 있으면 True / 1 = True, 0 = False
        이미지URL = 이미지목록[0].get_attribute("src") # 두 번째 나 세 번째 이미지는 존재하는지 모르기 때문에 우선 맨 첫번째 이미지 경로만 갖고 오도록하기

    print(f'==={검색}')
    print(f'제목 : {제목}')
    print(f'이미지URL : {이미지URL}')
    print()

    결과리스트.append([검색,제목,이미지URL])
    time.sleep(2)

browser.close()
p.stop()

df = pd.DataFrame(결과리스트, columns=['검색', '제목', '이미지경로'])
df.to_csv('나무위키_이미지데이터.csv',index=False,encoding='utf-8-sig')
print('나무위키_이미지데이터.csv 저장완료!')


