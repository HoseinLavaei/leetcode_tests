from .rotate_list import Solution
from .rotate_list import ListNode


def build_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def list_values(head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    return values


def test_rotate_list():
    head = build_list([1, 2, 3, 4, 5])

    result = Solution().rotateRight(head, 2)

    assert list_values(result) == [4, 5, 1, 2, 3]

