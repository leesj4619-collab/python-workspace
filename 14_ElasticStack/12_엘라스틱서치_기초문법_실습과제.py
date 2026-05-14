from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")
def 실습1():
    # TODO: "my_first_index" 인덱스를 생성하세요
    es.indices.create(index="my_first_index")

    # TODO: "my_first_index" 인덱스가 존재하는지 확인하세요
    es.indices.exists(index="my_first_index")

    # TODO: "my_first_index" 인덱스를 삭제하세요
    es.indices.delete(index="my_first_index")

def 실습2():
    # TODO: "products" 인덱스를 매핑과 함께 생성하세요
    es.indices.create(index="products", body={
        "mappings": {
            "properties": {
                # TODO: name 필드 추가 (형태소 분석 되어야 함)
                'name':{'type':'text'},
                # TODO: brand 필드 추가 (정확히 일치 검색용)
                'brand':{'type':'keyword'},
                # TODO: price 필드 추가
                'price':{'type':'integer'},
                # TODO: rating 필드 추가
                'rating':{'type':'float'},
                # TODO: created_at 필드 추가
                'created_at':{'type':'date'}
            }
        }
    })

def 실습3():
    # TODO: name 필드에서 "나이키 운동화" match 검색 쿼리를 작성하세요
    query = {
        "query": {
            "match": {          # TODO: 어떤 검색 타입?
                "name": "나이키 운동화"   # TODO: 어떤 필드?
            }
        }
    }
    # TODO: brand 필드에서 "Nike" 와 100% 일치하는 term 검색 쿼리를 작성하세요
    query = {
        "query": {
            "term": {          # TODO: 어떤 검색 타입?
                "brand": "Nike"   # TODO: 어떤 필드?
            }
        }
    }
    # TODO: price 필드에서 범위 검색 쿼리를 작성하세요
    query = {
        "query": {
            "range": {
                "price": {        # TODO: 어떤 필드?
                    "gte": 10000,   # TODO: 이상 연산자는?
                    "lte": 50000,   # TODO: 이하 연산자는?
                }
            }
        }
    }

def 실습4():
    # TODO: 아래 bool 쿼리의 빈칸을 채우세요
    query = {
        "query": {
            "bool": {
                "must": [                          # TODO: 반드시 만족해야 하는 조건
                    {"match": {"name": "나이키 운동화"}}
                ],
                "filter": [                          # TODO: 점수 계산 없이 필터링
                    {"range": {"price": {"lte": 50000}}}
                ],
                "must_not": [                          # TODO: 이 조건은 제외
                    {"term": {"brand": "품절"}}
                ]
            }
        }
    }

def 실습5():
    # TODO: 빈칸을 채워서 완성하세요
    query = {
        "query": {"match_all": {}},

        "sort": [
            {"price": {"order": "acs"}}    # TODO: 낮은 순 = ?
        ],

        "from": 0,     # TODO: 1페이지 시작은 몇 번째부터?
        "size": 10,    # TODO: 몇 개씩?

        "highlight": {
            "fields": {
                "name": {}    # TODO: 어떤 필드를 강조?
            }
        }
    }

def 실습6():
    # TODO: brand 기준으로 그룹화해서 상품 수를 구하는 집계 쿼리를 작성하세요
    query = {
        "aggs": {
            "브랜드별_상품수": {
                "term": {"field": "brand"}   # TODO: 집계 타입과 필드는?
            }
        }
    }
    # TODO: rating 필드의 평균을 구하는 집계 쿼리를 작성하세요
    query = {
        "aggs": {
            "평균_평점": {
                "avg": {"field": "rating"}   # TODO: 평균 집계 타입과 필드는?
            }
        }
    }