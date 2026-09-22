from dataclasses import dataclass
@dataclass(frozen=True)
class Record: id:str; lexical:float; semantic:float
def hybrid(records:list[Record],alpha:float=.35)->list[Record]:
 if not 0<=alpha<=1: raise ValueError("alpha must be between 0 and 1")
 return sorted(records,key=lambda r:alpha*r.lexical+(1-alpha)*r.semantic,reverse=True)
