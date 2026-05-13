import config
import db


def search_mysql_by_type(type_name: str):
    # TODO: MySQL에서 type1 또는 type2 가 type_name 인 포켓몬을 조회하세요.
    # 힌트: WHERE type1 = %s OR type2 = %s
    pass


def search_mysql_by_name(keyword: str):
    # TODO: MySQL에서 name에 keyword 가 포함된 포켓몬을 조회하세요.
    # 힌트: WHERE name LIKE %s  /  f"%{keyword}%"
    pass


def search_es_by_type(es, type_name: str):
    # TODO: ES에서 type1 필드가 type_name 인 포켓몬을 검색하세요.
    # 힌트: {"query": {"term": {"type1": type_name}}}
    pass


def search_es_by_name(es, keyword: str):
    # TODO: ES에서 name 필드에 keyword 가 포함된 포켓몬을 검색하세요.
    # 힌트: {"query": {"match": {"name": keyword}}}
    pass


def print_results(hits):
    # 검색 결과 출력 함수 (완성되어 있습니다. 수정하지 마세요.)
    if not hits:
        print("  검색 결과가 없습니다.")
        return
    for p in hits:
        t2 = f"/{p['type2']}" if p.get("type2") else ""
        print(f"  #{p['id']:03d} {p['name']:<12} 타입: {p['type1']}{t2:<10} "
              f"키: {p['height']}dm  몸무게: {p['weight']}hg  경험치: {p['base_exp']}")