from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Recursive_solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        else:
            next_reversed = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return next_reversed

class Iterative_solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        else:
            prev = head
            crt = head.next
            while crt.next != None:
                # continue here!
                pass
        
my_list = ListNode(val = 1)
my_list.next = ListNode(val=2)
my_list.next.next = ListNode(val=3)
my_list.next.next.next = ListNode(val=4)
my_list.next.next.next.next = ListNode(val=5)

my_sol = Recursive_solution()
temp = my_sol.reverseList(my_list)
while temp is not None:
    print(temp.val)
    temp = temp.next

# Rk: solution (including iterative way) here: https://www.youtube.com/watch?v=G0_I-ZF0S38