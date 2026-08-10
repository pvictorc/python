
def divisao(a,b):
    if b==0:
        raise ValueError("Divisor não pode ser zero")
    return a/b

#casos de teste
def test_divisao_normal():
    assert divisao(10,2)==5
