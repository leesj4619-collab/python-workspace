import tkinter as tk
from playwright.sync_api import sync_playwright
import pandas as pd
import requests
import os
import time

# ─────────────────────────────────────
# TODO 1: 이미지 저장 + CSV 저장 핵심 함수
# ─────────────────────────────────────
def 크롤링실행(검색어, 상태라벨):

    # TODO 1-1: 상태라벨 텍스트를 "검색 중..." 으로 바꾸고
    #           창을 즉시 갱신하세요 (힌트: update())
    상태라벨.config(text="검색 중..")
    상태라벨.update()

    # TODO 1-2: 이미지 저장 폴더를 만드세요
    os.makedirs('나무위키이미지', exist_ok=True)

    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # TODO 1-3: 나무위키 검색어 URL 로 이동하세요
    page.goto(f'https://namu.wiki/w/{검색어}')
    time.sleep(2)

    # TODO 1-4: 페이지 제목과 본문 앞 300자를 가져오세요
    제목 = page.title()
    본문 = page.locator('body').inner_text()[:300]

    # TODO 1-5: .D3JLvbdh 선택자로 이미지 목록을 전부 가져오세요
    이미지데이터 = page.locator('.D3JLvbdh').all()

    이미지주소 = None
    for 이미지 in 이미지데이터:
        alt = 이미지.get_attribute('alt') or ""
        주소 = 이미지.get_attribute('src')
        # TODO 1-6: 아이콘 제외 조건 작성
        if 주소 and '아이콘' not in alt:
            이미지주소 = 주소
            break

    browser.close()
    p.stop()

    # ── 이미지 저장 ──────────────────────
    이미지파일경로 = ""
    if 이미지주소:
        # TODO 1-7: //로 시작하면 https: 붙이기
        if 이미지주소.startswith("//"):
            이미지주소 = 'https:' + 이미지주소

        확장자 = 이미지주소.split(".")[-1].split("?")[0]
        if 확장자 not in ["jpg", "jpeg", "png", "webp", "gif"]:
            확장자 = "jpg"

        try:
            응답 = requests.get(이미지주소, timeout=5)
            # TODO 1-8: 파일 이름 완성 (예: 나무위키이미지/너구리.webp)
            이미지파일경로 = f"나무위키이미지/{검색어}.{확장자}"
            with open(이미지파일경로, "wb") as f:
                f.write(응답.content)
        except:
            이미지파일경로 = "이미지 저장 실패"

    # ── CSV 저장 ─────────────────────────
    결과 = [[검색어, 제목, 본문, 이미지주소, 이미지파일경로]]
    df = pd.DataFrame(결과, columns=["검색어", "제목", "본문", "이미지URL", "이미지파일경로"])
    # TODO 1-9: CSV 파일명 "나무위키결과.csv" 로 저장 (한글 깨짐 방지)
    df.to_csv('나무위키결과.csv', index=False, encoding='utf-8-sig')

    # TODO 1-10: 상태라벨을 "완료! CSV + 이미지 저장됨" 으로 바꾸세요
    상태라벨.config(text='완료! CSV + 이미지 저장됨')


# ─────────────────────────────────────
# TODO 2: 버튼 클릭 시 실행할 함수
# ─────────────────────────────────────
def 버튼클릭():
    # TODO 2-1: 입력창에서 검색어를 가져오세요
    검색어 = 입력창.get()

    # TODO 2-2: 검색어가 비어있으면 상태라벨에 "검색어를 입력하세요!" 출력 후 return
    if not 입력창:
        상태라벨.config(text='검색어를 입력하세요!')
        return

    # TODO 2-3: 크롤링실행 함수를 호출하세요 (검색어, 상태라벨 전달)
    크롤링실행(검색어, 상태라벨)


# ─────────────────────────────────────
# TODO 3: tkinter GUI 창 구성
# ─────────────────────────────────────

# TODO 3-1: tkinter 창 만들고 제목 "나무위키 검색기", 크기 "400x200" 로 세팅
창 = tk.Tk()
창.title('나무위키 검색기')
창.geometry('400x200')

# TODO 3-2: 안내 라벨 "검색어를 입력하세요" 추가 (pady=10)
tk.Label(창, text='검색어를 입력하세요.', font=("맑은 고딕", 12)).pack(pady=10)

# TODO 3-3: 입력창 (width=30) 만들고 pack 하세요
입력창 = tk.Entry(창, width=30)
입력창.pack()

# TODO 3-4: "검색 시작" 버튼 추가 (command=버튼클릭, pady=10)
tk.Button(창, text='검색 시작', command=버튼클릭, font=("맑은 고딕", 11)).pack(pady=10)

# TODO 3-5: 상태라벨 (초기 텍스트 "", pady=10) 추가
상태라벨 = tk.Label(창, text="", font=("맑은 고딕", 10))
상태라벨.pack(pady=10)

# TODO 3-6: 창 유지 (mainloop)
창.mainloop()