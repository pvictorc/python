

def verifica_recusivo(palavra):
    """
    Função recursiva para verificar se uma palavra é um palíndromo.
    """
    print (f"verifica_recusivo({palavra})")
    if (palavra[0] != palavra[-1]):
        return False
    if len(palavra) <= 1:
        return True
    return verifica_recusivo(palavra[1:-1])

if __name__ == "__main__":
    # Solicitar ao usuário uma palavra
    palavra = input("Digite uma palavra: ")

    # Verificar se a palavra é um palíndromo recursivamente
    print (verifica_recusivo(palavra))
    