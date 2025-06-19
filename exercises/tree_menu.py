from collections import deque
from idlelib.tree import TreeNode


class TreeNode:

    def __init__(self, value, parent=None):
        self.__value = value
        self.__parent: TreeNode = parent
        self.__children = list()

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_parent(self, parent):
        self.__parent = parent

    def set_children(self, children):
        self.__children = children

    def get_children(self):
        return self.__children

    def add_child(self, child: TreeNode):
        self.__children.append(child)

    def __str__(self):
        return str(self.__value)

class Tree:

    def __init__(self, value):
        self.__root = TreeNode(value)

    def root(self):
        return self.__root

    def insert(self, parent: TreeNode, value):
        child = TreeNode(value, parent)
        parent.add_child(child)
        return child

    def print_levels(self):
        queue = deque([(self.__root, 0)])
        current_level = 0
        level_nodes = []
        while queue:
            node, level = queue.popleft()
            if level != current_level:
                print("Level", current_level, ":", " ".join(str(n.get_value()) for n in level_nodes))
                level_nodes = []
                current_level = level
            level_nodes.append(node)
            for child in node.get_children():
                queue.append((child, level + 1))
        if level_nodes:
            print("Level", current_level, ":", " ".join(str(n.get_value()) for n in level_nodes))
    
    def print_levels_and_shortcuts(self):
        queue = deque([(self.__root, 0)])
        current_level = 0
        level_nodes = []
        while queue:
            node, level = queue.popleft()
            if level != current_level:
                print("Level", current_level, ":", " ".join(str(n.get_value()) for n in level_nodes))
                level_nodes = []
                current_level = level
            level_nodes.append(node)
            for child in node.get_children():
                queue.append((child, level + 1))
        if level_nodes:
            print("Level", current_level, ":", " ".join(str(n.get_value()) for n in level_nodes))

    def traverse_preorder(self, node=None):
        if node is None:
            node = self.__root
        result = list()
        return self.__traverse_preorder(node, result)

    def __traverse_preorder(self, node, result):
        result.append(node)
        for child in node.get_children():
            self.__traverse_preorder(child, result)
        return result

    # busca em profundidade
    def depth_first_search(self, value, node=None):
        if node is None:
            node = self.__root
        if node.get_value() == value:
            return node
        for child in node.get_children():
            found = self.depth_first_search(value, child)
            if found:
                return found
        return None

    # busca em largura
    def breadth_first_search(self, compare_fn):
        queue = deque([self.__root])
        while queue:
            node = queue.popleft()
            if compare_fn(node):
                return node
            queue.extend(node.get_children())
        return None

    def breadth_first_search_old(self, value):
        queue = deque([self.__root])
        while queue:
            node = queue.popleft()
            if node.get_value() == value:
                return node
            queue.extend(node.get_children())
        return None

class MenuTree(Tree):

    def __init__(self, value):
        super().__init__(value)

    def find_shortcut(self, menu_item: str):
        return self.breadth_first_search(lambda n: n.get_value()[0] == menu_item).get_value()[1]

    def find_menu_item(self, shortcut: str):
        return self.breadth_first_search(lambda n: n.get_value()[1] == shortcut).get_value()[0]

    def find_all_menu_items(self, search_str):
       result = list()
       for node in self.traverse_preorder():
           if search_str in node.get_value()[0]:
               result.append( node.get_value()[0] )
       return result
       

if __name__ == "__main__":
    pycharm_app = MenuTree( ("App", None) )
    pycharm_menu = pycharm_app.insert(pycharm_app.root(), ("PyCharm", None))
    pycharm_app.insert(pycharm_menu, ("About PyCharm", None))
    pycharm_app.insert(pycharm_menu, ("Check for updates...", None))
    pycharm_app.insert(pycharm_menu, ("Settings...", "Cmd+,"))
    services_menu = pycharm_app.insert(pycharm_menu, ("Services", None))
    pycharm_app.insert(services_menu, ("Activity Monitor", None))
    pycharm_app.insert(services_menu, ("Allocations & Leaks", None))
    pycharm_app.insert(pycharm_menu, ("Hide PyCharm", "Cmd+H"))
    pycharm_app.insert(pycharm_menu, ("Hide others", "Opt+Cmd+H"))
    pycharm_app.insert(pycharm_menu, ("Show All", "Opt+Cmd+H"))
    pycharm_app.insert(pycharm_menu, ("Quit PyCharm", "Cmd+Q"))
    file_menu = pycharm_app.insert(pycharm_app.root(), ("File", None))
    pycharm_app.insert(file_menu, ("New Project...", None))
    pycharm_app.insert(file_menu, ("Project from version control", None))
    pycharm_app.insert(file_menu, ("New...", "Cmd+N"))

    # print(pycharm_app.find_shortcut("Check for updates..."))
    # print(pycharm_app.find_shortcut("Hide PyCharm"))

    print("Shortcut Cmd+H:")
    print(pycharm_app.find_menu_item("Cmd+H"))
    # print(pycharm_app.find_menu_item("Cmd+H"))
    # print(pycharm_app.find_menu_item(None))

    # print(pycharm_app.print_levels())

    result = pycharm_app.find_all_menu_items("PyCharm")
    print("Menu items containing 'PyCharm':")
    print("================================")
    for i in result:
        print(i)

    # tree = Tree(1)
    # child1 = tree.insert(tree.root(), 2)
    # child2 = tree.insert(tree.root(), 3)
    # tree.insert(tree.root(), 10)
    # tree.insert(child1, 4)
    # tree.insert(child1, 5)
    # child3 = tree.insert(child2, 6)
    # tree.insert(child3, 7)

    # tree.print_levels()

    # print("Depth-first search for 5:", tree.depth_first_search(5).get_value())
    # print("Breadth-first search for 6:", tree.breadth_first_search(6).get_value())
    