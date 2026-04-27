import tkinter as tk
def 실습과제1():
    창 = tk.Tk()
    창.title("실습과제")
    창.geometry("300x150")

    # 라벨 (안내 텍스트)
    tk.Label(창, text="이름을 입력하세요:").grid(row=0, column=0, padx=5, pady=10)

    # 입력창
    이름입력 = tk.Entry(창, width=15)
    이름입력.grid(row=0, column=1)

    # 결과 라벨
    결과 = tk.Label(창, text="", font=("D2Coding", 13))
    결과.grid(row=2, column=1, pady=10)

    # 인사 함수
    def 인사():
        이름 = 이름입력.get()         # 입력창에서 값 꺼내기
        결과.config(text=f"안녕하세요, {이름}님!")  # 라벨 텍스트 변경

    # 버튼                    command = 기능이름 뒤에 ()를 붙이지 말기
    tk.Button(창, text="인사하기", command=인사).grid(row=1, columnspan=2, pady=5)
    창.mainloop()   # 창 유지

def 실습과제2():
    창 = tk.Tk()
    창.title("BMI 계산기")
    창.geometry("300x200")

    # 키 입력
    tk.Label(창, text="키 (cm):").grid(row=0, column=0, padx=10, pady=5)
    키입력 = tk.Entry(창, width=10)
    키입력.grid(row=0, column=1)

    # 몸무게 입력
    tk.Label(창, text="몸무게 (kg):").grid(row=1, column=0, padx=10, pady=5)
    몸무게입력 = tk.Entry(창, width=10)
    몸무게입력.grid( row=1, column=1)

    # 결과 라벨
    결과 = tk.Label(창, text="결과:", font=("D2Coding", 10))
    결과.grid(row=3, column=2, pady=10)

    # BMI 계산 함수
    def BMI계산():
        try:
            키 = float(키입력.get()) / 100     # cm → m 변환
            몸무게 = float(몸무게입력.get())

            bmi = 몸무게 / (키 ** 2)          # BMI 공식
            bmi = round(bmi, 1)              # 소수점 1자리

            if bmi < 18.5:
                판정 = "저체중"
            elif bmi < 25.0:
                판정 = "정상"
            elif bmi < 35.0:
                판정 = "과체중"
            else:
                판정 = "비만"

            결과.config(text=f"BMI: {bmi} → {판정}")

        except ValueError:
            결과.config(text="숫자만 입력하세요!")

    # 버튼
    tk.Button(창, text="BMI계산하기", command=BMI계산).grid(row=2, columnspan=2, pady=5)
    창.mainloop()

def 실습과제3():
    창 = tk.Tk()
    창.title("메모장")
    창.geometry("400x350")

    # 제목 라벨
    tk.Label(창, text="나만의 메모장", font=("D2Coding", 14)).pack(10)  # ② 위아래 여백 속성

    # Text 위젯 (여러줄 입력)
    메모창 = tk.Text(창, width=45, height=12)    # ③ 여러줄 위젯 이름  ④ 높이 (줄 수)
    메모창.pack()                                  # ⑤ 배치 메서드 (grid 아님!)

    # 버튼 프레임 (버튼 2개를 나란히 놓기 위해)
    버튼묶음 = tk.Frame(창)
    버튼묶음.pack()                                # ⑥ 배치 메서드

    # 저장 함수
    def 저장():
        내용 = 메모창.get("1.0", tk.END)          # ⑦ 시작점 (1행 0열)
        with open("memo.txt", "w") as f:        # ⑧ 파일 쓰기 모드
            f.write(내용)                           # ⑨ 파일에 쓰는 메서드
        상태라벨.config(text="저장 완료!")

    # 불러오기 함수
    def 불러오기():
        try:
            with open("memo.txt", "r") as f:    # ⑩ 파일 읽기 모드
                내용 = f.read()                    # ⑪ 파일 전체 읽는 메서드
            메모창.delete("1.0", tk.END)          # ⑫ 기존 내용 전체 지우기 시작점
            메모창.insert(  "1.0", 내용)             # ⑬ 내용 삽입 메서드
            상태라벨.config(text="불러오기 완료")
        except FileNotFoundError:
            상태라벨.config(text="저장된 파일이 없어요!")

    # 버튼 2개 (버튼묶음 안에 배치)
    tk.Button(버튼묶음, text="저장",    command=저장).pack(side=tk.LEFT,  padx=10)  # ⑭
    tk.Button(버튼묶음, text="불러오기", command=불러오기).pack(side=tk.RIGHT,  padx=10)  # ⑮ ⑯ 오른쪽

    # 상태 표시 라벨
    상태라벨 = tk.Label(창, text="", font=("D2Coding", 11))
    상태라벨.pack()                               # ⑰ 배치

    창.mainloop()                                     # ⑱ 창 유지

실습과제2()