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

    def is_leaf(self):
        return not self.has_left_child() and not self.has_right_child()

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

    def __init__(self, data):
        if not data:
            raise ValueError("Data cannot be None or empty")
        self._root = BinaryNode(data)
        self.__qtd_nodes = 1

    def empty(self):
        return not self._root

    def root(self):
        if self.empty():
            raise ValueError("The tree is empty")
        else:
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

    """def _insert_node(self, node):
        if self.empty():
            self._root = node
            return self._root
        else:
            return self.__insert_children(self._root, node)
"""

    def insert(self, elem):
        node = BinaryNode(elem)
        if self.empty():
            self._root = node
            self.__qtd_nodes += 1
            return self._root
        else:
            return self.__insert_children(self._root, node)

    def __insert_children(self, root: BinaryNode, node):
        if node <= root:
            if not root.has_left_child():  # não existe nó a esquerda (caso base)
                root.set_left_node(node)
                root.left_node().set_parent(root)
                self.__qtd_nodes += 1
                return root.left_node()
            else:
                return self.__insert_children(root.left_node(), node)  # sub-árvore esquerda
        else:
            if not root.has_right_child():  # não existe nó a direta (caso base)
                root.set_right_node(node)
                root.right_node().set_parent(root)
                self.__qtd_nodes += 1
                return root.right_node()
            else:
                return self.__insert_children(root.right_node(), node)  # sub-árvore direta

    def insert_iterative(self, elem):
        node = BinaryNode(elem)
        if self.empty():
            self._root = node
            self.__qtd_nodes += 1
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
        self.__qtd_nodes += 1
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

            self.__qtd_nodes -= 1
            return y
        else:
            return None

    def delete_subtree(self, value):
        belongs, n = self.search(value)
        if belongs:
            l = list()
            stl = self.__in_order(n, l)
            if n.parent_node():
                if n.parent_node().left_node() == n:
                    n.parent_node().set_left_node(None)
                else:
                    n.parent_node().set_right_node(None)
            else:
                self._root = None
            self.__qtd_nodes = self.__qtd_nodes - len(stl)

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
        lista.append(root)
        self.__in_order(root._right, lista)
        return lista

    def __pre_order(self, root, lista):
        if not root:
            return
        lista.append(root)
        self.__pre_order(root._left, lista)
        self.__pre_order(root._right, lista)
        return lista

    def __post_order(self, root, lista):
        if not root:
            return
        self.__post_order(root._left, lista)
        self.__post_order(root._right, lista)
        lista.append(root)
        return lista

    def print_binary_tree(self):
        if self._root:
            print(self.traversal(False, True, False)[1])

    def __len__(self):
        # return len(self.traversal()[0])
        return self.__qtd_nodes

    def number_of_left_leaves(self):
        if self.empty():
            return 0
        nodes = self.traversal()
        left_leaves = [node for node in nodes[0] if node.has_left_child() and node.left_node().is_leaf()]
        return len(left_leaves)

    def number_of_left_leaves_2(self):
        if self.empty():
            return 0
        return self.__number_of_left_leaves(self._root)

    def __number_of_left_leaves(self, node):
        if not node:
            return 0

        count = 0
        if node.has_left_child() and node.left_node().is_leaf():
            count += 1

        count += self.__number_of_left_leaves(node.left_node())
        count += self.__number_of_left_leaves(node.right_node())

        return count


class ExpressionTree:

    def __init__(self, expression):
        self.__root = None
        self.__expression = expression
        self.__tokens = self.__tokenize()
        self.__build_tree()

    def set_expression(self, expression):
        self.__root = None
        self.__expression = expression
        self.__tokens = self.__tokenize()
        self.__build_tree()

    def __tokenize(self):
        return self.__expression.split()

    def __build_tree(self):
        postfix = self.__infix_to_postfix(self.__tokens)  # converte a expressão infixa para pós-fixada
        stack = []  # pilha para armazenar os nós da árvore
        for token in postfix:  # percorre os tokens da expressão pós-fixada
            if not self.__is_operator(token):  # se o token não é um operador
                stack.append(BinaryNode(token))  # adiciona o token como um nó folha na pilha
            else:  # se o token é um operador
                right = stack.pop()  # remove o nó da direita da pilha
                left = stack.pop()  # remove o nó da esquerda da pilha
                node = BinaryNode(token)  # cria um novo nó com o operador
                node.set_left_node(left)  # define o nó da esquerda
                left.set_parent(node)  # define o pai do nó da esquerda
                node.set_right_node(right)  # define o nó da direita
                right.set_parent(node)  # define o pai do nó da direita
                stack.append(node)  # adiciona o novo nó à pilha
        self.__root = stack[0] if stack else None  # define a raiz da árvore como o único nó restante na pilha

    def __infix_to_postfix(self, tokens):
        precedence = {'**': 4, '*': 3, '/': 3, '+': 2, '-': 2}  # define a precedência dos operadores
        right_assoc = {'**'}  # define os operadores com associatividade à direita
        output = []  # guarda a saída em notação pós-fixada
        stack = []  # guarda operadores e parênteses
        for token in tokens:  # percorre os tokens da expressão
            if not self.__is_operator(token) and token not in ('(', ')'):  # se o token não é um operador ou parênteses
                output.append(token)
            elif token in precedence:  # se o token é um operador
                while (stack and stack[-1] in precedence and  # verifica se o topo da pilha é um operador
                       ((token not in right_assoc and precedence[token] <= precedence[
                           stack[-1]]) or  # verifica a precedência
                        (token in right_assoc and precedence[token] < precedence[
                            stack[-1]]))):  # verifica a precedência
                    output.append(stack.pop())  # adiciona o operador à saída
                stack.append(token)  # adiciona o operador à pilha
            elif token == '(':  # se o token é um parêntese esquerdo
                stack.append(token)  #
            elif token == ')':  # se o token é um parêntese direito
                while stack and stack[
                    -1] != '(':  # enquanto a pilha não estiver vazia e o topo não for um parêntese esquerdo
                    output.append(stack.pop())  # adiciona os operadores à saída
                stack.pop()  # Remove '('
        while stack:  # enquanto a pilha não estiver vazia
            output.append(stack.pop())  # Adiciona os operadores restantes à saída
        return output  # retorna a saída em notação pós-fixada

    # def __build_tree(self):
    #     root = None
    #     for i in range(len(self.__tokens)):
    #         if self.__is_operator(self.__tokens[i]):  # é um operador
    #             if not root:
    #                 operator = BinaryNode(data=self.__tokens[i])
    #                 operand1 = BinaryNode(data=self.__tokens[i - 1])
    #                 operand2 = BinaryNode(data=self.__tokens[i + 1])
    #                 root = self.__attach(operator, operand1, operand2)
    #             else:
    #                 operator = BinaryNode(data=self.__tokens[i])
    #                 operand1 = root
    #                 operand2 = BinaryNode(data=self.__tokens[i + 1])
    #                 root = self.__attach(operator, operand1, operand2)
    #     self.__root = root

    # def __attach(self, root: BinaryNode, left: BinaryNode, right: BinaryNode):
    #     if root:
    #         if left:
    #             root.set_left_node(left)
    #             root.left_node().set_parent(root)
    #         if right:
    #             root.set_right_node(right)
    #             root.right_node().set_parent(root)
    #     return root

    def __is_operator(self, token: str) -> bool:
        return token in ('+', '-', '*', '/', '**')

    # def calculate(self):
    #     result = self.__calculate(self.__root)
    #     return eval(result)
    #
    # def __calculate(self, node):
    #     if node.is_leaf():
    #         return node.data()
    #     else:
    #         operator = node.data()
    #         x = self.__calculate(node.left_node())
    #         y = self.__calculate(node.right_node())
    #         return x + operator + y

    def evaluate(self):
        return self.__evaluate(self.__root)

    def __evaluate(self, node):
        if not node:
            return 0

        if node.is_leaf():
            return node.data()

        left_value = self.__evaluate(node.left_node())
        right_value = self.__evaluate(node.right_node())

        if node.data() == '+':
            return float(left_value) + float(right_value)
        elif node.data() == '-':
            return float(left_value) - float(right_value)
        elif node.data() == '*':
            return float(left_value) * float(right_value)
        elif node.data() == '/':
            return float(left_value) / float(right_value)
        elif node.data() == '**':
            return float(left_value) ** float(right_value)
        else:
            raise ValueError(f"Unknown operator: {node.data()}")


if __name__ == '__main__':
    et = ExpressionTree('2 + 2')
    # print(et.calculate())
    # print(et.evaluate())
    # et.set_expression('3 + 3 - 1 + 50')
    # # print(et.calculate())
    # print(et.evaluate())
    # et.set_expression('3 ** 3')
    # # print(et.calculate())
    # print(et.evaluate())
    # et.set_expression('3 / 2 + 3')
    # # print(et.calculate())
    # print(et.evaluate())
    # et.set_expression('3 / 2 + 3 - 2')
    # # print(et.calculate())
    # print(et.evaluate())
    et.set_expression('3 / 2 + 3 - 2 * 2')
    # print(et.calculate())
    print(et.evaluate())
