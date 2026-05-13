from elasticsearch import Elasticsearch, helpers
import config
import db


def get_es():
    # TODO: config.ES_HOST 로 Elasticsearch 에 연결하고 반환하세요.
    # 힌트: return Elasticsearch(___)
    return Elasticsearch("http://localhost:9200")


def create_index(es):
    print("\n[4단계] Elasticsearch 인덱스 생성")

    if es.indices.exists(index=config.ES_INDEX):
        es.indices.delete(index=config.ES_INDEX)

    # TODO: 아래 매핑으로 인덱스를 생성하세요.
    # 필드별 타입:
    #   id        -> integer
    #   name      -> text
    #   height    -> integer
    #   weight    -> integer
    #   type1     -> keyword
    #   type2     -> keyword
    #   base_exp  -> integer
    #
    # 힌트: es.indices.create(index=config.ES_INDEX, body={
    #           "mappings": { "properties": { "name": {"type": "text"}, ... } }
    #       })
    es.indices.create(index=config.ES_INDEX, body={
        'mappings':{'properties': {'name':{'type':'text'},
                                   'id':{'type':'integer'},
                                   'height':{'type':'integer'},
                                   'weight':{'type':'integer'},
                                   'type1':{'type':'keyword'},
                                   'type2':{'type':'keyword'},
                                   'base_exp':{'type':'integer'}}}
    })

    print("완료")


def sync(es):
    print("\n[5단계] MySQL → Elasticsearch 동기화")

    # TODO: db.fetch_all() 로 MySQL 데이터를 가져온 뒤
    #       helpers.bulk() 로 ES 에 한꺼번에 저장하세요.
    #
    # 힌트:
    #   pokemons = db.fetch_all()
    #   def actions():
    #       for p in pokemons:
    #           yield { "_index": config.ES_INDEX, "_id": p["id"], "_source": p }
    #   helpers.bulk(es, actions())
    pokemons=db.fetch_all()
    def action():
        for p in pokemons:
            yield {
                '_index': config.ES_INDEX, '_id': p['id'],'_source': p
            }
        helpers.bulk(es, action())

    print("  동기화 완료")