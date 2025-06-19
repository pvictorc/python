
from time import sleep


class Node:
    def __init__(self, val):
        self.parent = None
        self.left = None
        self.right = None
        self.val = val

class BinaryTree:
    def __init__(self, node=None):
        self.__root = node

    def insert(self, val, node=None):
        if self.__root is None:
            self.__root = Node(val)
            return 

        current = self.__root

        if val <= current.val:
            
        else:
            dir = self.__root.right
            self.__insert(dir, val)
            self.__parent = self
        return self.__insert(self.__right, val)
    
    def print_tree(self):
        def _print_tree(node, level=0):
            if node is not None:
                _print_tree(node.right, level + 1)
                print(' ' * 4 * level + '->', node.val)
                _print_tree(node.left, level + 1)

        _print_tree(self.__root)
        
if __name__ == "__main__":
    # Criar uma árvore binária
    tree = BinaryTree()
    
    # Inserir valores na árvore
    values = [7, 3, 9, 1, 5, 8, 10]
    for value in values:
        tree.insert(value)
        # Imprimir a árvore
        tree.print_tree()
        sleep(1)