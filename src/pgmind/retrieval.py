from dataclasses import dataclass
@dataclass(frozen=True)
class Record: id:str; lexical:float; semantic:float
def hybrid(records,alpha=.35): return sorted(records,key=lambda r:alpha*r.lexical+(1-alpha)*r.semantic,reverse=True)
