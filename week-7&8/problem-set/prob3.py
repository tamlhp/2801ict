class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# i. Count the number of nodes in a binary tree
def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

# ii. Count the number of leaves in a binary tree
def count_leaves(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

# iii. Count the number of right children in a binary tree
def count_right_children(node):
    if not node:
        return 0
    right_count = count_right_children(node.right)
    left_count = count_right_children(node.left)
    return 1 + right_count + left_count if node.right else right_count + left_count

# iv. Find the height of the tree
def tree_height(node):
    if not node:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

# v. Delete all leaves from a binary tree
def delete_leaves(node):
    if not node:
        return None
    if not node.left and not node.right:
        return None
    node.left = delete_leaves(node.left)
    node.right = delete_leaves(node.right)
    return node

def is_bst(node, prev=None):
    if not node:
        return True

    # Traverse the left subtree
    if not is_bst(node.left, prev):
        return False

    # Check if the current node's value is greater than the previous node's value
    if prev and prev.value >= node.value:
        return False

    # Update the previous node's value
    prev = node

    # Traverse the right subtree
    return is_bst(node.right, prev)

def is_binary_search_tree(root):
    return is_bst(root)

# Construct a simple binary tree
#          1
#         / \
#        2   3
#       / \   \
#      4   5   6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# i. Count the number of nodes in a binary tree
print(f"Number of nodes: {count_nodes(root)}")

# ii. Count the number of leaves in a binary tree
print(f"Number of leaves: {count_leaves(root)}")

# iii. Count the number of right children in a binary tree
print(f"Number of right children: {count_right_children(root)}")

# iv. Find the height of the tree
print(f"Tree height: {tree_height(root)}")

# v. Delete all leaves from a binary tree
root = delete_leaves(root)
print("Leaves deleted from the binary tree.")


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

if is_binary_search_tree(root):
    print("The binary tree is a binary search tree.")
else:
    print("The binary tree is NOT a binary search tree.")


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def build_tree(pre_order, in_order):
    if not in_order:
        return None

    root_value = pre_order.pop(0)
    root = TreeNode(root_value)
    root_index = in_order.index(root_value)

    root.left = build_tree(pre_order, in_order[:root_index])
    root.right = build_tree(pre_order, in_order[root_index + 1:])

    return root

def pre_order_traversal(node):
    if node is None:
        return []
    return [node.val] + pre_order_traversal(node.left) + pre_order_traversal(node.right)

def in_order_traversal(node):
    if node is None:
        return []
    return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)

# Example
pre_order = [1, 2, 4, 5, 3, 6, 7]
in_order = [4, 2, 5, 1, 6, 3, 7]

root = build_tree(pre_order.copy(), in_order.copy())
print("Reconstructed Pre-order:", pre_order_traversal(root))
print("Reconstructed In-order:", in_order_traversal(root))
