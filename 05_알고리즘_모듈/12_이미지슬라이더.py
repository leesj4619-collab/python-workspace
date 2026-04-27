'''
pip install pillow
이미지 관련 모듈
'''
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps


class 이미지회전앱:
    def __init__(self, root):
        self.root = root
        self.root.title("이미지 회전기")
        self.root.geometry("700x620")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(False, False)

        self.원본이미지 = None
        self.현재각도 = 0
        self.반전여부 = False  # TODO 3-1: 반전 상태 저장용 변수 (True/False)

        self.UI만들기()

    def UI만들기(self):
        tk.Label(self.root, text="이미지 회전기",
                 font=("맑은 고딕", 20, "bold"),
                 bg="#1a1a2e", fg="#e94560").pack(pady=(20, 10))

        self.캔버스 = tk.Canvas(self.root, width=480, height=360,
                             bg="#0f3460", highlightthickness=0)
        self.캔버스.pack(pady=10)
        self.캔버스.create_text(240, 180, text="아래 버튼으로 이미지를 불러오세요.",
                             fill="#a0a0c0", tags="안내")

        btn = {"font": ("맑은 고딕", 11, "bold"), "bg": "#e94560", "fg": "white",
               "relief": "flat", "cursor": "hand2", "padx": 16, "pady": 8, "bd": 0}

        프레임 = tk.Frame(self.root, bg="#1a1a2e")
        프레임.pack(pady=10)

        tk.Button(프레임, text="열기",        command=self.이미지열기,        **btn).grid(row=0, column=0, padx=8)
        tk.Button(프레임, text="왼쪽 90도",   command=lambda: self.회전(-90), **btn).grid(row=0, column=1, padx=8)
        tk.Button(프레임, text="오른쪽 90도", command=lambda: self.회전(90),  **btn).grid(row=0, column=2, padx=8)

        # TODO 1: 아래 주석을 해제하고 command=??? 를 채우세요
        tk.Button(프레임, text="저장", command=self.이미지저장, **btn).grid(row=0, column=3, padx=8)

        # TODO 2: 아래 주석을 해제하고 command=??? 를 채우세요
        tk.Button(프레임, text="초기화", command=self.초기화, **btn).grid(row=1, column=0, padx=8, pady=8)

        # TODO 3: 아래 주석을 해제하고 command=??? 를 채우세요
        tk.Button(프레임, text="↔ 좌우반전", command=self.좌우반전, **btn).grid(row=1, column=1, padx=8, pady=8)

        self.슬라이더 = tk.Scale(self.root, from_=0, to=360, orient="horizontal",
                             length=400, command=self.슬라이더회전,
                             bg="#1a1a2e", fg="white", troughcolor="#0f3460",
                             highlightthickness=0)
        self.슬라이더.pack(pady=10)

        self.각도라벨 = tk.Label(self.root, text="현재 각도: 0°",
                             bg="#1a1a2e", fg="#e94560",
                             font=("맑은 고딕", 11, "bold"))
        self.각도라벨.pack()

    def 이미지열기(self):
        경로 = filedialog.askopenfilename(
            filetypes=[("이미지", "*.png *.jpg *.jpeg *.bmp *.gif")])
        if 경로:
            self.원본이미지 = Image.open(경로)
            self.현재각도 = 0
            self.슬라이더.set(0)
            self.이미지표시(0)

    def 회전(self, 방향):
        if not self.원본이미지: return
        self.현재각도 = (self.현재각도 + 방향) % 360
        self.슬라이더.set(self.현재각도)
        self.이미지표시(self.현재각도)

    def 슬라이더회전(self, 값):
        if not self.원본이미지: return
        self.현재각도 = int(값)
        self.이미지표시(self.현재각도)

    def 이미지표시(self, 각도):
        img = self.원본이미지.rotate(-각도, expand=True)

        # TODO 3-2: 반전여부가 True면 아래 코드를 완성하세요
        # 힌트: ImageOps.mirror(img) 사용
        if self.반전여부:
            img = True

        img.thumbnail((480, 360))
        self.tk이미지 = ImageTk.PhotoImage(img)
        self.캔버스.delete("all")
        self.캔버스.create_image(240, 180, anchor="center", image=self.tk이미지)
        self.각도라벨.config(text=f"현재 각도: {각도}°")

    # TODO 1: 저장 함수를 완성하세요
    def 이미지저장(self):
        if not self.원본이미지: return
        경로 = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])
        if 경로:
            img = self.원본이미지.rotate(-self.현재각도, expand=True)
            # TODO 1-1: img를 경로에 저장하세요
            # 힌트: img.???(경로)
            img.경로

    # TODO 2: 초기화 함수를 완성하세요
    def 초기화(self):
        if not self.원본이미지: return
        # TODO 2-1: 현재각도를 0으로 설정
        # TODO 2-2: 슬라이더를 0으로 → self.슬라이더.set(???)
        # TODO 2-3: 반전여부를 False로 설정
        # TODO 2-4: self.이미지표시(???) 호출

    # TODO 3: 좌우반전 함수를 완성하세요
    def 좌우반전(self):
        if not self.원본이미지: return
        # TODO 3-3: 반전여부를 반대로 뒤집으세요
        self.반전여부 = not self.반전여부
        # 힌트: self.반전여부 = not ???
        # TODO 3-4: self.이미지표시(???) 호출
        self.이미지표시()



root = tk.Tk()
이미지회전앱(root)
root.mainloop()