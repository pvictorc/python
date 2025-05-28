"""
Recebe uma string e retorna uma string Invertida.
"""

def inverte_string(str):
    if len(str) == 1:
        return str
    return ( str[-1] + inverte_string(str[:-1]) )

if __name__ == "__main__":

    str = input("Entre com a string: ")
    print(f"A string invertida é: {inverte_string(str)}")