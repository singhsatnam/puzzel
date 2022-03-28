class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.nxt: Node = None

class Solution:
    def merge_sorted_lists(self, head1: Node, head2: Node):
        self.print_list(head1)
        print()
        self.print_list(head2)

        start = head1
        curr_head2 = head2
        while(head1 != None and curr_head2 != None):

            if head1.nxt.val < curr_head2.val:
                print("itrying to add ", head1.nxt.val)
                head1 = head1.nxt
            else:
                print("etrying to add ", curr_head2.val)
                temp_head1_next = head1.nxt
                head1.nxt = curr_head2
                curr_head2 = curr_head2.nxt
                head1.nxt.nxt = temp_head1_next
                head1 = head1.nxt

        print()
        self.print_list(start)


        return start


    def print_list(self, head):
        print(head.val, end=",")
        while (head.nxt):
            head = head.nxt
            print(head.val, end=",")



head1 = Node(1)
node2 = Node(3)
node3 = Node(10)
node2.nxt = node3
head1.nxt = node2

head10 = Node(2)
node12 = Node(4)
node13 = Node(9)
node12.nxt = node13
head10.nxt = node12

soln = Solution()
soln.merge_sorted_lists(head1, head10)
