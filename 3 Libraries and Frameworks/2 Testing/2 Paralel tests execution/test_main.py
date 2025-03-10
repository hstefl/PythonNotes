
# 
# Execute `pytest -n 2`
# This will start 2 workers in parallel
#

def test_one():
    assert 1 == 1


def test_two():
    assert 1 == 1


def test_three():
    assert 1 == 1


def test_four():
    assert 1 == 1
