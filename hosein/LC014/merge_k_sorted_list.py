from typing import Optional
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        numbers = []
        for l in lists:
            current_list = l
            while current_list:
                numbers.append(current_list.val)
                current_list = current_list.next
        numbers = sorted(numbers)
        if not numbers:
            return None
        merged_list = current_merged_list = ListNode(numbers[0])
        for num in numbers[1:]:
            current_merged_list.next = ListNode(num)
            current_merged_list = current_merged_list.next

        return merged_list