from pgmind.safety import is_read_only
def test_read_only_gate():
    assert is_read_only("SELECT * FROM docs")
    assert not is_read_only("DELETE FROM docs")