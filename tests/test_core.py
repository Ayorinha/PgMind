from pgmind.core import *

def test_store(): assert HybridStore([Record("1","Alpha",(1.0,))]).keyword_search("alpha")[0].id=="1"
