'''
tkinter
- 파이썬으로 기본 GUI를 만들 수 있는 도구
- 파이썬 개발자가 만들어 기본으로 세팅되어 있는 도구
GUI = 마우스 키보드를 활용할 수 있는 프로그램?

좀 더 예쁜 GUI가 필요하다면
PyQt6 CustomTkinter를 사용해도 된다.
'''
import tkinter as tk # tkinter 가져올 것인데 이름이 길기 대문에 tk라는 이름으로 사용

window = tk.Tk()
window.title("내 첫 창")
window.geometry("400x300") # 가로 x 세로 크기

# 텍스트 라벨       화면                             컴퓨터에 설치된 글꼴, 글꼴 사이즈
label = tk.Label(window, text="안녕하세요!", font=(  "D2Coding",         20))
label.pack(pady=10)

# 입력 창
entry = tk.Entry(window, width=30)
entry.pack(pady=5)

def 버튼클릭():
    name = entry.get()
    label.config(tetx=f"안녕, {name}")

btn = tk.Button(window,text="클릭", command=버튼클릭)
btn.pack(pady=5)
# 맨 마지막에 작성
window.mainloop() # 오른쪽 맨 위에 있는 x 버튼을 클릭하기 전까지 프로그램을 계속 실행
