from pgmind.retrieval import Record,hybrid
def test_hybrid_order():
 r=hybrid([Record("sql",1,.2),Record("vec",.2,1)],.5); assert r[0].id=="sql"
