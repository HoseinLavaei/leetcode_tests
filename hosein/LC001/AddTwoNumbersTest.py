from .AddTwoNumbers import ListNode, Solution

def test_add_two_numbers():
    l1 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))))
    l2 = ListNode(9,ListNode(9,ListNode(9,ListNode(9))))
    l3 = Solution().addTwoNumbers(l1,l2)

    expected = ListNode(8,ListNode(9,ListNode(9,ListNode(9,ListNode(0,ListNode(0,ListNode(0,ListNode(1))))))))
    while True:
        if not l3 and not expected:
            break
        assert l3.val == expected.val
        l3 = l3.next
        expected = expected.next