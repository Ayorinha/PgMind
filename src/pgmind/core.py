from __future__ import annotations
from dataclasses import dataclass
@dataclass(frozen=True, slots=True)
class Record: id: str; text: str; embedding: tuple[float, ...]
class HybridStore:
    def __init__(self, records: list[Record] | None = None): self.records = list(records or [])
    def add(self, record: Record) -> None:
        if not record.id or not record.text.strip(): raise ValueError("record requires id and text")
        if self.records and len(record.embedding) != self.dimension(): raise ValueError("embedding dimension mismatch")
        self.records.append(record)
    def filter(self, predicate): return [r for r in self.records if predicate(r)]
    def keyword_search(self, term: str) -> list[Record]:
        if not term.strip(): raise ValueError("term must be non-empty")
        return [r for r in self.records if term.casefold() in r.text.casefold()]
    def dimension(self) -> int: return len(self.records[0].embedding) if self.records else 0
