from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1:
            return l2
        else:
            if not l2:
                return l1
            else:
                # case when both l1 and l2 are there
                l3 = ListNode()
                carry = 0
                while l1.next or l2.next:
                    if l1.next is None:
                        while l2.next:
                            curr = ListNode(l2.val)
                            l3.next = curr
                            l2 = l2.next
                    if l2.next is None:
                        while l1.next:
                            curr = ListNode(l1.val)
                            l3.next = curr
                            l1 = l1.next
                    num1 = l1.val
                    num2 = l2.val
                    sum = num1 + num2 + carry
                    if sum >= 10:
                        carry = sum % 10
                        sum = 1
                    curr = ListNode(sum)
                    l3.next = curr
                    l1 = l1.next
                    l2 = l2.next
