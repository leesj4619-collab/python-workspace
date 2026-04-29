# 공공데이터포털 CSV 파일 데이터 추출 실습
# https://www.data.go.kr 에서 회원가입 없이 다운로드 가능한 CSV 파일 사용
# 예시: 서울시 공공도서관 현황 또는 전국 약국 현황 등 아무 CSV 파일이나 가능

import pandas as pd

# =============================================
# 실습 전 준비
# 1. https://www.data.go.kr 접속
# 2. 검색창에 "서울시 공공도서관" 또는 원하는 키워드 검색
# 3. 파일데이터 탭 → CSV 파일 다운로드 (로그인 불필요)
# 4. 다운로드한 CSV 파일을 이 .py 파일과 같은 폴더에 넣기
# =============================================


def csv_기본정보_확인():
    df = pd.read_csv('서울시 공공도서관 현황정보.csv',encoding="cp949")

    # TODO: df.head() 로 앞 5줄 출력
    print("=== 앞 5줄 ===")
    head = df.head()


    # TODO: df.tail() 로 뒤 5줄 출력
    print("=== 뒤 5줄 ===")
    tail = df.tail()

    # TODO: len(df) 로 전체 행 개수 출력
    print("=== 전체 행 개수 ===")
    전체_행_개수 = len(df)

    # TODO: df.columns 로 열 이름 목록 출력
    print("=== 열 이름 목록 ===")
    열_이름_목록 = df.columns

    # TODO: df.shape 로 전체 행/열 크기 출력
    print("=== 전체 행/열 크기 ===")
    전체_행_열_크기 = df.shape
    print("앞 5줄",head)
    print("뒤 5줄",tail)
    print("전체 행 개수",전체_행_개수)
    print("열 이름 목록",열_이름_목록)
    print("전체 행/열 크기",전체_행_열_크기)


def 특정열_추출_후_csv_저장():
    # TODO: pd.read_csv() 로 CSV 파일 읽어오기
    df = pd.read_csv('서울시 공공도서관 현황정보.csv',encoding='cp949')
    # TODO: df.columns 출력해서 열 이름 먼저 확인하기
    열_이름_확인 = df.columns
    print("열 이름 확인:",열_이름_확인 )  # TODO: 이 줄을 수정하세요

    # TODO: 원하는 열 이름 2~3개를 골라서 아래 리스트에 문자열로 작성
    #       예시: ["도서관명", "자치구", "주소"]
    원하는열 = [
        '도서관명',
        '구명',
        '주소'
    ]

    # TODO: df[원하는열] 로 선택한 열만 추출해서 새로운 df 에 저장
    추출df = df[원하는열]  # TODO: 이 줄을 수정하세요

    # TODO: 추출한 데이터 출력
    print(추출df)

    # TODO: to_csv() 로 "공공데이터_추출결과.csv" 파일로 저장
    #       index=False, encoding="utf-8-sig" 잊지 말기
    df.to_csv('공공데이터_추출결과.csv',index=False,encoding='utf-8-sig')
    print("공공데이터_추출결과.csv 저장 완료")


csv_기본정보_확인()
특정열_추출_후_csv_저장()