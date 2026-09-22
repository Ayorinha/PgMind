import pytest
from pgmind.retrieval import Record
from pgmind.validation import validate_records, hybrid_score

def test_validation_and_score():
    r=Record("1", .2, .8)
    validate_records([r])
    assert hybrid_score(r, .25) == pytest.approx(.65)

def test_invalid_score():
    with pytest.raises(ValueError): validate_records([Record("1", 1.2, .1)])
