
def par(a: int):
    if a%2 ==0:
        return True
    return False

def test_par():
    assert par(2)==True
    assert par(0)==True

def test_par_false():
    assert par(3)==False