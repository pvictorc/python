class Flower:
    def __init__(self, nome :str, qtdPetalas :int, preco :float):
        self.__nome = nome
        self.__qtdPetalas = qtdPetalas
        self.__preco = preco
    
        # Getter for nome
        def get_nome(self):
            return self.__nome
    
        # Setter for nome
        def set_nome(self, nome):
            self.__nome = nome
    
        # Getter for qtdPetalas
        def get_qtdPetalas(self):
            return self.__qtdPetalas
    
        # Setter for qtdPetalas
        def set_qtdPetalas(self, qtdPetalas):
            self.__qtdPetalas = qtdPetalas
    
        # Getter for preco
        def get_preco(self):
            return self.__preco
    
        # Setter for preco
        def set_preco(self, preco):
            self.__preco = preco