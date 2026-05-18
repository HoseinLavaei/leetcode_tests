from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first_node = dummy
        second_node = dummy

        for _ in range(n + 1):
            first_node = first_node.next

        while first_node is not None:
            first_node = first_node.next
            second_node = second_node.next

        second_node.next = second_node.next.next
        return dummy.next
