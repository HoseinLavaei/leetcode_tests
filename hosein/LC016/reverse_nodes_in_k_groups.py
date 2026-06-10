from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_previous = dummy

        while True:
            kth = get_kth_node(group_previous, k)

            if not kth:
                break

            group_next = kth.next

            previous = group_next
            current = group_previous.next

            while current != group_next:
                temp = current.next
                current.next = previous
                previous = current
                current = temp

            old_group_start = group_previous.next
            group_previous.next = kth
            group_previous = old_group_start

        return dummy.next

def get_kth_node(current: ListNode, k: int) -> Optional[ListNode]:
    while current and k > 0:
        current = current.next
        k -= 1

    return current