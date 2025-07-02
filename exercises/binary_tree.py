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
        #return len(self.traversal()[0])
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

    def draw(self):
        """Draw the tree with the root at the top and children below, using / and \\ for connections."""
        if not self._root:
            print("[empty tree]")
            return

        def display(node):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            if node is None:
                return [], 0, 0, 0

            line1 = []
            line2 = []
            node_repr = str(node.data())
            new_root_width = len(node_repr)

            # Get the left and right sub-boxes, their widths, and root positions
            left, n, p, x = display(node.left_node())
            right, m, q, y = display(node.right_node())

            # Draw the branch connecting the current root node to left sub-box
            # Pad the line with spaces where necessary
            if n > 0:
                left_root = x + 1
                line1.append(' ' * (left_root))
                line1.append('_' * (n - left_root))
                line2.append(' ' * x + '/')
                line2.append(' ' * (n - x - 1))
            else:
                line1.append('')
                line2.append('')

            # Print the value of the node
            line1.append(node_repr)
            line2.append(' ' * new_root_width)

            # Draw the branch connecting the current root node to right sub-box
            if m > 0:
                right_root = y
                line1.append('_' * right_root)
                line1.append(' ' * (m - right_root))
                line2.append(' ' * right_root + '\\')
                line2.append(' ' * (m - right_root - 1))
            else:
                line1.append('')
                line2.append('')

            # Combine left and right sub-boxes with root
            gap = ' ' * new_root_width
            new_lines = [''.join(line1), ''.join(line2)]
            for i in range(max(len(left), len(right))):
                l_line = left[i] if i < len(left) else ' ' * n
                r_line = right[i] if i < len(right) else ' ' * m
                new_lines.append(l_line + gap + r_line)

            return new_lines, n + new_root_width + m, p + 2, n + new_root_width // 2

        lines, *_ = display(self._root)
        for line in lines:
            print(line.rstrip())


if __name__ == '__main__':
    tree = BinaryTree(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(7)
    tree.insert(3)
    tree.insert(14)
    tree.insert(20)
    tree.insert(19)
    tree.draw()
    tree.delete_subtree(10)


    print(len(tree))