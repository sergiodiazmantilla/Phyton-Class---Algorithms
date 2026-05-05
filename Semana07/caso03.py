class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(arr, i=0):
    if i >= len(arr):
        return None
    
    root = Node(arr[i])
    root.left = build_tree(arr, 2 * i + 1)
    root.right = build_tree(arr, 2 * i + 2)
    
    return root

def in_order_transversal(root):
    if root is None:
        return []
    
    return(
        in_order_transversal(root.left) + [root.value] + in_order_transversal(root.right)
    )

arr = [1, 2, 3, 4, 5, 6, 7]
root = build_tree(arr)
resultado = in_order_transversal(root)

print("Recorrido in-order: ", resultado)