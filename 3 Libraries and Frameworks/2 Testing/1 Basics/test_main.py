# pytest has a rich ecosystem of plugins to extend its functionality. Popular plugins include
# pytest-xdist for parallel test execution, pytest-cov for coverage reports, and pytest-mock for mocking.
#
# tests are executed by `pytest`

# TODO test cases

import pytest


@pytest.fixture
def sample_data():
    return {"a": "first", "b": "second", "c": "third"}


def test_1(sample_data):
    assert sample_data["a"] == "first"


@pytest.mark.parametrize("in_put,expected", [(1, 2), (2, 4), (3, 6)])
def test_2(in_put, expected):
    assert in_put * 2 == expected  # This commend will be part of report when test fail


# maker has to be registered (see conftest.py)
@pytest.mark.slow
def this_is_also_test():
    pass
