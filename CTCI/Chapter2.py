class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

    def __str__(self):
        return "Node with value " + str(self.val)


def create_list(array):
    if not array:
        return None

    head = ListNode(array[0])
    temp = head
    for i in range(1,len(array)):
        temp.next = ListNode(array[i])
        temp = temp.next

    return head

def print_l(head):
    if not head:
        print("No list")

    temp = head
    to_print = ""
    while(temp):
        to_print += str(temp.val)
        if temp.next:
            to_print +=  " -> "
        temp = temp.next

    print(to_print)


"""
2.1 Remove Dups
"""

def remove_duplicates(head):
    if not head:
       return None

    prev = None
    temp = head
    hash = {}
    while temp:
        if temp.val in hash:
            prev.next = temp.next
        else:
            hash[temp.val] = 1
            prev = temp
        temp = temp.next

    return head

"""
2.2 Return Kth to Last.
"""
def kth_to_last(head,k):
    if not head:
        return None

    f = head
    for i in range(k-1):
        f = f.next

    s = head
    while f.next:
        s = s.next
        f = f.next

    return s


"""
2.3 Delete Middle Node
"""

def delete_middle(node):
    if not node:
        return None

    node.val = node.next.val
    node.next = node.next.next

"""
2.4 Partition
"""

def partition(head,x):
    if not head:
        return None

    smallHead = smallTail = ListNode(0)
    bigHead = bigTail = ListNode(0)
    temp = head
    while temp:
        if temp.val < x:
            smallTail.next = temp
            smallTail = smallTail.next
        else:
            bigTail.next = temp
            bigTail = bigTail.next
        temp = temp.next

    smallTail.next = bigHead.next
    bigTail.next = None
    return smallHead.next or head


"""
2.5 Sum Lists
"""

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

"""
2.6 Palindrome
"""

def is_palindrome(head):
    if not head:
        return True

    stack = []
    slow = fast = head

    while fast and fast.next:
        stack.append(slow.val)
        fast = fast.next.next
        slow = slow.next

    if fast:
        slow = slow.next

    while slow:
        if slow.val != stack.pop():
            return False
        slow = slow.next

    return True

"""
2.7 Intersetion
"""

def intersection(l1,l2):
    if not l1 or not l2:
        return None

    t1 = l1
    t2 = l2
    length1 = 1
    length2 = 1
    while t1.next or t2.next:
        if t1.next:
            length1 += 1
            t1 = t1.next
        if t2.next:
            length2 += 1
            t2 = t2.next

    if t1 != t2:
        return None
    else:
        t1 = l1
        t2 = l2
        if length1 > length2:
            for i in range(abs(length1-length2)):
                t1 = t1.next
        elif length2 > length1:
            for i in range(abs(length1-length2)):
                t2 = t2.next

        while t1 != t2:
            t1 = t1.next
            t2 = t2.next

    return t1


"""
2.8 Loop detection.
"""

def loop_detection(head):
    if not head:
        return None

    slow = fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    if not slow or not fast:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast