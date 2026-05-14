class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, num1: ListNode | None, num2: ListNode | None
    ) -> ListNode | None:
        head = node = ListNode()
        carry = 0
        while True:
            if num1:
                node.val += num1.val
                num1 = num1.next
            if num2:
                node.val += num2.val
                num2 = num2.next
            carry, node.val = node.val // 10, node.val % 10
            if num1 is None and num2 is None:
                break
            node.next = ListNode(carry)
            node = node.next
        if carry > 0:
            node.next = ListNode(carry)
        return head
