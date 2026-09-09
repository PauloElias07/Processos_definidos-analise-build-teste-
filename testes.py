from main import soma, sub, multi, divi


def test_soma():
    assert soma(5, 5) == 10


def test_sub():
    assert sub(10, 5) == 5


def test_multi():
    assert multi(2, 5) == 10


def test_divi():
    assert divi(10, 2) == 5
