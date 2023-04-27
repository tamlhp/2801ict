class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def split_tree(root, K):
    if root is None:
        return None, None

    if root.val < K:
        left_tree, right_tree = split_tree(root.right, K)
        print(root.val)
        root.right = left_tree
        return root, right_tree
    else:
        left_tree, right_tree = split_tree(root.left, K)
        root.left = right_tree
        return left_tree, root

def insert(root, value):
    if root is None:
        return TreeNode(value)

    if value < root.val:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def in_order_traversal(node):
    if node is None:
        return []
    return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)

# Example
values = [50, 30, 70, 20, 40, 54, 80]
root = None
for value in values:
    root = insert(root, value)

print("Original In-order:", in_order_traversal(root))
K = 90
left_tree, right_tree = split_tree(root, K)
print("Left tree In-order:", in_order_traversal(left_tree))
print("Right tree In-order:", in_order_traversal(right_tree))

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def in_order_traversal(node):
    if node is None:
        return []
    return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)

def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

def build_balanced_bst(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    root = TreeNode(arr[mid])

    root.left = build_balanced_bst(arr[:mid])
    root.right = build_balanced_bst(arr[mid + 1:])

    return root

# Example
# Construct two example BSTs
tree1 = TreeNode(20)
tree1.left = TreeNode(10)
tree1.right = TreeNode(30)

tree2 = TreeNode(50)
tree2.left = TreeNode(40)
tree2.right = TreeNode(60)

# Merge the two BSTs
tree1_in_order = in_order_traversal(tree1)
tree2_in_order = in_order_traversal(tree2)
merged_array = merge_sorted_arrays(tree1_in_order, tree2_in_order)
merged_tree = build_balanced_bst(merged_array)

# Check the result
print("Merged Tree In-order:", in_order_traversal(merged_tree))

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def concatenate_trees(tree1, tree2):
    if not tree1:
        return tree2
    if not tree2:
        return tree1

    largest_node = tree1
    while largest_node.right:
        largest_node = largest_node.right

    smallest_node = tree2
    while smallest_node.left:
        smallest_node = smallest_node.left

    largest_node.right = smallest_node
    return tree1

# In-order traversal for testing
def in_order_traversal(node):
    if node is None:
        return []
    return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)


# Helper function to create a new TreeNode
def create_node(value):
    return TreeNode(value)

# Construct two example BSTs
tree1 = create_node(20)
tree1.left = create_node(10)
tree1.right = create_node(30)

tree2 = create_node(50)
tree2.left = create_node(40)
tree2.right = create_node(60)

# Concatenate the two BSTs
merged_tree = concatenate_trees(tree1, tree2)

# Check the result
print("Merged Tree In-order:", in_order_traversal(merged_tree))
