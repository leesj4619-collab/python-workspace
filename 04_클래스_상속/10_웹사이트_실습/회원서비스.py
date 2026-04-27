from db import DB연결

class 회원서비스:
    def __init__(self):
        self.conn = DB연결()

    def 전체조회(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users')
        return cursor.fetchall()
    # fetchall = 전체
    def 회원추가(self,이름,이메일):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO users(name,email) VALUES (%s %s)',(이름, 이메일))
        self.conn.commit()

    def 회원삭제(self, 아이디):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM users WHRER id = %s',(아이디,))
        self.conn.commit()

    def 상세조회(self, id):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        return cursor.fetchone()
    # fetchone = 한명만
