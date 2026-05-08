from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['mydb']
col_books = db['books']
col_products = db['products']
col_posts = db['posts']
def insert_문제1():
    한건저장 = col_books.insert_one(
        {'title': "파이썬 완전정복" , 'author': "김코딩" , 'price': 28000 , 'pub_year': 2024}
    )
    여러건저장 = col_books.insert_many([
        {'title':'mongoDB 바이블','author':'이데이터','price':35000 ,'pub_year':2023},
        {'title':'자바스크립트 입문','author':'박프론트','price':22000, 'pub_year':2025},
        {'title':'리눅스 실전', 'author':'최서버','price':19000,'pub_year':2022}
    ]
    )
    print('한건 저장 결과 id : ',한건저장.inserted_id)
    print('여러건 저장 결과 id : ',여러건저장.inserted_ids)

def insert_문제2():

    결과 = col_products.insert_many([
        {'product_name':'무선 마우스', 'price':35000 , 'stock':100 , 'tags':['전자기기','컴퓨터']},
        {'product_name':'맨투맨 티셔츠'   , 'price':45000 , 'stock':50  , 'options':{"color":['검정','흰색','회색'], "size":['S','M','L','XL']}},
        {'product_name':'블루투스 이어폰' , 'price':89000 , 'stock':30  , 'sale_price':71200 , 'discount_rate':20}
    ])
    print("상품 저장 결과 ids : ",결과.inserted_ids)
    '''
    mongoDB 와 같은 sql은 왜 각 행마다 필드가 달라도 저장이 되는가?
    
    관계형 DB는 테이블을 만들 때 구조를 먼저 정의 -> 데이터 제대로 들어오는 것이 가장 중요
    
    mongoDB와 같은 nosql은 각 행마다 독립적으로 존재하며 필요한 필드만 지니면 되며,
                          없는 필드는 그냥 없는 것이지 Null로 채우지 않는다.
                          
                데이터를 제대로 저장하자 xxxx -> 데이터를 빠르게 조회 // 데이터 작업을 할 때 문제 최소화
    '''

def insert_문제3():
    # 게시물 1 - insert_one
    한건결과 = col_posts.insert_one(
        {
        'author':"김개발" ,
        'content':"오늘 MongoDB 공부 시작!" ,
        'likes':0 ,
        'created_at':datetime.now()
        }
    )
    print('게시물1 저장 id : ', 한건결과.inserted_id)
    # 게시물 2 3 등록
    # 데이터 다수 = [] 시작 데이터 한 건 = { }
    여러건결과 = col_posts.insert_many([
    {'author':"이몽고" ,
     'content':"맛집 발견" ,
     'images':["img1.jpg","img2.jpg","img3.jpg"] ,
     'likes':0 ,
     'comments':[],
     'created_at':datetime.now()},
    {'author':"박클라" ,
    'content':"주말 코딩중" ,
    'hashtags':["개발","파이썬","mongoDB"] ,
    'likes':5,
    'comments':[
    {"writer":"최데이", "text":"멋지다!"},
    {"writer":"김개발", "text":"나도 공부해야지"}],
    'created_at':datetime.now()}
    ])
    print('게시물2 게시물3 등록 결과 ids : ',여러건결과.inserted_ids)

def read_문제1_도서관_books_컬렉션_조회():
    doc = col_books.find_one({'author':'김코팅'})
    print('김코딩 한 건 조회 :', doc)

    for doc in col_books.find().sort('pub_year',-1):
        print(f'최신순 정렬 : {doc}')

    for doc in col_books.find().sort('price',1).limit(2):
        print(f'최신순 정렬 : {doc}')

    for doc in col_books.find({}, {'_id':0,'title':1,'price':1}):
        print(f'최신순 정렬 : {doc}')

    count = col_books.count_documents({})
    print(f'전체 책 권수 세기 : {count}')

    for doc in col_books.find_one({'pub_year',-1}):
        print(f'최신순 정렬 : {doc}')


def read_문제2_쇼핑몰_product_조회():
    for doc in col_products.find():
        print(f'전체조회 : {doc}')

    for doc in col_products.find({'price':{'$gte':50000}}):
        print(f'price 가 50000 이상인 상품만 조회 : {doc}')

    for doc in col_products.find().sort('price', -1):
        print(f'price 기준 내림차순 정렬 조회 : {doc}')

    for doc in col_products.find_one({ }, sort=[("price", -1)]):
        print(f'가장 비싼 상품 1개만 조회 : {doc}')

    for doc in col_products.find({},{'_id':0,'product_name':1,'price':1}):
        print(f'product_name, price 필드만 보기 : {doc}')

    count = col_products.count_documents({'stock':{'$lte':50}})
    print(f'stock 이 50 이하인 상품 개수 세기 : {count}')

    for doc in col_products.find().skip(1).limit(2):
        print(f'2번째 상품부터 2개만 조회 {doc}')

    for doc in col_products.find({"discount_rate": {"$exists": True}}):
        print("할인 상품: ", doc)


def read_문제3_SNS_posts_조회():
    for doc in col_posts.find():
        print(f'전체 조회 : {doc}')

    doc = col_posts.find_one({'author':'김개발'})
    print('김개발 한 건 조회 : ',doc)

    for doc in col_posts.find({'likes':{'$gle':1}}):
        print('likes 가 1 이상인 게시물만 조회',doc)

    for doc in col_posts.find().sort('likes', 1):
        print('likes 기준 내림차순 정렬 조회',doc)

    for doc in col_posts.find({},{'_id':0,'author':1,'likes':1,'content':1}):
        print('author, content, likes 필드만 보기',doc)

    for doc in col_posts.find({'hashtags': {'$exists':True}}):
        print('hashtags 필드가 존재하는 게시물만 조회 ',doc)

    for doc in col_posts.find({"comments.writer": "최데이"}):
        print("최데이 댓글을 단 게시물만 조회", doc)

    # 8. 전체 게시물 수 세기
    count = col_posts.count_documents({})
    print("전체 게시무 수 : ", count)


#read_문제2_쇼핑몰_product_조회()
#insert_문제1()
#insert_문제2()
#insert_문제3()