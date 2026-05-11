from elasticsearch import Elasticsearch

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
