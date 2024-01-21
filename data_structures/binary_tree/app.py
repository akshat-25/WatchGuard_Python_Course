from node import Node
from binarytree import BinaryTree

tree = BinaryTree(Node(9))
tree.add(Node(5))
tree.add(Node(11))

tree.inorder()
tree.preorder()
tree.postorder()

print(tree.find(11))