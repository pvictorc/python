import os
from random import randint
from abc import ABC, abstractmethod
import time


class Jogo:

    def __init__(self, tamanho, ursos, peixes, num_rodadas):
        self.__ecossistema = Rio(tamanho, ursos, peixes)
        self.__num_rodadas = num_rodadas

    def run(self):
        print(self.__ecossistema)
        for x in range(self.__num_rodadas):
            self.__ecossistema.rodada()
            print(self.__ecossistema)


class Rio:
    def __init__(self, tamanho_rio: int, qtd_ursos: int, qtd_peixes: int):
        self.__rio = [None] * tamanho_rio
        self.__popular_rio(qtd_ursos, qtd_peixes)

    def __popular_rio(self, qtd_ursos, qtd_peixes):
        self.__posicionar(Urso, qtd_ursos)
        self.__posicionar(Peixe, qtd_peixes)

    def __posicionar(self, classe, qtd: int):
        for _ in range(qtd):
            posicao = randint(0, len(self.__rio) - 1)
            while self.__rio[posicao] is not None:
                posicao = randint(0, len(self.__rio) - 1)
            self.__rio[posicao] = classe()

    def rodada(self):
        for x in range(len(self.__rio)):
            if self.__rio[x] is not None:
                direcao = randint(-1, 1)
                nova_posicao = (x + direcao) % len(self.__rio)
                if nova_posicao != x:
                    self.__colisao(x, nova_posicao)

    def __colisao(self, posicao_atual, nova_posicao):
        animal_atual = self.__rio[posicao_atual]
        animal_novo = self.__rio[nova_posicao]

        acao = animal_atual.interagir(animal_novo)
        if acao == "comer":
            self.__rio[nova_posicao] = animal_atual
            self.__rio[posicao_atual] = None
        elif acao == "morrer":
            self.__rio[posicao_atual] = None
        elif acao == "reproduzir":
            self.__posicionar(type(animal_atual), 1)
        elif acao == "mover":
            self.__rio[nova_posicao] = animal_atual
            self.__rio[posicao_atual] = None


    def __str__(self):
        return "|".join(str(animal) if animal else " " for animal in self.__rio)


class Animal(ABC):
    @abstractmethod
    def interagir(self, outro) -> str:
        """Define a interação entre dois animais. Possíveis ações:
        - "comer": o animal come o outro
        - "morrer": o animal morre
        - "reproduzir": o animal se reproduz"""
        ...


class Urso(Animal):
    def interagir(self, outro):
        if outro:
            if isinstance(outro, Peixe):
                return "comer"
            elif isinstance(outro, Urso):
                return "reproduzir"
        return "mover"

    def __str__(self):
        return "🐻"


class Peixe(Animal):
    def interagir(self, outro):
        if outro:
            if isinstance(outro, Urso):
                return "morrer"
            elif isinstance(outro, Peixe):
                return "reproduzir"
        return "mover"

    def __str__(self):
        return "🐟"


if __name__ == '__main__':
    jogo = Jogo(10, 2, 3, 5)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        jogo.run()
        time.sleep(1)
