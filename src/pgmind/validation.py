from .retrieval import Record

def validate_records(records: list[Record]) -> None:
    if not records:
        raise ValueError("records cannot be empty")
    for record in records:
        if not record.id:
            raise ValueError("record id cannot be empty")
        if not 0.0 <= record.lexical <= 1.0 or not 0.0 <= record.semantic <= 1.0:
            raise ValueError("scores must be normalized to [0, 1]")

def hybrid_score(record: Record, alpha: float = .35) -> float:
    if not 0.0 <= alpha <= 1.0: raise ValueError("alpha must be in [0, 1]")
    return alpha * record.lexical + (1-alpha) * record.semantic
