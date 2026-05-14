from amir.LC001 import ListNode, Solution


def test_linkedlist_sum():
    sol = Solution()

    tests = [
        {
            "num1": ListNode(2, ListNode(4, ListNode(3))),
            "num2": ListNode(5, ListNode(6, ListNode(4))),
            "expected": ListNode(7, ListNode(0, ListNode(8))),
        },
        {
            "num1": ListNode(0),
            "num2": ListNode(0),
            "expected": ListNode(0),
        },
        {
            "num1": ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
            "num2": ListNode(9, ListNode(9)),
            "expected": ListNode(8, ListNode(9, ListNode(0, ListNode(0, ListNode(1))))),
        },
    ]

    for i, t in enumerate(tests):
        got = sol.addTwoNumbers(t["num1"], t["num2"])
        exp = t["expected"]

        while True:
            assert got.val == exp.val
            if got.next is None and exp.next is None:
                break
            assert got.next is not None and exp.next is not None
            got = got.next
            exp = exp.next
