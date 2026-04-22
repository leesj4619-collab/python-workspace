def problem1():
    messages = {
        '철수' : '잘 지내~',
        '훈이' : '바빠 ㅜ',
        '짱구' : '나도 잘 지내'
    }
    for 키이름 in messages.keys():
        print(f"단톡에 존재하는 사람들 : {키이름}")

    # 맨 앞에 오는 결과는 개발자가 최종적으로 보고자하는 형식으로 맞춰서 작성
    # for ~ 사이에 존재하는 변수이름으로 지칭해주는 것이 좋다.
    키결과 = {키이름 for 키이름 in messages.keys() }
    for 대화데이터 in messages.values():
        print(f"단톡에서 대화한 내용들 : {대화데이터}")


    for 키이름, 대화데이터 in messages.items():
        print(f"대화한유저 : {키이름} - {대화데이터}")


#problem1()

def problem2():
    messages = {
        '철수' : '잘 지내~',
        '훈이' : '바빠 ㅜ',
        '짱구' : '나도 잘 지내'
    }
    # 키 결과는 set 집합 형태로 묶여지는 키 이름 데이터들의 모음을 한 번에 조회할 때 사용
    키결과 = {키이름 for 키이름 in messages.keys() }

    # 대화결과들은 set 집합 형태로 묶여지는 대화 데이터들의 모음을 한 번에 조회할 때 사용
    대화결과들 = {대화데이터 for 대화데이터 in messages.values()}

    # : 을 이용해서 키 - 데이터 구분지어 작성
    키_대화_결과들 = {키이름 : 대화데이터 for 키이름, 대화데이터 in messages.items()}
    print(f"단톡 데이터들 :{키_대화_결과들}")
problem2()

