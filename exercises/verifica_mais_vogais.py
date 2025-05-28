

"""
Função recursiva para verificar se uma string tem mais vogais do que consoantes.
"""
def verifica_mais_vogais(palavra, vogais, consoantes):
    # condição de parada
    if len(palavra) == 1:
        if palavra[0].isalpha(): 
            if (palavra[0] in "aeiouAEIOU"):
                vogais+=1
            else:
                consoantes+=1
        
        # print (f"Palavra: ({palavra}), vogais: {vogais}, consoantes: {consoantes}, len(palavra): {len(palavra)}")
        return vogais>consoantes
    
    # verifica se é vogal
    if (palavra[0].isalpha()):
        if (palavra[0] in "aeiouAEIOU"):
            return verifica_mais_vogais(palavra[1:], vogais+1, consoantes)
        else:
            return verifica_mais_vogais(palavra[1:], vogais, consoantes+1)
    else:
        return verifica_mais_vogais(palavra[1:], vogais, consoantes)


if __name__ == "__main__":
    # Solicitar ao usuário uma palavra
    palavra = input("Digite uma palavra: ")

    # Verificar se a palavra é um palíndromo recursivamente
    print (verifica_mais_vogais(palavra,0,0))
    