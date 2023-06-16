from main import add_function, subtract_function, multiply_function, divide_function

def test_add_function():
    assert add_function(2, 3) == 5

def test_subtract_function():
    assert subtract_function(25, 5) == 20

def test_multiply_function():
    assert multiply_function(4, 5) == 20

def test_divide_function():
    assert divide_function(2, 1) == 2