class ListNode:
    def __init__(self,val=0):
        self.val = val
        self.next = None

class Solution(object):
    def partition(self,head,x):
        if not head or not head.next:
            return head

        smallHead = smallTail = ListNode(0)
        bigHaed = bigTail = ListNode(0)
        temp = head
        while temp:
            if temp.val < x:
                smallTail.next = temp
                smallTail = smallTail.next
            else:
                bigTail.next = temp
                bigTail = bigTail.next
            temp = temp.next

        smallTail.next = bigHaed.next
        bigTail.next = None

        return smallHead.next or head