# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        current_l1 = l1
        current_l2 = l2
        current_l3 = l3
        carry = 0

        while True:
            if current_l1 is not None or current_l2 is not None:
                val1 = 0
                val2 = 0
                if current_l1 is not None:
                    val1 = current_l1.val
                if current_l2 is not None:
                    val2 = current_l2.val
                sum = val1 + val2
                if sum + carry >= 10:
                    current_l3.val = sum - 10 + carry
                    carry = 1
                else:
                    current_l3.val = sum + carry
                    carry = 0
                if (current_l1 is not None and current_l1.next is not None) or (current_l2 is not None and current_l2.next is not None):
                    current_l3.next = ListNode()
                elif carry == 1:
                    current_l3.next = ListNode()
                    current_l3.next.val = carry

                if current_l1 is not None:
                    current_l1 = current_l1.next
                if current_l2 is not None:
                    current_l2 = current_l2.next
                current_l3 = current_l3.next
            else:
                break

        return l3
