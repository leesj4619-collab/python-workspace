from elasticsearch import Elasticsearch, NotFoundError


def 실습3교시():
    es = Elasticsearch("http://localhost:9200")

    # 실습용 데이터 세팅
    es.indices.delete(index="books", ignore=[400, 404])
    es.indices.create(index="books", ignore=400)

    books = [
        {"id": 1, "title": "엘라스틱서치 입문",  "author": "홍길동", "price": 30000},
        {"id": 2, "title": "파이썬 기초",        "author": "김철수", "price": 25000},
        {"id": 3, "title": "도커 완전정복",       "author": "이영희", "price": 28000},
        {"id": 4, "title": "리눅스 마스터",       "author": "박민준", "price": 32000},
        {"id": 5, "title": "FastAPI 실전",        "author": "최수진", "price": 27000},
    ]

    for book in books:
        es.index(index="books", id=book["id"], document=book)

    print("데이터 세팅 완료\n")

    # ──────────────────────────────────────────────────────
    # TODO 1. id가 2인 문서를 조회하고 title, author를 출력하세요
    # 힌트: es.get(index=..., id=...)
    # 출력 예시: 제목: 파이썬 기초 | 저자: 김철수


    result = es.get(index="books" , id=2)  # TODO: 여기를 채우세요
    # print("제목:", result["_source"]["???"], "| 저자:", result["_source"]["???"])
    print("제목:", result["_source"]['title'], "| 저자:", result["_source"]['author'])

    # ──────────────────────────────────────────────────────
    # TODO 2. id가 4인 문서를 조회하고 title, price를 출력하세요

    # 출력 예시: 제목: 리눅스 마스터 | 가격: 32000

    result2 = es.get(index='books',id=4)  # TODO: 여기를 채우세요
    # print("제목:", ??? , "| 가격:", ???)
    print('제목:',result2['_source']['title'],"| 가격:",result2['_source']['price'])
# ==========================================================================================#

es = Elasticsearch("http://localhost:9200")

# 실습용 데이터 세팅
es.indices.delete(index="movies", ignore=[400, 404])
es.indices.create(index="movies", ignore=400)

movies = [
    {"id": 1, "title": "어벤져스",     "genre": "액션",   "rating": 8.4, "year": 2012},
    {"id": 2, "title": "기생충",       "genre": "드라마", "rating": 8.6, "year": 2019},
    {"id": 3, "title": "어벤져스 엔드게임", "genre": "액션", "rating": 8.4, "year": 2019},
    {"id": 4, "title": "인터스텔라",   "genre": "SF",     "rating": 8.6, "year": 2014},
    {"id": 5, "title": "버드박스",     "genre": "공포",   "rating": 6.6, "year": 2018},
]

for movie in movies:
    es.index(index="movies", id=movie["id"], document=movie)

print("데이터 세팅 완료\n")

# ──────────────────────────────────────────────────────
# TODO 1. title에 "어벤져스" 가 포함된 문서를 검색하고
#         title과 year를 출력하세요
# 힌트: es.search(index=..., body={"query": {"match": {...}}})
# 출력 예시:
# - 어벤져스 (2012)
# - 어벤져스 엔드게임 (2019)
query1= {'query':{
    'match':{
        'title':'어벤져스'
    }
}
}
result1 = es.search(index='movies',body=query1)  # TODO: 여기를 채우세요
for hit in result1['hits']['hits']:
    src = hit['_source']
    print(f'-{src['title']} ({src['year']})')
# result1 = es.search(???)
# for hit in result1["hits"]["hits"]:
#     print(???)

# ──────────────────────────────────────────────────────
# TODO 2. genre가 "액션" 인 문서를 검색하고
#         title, genre, rating을 출력하세요
# 출력 예시:
# - 어벤져스 | 액션 | 8.4

query2 = {'query':{
            'term':{
                'genre.keyword':'액션'
            }
}}  # TODO: 여기를 채우세요
result2 = es.search(index='movies',body=query2)
for hit in result2['hits']['hits']:
    src = hit['_source']
    print(f"- {src['title']} | {src['genre']} | {src['rating']}")

# ──────────────────────────────────────────────────────
# TODO 3. id=4 문서의 rating을 9.0으로 수정하고
#         수정된 결과를 조회해서 출력하세요
# 힌트: es.update(index=..., id=..., doc={...})
# 출력 예시: 수정 후: {'title': '인터스텔라', 'rating': 9.0, ...}
es.update(index='movies',id=4,doc={'rating':9.0})
update = es.get(index='movies',id=4)
print('\n 수정 후 : ',update['_source'])
# TODO: 여기를 채우세요

# ──────────────────────────────────────────────────────
# TODO 4. id=5 문서를 삭제하고
#         삭제 후 id=5 조회 시 "삭제된 문서입니다" 출력하세요
# 힌트: es.delete() 후 try/except
es.delete(index='movies',id=5)
try:
    es.get(index='movies', id=5)
except NotFoundError:
    print('삭제된 문서입니다.')
# 확인되지 않은 참조 'NotFoundError'
# elasticsearch 에서 문서를 찾을 수 없을 때 표기하기 위한 자체 에러 표기법
# NotFoundError 라는 에러가 발생했을 때 대처를 하기 위해서는
# elasticsearch 에서 제공하는 NotFoundError 표기
# from elasticsearch import Elasticsearch, NotFoundError
# ──────────────────────────────────────────────────────
# TODO: 여기를 채우세요

# ──────────────────────────────────────────────────────
# TODO 5. movies 인덱스 전체를 삭제하세요
#         삭제 후 "movies 인덱스 삭제 완료" 출력
es.indices.delete(index='movies')
print('movies 인덱스 삭제 완료')
# TODO: 여기를 채우세요
