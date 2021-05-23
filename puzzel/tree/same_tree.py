from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True

        deq = deque([(p, q), ])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False

            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True


# class Solution:
#     def isSameTree(self, p, q):
#         """
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: bool
#         """
#         # p and q are both None
#         if not p and not q:
#             return True
#         # one of p and q is None
#         if not q or not p:
#             return False
#         if p.val != q.val:
#             return False
#         return self.isSameTree(p.right, q.right) and \
#                self.isSameTree(p.left, q.left)


soln = Solution()
print(soln.isSameTree(p=[1, 2, 1], q=[1, None, 2]))
