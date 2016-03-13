# O(N) time and O(1) space
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        temp = head
        while temp:
            copy = RandomListNode(temp.label)
            next = temp.next
            temp.next = copy
            copy.next = next
            temp = next

        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            else:
                temp.next.random = None
            temp = temp.next.next

        temp = head
        head_copy = temp.next if temp else None
        while temp:
            copy = temp.next
            if copy.next:
                temp.next = copy.next
                copy.next = copy.next.next
            else:
                temp.next = None
            temp = temp.next

        return head_copy

# O(N) time and O(N) space

class Solution(object):
    def copyRandomList(self, head):
        copy_list = []
        hashed_nodes = {}
        i = 0
        temp = head
        while temp:
            hashed_nodes[temp] = i
            copy_list.append(RandomListNode(temp.label))
            if i > 0:
                copy_list[i-1].next = copy_list[i]
            temp, i = temp.next, i + 1

        temp = head

        while temp:
            if temp.random == None:
                copy_list[hashed_nodes[temp]].random = None
            else:
                copy_list[hashed_nodes[temp]].random = copy_list[hashed_nodes[temp.random]]
            temp = temp.next

        return copy_list[0] if copy_list else None