from src.calculator import add,mul,div,sub

def test_add():
    assert add(1,1) == 2

def test_add():
    assert add(-1,1) == 0

def test_add():
    assert add(1,-1) == 0  

def test_add():
    assert add(-1,-1) == -2     

def test_sub():
    assert sub(1,1) == 0

def test_sub():
    assert sub(-1,-1) == 0    

def test_sub():
    assert sub(1,-1) == 2

def test_sub():
    assert sub(-1,1) == -2         

def test_div():
    assert div(1,1) == 1

def test_div():
    assert div(-1,-1) == 1

def test_div():
    assert div(1,-1) == -1

def test_div():
    assert div(-1,1) == -1

def test_mul():
    assert mul(1,1) == 1    
def test_mul():
    assert mul(-1,-1) == 1
def test_mul():
    assert mul(1,-1) == -1   
def test_mul():
    assert mul(-1,1) == -1            
