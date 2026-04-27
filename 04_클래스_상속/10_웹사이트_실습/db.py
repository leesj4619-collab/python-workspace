import mysql.connector

def DB연결():
    conn = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='tjee1234',
        database='instagram_clone'
    )
    # 나중에 conn 또한 연결 문제가 생기거나 할 때 대응을 하기 위하여 conn이라는
    # 변수 공간에 db 연결 세팅 담아두는 것
    return conn