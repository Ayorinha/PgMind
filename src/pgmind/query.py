"""Safe query planning primitives independent of a database driver."""
from dataclasses import dataclass

@dataclass(frozen=True)
class QueryPlan:
    sql: str
    parameters: tuple[object, ...]

def parameterized(sql: str, parameters: tuple[object, ...]) -> QueryPlan:
    if not sql.strip():
        raise ValueError("sql must not be empty")
    return QueryPlan(sql=sql, parameters=parameters)
