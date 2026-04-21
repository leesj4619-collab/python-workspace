def 프로필출력():
    name = '홍길동'
    age = '25'
    height = 175.5
    print(f"이름: {name}")
    print(f"나이: {age}")
    print(f"키: {height}cm")

#프로필출력()

def 나이계산기():
    name = input("이름을 입력하세요: ")
    birth = int(input("태어난 연도를 입력하세요: "))
    age = 26
    print(f"이름을 입력하세요: {name}\n태어난 연도를 입력하세요: {birth}\n{name}님의 나이는 {age}살 입니다!")

#나이계산기()

def 학점계산기():
    score = int(input("점수를 입력하세요: "))
    if score >= 95:
        print("A학점 입니다!")
    elif score >= 85:
        print("B학점 입니다!")
    elif score >= 75:
        print("C학점 입니다!")
    else:
        print("F학점 입니다!")

#학점계산기()

def 합계계산기():
    total = 0
    while True:
        num = input("숫자를 입력하세요 (exit 종료): ")
        if num.lower() == "exit":
            break
        total += int(num)
        print(f"합계: {total}")

#합계계산기()

def 파일저장():
    with open("result.txt", "w", encoding="utf-8") as file:
        while True:
            text = input("입력하세요 (exit 종료): ")
            if text.lower() == 'exit':
                print('저장 완료!')
                break
            file.write(text + "\n")

    def 파일읽기():
        count = 1
        with open("result.txt", "r", encoding="utf-8") as file:
            while True:
                line = file.readline()
                if line == "":
                    break
                print(f"{count}번째 줄: {line.strip()}")
                count += ?

    # 실행
    print("=== 파일 저장 ===")
    파일저장()
    print("\n=== 파일 읽기 ===")
    파일읽기()