class node:
    def __init__(self, data, left_node, right_node) -> None:
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        
def pre_(node):
    print(node.data, end='')
    if node.left_node != "." and node.left_node !="None":
        pre_(tree[node.left_node])
    if node.right_node != "." and node.right_node !="None":
        pre_(tree[node.right_node])

def in_(node):
    
    if node.left_node != "." and node.left_node !="None":
        in_(tree[node.left_node])
    print(node.data, end='')    
    if node.right_node != "." and node.right_node !="None":
        in_(tree[node.right_node])
        
def post_(node):
    
    if node.left_node != "." and node.left_node !="None" :
        post_(tree[node.left_node])
    if node.right_node != "." and node.right_node !="None":
        post_(tree[node.right_node])
    print(node.data, end='')


n = int(input())
tree = {}
for i in range(n):
    data,left_node,right_node = input().split()
    tree[data] = node(data,left_node,right_node)
    
    [k for k, v in node.items() if v == '']
    

pre_(tree['A'])
print()
in_(tree['A'])
print()
post_(tree['A'])
print()