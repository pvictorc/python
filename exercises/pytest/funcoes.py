
def divisao(a,b):
    if b==0:
        raise ValueError("Divisor não pode ser zero")
    return a/b

def par(a: int):
    if a%2 ==0:
        return True
    return False
