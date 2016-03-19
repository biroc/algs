class ListNode:
    def __init__(self,data,next=None,previous=None,child=None):
        self.data = data
        self.next = next
        self.previous = previous
        self.child = child

# flatten
def append_child(child, tail):
    tail.next = child
    child.previous = tail
    temp = child
    while temp.next:
        temp = temp.next

    tail = temp


def flatten_list(head,tail):
    if not head:
        return None

    temp = head
    while temp:
        if temp.child:
            append_child(temp.child,tail)

        temp = temp.next

# unflatten
def unflatten(head,tail):

    temp = head

    explore(temp)

def explore(head):
    current = head

    while current:
        if current.child:
            current.child.prev.next = None
            current.child.prev = None
            explore(current.child)
        current = current.next