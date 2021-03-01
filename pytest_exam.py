import pytest
def func_float(x,y):
    if x==0:
        return x
    return x/y
def func_int(x):
    return x*x
@pytest.mark.parametrize("test_input,expected", [(-900, True), (900, True), (0.05, False)])
def test_int(test_input, expected):
    assert isinstance(test_input,int) == expected
    try:
        assert func_int("string")
    except TypeError:
        pass
def test_float():
    assert isinstance(func_float(5,8),float) == True
    assert isinstance(func_float(-1,7),float) == True
    try:
        assert isinstance(func_float("string", 1), float)
    except TypeError:
        pass
