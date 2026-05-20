from .SwapNodesInPairs import Solution
from .SwapNodesInPairs import ListNode

def to_list(node):
    result = []

    while node:
        result.append(node.val)
        node = node.next

    return result


def test_swap_nodes_in_pairs():
    result = Solution().swapPairs(ListNode(1, ListNode(2,ListNode(3,ListNode(4)))))
    assert to_list(result) == [2,1,4,3]