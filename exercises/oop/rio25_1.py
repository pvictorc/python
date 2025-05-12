""" Escreva um programa em Python que simula um ecosistema.
Este ecosistema consiste de um rio, modelado como uma lista,
que contém dois tipos de animais: ursos e peixes.

No ecosistema, cada elemento da lista deve ser um objeto do
tipo Urso, Peixe ou None (que indica que a posição do rio
está vazia).

A cada rodada do jogo, baseada em um processo aleatório, cada
animal tenta se mover para uma posição da lista adjacente (a
esquerda ou direita) ou permanece na sua mesma posição.

Se dois animais do mesmo tipo colidirem (urso com urso ou peixe com peixe),
eles permanecem em suas posições originais, mas uma nova instância do
animal deve ser posicionada em um local vazio, aleatoriamente determinado.

Se um Urso e um peixe colidirem, entretanto, o peixe morre."""
from random import randint


class Jogo:

    def __init__(self, tamanho, ursos, peixes, num_rodadas):
        self.__ecossistema = Rio(tamanho, ursos, peixes)
        self.__num_rodadas = num_rodadas

    def run(self):
        for x in range(self.__num_rodadas):
            self.__ecossistema.rodada()

class Rio:
    # para mover animais, ciar o rio,
    def __init__(self, tamanho_rio: int, qtd_ursos: int, qtd_peixes: int):
        self.__rio = [None] * tamanho_rio
        self.__popular_rio(qtd_ursos, qtd_peixes)

    def __popular_rio(self, qtd_ursos, qtd_peixes):
        self.__posicionar(Urso, qtd_ursos)
        self.__posicionar(Peixe, qtd_peixes)

    def __posicionar(self, classe, qtd: int):
        for x in range(qtd):
            posicao = randint(0, len(self.__rio) - 1)
            while self.__rio[posicao] is not None:
                posicao = randint(0, len(self.__rio) - 1)
            self.__rio[posicao] = classe()

    def rodada(self):
        for x in range(len(self.__rio)):
            if self.__rio[x] is not None:
                direcao = randint(-1, 1)
                nova_posicao = x + direcao
                if nova_posicao != x and 0 <= nova_posicao < len(self.__rio):
                    self.__colisao(x, nova_posicao)

    def __colisao(self, posicao_atual, nova_posicao):
        animal_posicao_atual = self.__rio[posicao_atual]
        animal_nova_posicao = self.__rio[nova_posicao]
        if animal_nova_posicao:
            if isinstance(animal_posicao_atual, animal_nova_posicao.__class__):
                self.__posicionar(animal_nova_posicao.__class__, 1)
            elif isinstance(animal_posicao_atual, Urso):
                self.__rio[nova_posicao] = animal_posicao_atual
                self.__rio[posicao_atual] = None
            else:
                self.__rio[posicao_atual] = None

        else:
            self.__rio[nova_posicao] = self.__rio[posicao_atual]
            self.__rio[posicao_atual] = None



class Animal:

    def reproduzir(self, other):
        ...
    def morrer(self):
        ...
    def comer(self):
        ...

class Urso(Animal):
    ...

class Peixe(Animal):
    ...


if __name__ == '__main__':
    jogo = Jogo(10, 2, 3, 5)
    jogo.run()