from hello import hello


def test_hello_returns_greeting():
    assert hello() == "Hello, World!"


def test_hello_returns_string():
    assert isinstance(hello(), str)
