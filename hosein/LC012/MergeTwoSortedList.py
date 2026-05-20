from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current_list1 = list1
        current_list2 = list2
        numbers = []
        while current_list1:
            numbers.append(current_list1.val)
            current_list1 = current_list1.next
        while current_list2:
            numbers.append(current_list2.val)
            current_list2 = current_list2.next
        numbers = sorted(numbers)
        if not numbers:
            return None
        merged_list = current_merged_list = ListNode(numbers[0])
        for num in numbers[1:]:
            current_merged_list.next = ListNode(num)
            current_merged_list = current_merged_list.next

        return merged_list
