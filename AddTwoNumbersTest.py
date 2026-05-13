from AddTwoNumbers import ListNode, Solution

l1 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))))
l2 = ListNode(9,ListNode(9,ListNode(9,ListNode(9))))

l3 = Solution().addTwoNumbers(l1,l2)
while True:
    if l3 is None:
        break
    print(l3.val)
    l3 = l3.next