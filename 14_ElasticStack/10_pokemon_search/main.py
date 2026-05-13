import db
import es_index
import search


def main():
    print("=" * 50)
    print("  포켓몬 MySQL + Elasticsearch 실습")
    print("=" * 50)

    # ── MySQL 준비 ──────────────────────────────────
    db.create_table()
    pokemons = db.fetch_from_api()
    db.insert_pokemons(pokemons)

    # ── ES 준비 ─────────────────────────────────────
    es = es_index.get_es()
    es_index.create_index(es)
    es_index.sync(es)

    # ── MySQL 검색 ───────────────────────────────────
    print("\n[MySQL] 불 타입 포켓몬")
    results = search.search_mysql_by_type("fire")
    search.print_results(results)

    print("\n[MySQL] 이름에 'saur' 포함된 포켓몬")
    results = search.search_mysql_by_name("saur")
    search.print_results(results)

    # ── ES 검색 ──────────────────────────────────────
    print("\n[ES] 물 타입 포켓몬")
    results = search.search_es_by_type(es, "water")
    search.print_results(results)

    print("\n[ES] 이름에 'char' 포함된 포켓몬")
    results = search.search_es_by_name(es, "char")
    search.print_results(results)

    print("\n  Kibana → http://localhost:5601")
    print("=" * 50)


if __name__ == "__main__":
    main()