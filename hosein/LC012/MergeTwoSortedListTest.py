from .MergeTwoSortedList import ListNode
from .MergeTwoSortedList import Solution


def to_list(node):
    result = []

    while node:
        result.append(node.val)
        node = node.next

    return result


def test_merge_two_sorted_list():
    result = Solution().mergeTwoLists(
        ListNode(1, ListNode(2, ListNode(4))),
        ListNode(1, ListNode(3, ListNode(4)))
    )
    assert to_list(result) == [1, 1, 2, 3, 4, 4]
