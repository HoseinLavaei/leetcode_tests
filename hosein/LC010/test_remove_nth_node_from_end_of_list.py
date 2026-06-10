from .remove_nth_node_from_end_of_list import Solution
from .remove_nth_node_from_end_of_list import ListNode


def to_list(node):
    values = []
    while node is not None:
        values.append(node.val)
        node = node.next
    return values


def test_remove_nth_from_end_of_list():
    result = Solution().removeNthFromEnd(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
        2,
    )

    assert to_list(result) == [1, 2, 3, 5]
