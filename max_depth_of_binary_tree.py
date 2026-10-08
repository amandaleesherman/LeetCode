def max_depth_of_binary_tree(root):
    if not root:
        return 0
    else:
        left_depth = max_depth_of_binary_tree(root.left)
        right_depth = max_depth_of_binary_tree(root.right)
        return max(left_depth, right_depth) + 1

print(max_depth_of_binary_tree([3,9,20,None,None,15,7]))  # Output: 3