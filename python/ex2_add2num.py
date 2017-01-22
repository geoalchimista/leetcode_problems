# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current_sum = l1.val + l2.val
        result = ListNode(current_sum % 10)  # initialize
        current_node = result
        carry = current_sum // 10

        while (l1.next is not None or l2.next is not None) or carry:
            current_sum = carry
            if l1.next is not None:
                l1 = l1.next
                current_sum += l1.val
            if l2.next is not None:
                l2 = l2.next
                current_sum += l2.val

            carry = current_sum // 10  # update the carry
            current_node.next = ListNode(current_sum % 10)
            current_node = current_node.next  # move to the next node

        return(result)
