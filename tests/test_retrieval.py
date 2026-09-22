from pgmind.retrieval import *
def test_hybrid(): assert hybrid([Record('a',1,0),Record('b',0,1)],.5)[0].id=='a'
