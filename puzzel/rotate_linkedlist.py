class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        len = 0
        temp = head
        while (temp):
            print(temp.val, "-> ", end='')
            temp = temp.next
            len = len + 1
        temp = head
        print("None")

        print("k =", k)
        k = k % len
        for i in range(len - k):
            temp = temp.next

        temp.next.next = head
        head = temp.next
        temp.next = None

        while (head):
            print(head.val, "-> ", end="")
            head = head.next
        print("None")


node_1 = ListNode(1)
node_2 = ListNode(2, node_1)
node_3 = ListNode(3, node_2)
node_4 = ListNode(4, node_3)
node_5 = ListNode(5, node_4)
soln = Solution()
soln.rotateRight(node_5, 2)
