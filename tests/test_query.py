from pgmind.query import parameterized

def test_parameterized_query_keeps_values_separate():
    plan=parameterized("select * from docs where id=%s",(7,))
    assert plan.parameters == (7,)
