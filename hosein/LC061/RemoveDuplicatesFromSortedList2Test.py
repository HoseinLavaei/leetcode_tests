from .RemoveDuplicatesFromSortedList2 import Solution
from .RemoveDuplicatesFromSortedList2 import ListNode

def to_list(node):
    values = []
    while node is not None:
        values.append(node.val)
        node = node.next
    return values

def test_remove_duplicates_from_sorted_List_2():
    input = ListNode(1,ListNode(2,ListNode(3,ListNode(3,ListNode(4,ListNode(4,ListNode(5)))))))
    output = ListNode(1,ListNode(2,ListNode(5)))
    assert to_list(Solution().deleteDuplicates(input)) == to_list(output)