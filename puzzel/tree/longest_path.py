class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def depth(p):
            if not p:
                print("None")
                return 0
            print("calling depth for left ", p.val)
            left = depth(p.left)
            print("calling depth for right ", p.val)
            right = depth(p.right)
            self.ans = max(self.ans, left + right)
            print("self= max(", self.ans, ", ", left, "+", right, ")=", self.ans)
            print("returning end. left=", left, " right=", right)
            return 1 + max(left, right)

        depth(root)
        print(self.ans)
        return self.ans

d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a = TreeNode(2, d, f)
b = TreeNode(3, e, g)
c = TreeNode(1, a, b)
soln = Solution()
soln.diameterOfBinaryTree(c)