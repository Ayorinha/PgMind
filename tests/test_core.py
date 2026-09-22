from pgmind.core import HybridStore, Record

def test_hybrid_store():
    s = HybridStore(); s.add(Record("1", "PostgreSQL vector search", (1.0, 0.0)))
    assert s.keyword_search("vector")[0].id == "1"; assert s.dimension() == 2
