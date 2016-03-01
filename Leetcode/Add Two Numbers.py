class ListNode:
    def __init__(self,val=0):
        self.val = val
        self.next = None

def sum_lists(l1,l2):
    if not l1 or not l2:
        return None

    dummy = result = ListNode(0)
    sum = 0
    while l1 or l2:
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        if sum >= 10:
            result.next = ListNode(sum % 10)
            sum = 1
        else:
            result.next = ListNode(sum)
            sum = 0
        result = result.next

    if sum:
        result.next = ListNode(sum)

    return dummy.next