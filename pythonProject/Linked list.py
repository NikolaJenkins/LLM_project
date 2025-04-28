class Node:
    val = None
    before_pointer = None
    after_pointer = None

root = Node()
root.val = 3
node_after = Node()
node_after.val = 5
root.after_pointer = node_after
node_before = Node()
node_before.val = 1
node_before.after_pointer = root
root.before_pointer = node_before
pointer = root.before_pointer

while pointer is not None:
    print(pointer.val)
    pointer = pointer.after_pointer