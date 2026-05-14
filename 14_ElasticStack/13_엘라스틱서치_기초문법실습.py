#엘라스틱서치만의 기능언어들
'''
index = table
document = row
field = column
shard = 분산 조각
node = 서버 1대
cluster = node 들의 집합 / 포도송이처럼 묶인 서버 무리

text    = 형태소 분석 O 문장 긴 글 검색 상품명 상품 설명에서 조회할 때
keyword = 형태소 분석 X 정확히 일치해야할 때  카테고리 / 브랜드
integer = 정수 숫자                        가격 / 재고
float   = 실수(소수점) 숫자                  평점
date    = 날짜                             등록일

역색인   = 단어기준으로 조회 - 어느 문서에 있는지 확인
쿼리 DSL = match match_all term range bool 페이지네이션 코드
DSL(Domain Specific Language) = 엘라스틱 서치에서 검색할 때 JSON 형식의 검색 문법
Domain   : 분야 영역
Specific : 특화된 , 그것만을 위한
Language : 언어
엘라스틱서치만의 기능언어들

create()    - nosql json 형태를 생성 sql table 생성하는 것과 같은 기능
index()     - nosql json 형태 데이터 추가 sql table 내에 데이터 저장하는 것과 같은 기능
get()       - id로 직접 데이터를 꺼내는 방식 색인 필요없이 바로 조회 가능
search()    - 역색인 테이블을 검색하는 거라 색인이 완료되어야 나온다.
            - 바로 search를 이용해서 데이터 추가된 것을 조회하고 싶다면
              search() 전에 refresh() 새로고침 작업을 해주어야 한다.
'''

from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

# 1. 연결 확인
# ping - pong   ping - pong 주고 받으며 연결상태 확인하는 기능
print(es.ping()) # True 답변이 오면 연결 성공

# 2. 인덱스 생성
def 인덱스생성():
    print('========================== 인덱스 생성 시작 ============================')
    es.indices.create(index='pokemon',body={
        'mappings':{                         # mapping.xml 과 비슷하다
            'properties':{                  # create 해주는 table() 와 비슷하다.
                'name':{'type':'text'},       # 형태소 분석 O match 검색용 -> 컬럼이름 : {컬럼속성:컬럼도메인}
                'type':{'type':'keyword'},    # 형태소 분석 X match 검색용 -> 컬럼이름 : {컬럼속성:컬럼도메인}
                'hp':{'type':'integer'},      # 숫자 -> range 검색용
                'desc':{'type':'text'},       # 형태소 분석 O match 검색용 -> 컬럼이름 : {컬럼속성:컬럼도메인}
            }
        }
    })

# 3. 문서 넣기

def 데이터저장():
    print('========================== 데이터 저장 시작 ============================')
    es.index(index="pokemon", id=1, body={"name": "이상해씨", "type": "풀",  "hp": 45, "desc": "등에 씨앗이 있다"})
    es.index(index="pokemon", id=4, body={"name": "파이리",   "type": "불꽃", "hp": 39, "desc": "꼬리 끝 불꽃이 생명력을 나타낸다"})
    es.index(index="pokemon", id=7, body={"name": "꼬부기",   "type": "물",  "hp": 44, "desc": "등껍질로 적의 공격을 막는다"})
    es.index(index="pokemon", id=25,body={"name": "피카츄",   "type": "전기", "hp": 35, "desc": "볼 주머니에서 전기를 방전한다"})
    es.index(index="pokemon", id=6, body={"name": "리자몽",   "type": "불꽃", "hp": 78, "desc": "날개로 날며 강력한 불꽃을 내뿜는다"})
    es.index(index="pokemon", id=9, body={"name": "거북왕",   "type": "물",  "hp": 79, "desc": "대포로 물대포를 쏜다"})
    print('========================== 데이터 저장 완료 ============================')

# 4. 문서 조회(Read)
# id로 한개 조회
# 4번 째에 존재하는 데이터 조회
def 데이터일부조회():
    print('========================== 데이터 하나 조회 시작 ============================')
    result = es.get(index='pokemon',id=4)
    print(result['_source'])
    print('========================== 데이터 하나 조회 완료 ============================')

# 전체 조회
# 4-1. for 문을 이용한 전체 조회 (기초)
def 데이터전체조회():
    print('========================== 데이터 전체 조회 시작 ============================')
    query = { 'query':{
        'match_all':{}
        }
    }
    result = es.search(index='pokemon',body=query)
    print(result)
    print('========================== 데이터 전체 조회 완료 ============================')
    '''
    {'took': 1, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0}, 
    'hits': 
    {'total': {'value': 6, 'relation': 'eq'}, 'max_score': 1.0, 
    'hits': 
    [{'_index': 'pokemon', '_id': '1', '_score': 1.0, '_source': {'name': '이상해씨', 'type': '풀', 'hp': 45, 'desc': '등에 씨앗이 있다'}}, 
    {'_index': 'pokemon', '_id': '4', '_score': 1.0, '_source': {'name': '파이리', 'type': '불꽃', 'hp': 39, 'desc': '꼬리 끝 불꽃이 생명력을 나타낸다'}}, 
    {'_index': 'pokemon', '_id': '7', '_score': 1.0, '_source': {'name': '꼬부기', 'type': '물', 'hp': 44, 'desc': '등껍질로 적의 공격을 막는다'}}, 
    {'_index': 'pokemon', '_id': '25', '_score': 1.0, '_source': {'name': '피카츄', 'type': '전기', 'hp': 35, 'desc': '볼 주머니에서 전기를 방전한다'}}, 
    {'_index': 'pokemon', '_id': '6', '_score': 1.0, '_source': {'name': '리자몽', 'type': '불꽃', 'hp': 78, 'desc': '날개로 날며 강력한 불꽃을 내뿜는다'}}, 
    {'_index': 'pokemon', '_id': '9', '_score': 1.0, '_source': {'name': '거북왕', 'type': '물', 'hp': 79, 'desc': '대포로 물대포를 쏜다'}}]}}

    '''
데이터전체조회()
# 4-2 bulk를 이용하는 전체 조회 (응용)