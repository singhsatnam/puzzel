class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list_from_array(arr):
    head = start = None
    for ele in arr:
        curr = ListNode(ele, None)
        if head is None:
            print("ele empty list", ele)
            head = start = curr
        else:
            print("ele extending list", ele)
            head.next = curr
            head = head.next
    return start


def print_llist(head):
    print("printing")
    while head:
        print(head.val)
        head = head.next


l1 = [2, 4, 3]
l2 = [5, 6, 4]

ll1 = create_linked_list_from_array(l1)
ll2 = create_linked_list_from_array(l2)


print_llist(ll1)
print_llist(ll2)
