"""Query safety validation."""
def is_read_only(sql: str) -> bool:
    normalized=" ".join(sql.strip().lower().split())
    if not normalized: return False
    return normalized.startswith(("select ","with ")) and not any(x in normalized for x in (" insert "," update "," delete "," drop "," alter "," truncate "))