import pymysql
import requests
import config


def get_conn():
    # TODO: config.MYSQL 정보로 pymysql 연결을 반환하세요.
    # 힌트: pymysql.connect(
    #           host=config.MYSQL["host"],
    #           port=config.MYSQL["port"],
    #           user=___, password=___, database=___,
    #           charset="utf8mb4"
    #       )
    pymysql.connect(
        host=config.MYSQL['host'],
        port=config.MYSQL['port'],
        user='pokeuser', password='pokepassword', database='pokemondb' ,
        charset='utf8mb4'
    )


def create_table():
    print("[1단계] MySQL 테이블 생성")
    conn = get_conn()
    cursor = conn.cursor()

    # TODO: 아래 컬럼을 가진 pokemons 테이블 생성 SQL을 완성하세요.
    # 컬럼:
    #   id            INT PRIMARY KEY
    #   name          VARCHAR(100)
    #   height        INT              -- 포켓몬 키 (단위: dm)
    #   weight        INT              -- 포켓몬 몸무게 (단위: hg)
    #   type1         VARCHAR(50)      -- 첫 번째 타입 (예: fire)
    #   type2         VARCHAR(50)      -- 두 번째 타입 없으면 NULL
    #   base_exp      INT              -- 기본 경험치
    # 힌트: CREATE TABLE IF NOT EXISTS pokemons ( ... )
    sql = """
    CREATE TABLE IF NOT EXISTS pokemons(
        id INT PRIMARY KEY,
        name          VARCHAR(100),
        height        INT,             
        weight        INT,          
        type1         VARCHAR(50),    
        type2         VARCHAR(50),      
        base_exp      INT
    )

    """

    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    print("  완료")


def fetch_from_api():
    print(f"\n[2단계] PokeAPI에서 포켓몬 {config.TOTAL_POKEMON}마리 가져오기")
    pokemons = []

    for i in range(1, config.TOTAL_POKEMON + 1):
        # TODO: f"{config.POKEAPI_URL}/{i}" 로 GET 요청을 보내고
        #       응답 JSON에서 아래 값을 꺼내 딕셔너리로 만드세요.
        #
        # 응답 JSON 구조 참고:
        #   data["id"]               -> 포켓몬 번호
        #   data["name"]             -> 이름
        #   data["height"]           -> 키
        #   data["weight"]           -> 몸무게
        #   data["base_experience"]  -> 기본 경험치
        #   data["types"][0]["type"]["name"]  -> 첫 번째 타입
        #   data["types"][1]["type"]["name"]  -> 두 번째 타입 (없으면 None)
        #
        # 힌트: resp = requests.get(url)
        #        data = resp.json()
        #        type2 = data["types"][1]["type"]["name"] if len(data["types"]) > 1 else None

        pass  # TODO: 이 줄을 지우고 코드를 작성하세요

        if i % 50 == 0:
            print(f"  {i}마리 완료...")

    print(f"  총 {len(pokemons)}마리 수집 완료")
    return pokemons


def insert_pokemons(pokemons: list):
    print(f"\n[3단계] MySQL INSERT ({len(pokemons)}건)")
    conn = get_conn()
    cursor = conn.cursor()

    sql = """
          INSERT IGNORE INTO pokemons (id, name, height, weight, type1, type2, base_exp)
          VALUES (%s, %s, %s, %s, %s, %s, %s) \
          """

    for p in pokemons:
        # TODO: p 딕셔너리에서 값을 꺼내 cursor.execute() 로 저장하세요.
        # 순서: id, name, height, weight, type1, type2, base_exp
        # 힌트: cursor.execute(sql, (p["id"], p["name"], ...))
        pass

    conn.commit()
    cursor.close()
    conn.close()
    print("  완료")


def fetch_all():
    # TODO: pokemons 테이블 전체를 조회해서 딕셔너리 리스트로 반환하세요.
    # 힌트: cursor = conn.cursor(pymysql.cursors.DictCursor)
    #        cursor.execute("SELECT * FROM pokemons")
    #        return cursor.fetchall()
    pass