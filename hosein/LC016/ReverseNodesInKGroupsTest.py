from .ReverseNodesInKGroups import Solution
from .ReverseNodesInKGroups import ListNode

def to_list(node):
    result = []

    while node:
        result.append(node.val)
        node = node.next

    return result


def test_reverse_nodes_in_k_groups():
    result = Solution().reverseKGroup(ListNode(1, ListNode(2,ListNode(3,ListNode(4,ListNode(5))))),3)
    assert to_list(result) == [3,2,1,4,5]