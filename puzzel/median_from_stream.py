from heapq import *


class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        print()
        print("Start add for ", num, "; small, large:", small, ", ", large)
        heappush(small, -heappushpop(large, num))
        print("Modified small; small, large:", small, ", ", large)
        if len(large) < len(small):
            print("len(large)", len(large), " < len(small)", len(small))
            heappush(large, -heappop(small))
            print("Modified large; small, large:", small, ", ", large)

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0


finder = MedianFinder()
finder.addNum(2)
finder.addNum(5)
print(finder.findMedian())
finder.addNum(1)
print(finder.findMedian())
finder.addNum(3)
print(finder.findMedian())

# class Node:
#     def __init__(self, val, size=1):
#         self.val = val
#         # size represents nodes below this
#         self.size = size
#         self.left = None
#         self.right = None
#
#
# class Tree:
#
#     def __init__(self):
#         self.root = None
#
#     def add_node(self, val, root=None):
#         # attach node after this node
#         if not root:
#             node = Node(val)
#             # set tree root
#             if not self.root:
#                 self.root = node
#             return node
#         if val <= root.val:
#             root.left = self.add_node(val, root.left)
#         else:
#             root.right = self.add_node(val, root.right)
#         size = 1
#         if root.left:
#             size += root.left.size
#         if root.right:
#             size += root.right.size
#         root.size = size
#         return root
#
#     def rank(self, k):
#         """
#         Get k rank node
#         """
#         temp = self.root
#         while True:
#             if not temp.left:
#                 left_size = 0  # handle when there is no left child
#             else:
#                 left_size = temp.left.size
#             if left_size == k:
#                 # Exactly k nodes in left subtree
#                 # Exactly k nodes smaller than this
#                 return temp.val
#             if left_size > k:
#                 # Go left
#                 temp = temp.left
#             else:
#                 # Go right
#                 # remaining number of elements which we have to look
#                 # = exclude left & root (left.size + 1)
#                 k = k - left_size - 1
#                 temp = temp.right
#         return -1
#
#
# class MedianFinder:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.bst = Tree()
#
#     def addNum(self, num):
#         """
#         Adds a num into the data structure.
#         :type num: int
#         :rtype: void
#         """
#         self.bst.add_node(num, self.bst.root)
#
#     def findMedian(self):
#         """
#         Returns the median of current data stream
#         :rtype: float
#         """
#         size = self.bst.root.size
#         mid = size / 2
#         if size % 2 == 0:
#             return (self.bst.rank(mid - 1) + self.bst.rank(mid)) / 2.0
#         else:
#             return float(self.bst.rank(mid))


# class MedianFinder:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.ref_array = []
#         self.length = 0
#
#     def addNum(self, num):
#         """
#         Adds a num into the data structure.
#         :type num: int
#         :rtype: void
#         """
#         # keep a sorted array
#         # use binary search to find insertion index
#
#         low = 0
#         high = self.length - 1
#
#         while low <= high:
#             mid = (low + high) // 2
#             if self.ref_array[mid] >= num:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#
#         self.ref_array.insert(low, num)
#         self.length += 1
#
#     def findMedian(self):
#         """
#         Returns the median of current data stream
#         :rtype: float
#         """
#         # as array is always sorted we can always use the same median property
#
#         if self.length % 2 == 0:
#             temp = self.length // 2
#             return (self.ref_array[temp] + self.ref_array[temp - 1]) / 2.0
#         else:
#             return self.ref_array[self.length // 2]
