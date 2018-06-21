# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def get_value(ln):
    tmp = ln
    value = 0
    while tmp is not None:
        value = value


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
            return None
        
        tmp1, tmp2 = l1, l2
        ret = ListNode(tmp1.val+tmp2.val)
        while tmp1.next is not None and tmp2.next is not None:
            ret.next.val = tmp1.val + tmp2.val
            tmp1 = tmp1.next
            tmp2 = tmp2.next

