from src.calculator import add, mul, div, sub

def test_add_positive_numbers():
    assert add(1, 1) == 2

def test_add_positive_negative_numbers():
    assert add(-1, 1) == 0

def test_add_negative_positive_numbers():
    assert add(1, -1) == 0

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_sub_positive_numbers():
    assert sub(1, 1) == 0

def test_sub_negative_numbers():
    assert sub(-1, -1) == 0

def test_sub_positive_negative_numbers():
    assert sub(1, -1) == 2

def test_sub_negative_positive_numbers():
    assert sub(-1, 1) == -2

def test_div_positive_numbers():
    assert div(1, 1) == 1

def test_div_negative_numbers():
    assert div(-1, -1) == 1

def test_div_positive_negative_numbers():
    assert div(1, -1) == -1

def test_div_negative_positive_numbers():
    assert div(-1, 1) == -1

def test_mul_positive_numbers():
    assert mul(1, 1) == 1

def test_mul_negative_numbers():
    assert mul(-1, -1) == 1

def test_mul_positive_negative_numbers():
    assert mul(1, -1) == -1

def test_mul_negative_positive_numbers():
    assert mul(-1, 1) == -1
