from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["library"]          # mydb 말고 library DB 새로 만들기
col_members = db["members"]     # 회원 컬렉션
col_books = db["books"]         # 도서 컬렉션
col_loans = db["loans"]         # 대출 컬렉션

def 회원등록():
    단건등록 = col_members.insert_one({
        'name':"홍길동" ,
        'age':28 ,
        'city':"서울" ,
        'grade':"일반" ,
        'tags':["소설","역사"]
    })
    print(f'단건등록 : {단건등록.inserted_id}')
    복수등록 = col_members.insert_many([
        {'name':"김도서" ,
         'age':35 ,
         'city':"부산" ,
         'grade':"VIP"  ,
         'tags':["IT","자기계발"]},
        {'name':"이열람" ,
         'age':22 ,
         'city':"서울" ,
         'grade':"일반" ,
         'tags':["소설","만화"]},
        {'name':"박반납" ,
         'age':41 ,
         'city':"대구" ,
         'grade':"VIP"  ,
         'tags':["역사","철학"]},
        {'name':"최연체" ,
         'age':19 ,
         'city':"서울" ,
         'grade':["정지"] ,
         'tags':["만화"]}
    ])
    print(f'복수등록 : {복수등록.inserted_ids}')
def 도서등록():
    복수등록 = col_books.insert_many([
        {'title':"파이썬 기초"        ,
         'author':"김코딩"  ,
         'price':25000 ,
         'pub_year':2024 ,
         'stock':5  ,
        'tags':["IT","프로그래밍"]},
        {'title':"세계사 한눈에"      ,
         'author':"이역사"  ,
        'price':18000 ,
        'pub_year':2023 ,
        'stock':3  ,
        'tags':["역사","교양"]},
        {'title':"자바스크립트 완전정복" ,
         'author':"박프론트" ,
         'price':32000 ,
         'pub_year':2025 ,
         'stock':2  ,
        'tags':["IT","프로그래밍"]},
        {'title':"철학의 시작"        ,
         'author':"최철학"  ,
         'price':21000 ,
         'puv_year':2022 ,
         'stock':7  ,
        'tags':["철학","교양"]},
        {'title':"만화로 보는 과학"   ,
         'author':"정만화"  ,
         'price':15000 ,
         'pub_year':2024 ,
         'stock':10,
         'tags':["만화","과학"]}
    ])
    print(f'복수등록 : {복수등록.inserted_ids}')
def 대출등록():
    단건등록 = col_loans.insert_one({
        'member_name':"홍길동" , 'title':"파이썬 기초" , 'is_returned':False , 'comments':[] , 'loan_date':'datetime.now()'
    })
    print(f'단건등록 : {단건등록.inserted_id}')

    복수등록 = col_loans.insert_many([
    {'member_name':"김도서"  ,
     'title':"세계사 한눈에"      ,
     'is_returned':True  ,
     'comments':[{"writer":"사서","text":"정상반납"}],
     'loan_date':'datetime.now()'},
    {'member_name':"이열람"  ,
     'title':"만화로 보는 과학"   ,
     'is_returned':False ,
     'comments':[],
     'loan_date':'datetime.now()'},
    {'member_name':"최연체"  ,
     'title':"철학의 시작"  ,
     'is_returned':False ,
     'comments':[{"writer":"사서","text":"연체중 연락요망"}],
     'loan_date':'datetime.now()'}
])
    print(f'복수등록 : {복수등록.inserted_ids}')

def 회원조회():
    # 1. members 전체 조회
    for doc in col_members.find():
        print(f'전체조회 : {doc}')
    # 2. city 가 "서울" 인 회원만 조회
    doc = col_members.find_one({'city':'서울'})
    print(f'city 가 "서울" 인 회원만 조회 : {doc}')
    # 3. grade 가 "VIP" 인 회원 한 건 조회
    doc = col_members.find_one({'grade':'VIP'})
    print(f'grade 가 "VIP" 인 회원 한 건 조회 : {doc}')
    # 4. age 기준 오름차순 정렬 조회
    for doc in col_members.find().sort('age', 1):
        print(f'age 기준 오름차순 정렬 조회 : {doc}')
    # 5. age 가 20 이상 40 이하인 회원만 조회
    for doc in col_members.find().sort({'age':{'$gte':20,'$lte':40}):
        print(f'age 가 20 이상 40 이하인 회원만 조회 : {doc}')
    # 6. name, age, grade 필드만 보기 (_id 숨기기)
    for doc in col_members.find({},{'_id':0,'name':1,'age':1,'grade':1}):
        print(f'name, age, grade 필드만 보기 (_id 숨기기) : {doc}')
    # 7. city 가 "서울" 인 회원 수 세기
    count = col_members.count_documents({'city':'서울'})
    print(f'city 가 "서울" 인 회원 수 세기 {count}')
    # 8. grade 가 "정지" 인 회원 존재 여부 확인 (True/False)

    # 9. age 낮은 회원 2명만 조회
    for doc in col_members.find().sort('age', 1).limit(2):
        print(f'age 낮은 회원 2명만 조회 : {doc}')
    # 10. tags 에 "IT" 가 포함된 회원만 조회

회원조회()









