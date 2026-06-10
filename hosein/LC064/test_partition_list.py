from .partition_list import Solution
from .partition_list import ListNode

def to_list(node):
    values = []
    while node is not None:
        values.append(node.val)
        node = node.next
    return values

def test_partition_list():
    input = Solution().partition(ListNode(1,ListNode(4,ListNode(3,ListNode(2,ListNode(5,ListNode(2)))))),3)
    output = ListNode(1,ListNode(2,ListNode(2,ListNode(4,ListNode(3,ListNode(5))))))
    assert to_list(input) == to_list(output)