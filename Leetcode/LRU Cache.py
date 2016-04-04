class ListNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.pre, self.next = None, None

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head, self.tail = None, None

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.set_head(node)
            return node.value
        return -1

    def remove(self,node):
        if node.pre:
            node.pre.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.pre = node.pre
        else:
            self.tail = node.pre

    def set_head(self,node):
        node.next = self.head
        node.pre = None
        if self.head:
            self.head.pre = node

        self.head = node

        if not self.tail:
            self.tail = self.head

    def set(self, key, value):
        if key in self.map:
            old = self.map[key]
            old.value = value
            self.remove(old)
            self.set_head(old)
        else:
            new = ListNode(key,value)
            if len(self.map) >= self.capacity:
                self.map.pop(self.tail.key, None)
                self.remove(self.tail)
            self.set_head(new)
            self.map[new.key] = new