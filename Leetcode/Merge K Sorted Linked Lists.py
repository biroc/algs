class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        finish = len(lists)-1
        while finish > 0:
            start = 0
            while start < finish:
                lists[start] = self.merge_lists(lists[start], lists[finish])
                start += 1
                finish -= 1

        return lists[0]

    def merge_lists(self,l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = temp = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next

        temp.next = l1 or l2
        return dummy.next