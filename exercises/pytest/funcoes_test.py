from funcoes import *

#casos de teste
def test_divisao_normal():
    assert divisao(10,2)==5

def test_par():
    assert par(2)==True
    assert par(0)==True

def test_par_false():
    assert par(3)==False