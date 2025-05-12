from abc import ABC, abstractmethod


class EmptyStack(Exception):
    """Error attempting to access an element from an empty container."""
    ...


class Stack(ABC):

    @abstractmethod
    def push(self, elem):
        """Empilha <elemento>"""
        pass

    @abstractmethod
    def pop(self):
        """Desempilha elemento da pilha"""
        pass

    @abstractmethod
    def top(self):
        """Verifica qual é o elemento que se encontra no topo da pilha, sem removê-lo"""
        pass

    @abstractmethod
    def is_empty(self):
        """Verifica se a pilha está vazia"""
        pass


class ArrayStack(Stack):
    """Implementação de pilha que utiliza uma lista Python para armazenar as informações"""

    def __init__(self):
        """Pilha vazia"""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def __str__(self):
        result = '| '
        for e in self._data:
            result += e.__str__() + ' | '
        return result

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)  # o topo da pilha é a última posição da lista interna

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise EmptyStack('Stack is empty')
        return self._data[-1]  # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
       Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise EmptyStack('Stack is empty')
        return self._data.pop()

    def __contains__(self, item):
        return item in self._data


class Queue(ABC):

    @abstractmethod
    def enqueue(self, elem):
        """Enfileira <elemento>"""
        pass

    @abstractmethod
    def dequeue(self):
        """Desenfileira elemento da pilha"""
        pass

    @abstractmethod
    def first(self):
        """Verifica qual é o elemento que se encontra no início da fila, sem removê-lo"""
        pass

    @abstractmethod
    def is_empty(self):
        """Verifica se a fila está vazia"""
        pass


class EmptyQueue(Exception):
    """Exceção que marca a tentativa de acessar elementos em uma fila vazia"""
    ...


class ArrayQueue(Queue):

    def __init__(self):
        self.__data = list()

    def __len__(self):
        return len(self.__data)

    def __str__(self):
        return str(self.__data)

    def enqueue(self, elem):
        self.__data.append(elem)

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueue("Fila vazia")
        return self.__data.pop(0)

    def first(self):
        if self.is_empty():
            raise EmptyQueue("Fila vazia")
        return self.__data[0]

    def is_empty(self):
        return len(self.__data) == 0


if __name__ == '__main__':
    """pilha = ArrayStack()

    pilha.push(5)
    pilha.push(3)
    print(pilha)
    print(len(pilha))
    print(pilha.is_empty())
    try:
        pilha.pop()
        print(pilha.top())
        print(pilha)
        pilha.pop()
        print(pilha)
        # pilha.pop()
        # pilha.top()
    except EmptyStack:
        print("pilha vazia: não pode retirar elemento!")
    else:
        print("Execução sem erros")
    finally:
        print("fim!")"""

    q = ArrayQueue()
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    print(q.first())
    print(q.dequeue())
    print(q)

    """programa = "public static void main(String[] args)  { System.out.prinln( 1 + 1); }"

    abertura = '([{'
    fecho = ')]}'

    p = ArrayStack()
    for i in programa:
        if i in abertura:
            p.push(i)
        elif i in fecho:
            p.pop()

    if p.is_empty():
        print("sintaxe correta!")
    else:
        print("erro de sintaxe!")"""


