# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        else:
            self.process(root, None)
        return root

    def process(self, root: 'Node', nxt: 'Node'):
        print("process")
        if root is None:
            return
        root.next = nxt
        if root.left:
            left_next = None
            if root.right is not None:
                left_next = root.right
            elif root.next is not None:
                if root.next.left:
                    left_next = root.next.left
                elif root.next.right:
                    left_next = root.next.right
            self.process(root.left, left_next)
        if root.right:
            right_next = None
            # print("right next is none")
            if root.next is not None:
                if root.next.left is not None:
                    right_next = root.next.left
                elif root.next.right is not None:
                    right_next = root.next.right
            else:
                right_next = None
            # print(root.right.val, right_next.val if right_next is not None else None)
            self.process(root.right, right_next)
        return

# [1,2,3,4,5,null,7]
a1 = Node(1)
a1.left = Node(2)
a1.right = Node(3)
a1.left.left = Node(4)
a1.left.right = Node(5)
a1.right.right = Node(7)

soln = Solution()
soln.connect(a1)
def print_next(node):
    if node is not None:
        print(node.val, node.next.val if node.next else None)
        if node.left:
            print_next(node.left)
        if node.right:
            print_next(node.right)
    else:
        return

print_next(a1)

