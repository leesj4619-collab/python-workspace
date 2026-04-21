'''
with를 이용해서 my_text.txt 파일을 만들고
한글깨짐없이 글을 작성 후 저장
변수명 = file
'''
def 한줄작성기능():
    with open("my_text.txt","w",encoding="UTF8") as file:
        text = input("입력하세요 : ")

        file.write(text+"\n")

def 여러줄작성기능():
    with open("my_text.txt","w",encoding="UTF8") as file:
        while True:
            글작성 = input("입력하세요(그만하려면 exit 입력) : ")
            if 글작성.lower() == "exit":
                print("저장완료!")
                break
            file.write(글작성+"\n")



def 영차():
    range(1, 6)
    print(range)

영차()
