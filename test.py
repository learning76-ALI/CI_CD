from main import say_goodbye, say_hello

def test_say_hello():
    assert say_hello() == "Hello world label"

def test_say_goodbye():
    assert say_goodbye() == "Goodbye world"
