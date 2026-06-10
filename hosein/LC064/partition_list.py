from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_dummy = ListNode()
        right_dummy = ListNode()

        left_tail = left_dummy
        right_tail = right_dummy

        current_node = head

        while current_node:
            if current_node.val < x:
                left_tail.next = current_node
                left_tail = left_tail.next
            else:
                right_tail.next = current_node
                right_tail = right_tail.next

            current_node = current_node.next

        right_tail.next = None
        left_tail.next = right_dummy.next

        return left_dummy.next