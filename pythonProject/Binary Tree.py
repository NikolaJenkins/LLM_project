from typing import List, Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self):
        self.root = TreeNode()

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        stack = []
        curr = root
        while curr is not None and len(stack) is not 0:
            stack.append(curr)
            if curr.left is None:
                if curr.right is None:
                    traversal.append(stack.pop())







s = Solution()
root1 = [1,None,2,3]
# assert s.inorderTraversal(root1) == [1,3,2]
root2 = [1,2,3,4,5,None,8,None,None,6,7,9]
# assert s.inorderTraversal(root2) == [4,2,6,5,7,1,3,9,8]
root3 = []
assert s.inorderTraversal(root3) == []
root4 = [1]
# assert s.inorderTraversal(root4) == [1]
