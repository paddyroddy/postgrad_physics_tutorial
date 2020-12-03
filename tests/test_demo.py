import pytest


def test_something(demo_fixture) -> None:
    """
    tests checks that something exists
    """
    assert isinstance(demo_fixture, str)
    assert len(demo_fixture) > 0


@pytest.mark.slow
def test_slow_test(runs) -> None:
    """
    this will only be executed if --runslow test is passed to pytest
    please don't ever right a test like this haha
    """
    old = -1
    for new in range(runs):
        assert new > old
        old = new
