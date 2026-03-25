from linked_binarytree import LinkedBinaryTree
# 1. Instantiate the concrete tree
t = LinkedBinaryTree()

# 2. Build the structure manually
# Let's make a simple tree: A is root, B is left child, C is right child
root_pos = t._add_root("A")
left_pos = t._add_left(root_pos, "B")
right_pos = t._add_right(root_pos, "C")

# Add one more level for depth
t._add_left(left_pos, "D") 

# 3. Test your function
print("Depths of all nodes:")
for d in t.alldepths():
    print(d)