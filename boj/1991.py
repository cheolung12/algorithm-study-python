class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def preorder(node):
    print(node.value, end='')
    if node.left: preorder(tree[node.left])
    if node.right: preorder(tree[node.right])

def inorder(node):
    if node.left: inorder(tree[node.left])
    print(node.value, end='')
    if node.right: inorder(tree[node.right])

def postorder(node):
    if node.left: postorder(tree[node.left])
    if node.right: postorder(tree[node.right])
    print(node.value, end='')

tree = {}
N = int(input())
for i in range(N):
    value, left, right = input().split()
    if left == ".": left = None
    if right == ".": right = None
    tree[value] = Node(value, left, right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])