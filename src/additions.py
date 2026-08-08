# app.py
# This is a test commit
def add(a, b):
    return a + b

def test_add(): # this the the test that should run
    assert add(1, 2) == 3
    assert add(1, -1) == 0