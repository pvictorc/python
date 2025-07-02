from abc import ABC, abstractmethod


class TreeADT(ABC):

    @abstractmethod
    def insert(self, value):
        """Insere <value> na árvore"""
        pass

    @abstractmethod
    def empty(self):
        """Verifica se a árvore está vazia"""
        pass

    @abstractmethod
    def root(self):
        """Retorna o nó raiz da árvore"""
        pass


class BinaryNode:

    def __init__(self, data=None, parent=None, left=None, right=None):
        self._data = data
        self._parent = parent
        self._left = left
        self._right = right

    def empty(self):
        return not self._data

    def data(self):
        return self._data

    def left_node(self):
        return self._left

    def right_node(self):
        return self._right

    def parent_node(self):
        return self._parent

    def set_parent(self, p):
        self._parent = p

    def set_left_node(self, l):
        self._left = l

    def set_right_node(self, r):
        self._right = r

    def set_data(self, d):
        self._data = d

    def has_left_child(self):
        result = False
        if self.left_node():
            result = True
        return result

    def has_right_child(self):
        result = False
        if self.right_node():
            result = True
        return result

    def __str__(self):
        return self._data.__str__()

    def __eq__(self, other):
        result = False
        if isinstance(other, BinaryNode):
            if self._data == other._data:
                result = True
        return result

    def __ne__(self, other):
        return not self.__eq__(other)

    def __le__(self, other):
        result = False
        if isinstance(other, BinaryNode):
            if self._data <= other._data:
                result = True
        return result

    def __lt__(self, other):
        result = False
        if isinstance(other, BinaryNode):
            if self._data < other._data:
                result = True
        return result


class BinaryTree(TreeADT):

    def __init__(self, data=None, node: BinaryNode = None):
        if node:
            self._root = node
        else:
            self._root = BinaryNode(data)

    def empty(self):
        return not self._root.data()

    def root(self):
        return self._root

    def minimum(self, root):
        result = root
        while result.left_node():
            result = result.left_node()
        return result

    def min_rec(self, root):
        if not root.left_node():
            return root
        else:
            self.min_rec(root.left_node())

    def maximum(self, root):
        result = root
        while result.right_node():
            result = result.right_node()
        return result

    def max_rec(self, root):
        if not root.right_node():
            return root
        else:
            self.max_rec(root.right_node())

    def _insert_node(self, node):
        if self.empty():
            self._root = node
            return self._root
        else:
            return self.__insert_children(self._root, node)

    def insert(self, elem):
        node = BinaryNode(elem)
        if self.empty():
            self._root = node
            return self._root
        else:
            return self.__insert_children(self._root, node)

    def __insert_children(self, root: BinaryNode, node):
        if node <= root:
            if not root.has_left_child(): # não existe nó a esquerda (caso base)
                root.set_left_node(node)
                root.left_node().set_parent(root)
                return root.left_node()
            else:
                return self.__insert_children(root.left_node(), node)  # sub-árvore esquerda
        else:
            if not root.has_right_child():  # não existe nó a direta (caso base)
                root.set_right_node(node)
                root.right_node().set_parent(root)
                return root.right_node()
            else:
                return self.__insert_children(root.right_node(), node)  # sub-árvore direta

    def insert_iterative(self, elem):
        node = BinaryNode(elem)
        if self.empty():
            self._root = node
            return self._root

        current = self._root
        parent = None
        while current:
            parent = current
            if node <= current:
                current = current.left_node()
            else:
                current = current.right_node()

        node.set_parent(parent)
        if node <= parent:
            parent.set_left_node(node)
        else:
            parent.set_right_node(node)
        return node

    def search(self, value: int):
        node = BinaryNode(value)
        if not self.empty():
            return self.__search_children(self._root, node)
        else:
            return False, node

    def __search_children(self, root, node):
        if not root:
            return False, node
        if root == node:
            return True, root
        elif node < root:
            return self.__search_children(root.left_node(), node)
        else:
            return self.__search_children(root.right_node(), node)

    def search_iterative(self, value: int):
        node = BinaryNode(value)
        root = self._root
        while root and root != node:
            if node < root:
                root = root.left_node()
            else:
                root = root.right_node()

        if root:
            return True, root
        else:
            return False, node

    def successor(self, node):
        belongs, n = self.search_iterative(node.data())
        if belongs:
            if n.right_node():
                return self.minimum(n.right_node())
            else:
                return n
        else:
            return None

    def delete(self, value):
        belongs, z = self.search_iterative(value)
        if belongs:
            if not z.has_left_child() or not z.has_right_child():
                y = z
            else:
                y = self.successor(z)

            if y.left_node():
                x = y.left_node()
            else:
                x = y.right_node()

            if x:
                x.set_parent(y.parent_node())

            if not y.parent_node():
                self._root = x
            elif y == y.parent_node().left_node():
                y.parent_node().set_left_node(x)
            else:
                y.parent_node().set_right_node(x)

            if y != z:
                z.set_data(y.data())

            return y
        else:
            return None

    def traversal(self, in_order=True, pre_order=False, post_order=False):
        result = list()
        if in_order:
            in_order_list = list()
            result.append(self.__in_order(self._root, in_order_list))
        else:
            result.append(None)

        if pre_order:
            pre_order_list = list()
            result.append(self.__pre_order(self._root, pre_order_list))
        else:
            result.append(None)

        if post_order:
            post_order_list = list()
            result.append(self.__post_order(self._root, post_order_list))
        else:
            result.append(None)

        return result

    def __in_order(self, root, lista):
        if not root:
            return
        self.__in_order(root._left, lista)
        lista.append(root._data)
        self.__in_order(root._right, lista)
        return lista

    def __pre_order(self, root, lista):
        if not root:
            return
        lista.append(root._data)
        self.__pre_order(root._left, lista)
        self.__pre_order(root._right, lista)
        return lista

    def __post_order(self, root, lista):
        if not root:
            return
        self.__post_order(root._left, lista)
        self.__post_order(root._right, lista)
        lista.append(root._data)
        return lista

    def print_binary_tree(self):
        if self._root:
            print(self.traversal(False, True, False)[1])


class AVLNode(BinaryNode):
    def __init__(self, data=None, parent=None, left=None, right=None):
        super().__init__(data, parent, left, right)
        self._height = 1  # Cada nó começa com altura 1
        # vai servir para calcular o balance factor

    def get_height(self):
        return self._height

    def set_height(self, h):
        self._height = h


class AVLTree(BinaryTree):
    def __init__(self, data=None, node: AVLNode = None):
        if node:
            self._root = node
        else:
            self._root = AVLNode(data)

    def insert(self, val):
        node = AVLNode(val)
        if self.empty():
            self._root = node
        else:
            self._root = self._insert_avl(self._root, node)

    def _insert_avl(self, root, node):
        if not root:
            return node

        if node < root:
            root.set_left_node(self._insert_avl(root.left_node(), node))
            root.left_node().set_parent(root)
        else:
            root.set_right_node(self._insert_avl(root.right_node(), node))
            root.right_node().set_parent(root)

        # Atualizar altura do nó atual
        root.set_height(1 + max(self._get_height(root.left_node()), self._get_height(root.right_node())))

        # Balancear a árvore
        return self._balance_tree(root)

    def _get_height(self, node):
        if not node:
            return 0
        return node.get_height()

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left_node()) - self._get_height(node.right_node())

    def _balance_tree(self, root):
        balance = self._get_balance(root)

        # Caso Esquerda-Esquerda
        if balance > 1 and self._get_balance(root.left_node()) >= 0:
            return self._rotate_right(root)

        # Caso Direita-Direita
        if balance < -1 and self._get_balance(root.right_node()) <= 0:
            return self._rotate_left(root)

        # Caso Esquerda-Direita
        if balance > 1 and self._get_balance(root.left_node()) < 0:
            root.set_left_node(self._rotate_left(root.left_node()))
            return self._rotate_right(root)

        # Caso Direita-Esquerda
        if balance < -1 and self._get_balance(root.right_node()) > 0:
            root.set_right_node(self._rotate_right(root.right_node()))
            return self._rotate_left(root)

        return root

    def _rotate_left(self, z):
        y = z.right_node()
        T2 = y.left_node()

        # Executa a rotação
        y.set_left_node(z)
        z.set_right_node(T2)

        if T2:
            T2.set_parent(z)

        y.set_parent(z.parent_node())
        z.set_parent(y)

        # Atualiza as alturas
        z.set_height(1 + max(self._get_height(z.left_node()), self._get_height(z.right_node())))
        y.set_height(1 + max(self._get_height(y.left_node()), self._get_height(y.right_node())))

        return y

    def _rotate_right(self, z):
        y = z.left_node()
        T3 = y.right_node()

        # Executa a rotação
        y.set_right_node(z)
        z.set_left_node(T3)

        if T3:
            T3.set_parent(z)

        y.set_parent(z.parent_node())
        z.set_parent(y)

        # Atualiza as alturas
        z.set_height(1 + max(self._get_height(z.left_node()), self._get_height(z.right_node())))
        y.set_height(1 + max(self._get_height(y.left_node()), self._get_height(y.right_node())))

        return y

    def delete(self, value):
        if not self.empty():
            self._root = self._delete_node(self._root, value)

    def _delete_node(self, root, value):
        if not root:
            return root

        # Busca o valor a ser deletado
        if value < root.data():
            root.set_left_node(self._delete_node(root.left_node(), value))
        elif value > root.data():
            root.set_right_node(self._delete_node(root.right_node(), value))
        else:
            # Caso o nó tenha um ou nenhum filho
            if not root.left_node() or not root.right_node():
                temp = root.left_node() if root.left_node() else root.right_node()

                if not temp:  # Nenhum filho
                    root = None
                else:  # Um filho
                    root = temp

            else:
                temp = self.minimum(root.right_node())
                root.set_data(temp.data())
                root.set_right_node(self._delete_node(root.right_node(), temp.data()))

        if not root:
            return root

        # Atualiza a altura
        root.set_height(1 + max(self._get_height(root.left_node()), self._get_height(root.right_node())))

        # Balanceia a árvore
        return self._balance_tree(root)


if __name__ == '__main__':
    values = [10, 20, 30, 40, 50, 25]
    binary = BinaryTree()
    avl = AVLTree()
    for value in values:
        binary.insert(value)
        avl.insert(value)

    print(binary.traversal(True, True, True))
    print(avl.traversal(True, True, True))
