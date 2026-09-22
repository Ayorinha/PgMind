from dataclasses import dataclass
@dataclass(frozen=True)
class Record:id:str;text:str;embedding:tuple[float,...]
class HybridStore:
 def __init__(self,records=None):self.records=records or []
 def filter(self,predicate):return [r for r in self.records if predicate(r)]
 def keyword_search(self,term):return [r for r in self.records if term.casefold() in r.text.casefold()]
 def dimension(self):return len(self.records[0].embedding) if self.records else 0
