import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def max_heapify(tree_root):
    if tree_root is not None:
        if tree_root.left is not None and tree_root.left.val > tree_root.val:
            tree_root.val, tree_root.left.val = tree_root.left.val, tree_root.val
            max_heapify(tree_root.left)
        if tree_root.right is not None and tree_root.right.val > tree_root.val:
            tree_root.val, tree_root.right.val = tree_root.right.val, tree_root.val
            max_heapify(tree_root.right)


def build_max_heap(tree_root):
    """
    Recursive function to build a max heap from a binary tree starting at the given root node.
    Parameters:
    - tree_root: TreeNode, the root node of the binary tree
    Returns:
    None
    """
    max_heapify(tree_root)
    if tree_root.left is not None:
        build_max_heap(tree_root.left)
    if tree_root.right is not None:
        build_max_heap(tree_root.right)


# Створення максимальної бінарної купи
root = Node(10)
root.left = Node(9)
root.right = Node(8)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)

# Створення дерева
build_max_heap(root)
# Відображення дерева
draw_tree(root)
