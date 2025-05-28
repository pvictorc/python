


if __name__ == "__main__":
    
    def soma_recursiva(n):
        if n == 1:
            return 1
        else:
            return n + soma_recursiva(n-1)
    
    n = 0
    n = int( input("Entre com o número int n: ") )
    print(f"A soma dos números de 1 a {n} é: {soma_recursiva(n)}")
    