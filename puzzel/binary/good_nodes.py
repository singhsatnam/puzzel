# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
from collections import deque


class TreeNode:
    def __init__(self, val=None, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


class GoodNodes:
    def goodNodes(self, root: TreeNode) -> int:
        return self.count_good_nodes(root)

    def count_good_nodes(self, curr: TreeNode, prev) -> int:
        if curr == None:
            return 0
        res, new_prev = (1, curr.val) if curr.val >= prev else (0, prev)
        right = self.count_good_nodes(curr.right, curr.val)
        left = self.count_good_nodes(curr.left, curr.val)

        final = res + right + left
        return final

    def count_good_nodes(self, root: TreeNode) -> int:
        print("S")
        if root == None:
            return 0
        stk = deque()
        stk.append((root, root.val))
        count = 0


        while stk:
            curr_node, max_val = stk.pop()
            print(curr_node.val, max_val)
            if curr_node.val > max_val:
                count = count + 1

            for kid in [curr_node.right, curr_node.left]:
                if kid != None:
                    stk.append((kid, curr_node.val if curr_node.val > max_val else max_val))

        return count





b1 = TreeNode(9)
b1.left = None
b1.right = TreeNode(3)
b1.right.left = 6

a1 = TreeNode(3)
a1.left = TreeNode(3)
a1.right = None
a1.left.left = TreeNode(4)
a1.left.right = TreeNode(2)

n1 = TreeNode(3)
n2 = TreeNode(2)
n1.left = n2
n4 = TreeNode(4)
n1.right = n4
n5 = TreeNode(6)
n4.right = n5
obj = GoodNodes()
print(obj.goodNodes(a1))
