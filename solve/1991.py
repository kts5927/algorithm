class node:
    def __init__(self, data, left_node, right_node) -> None:
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        
def pre_(node):
    print(node.data, end='')
    if node.left_node != "." :
        pre_(tree[node.left_node])
    if node.right_node != "." :
        pre_(tree[node.right_node])

def in_(node):
    
    if node.left_node != ".":
        in_(tree[node.left_node])
    print(node.data, end='')    
    if node.right_node != ".":
        in_(tree[node.right_node])
        
def post_(node):
    
    if node.left_node != "."  :
        post_(tree[node.left_node])
    if node.right_node != "." :
        post_(tree[node.right_node])
    print(node.data, end='')


n = int(input())
tree = {}
for i in range(n):
    data,left_node,right_node = input().split()
    tree[data] = node(data,left_node,right_node)
    
    
    

pre_(tree['A'])
print()
in_(tree['A'])
print()
post_(tree['A'])
print()