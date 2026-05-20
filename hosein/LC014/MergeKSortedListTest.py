from .MergeKSortedList import Solution
from .MergeKSortedList import ListNode

def to_list(node):
    result = []

    while node:
        result.append(node.val)
        node = node.next

    return result


def test_merge_k_sorted_list():
    result = Solution().mergeKLists([ListNode(1,ListNode(4,ListNode(5))),ListNode(1,ListNode(3,ListNode(4))),ListNode(2,ListNode(6))])
    assert to_list(result) == [1,1,2,3,4,4,5,6]