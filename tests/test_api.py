from vice_squad import hello


def test_hello():
    msg = hello()
    assert msg == "Hello from vice-squad!"
