class Aluno: 
    def __init__(self, nome, idade, matricula):
        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula

class AlunoPosgraduacao(Aluno):
    def __init__(self, graduacao):
        self.__graduacao = graduacao