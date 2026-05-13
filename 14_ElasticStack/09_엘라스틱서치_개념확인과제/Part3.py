# Q1. 역색인(Inverted Index)이 일반 색인보다 검색이 빠른 이유를 한 문장으로 설명해 보세요.
# 답: 일반 색인은 단어에서 문서를 찾아 전체를 스캔하여 단어를 불러오는 반면, 역색인은 문서를 형태소로 저장하여 문서에서 단어에 해당하는 문서를 불러와 빠릅니다.

# Q2. Elasticsearch의 Index / Document / Field 를 RDB 용어로 각각 뭐라고 부르나요?
# 답: Index = Table, Document = Row, Field = Column
#        문서의 집합     저장단위(JSON)      문서의 속성

# Q3. match 검색과 term 검색의 차이는 무엇인가요? (힌트: 형태소 분석)
# 답:  match 형태소 분석을 거쳐서 검색
#      term 형태소 분석 없이 입력한 값과 정확히 일치하는 것만 찾음
#      text 필드는 match keyword 필드는 term 사용

# Q4. docker compose down 과 docker compose stop 의 차이는 무엇인가요?
# 답:  docker compose down 사용하고 있는 docker를 삭제
#      docker compose stop 사용하고 있는 docker를 일시정지